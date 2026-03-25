---
name: sermon-planner
description: "Reads sermon-map, theological-map, date-map, and series-trajectory to identify coverage gaps, suggest next sermons, and plan series direction. The preacher's planning companion."
version: 1.0.0
---

# Sermon Planner

> *"Preach the word; be ready in season and out of season."* — 2 Timothy 4:2

## Purpose

Analyzes the existing sermon corpus (465+ manuscripts) and supporting maps to answer: **What should I preach next?**

## When to Fire

- On `/plan` command
- When discussing "what should I preach next" or "what haven't we covered"
- At the start of a new sermon series
- When evaluating theological coverage

## Data Sources

| File | What it tells us |
|------|-----------------|
| `.claude/sermon-map.md` | Every sermon indexed: passage, title, file, subject |
| `.claude/theological-map.md` | Doctrine coverage: what's been taught, what hasn't |
| `.claude/series-trajectory.md` | Where current series are heading, planned arcs |
| `.claude/date-map.md` | Preaching calendar: when sermons were delivered |

## Operations

### 1. GAP ANALYSIS — What haven't we preached?

Scan the sermon-map against the full biblical canon:
- **Books never preached from** — flag entire Bible books with zero sermons
- **Books with thin coverage** — only 1-2 sermons from a major book
- **Doctrines under-represented** — compare theological-map against core Reformed Baptist doctrines (LBCF 1689 chapters)
- **Series gaps** — started but unfinished series

Report format:
```
## Sermon Gap Analysis — [date]

### Bible Books Never Preached
- [list]

### Thin Coverage (1-2 sermons)
- [book]: [count] sermons

### Doctrine Gaps (vs. 1689 LBCF)
- Chapter [N]: [doctrine] — [0/few] sermons

### Unfinished Series
- [series name]: stopped at [passage], trajectory suggests [next]
```

### 2. NEXT SERMON SUGGESTIONS

Based on gaps, trajectory, and calendar:
- What the current series trajectory points to
- Passages frequently quoted but never dedicated a full sermon
- Doctrinal needs: "We haven't preached justification since [date]"
- Calendar awareness: upcoming holidays, church events, seasons

### 3. SERIES PLANNING

When starting a new series:
- Survey what exists on that book/topic already
- Identify natural break points in the text
- Estimate series length based on similar past series
- Flag potential overlap with existing sermons
- Suggest outline using theological-map connections

### 4. COVERAGE DASHBOARD

Quick overview:
```
## Preaching Dashboard — [date]

| Category | Count | Last Preached |
|----------|-------|--------------|
| Romans series | [N] sermons | [date] |
| Old Testament | [N] sermons | [date] |
| Doctrine: Justification | [N] sermons | [date] |
| Doctrine: Sanctification | [N] sermons | [date] |
| ...
```

## Integration

- **sermon-map** — primary data source for indexing
- **sermon-cross-reference** — finds thematic connections for series planning
- **cognitive-memory** — remembers planning decisions across sessions
- **thus-says-the-lord** — evaluation scores inform what needs revisiting

---

*Soli Deo Gloria* — Plan carefully, preach faithfully.
