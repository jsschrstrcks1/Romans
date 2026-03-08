#!/usr/bin/env python3
"""
Build three reference maps from downloaded John MacArthur sermons:
  maps/scripture.md  — Scripture passages → sermons, by book
  maps/subject.md    — Series/topics → sermons
  maps/theology.md   — Theological themes → sermons

Purpose: locating MacArthur quotes while writing, and verifying attributed quotes.
Not for reproduction. Short quotes with proper citation only.
"""

import json
import re
from pathlib import Path
from collections import defaultdict

MACARTHUR_DIR = Path(__file__).parent
SERMONS_DIR = MACARTHUR_DIR / "sermons"
MAPS_DIR = MACARTHUR_DIR / "maps"
MAPS_DIR.mkdir(exist_ok=True)

METADATA_FILE = MACARTHUR_DIR / "sermon-metadata-full.json"

# ── Bible book ordering ────────────────────────────────────────────────────────

OT_BOOKS = [
    "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy",
    "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel", "1 Kings", "2 Kings",
    "1 Chronicles", "2 Chronicles", "Ezra", "Nehemiah", "Esther", "Job",
    "Psalms", "Proverbs", "Ecclesiastes", "Song of Solomon", "Isaiah", "Jeremiah",
    "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", "Obadiah",
    "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi",
]
NT_BOOKS = [
    "Matthew", "Mark", "Luke", "John", "Acts",
    "Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians",
    "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians",
    "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews",
    "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John",
    "Jude", "Revelation",
]
ALL_BOOKS = OT_BOOKS + NT_BOOKS

# ── Theological themes ─────────────────────────────────────────────────────────

THEOLOGY_MAP = {
    "Christology": [
        "christ", "jesus", "son of god", "son of man", "lord", "messiah",
        "savior", "incarnation", "mediator", "lamb", "cross", "crucifixion",
        "resurrection", "ascension", "transfiguration", "atonement", "priesthood",
        "advent", "coming", "second coming", "virgin birth", "deity", "humanity",
    ],
    "Soteriology": [
        "salvation", "justification", "sanctification", "redemption", "reconciliation",
        "forgiveness", "propitiation", "imputation", "adoption", "regeneration",
        "repentance", "faith", "election", "predestination", "grace", "perseverance",
        "assurance", "conversion", "effectual calling", "glorification",
    ],
    "Doctrine of God": [
        "sovereignty", "holiness", "love", "justice", "mercy", "wrath", "trinity",
        "attributes", "providence", "foreknowledge", "decrees", "omniscience",
        "omnipotence", "omnipresence", "immutability",
    ],
    "Scripture & Revelation": [
        "scripture", "word of god", "inspiration", "inerrancy", "authority",
        "bible", "preaching", "exposition", "hermeneutic", "interpretation",
        "revelation", "canon", "sufficiency",
    ],
    "Pneumatology": [
        "holy spirit", "spirit", "pentecost", "gifts", "spiritual gifts",
        "tongues", "fruit of the spirit", "filling", "charismatic",
        "baptism of the spirit", "indwelling",
    ],
    "Ecclesiology": [
        "church", "baptism", "lord's supper", "worship", "prayer", "elder",
        "deacon", "discipline", "fellowship", "mission", "preaching", "ministry",
        "pastor", "leadership", "ordinance",
    ],
    "Eschatology": [
        "heaven", "hell", "judgment", "eternity", "resurrection", "rapture",
        "tribulation", "millennium", "second coming", "prophecy", "apocalypse",
        "glory", "eternal life", "death",
    ],
    "Christian Life & Ethics": [
        "prayer", "obedience", "suffering", "joy", "peace", "hope", "humility",
        "temptation", "sin", "holiness", "witness", "love", "discipleship",
        "stewardship", "family", "marriage", "children", "anxiety", "contentment",
        "integrity", "service",
    ],
    "Law & Gospel": [
        "law", "gospel", "grace", "works", "faith", "covenant", "promise",
        "circumcision", "freedom", "legalism", "antinomianism",
    ],
    "Apologetics & Worldview": [
        "apologetics", "creation", "evolution", "culture", "worldview",
        "philosophy", "truth", "reason", "evidence", "authority",
        "secular", "relativism",
    ],
    "Spiritual Warfare": [
        "satan", "devil", "demons", "spiritual warfare", "evil", "temptation",
        "armor of god", "spiritual battle",
    ],
}

# ── Load metadata ─────────────────────────────────────────────────────────────

def load_metadata() -> list[dict]:
    if METADATA_FILE.exists():
        return json.loads(METADATA_FILE.read_text())
    records = []
    for f in SERMONS_DIR.glob("*.json"):
        try:
            records.append(json.loads(f.read_text()))
        except Exception:
            pass
    return records


