#!/usr/bin/env python3
"""
Convert all Spurgeon sermon PDFs to Markdown, then remove the PDFs.
Runs from the spurgeon/ directory.
"""

import fitz  # pymupdf
import os
import sys
import re
import json
from pathlib import Path

SERMONS_DIR = Path(__file__).parent / "sermons"
INDEXES_DIR = SERMONS_DIR / "indexes"
MAPS_DIR = Path(__file__).parent / "maps"

# ── helpers ──────────────────────────────────────────────────────────────────

def pdf_to_markdown(pdf_path: Path) -> str:
    """Extract text from a PDF and return it as clean markdown."""
    doc = fitz.open(str(pdf_path))
    pages = []
    for page in doc:
        text = page.get_text()
        # Normalize excessive blank lines
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = text.strip()
        if text:
            pages.append(text)
    doc.close()
    return "\n\n---\n\n".join(pages)


def convert_directory(directory: Path, label: str):
    pdfs = sorted(directory.glob("*.pdf"))
    total = len(pdfs)
    print(f"\n{label}: {total} PDFs to convert")
    failed = []
    for i, pdf in enumerate(pdfs, 1):
        md_path = pdf.with_suffix(".md")
        if md_path.exists():
            pdf.unlink()
            continue
        try:
            md_content = pdf_to_markdown(pdf)
            md_path.write_text(md_content, encoding="utf-8")
            pdf.unlink()
            if i % 100 == 0 or i == total:
                print(f"  {i}/{total} done", flush=True)
        except Exception as e:
            print(f"  ERROR on {pdf.name}: {e}", flush=True)
            failed.append(pdf.name)
    if failed:
        print(f"  Failed: {failed}")
    else:
        print(f"  All {label} converted and PDFs removed.")


# ── main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    os.makedirs(MAPS_DIR, exist_ok=True)

    print("=== Converting Spurgeon sermons to Markdown ===")
    convert_directory(SERMONS_DIR, "Sermons")
    convert_directory(INDEXES_DIR, "Indexes")

    print("\nDone. Run build-maps.py next to build scripture/subject/theology maps.")
