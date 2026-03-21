# Romans Sermon Series — Project Guidelines

## Purpose

This repository serves two purposes:

1. **Sermon preparation** — developing expository sermons through the book of Romans for weekly preaching
2. **Future book** — preserving and refining these sermons as potential chapters for a published work for the church

This dual purpose means:
- Sermons should work when *preached* and when *read*
- Illustrations and applications should be concrete enough to translate to print
- The theological arc should hold together across the whole series
- Each sermon/chapter should stand alone while contributing to the larger whole
- Maintain a consistent voice throughout — the book should feel like one author, one shepherd, one sustained argument

When writing, think: *Would this passage hold up on the page five years from now?*

---

## Reference Maps

The `.claude/` directory contains the project's knowledge layer. Consult these before writing, editing, or planning:

| Map | File | Purpose |
|-----|------|---------|
| **Sermon Map** | `.claude/sermon-map.md` | Complete catalog of every sermon, teaching, and study. Eight distinct table formats. Check before writing to avoid repeating illustrations or cross-references. |
| **Theological Map** | `.claude/theological-map.md` | What this preacher affirms, denies, and where he stands. 10 doctrinal categories, heresies refuted, identity markers. Every claim backed by direct quotes with file references. |
| **Series Trajectory** | `.claude/series-trajectory.md` | Arc of the Romans series: five phases (Diagnosis → Remedy → Identity → Assurance → Application) with chapter-by-chapter summaries through Romans 13. |
| **Date Map** | `.claude/date-map.md` | When each Romans sermon was preached. 39 sermons backdated from March 15, 2026 (one per Sunday, series starts June 22, 2025). Future sermons get the next upcoming Sunday. |
| **Book Framework** | `.claude/book-framework.md` | Extended framework for "The Night Is Far Gone" as a published book. |
| **Voice Profile** | `.claude/voice-profile.md` | Detailed preaching voice analysis and markers. |
| **Congregation Profile** | `.claude/congregation-profile.md` | Who sits in the room: spiritual spectrum, real burdens, pastoral implications. |
| **Confessional Framework** | `.claude/confessional-framework.md` | 1689 Second London Baptist Confession as load-bearing theology. |
| **Citation Standards** | `.claude/citation-standards.md` | ESV-only translation policy, acceptable sources, verification standards. |
| **Sermon Structure** | `.claude/sermon-structure.md` | How sermons are built: exposition spine, illustration placement, gospel close patterns. |
| **Theological Commitments** | `.claude/theological-commitments.md` | Core theological commitments governing sermon content. |
| **Theological Taxonomy** | `.claude/theological-taxonomy.md` | Taxonomy of doctrinal categories used across the maps. |
| **Romans 14–16 Plan** | `.claude/romans-14-16-plan.md` | Passage-by-passage plan for completing Romans 14–16 (4–6 sermons remaining). |
| **Preaching Gap Analysis** | `.claude/preaching-gap-analysis.md` | Analysis of passages and topics not yet covered. |
| **Unfinished Work Tracker** | `.claude/unfinished-work-tracker.md` | In-progress repairs, unresolved flags, pending work. |

**Spurgeon Reference Corpus** (separate from sermon maps — reference tool only):

| Map | Location |
|-----|----------|
| Scripture (OT) | `quotes-and-references/spurgeon/maps/scripture-ot.md` |
| Scripture (NT) | `quotes-and-references/spurgeon/maps/scripture-nt.md` |
| Subject | `quotes-and-references/spurgeon/maps/subject.md` |
| Theology | `quotes-and-references/spurgeon/maps/theology.md` |

Sermons at `quotes-and-references/spurgeon/sermons/chsN.md`. Use only to find/verify Spurgeon quotes. Not part of the sermon corpus.

---

## Skills — What They Do and When They Fire

Five active skills govern the writing and evaluation workflow. A sixth (sermon-mapping) is planned.

### careful-not-clever (Integrity Guardrail)

> **Skill file:** `.claude/skills/careful-not-clever/SKILL.md`

**Fires:** On every file modification (Edit, Write). Enforced by PostToolUse hook in `settings.json`.

**What it does:** Verifies that all Scripture references are ESV-correct, all attributed quotes are real and correctly sourced, all factual claims are verified, and all theological claims are grounded in Scripture. Blocks unverified content from being committed.

