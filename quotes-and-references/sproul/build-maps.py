#!/usr/bin/env python3
"""
Build three reference maps from downloaded R.C. Sproul sermons:
  maps/scripture.md  — Scripture passages → sermons
  maps/subject.md    — Topics/subjects → sermons
  maps/theology.md   — Theological themes → sermons

Purpose: locating Sproul quotes while writing, and verifying attributed quotes.
Not for reproduction. Short quotes with proper citation only.
"""

import json
import re
from pathlib import Path
from collections import defaultdict

SPROUL_DIR = Path(__file__).parent
SERMONS_DIR = SPROUL_DIR / "sermons"
MAPS_DIR = SPROUL_DIR / "maps"
MAPS_DIR.mkdir(exist_ok=True)

METADATA_FILE = SPROUL_DIR / "sermon-metadata.json"

# ── Theological theme groupings ───────────────────────────────────────────────

THEOLOGY_MAP = {
    "Christology": [
        "christ", "jesus", "son of god", "son of man", "lord", "messiah",
        "savior", "incarnation", "mediator", "redeemer", "lamb of god",
        "resurrection", "ascension", "transfiguration", "baptism of jesus",
        "birth of jesus", "temptation of jesus", "person of christ",
        "atonement", "crucifixion", "cross", "burial",
    ],
    "Soteriology": [
        "salvation", "justification", "sanctification", "redemption",
        "forgiveness", "reconciliation", "propitiation", "imputation",
        "adoption", "regeneration", "new birth", "conversion", "repentance",
        "faith", "grace", "election", "predestination", "calling",
        "perseverance", "assurance", "free grace", "golden chain",
        "righteousness", "justified", "dead to sin", "alive to god",
    ],
    "Doctrine of God": [
        "sovereignty", "wrath of god", "holiness", "love of god",
        "justice of god", "mercy", "trinity", "attributes of god",
        "providence", "foreknowledge", "decrees", "creator",
        "everlasting love", "god's wrath", "god's judgment",
    ],
    "Scripture & Revelation": [
        "scripture", "word of god", "inspiration", "preaching",
        "gospel", "revelation", "truth", "bible",
    ],
    "Pneumatology": [
        "holy spirit", "spirit of god", "pentecost", "spiritual gifts",
        "fruit of the spirit", "indwelling",
    ],
    "Ecclesiology": [
        "church", "baptism", "lord's supper", "worship", "prayer",
        "ministry", "deacon", "elder", "discipline", "fellowship",
        "early church", "apostles", "mission",
    ],
    "Eschatology": [
        "heaven", "hell", "death", "resurrection", "judgment",
        "eternity", "eternal", "second coming", "glory",
        "son of man coming", "olivet", "tribulation",
    ],
    "Christian Life & Ethics": [
        "prayer", "obedience", "suffering", "trial", "comfort", "joy",
        "peace", "hope", "humility", "temptation", "sin", "holiness",
        "service", "witness", "love your neighbor", "love your enemies",
        "discipleship", "cost of discipleship", "stewardship",
        "marriage", "divorce", "children", "anxiety",
    ],
    "Evangelism & Mission": [
        "great commission", "mission", "evangelism", "gospel", "witness",
        "lost", "salvation", "call", "repentance", "faith",
    ],
    "Law & Gospel": [
        "law", "grace", "works", "faith", "circumcision",
        "covenant", "promise", "curse of the law", "freedom",
        "galatians", "romans",
    ],
}

# ── Scripture book display names ──────────────────────────────────────────────

BOOK_ORDER = [
    "Matthew", "Mark", "Luke", "John", "Acts", "Romans", "Galatians",
    "1 Peter", "2 Peter", "Hebrews", "Other"
]

# ── Load metadata ─────────────────────────────────────────────────────────────

def load_metadata() -> list[dict]:
    if METADATA_FILE.exists():
        return json.loads(METADATA_FILE.read_text())
    # Fall back to individual .json files
    records = []
    for f in SERMONS_DIR.glob("*.json"):
        try:
            records.append(json.loads(f.read_text()))
        except Exception:
            pass
    return records


# ── Build maps ────────────────────────────────────────────────────────────────

