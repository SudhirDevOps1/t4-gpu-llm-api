# Personal AI Notebook Store & Multi-Cloud GPU Hub

Free-tier GPU notebooks for **Google Colab (Tesla T4, ~15 GB)** and **Kaggle (2× Tesla T4, ~30 GB)**, plus a small browser chat client and an interactive storefront.

[![Store](https://img.shields.io/badge/Notebook_Store-Live_Catalog-10b981?style=for-the-badge&logo=github)](store/index.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-6f42c1?style=for-the-badge)](LICENSE)
[![Colab](https://img.shields.io/badge/Google_Colab-Free_T4-F9AB00?style=for-the-badge&logo=googlecolab)](#quick-start-colab)
[![Kaggle](https://img.shields.io/badge/Kaggle-Dual_T4-20BEFF?style=for-the-badge&logo=kaggle)](#running-on-kaggle-manual-import)
[![Notebook guard](https://img.shields.io/badge/Notebooks-output--free-06b6d4?style=for-the-badge)](#verification-status)

---

## Read this first — what the repo actually is

Some older descriptions in this project overstated what the notebooks do. This README is the corrected version:

- The LLM server is **Ollama**, not a custom FastAPI/vLLM server. Ollama exposes an OpenAI-compatible `/v1` API itself.
- **No tensor parallelism.** Ollama splits layers across GPUs when a model does not fit; it does not shard tensors. Kaggle's second T4 usually stays idle with a 14B Q4 model.
- **T4 is Turing (SM 7.5).** FlashAttention-2 needs Ampere or newer, so it is not used anywhere. INT8/FP8 kernels advertised in old cards were not real.
- **Password-protected by default.** Ollama ignores `Authorization`, and ComfyUI has no auth at all, so both tunnels now pass through a Basic-auth reverse proxy. Gradio apps use `demo.launch(auth=...)` or Colab's login-gated port proxy.
- **Real weights, real work.** The video notebook runs `Wan-AI/Wan2.1-T2V-1.3B-Diffusers`; the QLoRA notebook trains an adapter; the RAG notebook calls a real LLM endpoint.
- **Licences are not all permissive.** SDXL-Turbo is non-commercial; ComfyUI core is GPL-3.0. See the table.

---

## 🛍️ Interactive storefront

👉 [**Open the notebook store**](store/index.html) — searchable, filterable cards with model specs, licences and launch links.

The root [`index.html`](index.html) redirects here; the browser chat client lives at [`colab_ai_chat.html`](colab_ai_chat.html).

---

## 📚 Notebook catalog

| # | Notebook | What really runs | Licence | VRAM | Launch |
|:--|:--|:--|:--|:--|:--|
| 01 | [T4 LLM Server](t4-gpu-llm-api.ipynb) ([Colab copy](colab/01_t4_gpu_llm_api.ipynb)) | Ollama + OpenAI `/v1`, Qwen2.5-Coder 7B / DeepSeek-R1 8B / Llama 3.2 3B, Q4 GGUF | Apache-2.0 / MIT | ~5 GB | [Colab](https://colab.research.google.com/github/SudhirDevOps1/t4-gpu-llm-api/blob/main/t4-gpu-llm-api.ipynb) |
| 02 | [Kokoro TTS](colab/02_zero_shot_voice_tts.ipynb) | Kokoro-82M, 8 preset voices, 24 kHz WAV — **preset TTS, no voice cloning** | Apache-2.0 | ~2.8 GB | [Colab](https://colab.research.google.com/github/SudhirDevOps1/t4-gpu-llm-api/blob/main/colab/02_zero_shot_voice_tts.ipynb) |
| 03 | [Chatterbox Hindi voice clone](colab/08_f5_chatterbox_hindi_voice.ipynb) | Resemble AI Chatterbox Multilingual, Hindi (Devanagari), zero-shot cloning, emotion/CFG controls | MIT (upstream) | ~3.5 GB | [Colab](https://colab.research.google.com/github/SudhirDevOps1/t4-gpu-llm-api/blob/main/colab/08_f5_chatterbox_hindi_voice.ipynb) |
| 04 | [SDXL-Turbo image studio](colab/03_qwen_image_gen_studio.ipynb) | `stabilityai/sdxl-turbo` FP16, 1–4 steps at 512×512 | **Stability AI Non-Commercial** | ~7 GB | [Colab](https://colab.research.google.com/github/SudhirDevOps1/t4-gpu-llm-api/blob/main/colab/03_qwen_image_gen_studio.ipynb) |
| 05 | [Wan2.1 video studio](colab/04_wan_ltx_video_studio.ipynb) | `WanPipeline` from `Wan-AI/Wan2.1-T2V-1.3B-Diffusers`, 480×832, 33 frames, FP16 + FP32 VAE, CPU offload | Apache-2.0 | ~13 GB peak | [Colab](https://colab.research.google.com/github/SudhirDevOps1/t4-gpu-llm-api/blob/main/colab/04_wan_ltx_video_studio.ipynb) |
| 06 | [ComfyUI cloud studio](colab/05_comfyui_cloud_studio.ipynb) | ComfyUI + ComfyUI-Manager on `127.0.0.1:8188` behind auth proxy `:8189` | GPL-3.0 (core) | 4–14 GB | [Colab](https://colab.research.google.com/github/SudhirDevOps1/t4-gpu-llm-api/blob/main/colab/05_comfyui_cloud_studio.ipynb) |
| 07 | [RAG knowledge agent](colab/06_rag_knowledge_agent.ipynb) | `all-MiniLM-L6-v2` + ChromaDB retrieval + **real** `/v1/chat/completions` call | Apache-2.0 | ~1.2 GB | [Colab](https://colab.research.google.com/github/SudhirDevOps1/t4-gpu-llm-api/blob/main/colab/06_rag_knowledge_agent.ipynb) |
| 08 | [QLoRA fine-tuning](colab/07_qlora_training_studio.ipynb) | Qwen2.5-0.5B-Instruct in NF4 + LoRA on 300 guanaco samples; adapter zip out | Apache-2.0 | ~4 GB | [Colab](https://colab.research.google.com/github/SudhirDevOps1/t4-gpu-llm-api/blob/main/colab/07_qlora_training_studio.ipynb) |
| 09 | [Kaggle dual T4 LLM](kaggle/01_dual_t4_llm_engine.ipynb) | Ollama on 2× T4 with auth proxy; layer splitting (not tensor parallel) | Apache-2.0 / MIT | ~9 GB | [Notebook file](kaggle/01_dual_t4_llm_engine.ipynb) |
| 10 | [Kaggle dual T4 ComfyUI](kaggle/02_comfyui_dual_t4.ipynb) | Same ComfyUI + auth proxy setup; ComfyUI uses one GPU at a time | GPL-3.0 (core) | 4–14 GB | [Notebook file](kaggle/02_comfyui_dual_t4.ipynb) |

> `t4-gpu-llm-api.ipynb` and `colab/01_t4_gpu_llm_api.ipynb` are byte-identical on purpose: the root file is the one linked by the Colab badge.

---

## Quick start (Colab)

### LLM API — notebook 01

1. Open the notebook, set **Runtime → Change runtime type → T4 GPU**, then run cells top to bottom.
2. **Cell 1** checks the GPU and prints a session fingerprint.
3. **Cell 2** installs Ollama, cloudflared and `aiohttp` (needed by the proxy).
4. **Cell 3** starts Ollama bound to `127.0.0.1:11434` with `OLLAMA_NUM_PARALLEL=1` and a 24 h keep-alive.
5. **Cell 4** writes `auth_proxy.py` from [`core/auth_proxy.py`](core/auth_proxy.py); **Cell 5** starts it on `127.0.0.1:11435`. A random session password is printed — save it.
6. **Cell 6** pulls the model selected in the form (`qwen2.5-coder:7b` by default).
7. **Cell 7** opens the Cloudflare tunnel to the **proxy**, and prints the `/v1` base URL plus the password.
8. **Cell 8** downloads `colab_ai_chat.html`; **Cell 9** has stop/debug utilities.

Use the password as the API key in any OpenAI-compatible client:

```bash
curl https://YOUR-TUNNEL.trycloudflare.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR-SESSION-PASSWORD" \
  -d '{"model": "qwen2.5-coder:7b", "messages": [{"role": "user", "content": "Hello"}]}'
```

The proxy also accepts HTTP Basic (`admin` / password), so browsers and ComfyUI work too.

### Other notebooks

- **02 / 03 / 04 / 06 / 07** expose Gradio with `demo.launch(share=True, auth=studio_auth())`. Set a `STUDIO_PASSWORD` in Colab userdata (or Kaggle secrets) to control the password; otherwise a random one is printed per run.
- **05 (ComfyUI)** keeps ComfyUI on localhost and tunnels only the auth proxy. The browser shows a native login prompt; without the password the proxy returns `401` and ComfyUI-Manager is unreachable.
- **08 (Chatterbox)** runs the third-party `app.py` on `127.0.0.1:7860` and opens it through Colab's login-gated port proxy. It deliberately does **not** use `--share`, because that app has no password option.
- **05 (video)** needs a fresh runtime with ~15 GB free VRAM and downloads ~13 GB of weights on the first run. A 33-frame clip takes roughly 10–25 minutes on a free T4.

### Running on Kaggle (manual import)

Kaggle has no "open this GitHub notebook" button, and `kaggle.com/code/new` only opens a blank notebook. Import manually:

1. Create a new Kaggle notebook: **File → New Notebook**.
2. **Settings** → Accelerator: **GPU T4 x2**; **Internet: On**.
3. **File → Import Notebook → GitHub** and paste the repo URL, or download the `.ipynb` from this repo and use **File → Import Notebook → Upload**.
4. Pick `kaggle/01_dual_t4_llm_engine.ipynb` or `kaggle/02_comfyui_dual_t4.ipynb`, then run cells in order.
5. Put `STUDIO_PASSWORD` in **Kaggle Secrets** if you want a fixed Gradio/proxy password.

Quota on the free tier: 9 h per session, 30 h per week. Expect both GPUs to be visible, but only one to be busy.

---

## 🔐 Security model

Public `trycloudflare.com` URLs are random, **but anyone with the link can reach them**. Auth is what makes them safe.

| Surface | Before | Now |
|:--|:--|:--|
| Ollama tunnel | Open `/v1`, any bearer token accepted | Ollama bound to `127.0.0.1:11434`; only `11435` (Basic-auth proxy) is tunnelled |
| ComfyUI tunnel | Open `:8188`, ComfyUI-Manager reachable by anyone | ComfyUI on `127.0.0.1:8188`; only `:8189` (Basic-auth proxy) is tunnelled |
| Gradio demos | `share=True`, no password | `auth=studio_auth()` or Colab's login-gated port proxy |
| Secrets | Pasted into cells / printed in outputs | Colab `userdata` or Kaggle `UserSecretsClient`, with a random per-session fallback |

Notes:

- [`core/auth_proxy.py`](core/auth_proxy.py) is a small aiohttp reverse proxy. It accepts `Authorization: Basic base64(admin:password)` or `Authorization: Bearer password`, forwards HTTP (including streaming responses) and WebSockets, and returns `401` otherwise. Its source is copied into notebooks 01, 05 and the Kaggle notebooks so they work immediately after import.
- `core/` is a **reference/helper folder**, not an enforced framework. The notebooks have their own inline copies of the fingerprint, secret and VRAM helpers; importing `core/` is not required.
- Passwords generated by `secrets.token_urlsafe(9)` are printed once in the cell output. Since notebooks are committed with no saved outputs, they do not end up in Git.
- Basic auth is still plaintext over the tunnel — Cloudflare terminates TLS, so the hop from browser to proxy is HTTPS. Do not reuse an important password here.
- `scripts/clean_notebooks.py --check` runs in CI to guarantee that no notebook is committed with saved outputs (which could contain tokens, audio or tracebacks).

---

## 📂 Repository layout

```text
.
├── README.md                          # this file
├── LICENSE                            # MIT for repo code; upstream models keep their own licences
├── index.html                         # redirects to store/index.html
├── colab_ai_chat.html                 # standalone browser chat client
├── store/index.html                   # interactive notebook storefront
├── core/
│   ├── auth_proxy.py                  # tested Basic/Bearer HTTP+WS reverse proxy
│   ├── security.py                    # reference secret helper (Colab/Kaggle/env/getpass)
│   ├── instance.py                    # reference session fingerprint helper
│   ├── vram_guard.py                  # reference VRAM/env helper (not model parallelism)
│   └── __init__.py
├── scripts/clean_notebooks.py         # strip / verify notebook outputs
├── .github/workflows/notebook-guard.yml
├── colab/                             # 8 Colab notebooks (01–08)
├── kaggle/                            # 2 Kaggle notebooks
├── goldfish_review_report.md          # historical audit notes
└── .gitignore
```

---

## Verification status

Honest summary of what has and has not been checked in this pass:

**Checked locally**

- All 11 notebooks are valid JSON and every Python code cell compiles (magic lines like `!pip` are ignored by the checker).
- `t4-gpu-llm-api.ipynb` and `colab/01_t4_gpu_llm_api.ipynb` are byte-identical.
- `python scripts/clean_notebooks.py --check` passes for 12 notebooks.
- `core/auth_proxy.py` was integration-tested against a local aiohttp backend: 401 without auth, 200 for Basic and Bearer, 401 for a wrong password, POST body forwarding, streaming responses, and WebSocket text + binary echo all passed.
- `store/index.html` JavaScript parses with `node --check`; the 10 catalog entries and their links were evaluated and checked. No `kaggle.com/code/new` placeholders remain.

**Not checked (needs a real runtime)**

- Wan2.1 inference, Kokoro, SDXL-Turbo and Chatterbox were not run on a GPU here. The Wan API was checked against the current diffusers docs; expect multi-minute runtimes.
- TRL `SFTConfig` / `processing_class` arguments and the pinned dependency stack were not executed.
- The auth proxy was not end-to-end tested against real Ollama/ComfyUI binaries — only against a local stand-in server.
- Cloudflare quick tunnels and Colab/Kaggle secrets need a live session.

If something fails on a real runtime, open an issue with the notebook name, platform, and full traceback.

---

## 🤝 Contributing

1. Keep notebook outputs empty (`python scripts/clean_notebooks.py` before committing).
2. Do not commit tokens, passwords, or generated media.
3. When changing a model claim, change the notebook, `README.md`, and `store/index.html` together.

---

## 📄 Licence

[MIT](LICENSE) for the code, notebooks and pages in this repository. This does **not** relicense upstream model weights or checkpoints: SDXL-Turbo is non-commercial, ComfyUI core is GPL-3.0, and each Hugging Face model card governs its own weights and outputs.
