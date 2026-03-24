# Organizational Structure Plan

*Prepared March 24, 2026 — based on manual audit of the full repository.*

---

## Current State: What We Have

| Location | Files | Contents |
|----------|-------|----------|
| `/` (root) | 464 .md | Sermons, notes, studies, personal, drafts — all flat |
| `quotes-and-references/` | 1,325 .md | MacArthur (769), Sproul (548), Spurgeon (6), illustrations (1) |
| `Other-Sermons/Sermons/` | 26 .md | Raw drafts, variants, and newly imported sermons |
| `Other-Sermons/_review/` | 5 .md | Voice audits and evaluation reports |
| `Other-Sermons/sebts-reference/` | 7 files | Greek translations, seminary papers |
| `sebts-reference/` | 5 .md | Seminary papers and syllabi (separate copy) |
| `pastoral-resources/` | 3 .md | Shelter policy, emergency contacts, community resources |
| `Other-Sermons/pastoral-resources/` | 0 | Empty duplicate |
| `A journey in grace/` | 52 JPGs | Book study photos (no markdown) |
| `.claude/` | 4 maps | sermon-map, theological-map, date-map, series-trajectory |

**Total: ~1,833 markdown files across the repository.**

---

## Problems Identified

### 1. Root directory is a flat pile
464 files with no folder structure. Polished manuscripts sit next to raw transcripts, personal notes, Sunday school lessons, funeral services, theological papers, and planning documents. Finding anything requires search or the sermon-map.

### 2. Inconsistent naming
- Mixed case: `Romans 1a` vs `romans 12 pt 4`
- Mixed prefixes: `Sermon - Title` vs `Book Chapter` vs bare lowercase
- Draft markers vary: `(raw draft)`, `(raw transcript)`, `(raw notes)`, `(raw early draft)`, `(flagged draft)`, `(repaired draft)`, `(rebuilt draft)`
- Parenthetical suffixes: `(2)`, `(b)`, `pt 2`, `pt3`, `Part 2`

### 3. Duplicate directory trees
- `sebts-reference/` exists at root (5 files) AND inside `Other-Sermons/` (7 files) — different contents, same purpose
- `pastoral-resources/` exists at root (3 files) AND empty inside `Other-Sermons/`

### 4. `Other-Sermons/` is ambiguous
Contains raw drafts, variant versions, reviews, sebts papers, and newly imported sermons. The name doesn't describe what makes these "other." It's functioning as a staging/import area.

### 5. Multiple versions of the same sermon with no clear lineage
Example — Sola Christus:
- `Sola Christus.md`
- `Sola Christus (AutoRecovered).md`
- `Sermon - Sola Christus 2024.md`

Example — Psalm 46:
- `Psalm 46.md`
- `Psalm 46 - Refuge.md`
- `Other-Sermons/Sermons/Psalm 46 - variant 2.md`

### 6. Non-sermon files mixed with sermons
Root contains wedding ceremonies, funeral services, pandemic journals, church policies, evangelism content surveys, plagiarism reports, and Bible study materials — all mixed with sermon manuscripts.

---

## Proposed Structure

