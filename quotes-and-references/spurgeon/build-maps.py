#!/usr/bin/env python3
"""
Build three maps from converted Spurgeon sermon text:
  maps/scripture.md  — Scripture references → sermons
  maps/subject.md    — Subjects/topics → sermons
  maps/theology.md   — Theological themes → sermons (grouped)

Purpose: locating Spurgeon quotes while writing, and verifying attributed quotes.
Not for reproduction or plagiarism.
"""

import re
import json
from pathlib import Path
from collections import defaultdict

SERMONS_DIR = Path(__file__).parent / "sermons"
INDEXES_DIR = SERMONS_DIR / "indexes"
MAPS_DIR = Path(__file__).parent / "maps"
MAPS_DIR.mkdir(exist_ok=True)

# ── Theological theme groupings ───────────────────────────────────────────────
# Map keyword patterns in subject headings to broad theological categories.

THEOLOGY_MAP = {
    "Christology": [
        "christ", "jesus", "son of god", "son of man", "lord", "messiah",
        "savior", "saviour", "incarnation", "virgin birth", "hypostatic",
        "mediator", "redeemer", "lamb of god", "king", "priest", "prophet",
        "second advent", "second coming", "ascension", "resurrection of christ",
        "names of christ", "person of christ", "work of christ",
    ],
    "Soteriology": [
        "salvation", "atonement", "justification", "sanctification",
        "redemption", "forgiveness", "pardon", "reconciliation", "propitiation",
        "substitution", "imputation", "adoption", "regeneration", "new birth",
        "conversion", "repentance", "faith", "grace", "election", "predestination",
        "effectual calling", "perseverance", "assurance", "free grace",
        "free will", "security", "eternal life", "born again",
    ],
    "Pneumatology": [
        "holy spirit", "holy ghost", "spirit of god", "comforter", "paraclete",
        "indwelling", "filling of the spirit", "gifts of the spirit",
        "fruit of the spirit", "spiritual gifts", "tongues", "baptism of the spirit",
    ],
    "Doctrine of God": [
        "sovereignty", "omnipotence", "omniscience", "omnipresence",
        "immutability", "holiness of god", "love of god", "wrath of god",
        "justice of god", "mercy of god", "trinity", "father", "godhead",
        "attributes of god", "providence", "foreknowledge", "decrees",
        "eternal purpose", "creator", "creation",
    ],
    "Scripture & Revelation": [
        "scripture", "bible", "word of god", "inspiration", "infallibility",
        "preaching", "gospel", "revelation", "truth", "text",
    ],
    "Ecclesiology": [
        "church", "baptism", "lord's supper", "communion", "ordinance",
        "worship", "prayer", "sabbath", "ministry", "deacon", "elder",
        "membership", "discipline", "fellowship", "congregation",
        "metropolitan tabernacle", "new park street",
    ],
    "Eschatology": [
        "heaven", "hell", "death", "resurrection", "judgment", "eternity",
        "eternal", "last things", "future", "millennium", "second coming",
        "rapture", "glory", "immortality", "soul", "final",
    ],
    "Christian Life": [
        "prayer", "devotion", "obedience", "suffering", "trial", "comfort",
        "joy", "peace", "hope", "love", "humility", "pride", "temptation",
        "sin", "holiness", "consecration", "service", "witness", "evangelism",
        "missions", "giving", "stewardship", "thankfulness", "gratitude",
        "patience", "courage", "fear", "anxiety", "trust",
    ],
    "Evangelism & The Lost": [
        "sinner", "lost", "unconverted", "worldly", "unbelief", "invitation",
        "call", "seek", "seek the lord", "come to christ", "whosoever",
        "perishing", "urgent", "soul-winning", "awakening", "revival",
    ],
}

# ── Parse existing index files ────────────────────────────────────────────────

def parse_scripture_index(md_path: Path) -> list[dict]:
    """
    Parse a converted scripture index (NT or OT) into structured records.
    Returns list of {reference, volume, title, sermon_no}.
    """
    if not md_path.exists():
        return []
    text = md_path.read_text(encoding="utf-8")
    records = []
    # Pattern: "Book ch:v  Volume  Title (Sermon #N)  N"
    # The columns are: Scripture | Volume | Link | Sermon Number
    line_pattern = re.compile(
        r'^([A-Z][A-Za-z0-9 .:;\-,]+?)\s{2,}(\d+)\s{2,}(.+?)\s{2,}(\d+)\s*$',
        re.MULTILINE
    )
    for m in line_pattern.finditer(text):
        ref = m.group(1).strip()
        title = m.group(3).strip()
        try:
            sermon_no = int(m.group(4).strip())
        except ValueError:
            continue
        records.append({"reference": ref, "title": title, "sermon_no": sermon_no})
    return records