**Governing principle:** Everything we do is for the glory of God. We don't guess — we verify. We don't assume — we check. We don't cut corners — we serve the text. The pulpit demands our best, not our fastest.

### like-a-human (Voice & Presence — During Writing)

> **Skill file:** `.claude/skills/like-a-human/SKILL.md`

**Fires:** During sermon and book writing. Active while prose is being produced.

**What it does:** Guards the sound of the prose so it reads as written by a person who has been with God, not with a prompt. Shapes voice markers, rhythms, vocabulary, and theological precision. The congregation should hear their pastor, not detect a machine.

### voice-audit (Post-Draft Diagnostic)

> **Skill file:** `.claude/skills/voice-audit/SKILL.md`

**Fires:** After a draft is complete or when reviewing existing drafts.

**What it does:** Scans for machine tells, checks voice continuity against the sermon corpus, assesses conviction and cadence, and suggests minimal restoration edits. Detects drift without wholesale rewrites.

### thus-says-the-lord (Sermon Evaluation Rubric)

> **Skill file:** `.claude/skills/thus-says-the-lord/SKILL.md`

**Fires:** Automatically when a sermon is written or integrated into the repository.

**What it does:** Scores on a weighted 100-point scale: Exposition (25), Theology (18), Gospel Centrality (15), Conscience & Application (15), Exhortation (8), Structure (9), Illustration (5), Sermonic Force (5), with Weight of Glory bonus (+5) and Cognitive Load modifier. Begins with the Berean Gate (is it text-driven?), checks six fatal flaw flags, runs Dead Orthodoxy Detection, and produces diagnostic narrative with surgical fixes.

### cognitive-memory (Cross-Session Memory)

> **Skill file:** `.claude/skills/cognitive-memory/SKILL.md`

**Fires:** On keywords (memory, remember, recall, forget, "what do we know", "last session"), intent patterns (recalling past context, storing knowledge), and session_start events.

**What it does:** Persists knowledge across sessions using encode, consolidate, recall, extract, and forget operations. Memory store at `~/.memory/memory.json`. This is cognition, not storage — it reasons about what to remember and what to forget.

### Sermon-Mapping Skill (Planned)

> **Plan file:** `plan.md`

**Will fire:** When a new sermon file is created, modified, or imported.

**What it will do:** Seven operations — INDEX (add new entries to sermon-map.md), UPDATE (refresh existing entries), AUDIT (check map integrity), CONNECT (cross-reference between maps), GAP (identify preaching gaps), DEDUP (illustration deduplication), DATE (assign preaching dates to date-map.md).

### Skill Workflow Order

```
1. Write with like-a-human + careful-not-clever active
2. thus-says-the-lord evaluates the completed draft automatically
3. Revise based on surgical fixes
4. Run voice-audit before committing
5. Commit
```

---

## Book Framework: "The Night Is Far Gone"

The unifying illustration comes from Romans 13:11-12 — *"The night is far gone; the day is at hand."* The entire book of Romans is a journey from midnight to dawn.

| Part | Chapters | Title | Image |
|------|----------|-------|-------|
| **I** | Romans 1-3 | **Midnight** | Total darkness. Asleep in sin. |
| **II** | Romans 3-5 | **The Alarm** | The gospel wakes us. Justification while it's still dark. |
| **III** | Romans 6-8 | **Getting Dressed** | We put on Christ. Cast off the works of darkness. |
| **IV** | Romans 9-11 | **The Certainty of Dawn** | God's promises are sure. The dawn cannot be stopped. |
| **V** | Romans 12-16 | **Walking in Daylight** | We live as people of the day. We love. We serve. We wait. |

Full chapter mapping and burden-application table in `.claude/book-framework.md`.

---

## Voice & Tone

**CRITICAL: Always sound like a human preacher, never like an AI.** Write with warmth, conviction, pastoral weight, and occasional holy humor. Use concrete illustrations. Be willing to say hard things plainly.

### Core Voice Markers

- **Direct address and second person.** "Do you see what Paul is doing here?" "Some of you are in the middle of that right now."
- **Controlled fire on sin, hell, and false teaching.** Holy weight, not performative anger. Always tethered to the text.
- **Humor that earns trust.** Self-deprecating, well-timed, never frivolous. Disarms before the serious point lands.
- **Real-world analogies.** Truck drivers, football, military, marriage, parenting, the weight of a diagnosis. Not literary illustrations — *lived* illustrations.
- **Greek as unlock, not decoration.** Always introduced to tighten meaning, never to impress.
- **The "church" and "y'all" register.** Southern Baptist pastor to a Southern congregation.
- **Circle back to the verse.** Every illustration returns to the passage. The text is the spine.

