#!/usr/bin/env python3
"""
Download John MacArthur sermons from gty.org and save as Markdown.
Phase 1: Collect all sermon metadata via the year-based API (fast).
Phase 2: Fetch individual pages for full transcripts.

Source: Grace to You (https://www.gty.org)
"""

import requests
import re
import json
import time
import sys
from pathlib import Path
from bs4 import BeautifulSoup

MACARTHUR_DIR = Path(__file__).parent
SERMONS_DIR = MACARTHUR_DIR / "sermons"
SERMONS_DIR.mkdir(exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; research/1.0)",
    "Content-Type": "application/json",
}
PAGE_HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; research/1.0)",
}

# ── Phase 1: Collect metadata via year API ────────────────────────────────────

def fetch_year_sermons(year: int) -> list[dict]:
    """Fetch all sermon metadata for a given year from the GTY API."""
    try:
        r = requests.post(
            "https://www.gty.org/api/core-non-user",
            headers=HEADERS,
            json={"relativePath": f"/api/website/sermons-by-field?locale=en&year={year}&start=0&limit=500"},
            timeout=20,
        )
        r.raise_for_status()
        data = r.json()
        return [s for s in data if isinstance(s, dict) and s.get("type") == "sermon"]
    except Exception as e:
        print(f"  Error fetching {year}: {e}")
        return []


def collect_all_metadata() -> list[dict]:
    """Collect metadata for all MacArthur sermons (1969–2026)."""
    all_sermons = []
    for year in range(1969, 2027):
        sermons = fetch_year_sermons(year)
        if sermons:
            print(f"  {year}: {len(sermons)} sermons")
            all_sermons.extend(sermons)
        time.sleep(0.4)
    return all_sermons


# ── Phase 2: Fetch transcript from individual sermon page ─────────────────────

def extract_transcript_from_page(code: str, slug: str) -> str:
    """Fetch the individual sermon page and extract the full transcript HTML."""
    url = f"https://www.gty.org/sermons/{code}/{slug}"
    try:
        r = requests.get(url, headers=PAGE_HEADERS, timeout=20)
        r.raise_for_status()
    except Exception as e:
        return f"[Transcript unavailable: {e}]"

    soup = BeautifulSoup(r.text, "html.parser")
    all_script = "".join(s.string or "" for s in soup.find_all("script"))
    # Unescape JSON
    unescaped = (all_script
                 .replace('\\"', '"')
                 .replace('\\n', '\n')
                 .replace('\\r', '\r')
                 .replace('\\/', '/'))

    # Transcript is in RSC streaming data as HTML paragraphs
    # Pattern: series of <p>...</p> blocks with sermon content
    # Find the first substantial text block (>500 chars) that looks like sermon text
    html_blocks = re.findall(r'\\u003cp\\u003e(.*?)\\u003c/p\\u003e', all_script, re.DOTALL)
    if not html_blocks:
        # Try the unescaped version
        p_matches = re.findall(r'<p>(.*?)</p>', unescaped, re.DOTALL)
        if p_matches:
            # Filter to substantial paragraphs (not nav/metadata)
            content = "\n\n".join(p for p in p_matches if len(p) > 100)
            if content:
                return content

    if html_blocks:
        # Decode the \u003c escaped HTML
        decoded = []
        for block in html_blocks:
            text = (block
                    .replace("\\u003c", "<")
                    .replace("\\u003e", ">")
                    .replace("\\u0026", "&")
                    .replace("\\u2019", "\u2019")
                    .replace("\\u2018", "\u2018")
                    .replace("\\u201c", "\u201c")
                    .replace("\\u201d", "\u201d")
                    .replace("\\u2014", "\u2014")
                    .replace("\\u2013", "\u2013"))
            # Strip inner HTML tags
            clean = re.sub(r'<[^>]+>', ' ', text).strip()
            if len(clean) > 80:
                decoded.append(clean)
        if decoded:
            return "\n\n".join(decoded)

    # Fallback: try the meta description
    meta = soup.find("meta", {"name": "description"})
    if meta:
        return f"[Partial transcript from description]\n\n{meta.get('content', '')}"

    return "[Transcript not extracted]"