def parse_subject_index(md_path: Path) -> list[dict]:
    """
    Parse the general subject/title index (chstix).
    Returns list of {subject, sermon_no, title}.
    """
    if not md_path.exists():
        return []
    text = md_path.read_text(encoding="utf-8")
    records = []
    # Lines like: "Subject Title ..... N" or "Title  VolumeNo  SermonNo"
    # chstix format: "Title  Vol  Sermon#  No"
    line_pattern = re.compile(
        r'^(.+?)\s{2,}(\d+)\s{2,}(.+?)\s{2,}(\d+)\s*$',
        re.MULTILINE
    )
    for m in line_pattern.finditer(text):
        subject = m.group(1).strip()
        title = m.group(3).strip()
        try:
            sermon_no = int(m.group(4).strip())
        except ValueError:
            continue
        if len(subject) > 2 and not subject.startswith("Page"):
            records.append({"subject": subject, "title": title, "sermon_no": sermon_no})
    return records


# ── Extract sermon metadata from converted .md files ─────────────────────────

def extract_sermon_metadata(md_path: Path) -> dict | None:
    """Pull title, scripture, and date from a sermon .md file."""
    try:
        text = md_path.read_text(encoding="utf-8", errors="ignore")[:2000]
    except Exception:
        return None

    sermon_no = None
    m = re.search(r'Sermon\s+#(\d+)', text, re.IGNORECASE)
    if m:
        sermon_no = int(m.group(1))

    title = None
    # Title is typically an ALL-CAPS line after the sermon number header
    m = re.search(r'NO\.\s*\d+\s*\n+([A-Z][A-Z\s\'\-\,\!\?]+)\n', text)
    if m:
        title = m.group(1).strip().title()

    date = None
    m = re.search(r'(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)\s+\d+,?\s+\d{4}', text, re.IGNORECASE)
    if m:
        date = m.group(0).strip()

    scripture_text = None
    # Quoted scripture usually in quotes on its own line near the top
    m = re.search(r'"([^"]{10,120})"\s*\n\s*([A-Z][a-z]+ \d+:\d+)', text)
    if m:
        scripture_text = f"{m.group(1).strip()} — {m.group(2).strip()}"

    return {
        "sermon_no": sermon_no,
        "title": title,
        "date": date,
        "scripture_text": scripture_text,
        "file": md_path.name,
    }


# ── Build and write maps ──────────────────────────────────────────────────────

def build_scripture_map():
    print("Building scripture map...")
    ot_path = INDEXES_DIR / "sindex_ot.md"
    nt_path = INDEXES_DIR / "sindex_nt.md"

    ot_records = parse_scripture_index(ot_path)
    nt_records = parse_scripture_index(nt_path)

    def records_to_md(records: list, testament: str) -> str:
        # Group by book
        by_book = defaultdict(list)
        for r in records:
            parts = r["reference"].split()
            book = parts[0] if parts else "Unknown"
            by_book[book].append(r)

        lines = [f"# Spurgeon Sermons — {testament} Scripture Index\n"]
        lines.append("*For locating and verifying Spurgeon quotes. Not for reproduction.*\n")
        lines.append(f"**{len(records)} entries**\n")
        for book in sorted(by_book.keys()):
            lines.append(f"\n## {book}\n")
            lines.append("| Reference | Sermon No. | Title |")
            lines.append("|-----------|------------|-------|")
            for r in sorted(by_book[book], key=lambda x: x["reference"]):
                lines.append(f"| {r['reference']} | [{r['sermon_no']}](../sermons/chs{r['sermon_no']}.md) | {r['title']} |")
        return "\n".join(lines)

    (MAPS_DIR / "scripture-ot.md").write_text(records_to_md(ot_records, "Old Testament"), encoding="utf-8")
    (MAPS_DIR / "scripture-nt.md").write_text(records_to_md(nt_records, "New Testament"), encoding="utf-8")
    print(f"  OT: {len(ot_records)} entries | NT: {len(nt_records)} entries")


