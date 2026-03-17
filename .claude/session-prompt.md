# Session Onboarding Prompt

*Paste this at the start of a new Claude Code session to resume work on this repository without re-exploration.*

*Last updated: March 16, 2026*

---

## What This Repository Is

This is a pastor's sermon archive and active sermon-preparation workspace. It serves two purposes:

1. **Weekly preaching** — expository sermons through Romans (currently the active series) and a large archive of other sermons across ~40 books of the Bible.
2. **Future book** — "The Night Is Far Gone" (working title), a Romans-based book structured around the Romans 13:11-12 night/dawn metaphor.

The pastor is the sole author. All content in this repository is his spoken or written word. When writing or editing, preserve his voice exactly. Never add AI tells, sermonic clichés, or language that sounds composed rather than spoken.

---

## Authoritative Reference Files

Read these before doing any substantial work. They are the ground truth for this repository.

| File | Purpose |
|------|---------|
| `claude.md` | Master project guidelines, book framework, congregation profile summary, voice standards |
| `.claude/voice-profile.md` | Voice fingerprint — vocabulary, cadence, forbidden phrases, what sounds like him |
| `.claude/theological-commitments.md` | Confessional Reformed/Baptist theology — what he believes and how he argues |
| `.claude/sermon-map.md` | Complete catalog of every sermon (~200+) — organized by Bible book and by subject |
| `.claude/theological-map.md` | Cross-reference of theological themes across the corpus |
| `.claude/unfinished-work-tracker.md` | **Start here** — the canonical list of all open work items, organized by category |
| `.claude/citation-standards.md` | Standards for Scripture quotation (ESV default), attribution, and integrity flags |
| `.claude/preaching-gap-analysis.md` | 11-part analysis of books/passages never preached; useful for sermon planning |

---

## Current State (as of March 16, 2026)

### What was done in the most recent session

- Merged 10 new files from `origin/main` into the working branch
- All 10 files verified and added to `sermon-map.md`
- `unfinished-work-tracker.md` updated with new findings
- `1 Corinthians 12 - Church Membership.md` reviewed — clean, Integrity Log complete
- Two newly-merged files have standing pastoral flags (documented in tracker Part IV):
  - `Deuteronomy 8 - Count Your Blessings (repaired draft).md` — 3 flags
  - `Psalm 42 - As the Deer Pants.md` — 2 flags

### Summary of open items (from tracker)

| Category | Count |
|----------|-------|
| Blocked sermons (no source text) | 1 — Psalm 106 "At the Altar of Our Convenience" |
| Incomplete manuscripts | 3 — Thankfulness (truncated), Sola Christus 2024 (draft), Rapture study paper |
| Raw drafts with standing flags | 12 files |
| Study papers incomplete | 2 |
| Book project items | 4 |
| Sermon-map ⚠️ flags | 46+ entries |

---

## Open Work — Priority Order

### Tier 1: Needs pastor input before any action

These cannot be resolved without material or a decision from the pastor.

- **Psalm 106 "At the Altar of Our Convenience"** — no source text in repo; must re-submit transcript
- **Sermon - Thankfulness.md** — truncated; must submit remainder of transcript
- **Sermon - Sola Christus 2024.md** — Scripture reference blank ("Our scripture will be ___"); three roles of Christ never expounded; pastor must complete or designate the 2020 version as authoritative

### Tier 2: Ready to polish (one session each)

These files have standing verification flags. Each can be resolved in a focused session.

| File | Key remaining flags |
|------|-------------------|
| `Sermon - Sola Scriptura 2021.md` | Trevor Noah attribution almost certainly wrong — find real source before preaching; 4 Luther quotes content-consistent but no primary LW source confirmed |
| `Sermon - Faithful and God-Fearing.md` | Gospel presentation not developed (must complete before preaching); Pascal's Wager section unfinished; Alvin Reid quote source unverified |
| `Philippians 4 (raw draft).md` | Samuel Sey quote unverified; Baxter full passage unverified; Mo-Jer-Hai not sourced; pew Bible page # blank |
| `Romans 7.md` | Tesla story disputed; "3 in 5 dieters" unverified |
| `Psalm 8 - Hebrews 2 (raw draft).md` | Platt cab driver unverified; Edwards "just the sin" suspect; MacArthur paraphrase unconfirmed |
| `Romans 1 - Psalm 22 (Prophecy raw draft).md` | Ps 22 fulfillment table needs line-by-line ESV check before printing |
| `Romans 3 - antinomianism draft.md` | John Brown quote needs physical copy to verify |
| `Psalm 103 - Bless the Lord (raw draft).md` | JFB quote unverified |
| `Deuteronomy 8 - Count Your Blessings (repaired draft).md` | Oatman hymn story may be invented; Edwards quote wording doesn't match primary text; Col 3:6 application strained |
| `Psalm 42 - As the Deer Pants.md` | PhD scholar for deer/predator claim unnamed; song attribution needs verify for print |
| `Psalm 119 161-168 (raw draft).md` | Florida opiates statistic — directionally accurate but exact phrase unverified |
| `Psalm 2 (raw draft).md` | "53 countries" and "Russia in Revelation" — dated/interpretive, already flagged inline |

### Tier 3: Book project — "The Night Is Far Gone"

No work has begun on converting sermons from preached format to read format. Four items open:

1. Book title decision — three options proposed; no selection: *The Night Is Far Gone*, *Waking Up*, *From Midnight to Morning*
2. `Notes - Empire and Suppression (Romans 1 Book Revision).md` — raw material not yet integrated into the Romans 1 chapter
3. All 16 chapters need preach-to-read format revision
4. Inter-chapter transitions not yet written

### Tier 4: Study papers

- `Notes - 2 Corinthians 5-15 Rebuttal (Calvinism Objection).md` — first argument developed; additional arguments unwritten
- `Rapture - Study Paper (incomplete draft).md` — introduction only; all Scripture analysis and position comparisons missing

---

## Integrity Standards (non-negotiable)

These apply to every file touched:

1. **Scripture** — ESV by default. Every quoted verse must be verified word-for-word against ESV before committing. Never paraphrase and mark as quoted.
2. **Attributed quotes** — Every named quotation must be traceable to a primary or well-documented secondary source. Unverified quotes get a ⚠️ flag in the source notes, never silent removal.
3. **Statistics and factual claims** — Must be sourced. If a claim cannot be verified, it gets a ⚠️ flag and a note about what was found. Do not silently soften or remove without documenting.
4. **Personal illustrations** — The pastor's own stories and congregant testimonies are taken as given. No verification required. Never name congregants in any published version.
5. **Integrity Log** — Every polished manuscript gets an Integrity Log at the bottom documenting what was checked, what was corrected, and what flags remain.

The guiding principle: **careful, not clever**. The goal is not impressive output — it is faithful, accurate, verifiable work that honors the text and the people who will hear it.

---

## Git

- Working branch: `claude/review-and-prepare-sermons-Oyfhs`
- Push with: `git push -u origin claude/review-and-prepare-sermons-Oyfhs`
- Commit after every meaningful unit of work with a clear message documenting what was verified and what flags remain

---

## How to Start

1. Read `.claude/unfinished-work-tracker.md` for the current full open-items list
2. Ask the pastor what he wants to work on, or pick the highest-priority Tier 2 item if he says "continue"
3. Before editing any sermon file, read it fully and check the sermon-map entry for prior flags
4. Apply the `careful-not-clever` skill standard throughout
