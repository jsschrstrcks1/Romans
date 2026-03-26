---
name: sermon-cross-reference
description: "Finds thematic connections, repeated illustrations, theological threads, and preaching history across 465+ sermon manuscripts. Complements sermon-map (which indexes) with deep cross-referencing (which connects)."
version: 1.0.0
---

# Sermon Cross-Reference

> "All Scripture is breathed out by God and profitable for teaching..." — 2 Timothy 3:16 (ESV)

## Purpose

With 465+ sermon manuscripts, the preaching corpus is rich with interconnected theology, recurring illustrations, and argument chains that span years. This skill finds those connections — so the preacher can callback, avoid repetition, and build on foundations already laid.

## When to Fire

- On `/xref` command
- When drafting a sermon that references previous teaching
- When reviewing a passage that has been preached before
- When looking for illustration reuse

## Relationship to Other Skills

| Skill | Relationship |
|-------|-------------|
| **sermon-map** | sermon-map INDEXES (maintains the map files). Cross-reference CONNECTS (finds relationships between entries). |
| **cognitive-memory** | Cross-reference discoveries are encoded as memories for cross-session persistence |
| **careful-not-clever** | Never fabricate connections. If a link isn't there, say so. |
| **thus-says-the-lord** | Cross-references can inform evaluation — has this doctrine been established before? |

## Six Operations

### 1. PASSAGE — Find all sermons referencing a Scripture

```
/xref passage Romans 5:8
/xref passage John 3:16
/xref passage Psalm 23
```

Search all .md files for:
- Direct passage references (e.g., "Romans 5:8")
- Passage ranges that include the verse (e.g., "Romans 5:1-11")
- Quotations of the verse text
- Cross-reference mentions in other sermon's notes

**Output:** List of sermons with the passage, how it's used (primary text, cross-reference, illustration, quotation), and the surrounding context.

### 2. DOCTRINE — Find all sermons teaching a doctrine

```
/xref doctrine justification
/xref doctrine "definite atonement"
/xref doctrine "effectual calling"
```

Search for:
- Doctrinal terms (justification, sanctification, propitiation, imputation)
- Reformed vocabulary (effectual calling, irresistible grace, total depravity, unconditional election, definite atonement, perseverance of the saints)
- Confessional references (1689 LBCF chapters, Westminster, Heidelberg)
- Greek/Hebrew terms (logizomai, hilasterion, dikaioo)

**Output:** Sermons teaching this doctrine, with excerpts showing how it was explained and applied.

### 3. ILLUSTRATION — Find repeated illustrations

```
/xref illustration courtroom
/xref illustration "prodigal son"
/xref illustration adoption
```

Search for recurring metaphors, analogies, and stories:
- Legal metaphors (courtroom, verdict, pardon)
- Family metaphors (adoption, inheritance, prodigal)
- Athletic metaphors (race, prize, discipline)
- Military metaphors (armor, battle, victory)
- Named stories and examples from church history

**Output:** Every sermon using this illustration, with context. Flag if overused (>3 appearances).

### 4. THREAD — Trace an argument across a series

```
/xref thread "faith and works"
/xref thread "suffering produces hope"
/xref thread "law and gospel"
```

Follow a theological argument as it develops across multiple sermons in a series:
- How was it introduced?
- Where was it deepened?
- What counter-arguments were addressed?
- Where does it reach its climax?

**Output:** Chronological trace of the argument with excerpts from each sermon.

### 5. HISTORY — Preaching history for a Bible book

```
/xref history Galatians
/xref history "1 John"
/xref history Psalms
```

Compile everything preached from a given Bible book:
- Which passages have been covered
- Which passages are gaps (never preached)
- Series context (standalone vs. series)
- Date information if available from date-map.md

**Output:** Coverage map with preached/unpreached passages.

### 6. CALLBACK — Suggest callbacks for current draft

```
/xref callback "Romans 8 - More Than Conquerors.md"
```

Given a current sermon draft, find opportunities to reference previous sermons:
- "As we saw in our study of Romans 5..."
- "Remember when we looked at Abraham's faith in chapter 4..."
- "This connects to what we learned about justification..."

**Output:** Suggested callback points with the specific previous sermon and a draft callback phrase.

## Search Strategy

1. **Primary:** Search `.claude/sermon-map.md` for structured references (fastest)
2. **Secondary:** Search `.claude/theological-map.md` for doctrinal connections
3. **Deep:** Grep the actual .md sermon files for full-text matches
4. **Verify:** Read surrounding context to confirm relevance (not just keyword match)

## File Naming Patterns

Sermon files follow these patterns:
- `Romans 4 - In Christ Alone.md` (book chapter - title)
- `1 Peter 3.md` (book chapter only)
- `1 john 2 1-6 lakeview.md` (book chapter verses location)
- `Hebrews 11 - Faith.md` (book chapter - title)
- Files with "(raw draft)" or "(raw transcript)" in the name are unpolished

## Map Files

- `.claude/sermon-map.md` — Master index with passage, title, file, subject
- `.claude/theological-map.md` — Doctrinal themes mapped to sermons
- `.claude/series-trajectory.md` — Series arcs and progression
- `.claude/date-map.md` — Chronological preaching history

---

*Soli Deo Gloria* — The Word of God is a unified whole. Cross-referencing reveals the golden thread.