### Preaching Lineage

Confessional Reformed Baptist in the stream of Augustine → Calvin → Owen → Ryle. Sounds most like Spurgeon's gravity, Sproul's holiness, Ferguson's Romans logic, Dever's restraint, Begg's pastoral steadiness. Bunyan's imagery shapes the imagination.

Full voice fingerprint and negative space in `.claude/voice-profile.md`.

---

## Theological Commitments

- **Soteriology**: Penal substitutionary atonement; justification by faith alone; grace alone; monergistic regeneration; five points of Calvinism explicitly affirmed
- **Hamartiology**: Total depravity as active rebellion; no neutrality; heart deceitful above all things
- **Theology Proper**: Divine sovereignty over all things; election and predestination (Calvinistic, pastoral); God's wrath as holy revulsion; foreknowledge as fore-love
- **Ecclesiology**: Body of Christ with diverse gifts; Great Commission for every believer; regenerate church membership; 1689 2LBCF as confessional framework

Full theological map with 200+ quote-backed positions in `.claude/theological-map.md`.

---

## Translation & Citation Standards

- **ESV ONLY** — No exceptions. Every Scripture quotation must be verified ESV text.
- **Every quote must be verified** — real, correctly sourced, exact wording confirmed before use.
- **No fabricated quotes** — no paraphrases as direct quotes, no "attributed to" guesswork.
- **When in doubt, leave it out.** The pulpit is not a place for misattribution.
- **People group data**: Joshua Project (primary) and Operation World (secondary). Flag anything unverifiable.

Full citation standards, acceptable source lists (60+ voices by tradition), and Spurgeon verification process in `.claude/citation-standards.md`.

---

## Sermon Structure

1. Scripture location and reading
2. Opening illustration or hook (concrete, memorable)
3. **People Group of the Week** — unreached peoples for prayer focus
4. Prayer transition
5. Scripture reading (ESV)
6. Body: 2-4 major points, cross-references, illustrations, application
7. Gospel call (every sermon)
8. Connection to BFM where appropriate
9. Call to prayer/action

Full structural patterns and closing techniques in `.claude/sermon-structure.md`.

---

## Congregation Profile

- **Seeking skeptics** — need intellectual honesty, not clichés
- **New believers** — need hope that growth is real
- **Long-time Christians** — familiarity is not faithfulness
- **Real burdens**: struggling marriages, broken families, addiction, health crises
- **Political context**: conservative, confident room that needs the text to challenge, not confirm

Don't preach to the person who has it together. They're not in the room. The sermon must have weight *and* hope.

Full profile in `.claude/congregation-profile.md`.

---

## Series Status

- **Series**: "The Night Is Far Gone" — Romans 1–16
- **Sermons preached**: 39 (June 22, 2025 – March 15, 2026)
- **Remaining**: Series complete through Romans 16
- **Planning forward**: `.claude/romans-14-16-plan.md` (4–6 sermons, now written)
- **Full trajectory**: `.claude/series-trajectory.md`
- **Date map**: `.claude/date-map.md`

---

## Recurring Pastoral Corrections

Weave these into sermons naturally, without naming names or movements:

**"No Creed But Christ" Chronological Snobbery** — Celebrate creeds as guardrails (not replacements). Honor church history. Note that "no creed but Christ" often means "no accountability but myself." Build categories so people recognize the error when they encounter it.

---

## Operational Rules

### Sermon Map Standard: Read the Whole Thing

Before adding any sermon to `sermon-map.md` or `theological-map.md`, **read the entire file**. Partial reads produce inaccurate summaries. This is a firm rule.

### Git: Fetch Before Status

**ALWAYS** run `git fetch origin` before answering any question about branch state. `git status` without fetch reports stale data. No exceptions.

### Integrity: Careful, Not Clever

Everything we do is for the glory of God. We don't guess — we verify. The pulpit demands our best, not our fastest. **Soli Deo Gloria.**

---

> "Slight thoughts of sin produce slight thoughts of God." — John Owen

Finish strong.