def build_scripture_map(records: list[dict]):
    print("Building scripture map...")
    # Group by series (= book)
    by_series = defaultdict(list)
    no_scripture = []
    for r in records:
        scripture = r.get("scripture", "").strip()
        if scripture:
            by_series[r.get("series", "Other")].append(r)
        else:
            no_scripture.append(r)

    lines = ["# R.C. Sproul Sermons — Scripture Index\n"]
    lines.append("*For locating and verifying Sproul quotes. Not for reproduction.*\n")
    lines.append(f"**{len(records)} sermons**\n")

    for series in BOOK_ORDER:
        sermons = by_series.get(series, [])
        if not sermons:
            continue
        lines.append(f"\n## {series}\n")
        lines.append("| Scripture | Title | File |")
        lines.append("|-----------|-------|------|")
        for r in sermons:
            scripture = r.get("scripture", "")
            title = r.get("title", r["slug"])
            slug = r["slug"]
            lines.append(f"| {scripture} | {title} | [sermons/{slug}.md](../sermons/{slug}.md) |")

    if no_scripture:
        lines.append("\n## Uncategorized (scripture not detected)\n")
        lines.append("| Title | Series | File |")
        lines.append("|-------|--------|------|")
        for r in no_scripture:
            lines.append(f"| {r.get('title', r['slug'])} | {r.get('series', '')} | [sermons/{r['slug']}.md](../sermons/{r['slug']}.md) |")

    (MAPS_DIR / "scripture.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"  {len(records)} sermons indexed by scripture")


def build_subject_map(records: list[dict]):
    print("Building subject map...")
    # Group by topic
    by_topic = defaultdict(list)
    for r in records:
        topic = r.get("topic", "").strip() or "Uncategorized"
        by_topic[topic].append(r)

    lines = ["# R.C. Sproul Sermons — Subject Index\n"]
    lines.append("*For locating and verifying Sproul quotes. Not for reproduction.*\n")
    lines.append(f"**{len(records)} sermons, {len(by_topic)} topics**\n")

    for topic in sorted(by_topic.keys()):
        sermons = by_topic[topic]
        lines.append(f"\n## {topic}\n")
        lines.append("| Title | Series | Scripture | File |")
        lines.append("|-------|--------|-----------|------|")
        for r in sermons:
            title = r.get("title", r["slug"])
            series = r.get("series", "")
            scripture = r.get("scripture", "")
            slug = r["slug"]
            lines.append(f"| {title} | {series} | {scripture} | [sermons/{slug}.md](../sermons/{slug}.md) |")

    (MAPS_DIR / "subject.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"  {len(by_topic)} topics written")


def build_theology_map(records: list[dict]):
    print("Building theology map...")

    theme_sermons: dict[str, dict[str, dict]] = {theme: {} for theme in THEOLOGY_MAP}

    for r in records:
        slug = r["slug"]
        title = r.get("title", slug)
        topic = (r.get("topic", "") + " " + r.get("topic_parent", "") + " " + r.get("topic_grandparent", "")).lower()
        title_lower = title.lower()
        combined = title_lower + " " + topic

        for theme, keywords in THEOLOGY_MAP.items():
            for kw in keywords:
                if kw in combined:
                    theme_sermons[theme][slug] = r
                    break

    lines = ["# R.C. Sproul Sermons — Theological Theme Index\n"]
    lines.append("*For locating and verifying Sproul quotes. Not for reproduction.*\n")
    lines.append("Grouped by theological category.\n")

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
            lines.append("*No sermons matched this theme.*\n")
            continue
        lines.append("| Title | Series | Scripture | File |")
        lines.append("|-------|--------|-----------|------|")
        for slug, r in sorted(sermons.items(), key=lambda x: x[1].get("series", "") + x[1].get("title", "")):
            title = r.get("title", slug)
            series = r.get("series", "")
            scripture = r.get("scripture", "")
            lines.append(f"| {title} | {series} | {scripture} | [sermons/{slug}.md](../sermons/{slug}.md) |")

    (MAPS_DIR / "theology.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"  {total} theme associations written")


def write_readme():
    content = """# R.C. Sproul Sermon Maps

Reference indexes for locating and verifying R.C. Sproul quotes during sermon writing.

## Scope — Read This First

These maps index **Sproul's sermons only**. They are:

- **Separate** from `.claude/sermon-map.md` and `.claude/theological-map.md`, which index your own sermons
- **Not to be merged** into any broader sermon index system
- **Not a source for sermon content** — only for finding and verifying short quotes

Permitted uses:
- Finding a Sproul quote on a topic while writing
- Verifying the exact wording of an attributed Sproul quote
- Confirming which sermon a quote comes from before citing it

Not permitted:
- Reproducing full sermons or extended passages
- Treating Sproul's content as your own

> Always cite: *"Quote." — R.C. Sproul, Sermon Title, Ligonier Ministries*

---

## Maps

| File | Contents |
|------|----------|
| [scripture.md](scripture.md) | Scripture passages → sermons, grouped by book |
| [subject.md](subject.md) | Topics/subjects → sermons |
| [theology.md](theology.md) | Theological themes (Christology, Soteriology, etc.) |

## Sermon Series Covered

| Series | Book |
|--------|------|
| Matthew | Gospel of Matthew |
| Mark | Gospel of Mark |
| Luke | Gospel of Luke |
| John | Gospel of John |
| Acts | Acts of the Apostles |
| Romans | Romans |
| Galatians | Galatians |
| 1 Peter | 1 Peter |
| 2 Peter | 2 Peter |
| Hebrews | Hebrews |

---

## How to Use

**Finding a quote on a topic:**
1. Open `subject.md` or `theology.md`
2. Find the topic → note the sermon file
3. Open `../sermons/slug.md` and search for the quote

**Verifying an attributed quote:**
1. Open `scripture.md`, find the passage
2. Open the linked sermon file
3. Confirm exact wording, then cite properly

**Citation format:**
> "Quote here." — R.C. Sproul, *Sermon Title*, Ligonier Ministries
"""
    (MAPS_DIR / "README.md").write_text(content, encoding="utf-8")


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Building R.C. Sproul sermon maps ===\n")
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
