#!/usr/bin/env python3
"""Strip saved outputs from Jupyter notebooks.

Notebook outputs (base64 audio, embedded HTML, tracebacks) bloat the repository
and can leak tokens or private data from a previous run. Every notebook in this
repository is committed with ``outputs: []`` and ``execution_count: null``.

Usage:
    python scripts/clean_notebooks.py                 # clean all repo notebooks
    python scripts/clean_notebooks.py --check         # CI mode: exit 1 if an output is saved
    python scripts/clean_notebooks.py a.ipynb b.ipynb # only the given files

No third-party dependencies required.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".ipynb_checkpoints", "node_modules"}


def product_notebooks() -> list[Path]:
    """Root-level notebooks plus every notebook under colab/ and kaggle/."""
    found: list[Path] = []
    for base in (ROOT, ROOT / "colab", ROOT / "kaggle"):
        if not base.is_dir():
            continue
        found.extend(sorted(p for p in base.glob("*.ipynb") if p.is_file()))
    return sorted(set(found))


def dirty_cells(nb: dict) -> list[int]:
    return [
        i
        for i, cell in enumerate(nb.get("cells", []))
        if cell.get("cell_type") == "code"
        and (cell.get("outputs") or cell.get("execution_count") is not None)
    ]


def load(path: Path) -> tuple[dict, str]:
    raw = path.read_bytes()
    newline = "\r\n" if b"\r\n" in raw else "\n"
    return json.loads(raw.decode("utf-8")), newline


def save(path: Path, nb: dict, newline: str) -> None:
    with path.open("w", encoding="utf-8", newline=newline) as fh:
        json.dump(nb, fh, ensure_ascii=False, indent=1)
        fh.write("\n")


def strip(path: Path) -> tuple[int, int, int]:
    """Remove outputs in place. Returns (cells_cleaned, bytes_before, bytes_after)."""
    before = path.stat().st_size
    nb, newline = load(path)
    cells = 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "code":
            if cell.get("outputs") or cell.get("execution_count") is not None:
                cells += 1
            cell["outputs"] = []
            cell["execution_count"] = None
    if cells:
        save(path, nb, newline)
    return cells, before, path.stat().st_size


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Do not write. Exit 1 if any notebook still has saved outputs.",
    )
    args = parser.parse_args()

    targets = [p.resolve() for p in args.paths] if args.paths else product_notebooks()
    targets = [p for p in targets if p.is_file() and not SKIP_DIRS.intersection(p.parts)]

    if not targets:
        print("No notebooks found.", file=sys.stderr)
        return 1

    offenders: list[tuple[Path, list[int]]] = []
    cleaned = 0

    for path in targets:
        try:
            nb, _ = load(path)
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            print(f"SKIP  {path.relative_to(ROOT)}: not valid JSON ({exc})", file=sys.stderr)
            return 1

        dirty = dirty_cells(nb)
        if not dirty:
            continue

        if args.check:
            offenders.append((path, dirty))
            continue

        cells, before, after = strip(path)
        cleaned += 1
        print(
            f"CLEAN {path.relative_to(ROOT)}: {cells} cell(s), "
            f"{before / 1024:,.0f} KB -> {after / 1024:,.0f} KB"
        )

    if args.check:
        if offenders:
            print("\nSaved outputs found (run: python scripts/clean_notebooks.py):", file=sys.stderr)
            for path, dirty in offenders:
                print(f"  {path.relative_to(ROOT)}: cells {dirty}", file=sys.stderr)
            return 1
        print(f"OK: {len(targets)} notebook(s) committed output-free.")
        return 0

    if cleaned:
        print(f"\nDone: {cleaned} notebook(s) cleaned.")
    else:
        print(f"Nothing to do: {len(targets)} notebook(s) already output-free.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