# ── Helpers ───────────────────────────────────────────────────────────────────

def format_scripture(scripture: str) -> str:
    """Clean up scripture reference formatting."""
    return scripture.strip() if scripture else ""


def get_primary_series(series_list: list) -> tuple[str, str]:
    """Get the primary series title and code."""
    if not series_list:
        return "", ""
    s = series_list[0]
    return s.get("title", ""), s.get("slug", "")


def sermon_to_markdown(meta: dict, transcript: str) -> str:
    """Format a sermon as a Markdown document."""
    series_title, series_slug = get_primary_series(meta.get("series", []))
    scripture = format_scripture(meta.get("scripture", ""))
    date = meta.get("date", "")
    code = meta.get("code", "")
    slug = meta.get("slug", "")
    title = meta.get("title", slug.replace("-", " ").title())
    url = f"https://www.gty.org/sermons/{code}/{slug}"

    lines = [
        f"# {title}",
        f"\n**Scripture:** {scripture or '(see transcript)'}",
        f"**Series:** {series_title or 'Standalone'}",
        f"**Date:** {date}",
        f"**Code:** {code}",
        f"**Source:** [{url}]({url})",
        "\n---\n",
        transcript or "[No transcript]",
    ]
    return "\n".join(lines)


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    metadata_file = MACARTHUR_DIR / "sermon-metadata.json"

    # Phase 1: collect metadata
    if metadata_file.exists():
        print("Loading existing metadata...")
        all_sermons = json.loads(metadata_file.read_text())
        print(f"  {len(all_sermons)} sermons loaded")
    else:
        print("Phase 1: Collecting metadata from GTY API (1969–2026)...")
        all_sermons = collect_all_metadata()
        # Save metadata (without transcripts)
        slim = [{k: v for k, v in s.items() if k not in ("audio", "coverImage", "headerImage", "altImage", "youtube", "youtubeAudio", "live", "sync")}
                for s in all_sermons]
        metadata_file.write_text(json.dumps(slim, indent=2), encoding="utf-8")
        print(f"\nPhase 1 complete: {len(all_sermons)} sermons")

    # Phase 2: download individual sermon pages with transcripts
    print(f"\nPhase 2: Downloading {len(all_sermons)} sermon transcripts...")
    saved = skipped = errors = 0
    meta_records = []  # for map building (no transcript)

    for i, sermon in enumerate(all_sermons, 1):
        code = sermon.get("code", "")
        slug = sermon.get("slug", "")
        if not code or not slug:
            errors += 1
            continue

        # File path uses code+slug to avoid name collisions
        safe_name = f"{code}_{slug}".replace("/", "-")
        md_path = SERMONS_DIR / f"{safe_name}.md"
        meta_path = SERMONS_DIR / f"{safe_name}.json"

        # Build meta record for maps
        series_title, series_slug = get_primary_series(sermon.get("series", []))
        meta_rec = {
            "code": code,
            "slug": slug,
            "title": sermon.get("title", ""),
            "scripture": format_scripture(sermon.get("scripture", "")),
            "series": series_title,
            "series_slug": series_slug,
            "date": sermon.get("date", ""),
            "topics": sermon.get("topics", ""),
            "url": f"https://www.gty.org/sermons/{code}/{slug}",
            "filename": f"{safe_name}.md",
        }
        meta_records.append(meta_rec)

        if md_path.exists():
            skipped += 1
        else:
            transcript = extract_transcript_from_page(code, slug)
            md_path.write_text(sermon_to_markdown(sermon, transcript), encoding="utf-8")
            meta_path.write_text(json.dumps(meta_rec, indent=2), encoding="utf-8")
            saved += 1
            time.sleep(0.5)

        if i % 100 == 0 or i == len(all_sermons):
            print(f"  {i}/{len(all_sermons)} — saved: {saved}, skipped: {skipped}, errors: {errors}", flush=True)

    # Save combined metadata for maps
    combined = MACARTHUR_DIR / "sermon-metadata-full.json"
    combined.write_text(json.dumps(meta_records, indent=2), encoding="utf-8")

    print(f"\nDone. {saved} saved, {skipped} already existed, {errors} errors.")
    print(f"Combined metadata: sermon-metadata-full.json")