def build_subject_map():
    print("Building subject map...")
    chstix_path = INDEXES_DIR / "chstix.md"
    records = parse_subject_index(chstix_path)

    # Group alphabetically by first letter
    by_letter = defaultdict(list)
    for r in records:
        letter = r["subject"][0].upper() if r["subject"] else "#"
        if not letter.isalpha():
            letter = "#"
        by_letter[letter].append(r)

    lines = ["# Spurgeon Sermons — Subject Index\n"]
    lines.append("*For locating and verifying Spurgeon quotes. Not for reproduction.*\n")
    lines.append(f"**{len(records)} entries**\n")
    lines.append("\n## Quick Navigation\n")
    nav = " | ".join(f"[{l}](#{l.lower()})" for l in sorted(by_letter.keys()))
    lines.append(nav + "\n")

    for letter in sorted(by_letter.keys()):
        lines.append(f"\n## {letter}\n")
        lines.append("| Subject | Sermon No. | Title |")
        lines.append("|---------|------------|-------|")
        for r in sorted(by_letter[letter], key=lambda x: x["subject"].lower()):
            lines.append(f"| {r['subject']} | [{r['sermon_no']}](../sermons/chs{r['sermon_no']}.md) | {r['title']} |")

    (MAPS_DIR / "subject.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"  {len(records)} subject entries written")


def build_theology_map():
    print("Building theology map...")
    chstix_path = INDEXES_DIR / "chstix.md"
    records = parse_subject_index(chstix_path)

    # Also pull subject records from NT/OT indexes
    ot_records = parse_scripture_index(INDEXES_DIR / "sindex_ot.md")
    nt_records = parse_scripture_index(INDEXES_DIR / "sindex_nt.md")
    all_titles = [(r["title"], r["sermon_no"]) for r in records]
    all_titles += [(r["title"], r["sermon_no"]) for r in ot_records + nt_records]

    # Deduplicate by sermon number per theme
    theme_sermons: dict[str, dict[int, str]] = {theme: {} for theme in THEOLOGY_MAP}

    for title, sermon_no in all_titles:
        title_lower = title.lower()
        for theme, keywords in THEOLOGY_MAP.items():
            for kw in keywords:
                if kw in title_lower:
                    theme_sermons[theme][sermon_no] = title
                    break

    # Also scan subject field
    for r in records:
        subject_lower = r["subject"].lower()
        for theme, keywords in THEOLOGY_MAP.items():
            for kw in keywords:
                if kw in subject_lower:
                    theme_sermons[theme][r["sermon_no"]] = r["title"]
                    break

    lines = ["# Spurgeon Sermons — Theological Theme Index\n"]
    lines.append("*For locating and verifying Spurgeon quotes. Not for reproduction.*\n")
    lines.append("Grouped by theological category, derived from the subject and scripture indexes.\n")

    total = sum(len(v) for v in theme_sermons.values())
    lines.append(f"**{total} theme-sermon associations across {len(THEOLOGY_MAP)} categories**\n")

    lines.append("\n## Categories\n")
    for theme in THEOLOGY_MAP:
        count = len(theme_sermons[theme])
        anchor = theme.lower().replace(" ", "-").replace("&", "").replace("  ", "-")
        lines.append(f"- [{theme}](#{anchor}) ({count} sermons)")

    for theme in THEOLOGY_MAP:
        sermons = theme_sermons[theme]
        lines.append(f"\n## {theme}\n")
        if not sermons:
            lines.append("*No indexed sermons matched this theme.*\n")
            continue
        lines.append("| Sermon No. | Title |")
        lines.append("|------------|-------|")
        for sno in sorted(sermons.keys()):
            lines.append(f"| [{sno}](../sermons/chs{sno}.md) | {sermons[sno]} |")

    (MAPS_DIR / "theology.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"  {total} theme associations written across {len(THEOLOGY_MAP)} themes")


def write_maps_readme():
    content = """# Spurgeon Sermon Maps

Reference indexes for locating and verifying Spurgeon quotes during sermon writing.

> These maps are for **quote location and verification only** — not for reproduction or plagiarism.
> Always cite: *"Quote." — C.H. Spurgeon, Sermon Title, No. N, Date.*

## Maps

| File | Contents |
|------|----------|
| [scripture-ot.md](scripture-ot.md) | OT passages → sermons that expound them |
| [scripture-nt.md](scripture-nt.md) | NT passages → sermons that expound them |
| [subject.md](subject.md) | Alphabetical subject/topic index |
| [theology.md](theology.md) | Theological themes: Christology, Soteriology, Pneumatology, etc. |

## How to Use

**Finding a quote on a topic:**
1. Open `subject.md` or `theology.md`
2. Find the topic → note the sermon number(s)
3. Open `../sermons/chsN.md` and search for the quote

**Verifying an attributed quote:**
1. If you know the scripture text, use `scripture-nt.md` or `scripture-ot.md`
2. Find the passage → check the listed sermons
3. Open the sermon file and confirm the exact wording

**Citation format:**
> "Quote here." — C.H. Spurgeon, *Sermon Title*, No. N, Date
"""
    (MAPS_DIR / "README.md").write_text(content, encoding="utf-8")


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Building Spurgeon sermon maps ===\n")
    build_scripture_map()
    build_subject_map()
    build_theology_map()
    write_maps_readme()
    print("\nDone. Maps written to maps/")