def extract_book(scripture: str) -> str:
    """Extract the Bible book name from a scripture reference."""
    if not scripture:
        return ""
    # Match numbered books: "1 Samuel 3:1", "1 Corinthians 13:1"
    m = re.match(r'^(\d+\s+[A-Za-z]+(?:\s+[A-Za-z]+)?)', scripture)
    if m:
        candidate = m.group(1).title()
        for book in ALL_BOOKS:
            if book.lower().startswith(candidate.lower()[:6]):
                return book
    # Match plain book names
    m = re.match(r'^([A-Za-z]+(?:\s+[A-Za-z]+)?)', scripture)
    if m:
        candidate = m.group(1).title()
        for book in ALL_BOOKS:
            if book.lower().startswith(candidate.lower()[:5]):
                return book
    return scripture.split()[0].title() if scripture else ""


# ── Build scripture map ────────────────────────────────────────────────────────

def build_scripture_map(records: list[dict]):
    print("Building scripture map...")
    by_book: dict[str, list[dict]] = defaultdict(list)
    no_book = []

    for r in records:
        book = extract_book(r.get("scripture", ""))
        if book:
            by_book[book].append(r)
        else:
            no_book.append(r)

    lines = [
        "# John MacArthur Sermons — Scripture Index\n",
        "*For locating and verifying MacArthur quotes. Not for reproduction.*\n",
        f"**{len(records)} sermons**\n",
    ]

    # Statistics
    lines.append("## Summary by Book\n")
    lines.append("| Book | Sermons |")
    lines.append("|------|---------|")
    for book in ALL_BOOKS:
        if book in by_book:
            anchor = book.lower().replace(" ", "-")
            lines.append(f"| [{book}](#{anchor}) | {len(by_book[book])} |")
    if no_book:
        lines.append(f"| [Topical/Other](#topicalother) | {len(no_book)} |")
    lines.append("")

    # Per-book sections
    lines.append("---\n")
    for book in ALL_BOOKS:
        sermons = by_book.get(book, [])
        if not sermons:
            continue
        lines.append(f"\n## {book}\n")
        lines.append("| Scripture | Title | Date | Series | File |")
        lines.append("|-----------|-------|------|--------|------|")
        # Sort by scripture reference then date
        for r in sorted(sermons, key=lambda x: (x.get("scripture", ""), x.get("date", ""))):
            scripture = r.get("scripture", "")
            title = r.get("title", "")
            date = r.get("date", "")[:7]  # YYYY-MM
            series = r.get("series", "")
            fn = r.get("filename", "")
            lines.append(f"| {scripture} | {title} | {date} | {series} | [↗](../sermons/{fn}) |")

    if no_book:
        lines.append("\n## Topical/Other\n")
        lines.append("| Title | Date | Series | File |")
        lines.append("|-------|------|--------|------|")
        for r in sorted(no_book, key=lambda x: x.get("date", "")):
            title = r.get("title", "")
            date = r.get("date", "")[:7]
            series = r.get("series", "")
            fn = r.get("filename", "")
            lines.append(f"| {title} | {date} | {series} | [↗](../sermons/{fn}) |")

    (MAPS_DIR / "scripture.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"  {sum(len(v) for v in by_book.values())} sermons indexed by book, {len(no_book)} topical")


# ── Build subject/series map ───────────────────────────────────────────────────

def build_subject_map(records: list[dict]):
    print("Building subject/series map...")
    by_series: dict[str, list[dict]] = defaultdict(list)

    for r in records:
        series = r.get("series", "").strip() or "Standalone Sermons"
        by_series[series].append(r)

    lines = [
        "# John MacArthur Sermons — Series Index\n",
        "*For locating and verifying MacArthur quotes. Not for reproduction.*\n",
        f"**{len(records)} sermons across {len(by_series)} series**\n",
        "## Series List\n",
    ]
    # Sort by series name, standalone last
    sorted_series = sorted(
        by_series.keys(),
        key=lambda s: ("z" if s == "Standalone Sermons" else s.lower())
    )
    lines.append("| Series | Sermons |")
    lines.append("|--------|---------|")
    for s in sorted_series:
        anchor = re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
        lines.append(f"| [{s}](#{anchor}) | {len(by_series[s])} |")
    lines.append("\n---\n")

    for s in sorted_series:
        sermons = by_series[s]
        anchor = re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
        lines.append(f"\n## {s}\n")
        lines.append("| # | Title | Scripture | Date | File |")
        lines.append("|---|-------|-----------|------|------|")
        for j, r in enumerate(sorted(sermons, key=lambda x: x.get("date", "")), 1):
            title = r.get("title", "")
            scripture = r.get("scripture", "")
            date = r.get("date", "")[:7]
            fn = r.get("filename", "")
            lines.append(f"| {j} | {title} | {scripture} | {date} | [↗](../sermons/{fn}) |")

    (MAPS_DIR / "subject.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"  {len(sorted_series)} series written")


# ── Build theology map ─────────────────────────────────────────────────────────

def build_theology_map(records: list[dict]):
    print("Building theology map...")
    theme_sermons: dict[str, dict[str, dict]] = {theme: {} for theme in THEOLOGY_MAP}

    for r in records:
        slug = r.get("slug", "")
        title = r.get("title", "").lower()
        series = r.get("series", "").lower()
        scripture = r.get("scripture", "").lower()
        combined = f"{title} {series} {scripture}"

        for theme, keywords in THEOLOGY_MAP.items():
            for kw in keywords:
                if kw in combined:
                    theme_sermons[theme][slug] = r
                    break

    lines = [
        "# John MacArthur Sermons — Theological Theme Index\n",
        "*For locating and verifying MacArthur quotes. Not for reproduction.*\n",
        "Grouped by theological category, derived from sermon titles and series.\n",
    ]
    total = sum(len(v) for v in theme_sermons.values())
    lines.append(f"**{total} theme-sermon associations across {len(THEOLOGY_MAP)} categories**\n")

    lines.append("## Categories\n")
    for theme in THEOLOGY_MAP:
        count = len(theme_sermons[theme])
        anchor = re.sub(r'[^a-z0-9]+', '-', theme.lower()).strip('-')
        lines.append(f"- [{theme}](#{anchor}) ({count} sermons)")
    lines.append("\n---\n")

    for theme in THEOLOGY_MAP:
        sermons = theme_sermons[theme]
        anchor = re.sub(r'[^a-z0-9]+', '-', theme.lower()).strip('-')
        lines.append(f"\n## {theme}\n")
        if not sermons:
            lines.append("*No sermons matched this theme.*\n")
            continue
        lines.append("| Title | Scripture | Series | Date | File |")
        lines.append("|-------|-----------|--------|------|------|")
        for slug, r in sorted(sermons.items(), key=lambda x: x[1].get("date", "")):
            title = r.get("title", "")
            scripture = r.get("scripture", "")
            series = r.get("series", "")
            date = r.get("date", "")[:7]
            fn = r.get("filename", "")
            lines.append(f"| {title} | {scripture} | {series} | {date} | [↗](../sermons/{fn}) |")

    (MAPS_DIR / "theology.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"  {total} theme associations written")


def write_readme():
    content = """# John MacArthur Sermon Maps

Reference indexes for locating and verifying John MacArthur quotes during sermon writing.

## Scope — Read This First

These maps index **MacArthur's sermons only**. They are:

- **Separate** from `.claude/sermon-map.md` and `.claude/theological-map.md`, which index your own sermons
- **Not a source for sermon content** — only for finding and verifying short quotes
- Covers **3,500+ sermons from 1969 to present**

Permitted uses:
- Finding a MacArthur quote on a topic while writing
- Verifying the exact wording of an attributed MacArthur quote
- Confirming which sermon a quote comes from before citing it

Not permitted:
- Reproducing full sermons or extended passages
- Treating MacArthur's content as your own

> Always cite: *"Quote." — John MacArthur, Sermon Title, Grace to You*

---

## Maps

| File | Contents |
|------|----------|
| [scripture.md](scripture.md) | Scripture passages → sermons, grouped by book (Genesis to Revelation) |
| [subject.md](subject.md) | Sermon series → sermons (all 200+ MacArthur series) |
| [theology.md](theology.md) | Theological themes (Christology, Soteriology, etc.) |

## Coverage

MacArthur preached through many complete books of the Bible. Major series include:
- Matthew (multiple volumes)
- Luke (multiple volumes)
- John (multiple volumes)
- Acts, Romans, 1–2 Corinthians, Galatians, Ephesians, Philippians, Colossians
- 1–2 Peter, James, Revelation
- Genesis ("The Battle for the Beginning")
- Many topical and special series

---

## How to Use

**Finding a quote on a topic:**
1. Open `theology.md` or `subject.md`
2. Find the theme/series → note the sermon filename
3. Open `../sermons/filename.md` and search for the quote

**Verifying an attributed quote:**
1. Open `scripture.md`, find the passage
2. Open the linked sermon file
3. Confirm exact wording, then cite properly

**Citation format:**
> "Quote here." — John MacArthur, *Sermon Title*, Grace to You
"""
    (MAPS_DIR / "README.md").write_text(content, encoding="utf-8")


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Building John MacArthur sermon maps ===\n")
    records = load_metadata()
    print(f"Loaded {len(records)} sermon records\n")

    if not records:
        print("No metadata found. Run download-sermons.py first.")
        exit(1)

    build_scripture_map(records)
    build_subject_map(records)
    build_theology_map(records)
    write_readme()

    print("\nDone. Maps written to maps/")
