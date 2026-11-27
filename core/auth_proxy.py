#!/usr/bin/env python3
"""Password-protected reverse proxy for notebook servers (Ollama / ComfyUI).

Colab and Kaggle tunnels expose a port to the public internet. Ollama ignores
the Authorization header entirely and ComfyUI ships without any auth layer, so
an open tunnel means anyone with the URL can use (or reconfigure) your runtime.

This proxy sits on a second port, requires HTTP Basic auth (or
``Authorization: Bearer <password>`` so OpenAI-compatible clients keep working),
and forwards HTTP + WebSocket traffic to the local service.

    python auth_proxy.py --target-port 8188 --port 8189
    PROXY_PASSWORD=... python auth_proxy.py --target-port 11434 --port 11435

Only aiohttp is required (already installed by ComfyUI; one-line pip otherwise).
"""

from __future__ import annotations

import argparse
import asyncio
import base64
import hmac
import os
import sys

from aiohttp import ClientSession, ClientTimeout, TCPConnector, WSMsgType, web

# Headers that must not be forwarded between the two hops.
SKIP_REQUEST = {
    "host", "connection", "keep-alive", "proxy-authenticate", "proxy-authorization",
    "te", "trailer", "transfer-encoding", "upgrade", "expect", "origin", "referer",
}
SKIP_RESPONSE = {
    "connection", "keep-alive", "proxy-authenticate", "proxy-authorization",
    "te", "trailer", "transfer-encoding", "upgrade", "content-encoding", "content-length",
}

SESSION = web.AppKey("session", ClientSession)


def build_app(target_port: int, user: str, password: str) -> web.Application:
    basic = "Basic " + base64.b64encode(f"{user}:{password}".encode()).decode()
    bearer = f"Bearer {password}"
    backend = f"127.0.0.1:{target_port}"

    async def start_session(app: web.Application) -> None:
        # Created on the running loop (required by aiohttp >= 3.10).
        app[SESSION] = ClientSession(
            connector=TCPConnector(limit=128),
            timeout=ClientTimeout(total=None, sock_connect=30, sock_read=None),
        )

    async def close_session(app: web.Application) -> None:
        await app[SESSION].close()

    def authorized(request: web.Request) -> bool:
        supplied = request.headers.get("Authorization", "")
        return hmac.compare_digest(supplied, basic) or hmac.compare_digest(supplied, bearer)

    def reject(request: web.Request) -> web.Response:
        return web.Response(
            status=401,
            text="401: authentication required\n",
            headers={"WWW-Authenticate": 'Basic realm="notebook", charset="UTF-8"'},
        )

    async def proxy_http(request: web.Request) -> web.StreamResponse:
        if not authorized(request):
            return reject(request)
        headers = {k: v for k, v in request.headers.items() if k.lower() not in SKIP_REQUEST}
        body = await request.read() if request.body_exists else None
        try:
            async with request.app[SESSION].request(
                request.method,
                f"http://{backend}{request.rel_url}",
                headers=headers,
                data=body,
                allow_redirects=False,
            ) as upstream:
                response = web.StreamResponse(status=upstream.status, reason=upstream.reason)
                for key, value in upstream.headers.items():
                    if key.lower() not in SKIP_RESPONSE:
                        response.headers[key] = value
                await response.prepare(request)
                if request.method != "HEAD":
                    async for chunk in upstream.content.iter_any():
                        await response.write(chunk)
                await response.write_eof()
                return response
        except Exception as exc:  # backend down / refused
            return web.Response(status=502, text=f"502: backend unavailable ({exc})\n")

    async def proxy_ws(request: web.Request) -> web.StreamResponse:
        if not authorized(request):
            return reject(request)
        client = web.WebSocketResponse(heartbeat=30)
        await client.prepare(request)
        try:
            async with request.app[SESSION].ws_connect(
                f"ws://{backend}{request.rel_url}", heartbeat=30, max_msg_size=0
            ) as upstream:

                async def pump(src, dst) -> None:
                    async for message in src:
                        if message.type == WSMsgType.TEXT:
                            await dst.send_str(message.data)
                        elif message.type == WSMsgType.BINARY:
                            await dst.send_bytes(message.data)
                        elif message.type in (WSMsgType.CLOSE, WSMsgType.CLOSING,
                                              WSMsgType.CLOSED, WSMsgType.ERROR):
                            break

                up = asyncio.create_task(pump(client, upstream))
                down = asyncio.create_task(pump(upstream, client))
                await asyncio.wait({up, down}, return_when=asyncio.FIRST_COMPLETED)
                for task in (up, down):
                    task.cancel()
        except Exception:
            pass
        finally:
            await client.close()
        return client

    app = web.Application(client_max_size=1024 ** 3)
    app.router.add_get("/ws", proxy_ws)
    app.router.add_route("*", "/{tail:.*}", proxy_http)
    app.on_startup.append(start_session)
    app.on_cleanup.append(close_session)
    return app


def main() -> int:
    parser = argparse.ArgumentParser(description="Basic-auth reverse proxy for notebook servers")
    parser.add_argument("--target-port", type=int, required=True, help="local service port (e.g. 8188)")
    parser.add_argument("--port", type=int, default=0, help="listen port (default: target + 1)")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--user", default=os.getenv("PROXY_USER", "admin"))
    parser.add_argument("--password", default=os.getenv("PROXY_PASSWORD", ""))
    args = parser.parse_args()

    if not args.password:
        print("error: set PROXY_PASSWORD or pass --password", file=sys.stderr)
        return 2

    port = args.port or args.target_port + 1
    print(f"auth proxy: 127.0.0.1:{port} -> 127.0.0.1:{args.target_port} (user={args.user})")
    web.run_app(build_app(args.target_port, args.user, args.password),
                host=args.host, port=port, print=None)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