```
Romans/
│
├── sermons/                          # All sermon manuscripts
│   ├── romans/                       # Romans series ("Night Is Far Gone")
│   │   ├── Romans 1a - The Power of God for Salvation.md
│   │   ├── Romans 1b - Without Excuse.md
│   │   └── ...
│   ├── old-testament/                # OT sermon manuscripts
│   │   ├── Genesis 22 - There and Back Again.md
│   │   ├── Psalm 23.md
│   │   └── ...
│   ├── new-testament/                # NT sermon manuscripts (non-Romans)
│   │   ├── 1 Peter 2.md
│   │   ├── John 10 - The Good Shepherd.md
│   │   └── ...
│   ├── topical/                      # Topical/titled sermons not passage-primary
│   │   ├── Sermon - The Watching World.md
│   │   ├── Sermon - Legacies.md
│   │   └── ...
│   └── series/                       # Named series groupings
│       ├── sola/                     # Five Solas Reformation series
│       ├── thanksgiving/             # Annual Thanksgiving messages
│       └── ...
│
├── drafts/                           # Raw, unpolished, in-progress
│   ├── raw-transcripts/              # Transcribed from audio
│   ├── raw-drafts/                   # First written drafts
│   └── variants/                     # Alternate versions for comparison
│
├── services/                         # Non-Sunday-morning occasions
│   ├── funerals/
│   ├── weddings/
│   ├── prayer-services/
│   └── special-events/               # IDOP, VBS, ordination, etc.
│
├── teaching/                         # Non-sermon instruction
│   ├── sunday-school/
│   ├── bible-studies/                # Including "Journey in Grace"
│   └── notes/                        # Study notes, research, outlines
│
├── theology/                         # Doctrinal papers and studies
│   ├── christology.md
│   ├── hamartiology.md
│   ├── Gap Theory - A Biblical and Confessional Evaluation.md
│   └── ...
│
├── pastoral-resources/               # Church admin and policy (already exists)
│   ├── Church Emergency Shelter Assistance Policy.md
│   ├── Emergency Contacts.md
│   └── Pasco Community Resources.md
│
├── sebts-reference/                  # Seminary work (consolidated)
│   ├── greek-translations/
│   ├── papers/
│   └── syllabi/
│
├── quotes-and-references/            # Already well-organized — keep as-is
│   ├── macarthur/
│   ├── sproul/
│   ├── spurgeon/
│   └── illustrations/
│
├── A journey in grace/               # Book study photos — keep as-is
│
├── _review/                          # Evaluation reports (from Other-Sermons/_review)
│
└── personal/                         # Pandemic journal, personal reflections
```

---

## Key Decisions to Make Before Moving Files

These require your input. I will not assume.

### Decision 1: Romans series — separate folder or stay at root?
The Romans series is the heart of this repository. Putting it in `sermons/romans/` is clean, but it changes every path in the sermon-map and series-trajectory. Alternative: keep Romans sermons at root, move everything else.

### Decision 2: Flat sermons folder or OT/NT split?
Option A: `sermons/` with all 400+ sermon files flat inside (simple, matches current mental model)
Option B: `sermons/old-testament/`, `sermons/new-testament/`, `sermons/topical/` (organized, but more clicks)

### Decision 3: What counts as a "draft"?
47 files are tagged `(raw draft)`, `(raw transcript)`, etc. Some may be the only version of that sermon. Moving them to `drafts/` could orphan them from their polished siblings. Alternative: keep drafts next to their final versions with a naming convention.

### Decision 4: What to do with `Other-Sermons/`?
Once its contents are properly placed, delete it entirely? Or keep it as an import staging area for future zip imports?

### Decision 5: Naming convention going forward?
Current mix of styles is organic and natural. Enforcing a strict convention means renaming hundreds of files. Options:
- **Leave as-is**: Don't rename. Just organize into folders.
- **Normalize gradually**: New files follow convention; old files stay.
- **Full rename**: `[Book] [Chapter]:[Verses] - [Title] ([status]).md`

### Decision 6: Do we move files, or just document the plan?
Moving 400+ files in git changes every path. This is a one-way door that affects git blame, sermon-map references, and any external links. We should be certain before executing.

---

## What NOT to Change

- **`quotes-and-references/`** — Already well-organized (macarthur/sproul/spurgeon with maps and sermons subdirs). Leave it alone.
- **`.claude/` maps** — These get regenerated by the sermon-map skill. They'll update after any reorganization.
- **`A journey in grace/`** — Book study photos. No structural change needed.
- **File contents** — This plan is about *location*, not editing sermon text.

---

## Recommended Execution Order

If we proceed:

1. **Consolidate duplicates first** — Merge the two `sebts-reference/` directories. Delete empty `Other-Sermons/pastoral-resources/`.
2. **Create folder structure** — Make the directories before moving anything.
3. **Move non-sermon files** — Services, teaching, theology, personal. Smallest set, lowest risk.
4. **Move drafts and variants** — Clear the obvious staging material from `Other-Sermons/Sermons/`.
5. **Move sermons by testament** — The big move. Do OT and NT separately.
6. **Romans series last** — Most important, most referenced. Move only after everything else is stable.
7. **Regenerate all maps** — Run sermon-map skill to rebuild all four map files.
8. **Verify** — Spot-check that no files were lost or misplaced.

---

## What I Need From You

Before I touch a single file:

1. Which decisions above do you want to make now?
2. Is there a reason for the current flat structure I should respect? (e.g., a tool or workflow that expects root-level files)
3. Should I proceed with the consolidation of duplicates as a safe first step?

*Soli Deo Gloria.*
