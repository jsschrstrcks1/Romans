# Sermon Infrastructure Expansion Plan

**Branch**: `claude/plan-sermon-mapping-skill-9vaYZ`
**Scope**: 17 deliverables across new maps, skill operations, standardization, and cross-reference integrity.

---

## Design Principle: Self-Contained Reference Documents

Every map stores **full text** — not references, not summaries. Quotes store the quote. Illustrations store the illustration (or a condensed retelling for longer ones). The maps are designed for AI retrieval: a session that reads the quote map gets every quote, its source, its verification status, and every sermon that uses it — without chasing links.

---

## Phase 1: New Maps (Full-Text, AI-Optimized)

### 1. Quote Map — `.claude/quote-map.md`

**Format**: One entry per unique quote. Grouped by source author (alphabetical). Each entry:

```markdown
### Octavius Winslow

| # | Quote | Source | Verification | Used In | Count |
|---|-------|--------|-------------|---------|-------|
| 1 | "So completely was Jesus bent upon saving sinners by the sacrifice of Himself, He created the tree upon which He was to die, and nurtured from infancy the men who were to nail Him to the accursed wood." | Attributed to Winslow (no primary source confirmed) | ⚠️ Yellow — quote is real but exact source book unknown | `Romans 1c`, `Romans 1 (2024).md`, `Romans 1b` | 3 |
```

**Verification Hierarchy** (replaces flat ⚠️):

| Tier | Symbol | Meaning | Example |
|------|--------|---------|---------|
| Green | ✅ | Verified: exact wording confirmed against primary source | Spurgeon quote traced to sermon #2234 |
| Yellow | ⚠️ | Partially verified: quote is real, exact source uncertain | Winslow quote — widely attributed, no page/volume confirmed |
| Red | ❌ | Unverified or disputed: may be fabricated, misattributed, or conflated | "Einstein said..." with no primary source |

**Verification chain** column records provenance: `"via MacArthur sermon 2234"`, `"confirmed ESV Ps 19:1"`, `"widely attributed, no primary found"`.

**Extraction source**: 124 ⚠️ flags and 71 ✅ flags already in sermon-map.md. Systematic extraction from Subject columns.

**Estimated entries**: 150–200 unique quotes across the corpus.

---

### 2. Illustration Map — `.claude/illustration-map.md`

**Format**: One entry per unique illustration. Grouped by type, then alphabetical by name/identifier.

**Type categories**: Personal, Pastoral, Military, Medical, Historical, Literary, Scientific, Theological, Humorous, Cultural.

```markdown
### Historical

| # | Name | Illustration | Passage(s) | Used In | Count |
|---|------|-------------|------------|---------|-------|
| 1 | Bannockburn | Robert the Bruce, outnumbered at Bannockburn (1314), watched a spider try and fail to spin a web seven times — and succeed on the eighth. Rose from hiding to fight again. Scotland won its independence. Used as endurance/perseverance illustration. | Rom 5:3-5, Heb 12:1-2 | `Romans 5.md`, `Sermon - Hope.md` | 2 |
```

**For longer illustrations**: Store a condensed retelling (3–5 sentences) that preserves the teaching point, emotional arc, and key details. The map reader should understand the illustration without opening the sermon file.

**Recurring personal illustrations** (track carefully for reuse awareness):
- Aunt Judy (missions, mentally disabled ministry, Spanish Harlem) — 2–4 uses
- Dottie (congregant, frequently named) — 2–4 uses
- Grace the dog (killed 4 lambs) — 2–4 uses
- Hurricane Irma — 2–4 uses
- Marine Corps Crucible — 2–4 uses
- Nicaragua AIDS colony — 2–4 uses
- Hiroo Onoda (Japanese soldier, held out 29 years) — 2–4 uses

**Estimated entries**: 60+ named illustrations, 40+ unnamed (semantic matching, best-effort).

---

### 3. People Group Registry — `.claude/people-group-map.md`

**Format**: One entry per people group. Alphabetical by group name.

```markdown
| # | People Group | Region | Population | % Christian | Characteristics | Prayer Status | Sermon(s) |
|---|-------------|--------|-----------|-------------|----------------|--------------|-----------|
| 1 | Balija | India | ~2.5M | <0.1% | Hindu traders (bangles, salt, pearls); add Jesus to idol collection rather than exchange; alcohol permitted despite non-low caste (unusual) | Frontier | `Romans 1c` |
```

**Prayer Status values**: Frontier (<0.1%), Unreached (<2%), Minimally Reached (2–5%), Reached (>5%).

**Source**: 79 existing entries in sermon-map.md. Already follow consistent format. Nearly free to extract.

---

### 4. BFM Article Index — `.claude/bfm-article-index.md`

**Format**: One row per BFM 2000 article. Shows preaching coverage.

```markdown
| Article | Title | Preached? | Sermon(s) | Full Text Read? | Notes |
|---------|-------|-----------|-----------|----------------|-------|
| I | The Scriptures | ✅ | `2 Tim 3 14-17`, `Sola Scriptura.md` | Yes | Baptist confession history integrated |
| 2A | God the Father | ✅ | `Romans 1c` | Yes | Full text read from pulpit |
| 2B | God the Son | ? | | | Not yet identified |
```

**Source**: 24 BFM references already tracked in sermon-map.md. 18 BFM 2000 articles total. Quick to build; shows which articles have and haven't been preached.

---

### 5. 1689 Second London Baptist Confession Map — `.claude/1689-map.md`

**Format**: Chapter-by-chapter coverage against the sermon corpus.

```markdown
| Chapter | Title | Cited? | Sermon(s) | How Used | Notes |
|---------|-------|--------|-----------|----------|-------|
| 1 | Of the Holy Scriptures | ✅ | `2 Tim 3 14-17`, `Sola Scriptura.md` | Confession history, authority of Scripture | |
| 3 | Of God's Decree | ✅ | `Romans 9.md`, `Romans 9 (B).md` | Election, predestination | Cited from pulpit |
| 24 | Of the Civil Magistrate | ✅ | `Romans 13.md` | Applied to Romans 13 | theological-map line 798 |
```

**Source**: 13 explicit 1689 references in theological-map.md, 2 in sermon-map.md. The 1689 has 32 chapters — this map shows which have been cited, which haven't, and where the gaps are.

---

### 6. Passage Chain Map — `.claude/passage-chain-map.md`

**Format**: Theological chains showing passage dependencies.

```markdown
### Adam → Christ (Federal Headship)

| Step | Passage | Doctrine | Sermon(s) | Status |
|------|---------|----------|-----------|--------|
| 1 | Genesis 1:26-28 | Imago Dei, dominion mandate | `Gen 1-2 - beautiful but not safe.txt` | ✅ Preached |
| 2 | Genesis 3:1-24 | Fall, curse, protoevangelium | `Genesis 3 - Sanctity of Life Sunday.md` | ✅ Preached |
| 3 | Romans 5:12-21 | One man's sin → one man's righteousness | `Romans 5.md` | ✅ Preached |
| 4 | 1 Corinthians 15:20-28 | Last Adam, resurrection | | ⬜ Not yet preached |
| 5 | Revelation 21:1-5 | New creation, curse reversed | | ⬜ Not yet preached |
```

**Enables**: "If you're preaching X, you should have covered Y first." Prerequisite awareness for sermon planning.

**Note**: Another thread is already working on this. If that thread completes it, this task is done. If not, build it here.

---

## Phase 2: Skill Operations (Add to sermon-map SKILL.md)

### 7. Operation 8: QUOTE — Quote Map Maintenance

**Trigger**: When a sermon is indexed or updated that contains attributed quotes.

**Procedure**:
1. Extract all attributed quotes from the sermon
2. Check quote-map.md for existing entries (Grep by author or key phrase)
3. If new: add entry with full text, source, verification tier, sermon reference
4. If existing: increment usage count, add sermon to "Used In" column
5. Apply verification hierarchy (Green/Yellow/Red) based on available evidence
6. Record verification chain

---

### 8. Operation 9: ILLUSTRATE — Illustration Map Maintenance

**Trigger**: When a sermon is indexed or updated that contains named or significant illustrations.

**Procedure**:
1. Extract all illustrations (named + significant unnamed)
2. Check illustration-map.md for existing entries (Grep by name or type)
3. If new: add entry with full text/retelling, type, passage, sermon reference
4. If existing: increment usage count, add sermon to "Used In"
5. Flag reuse for human review (same as DEDUP Tier 1, now backed by the illustration map)

---

## Phase 3: Subject Index Enhancements

### 9. Subject Index by Sermon Count (Least to Most)

**New section** in sermon-map.md (or separate file `.claude/subject-density-index.md`):

A ranked list of all 44 subject categories sorted by entry count, least to most. This is a **preaching gap signal** — thin categories reveal undertreated topics.

```markdown
## Subject Index — By Sermon Count (Least → Most)

| Rank | Category | Entries | Gap Signal |
|------|----------|---------|-----------|
| 1 | Lord's Supper / Communion | 1 | 🔴 Critical gap |
| 2 | Resources / Unattributed Material | 1 | — (meta-category) |
| 3 | Sanctity of Life | 1 | 🔴 Critical gap |
| 4 | Hypocrisy / Self-Righteousness | 2 | 🟡 Thin |
| 5 | Identity in Christ / Exile | 2 | 🟡 Thin |
| ... | ... | ... | ... |
| 44 | Evangelism / Missions / Great Commission | 20 | ✅ Strong |
```

**Gap signals**: 🔴 Critical (1 entry), 🟡 Thin (2–3 entries), ✅ Strong (5+).

---

## Phase 4: Standardization & Disambiguation

### 10. Companion File Decision Tree

**Problem**: When two or more files cover the same passage, no standard way to distinguish "different version of same sermon" from "independent sermon on same passage."

**Decision tree** (add to SKILL.md under INDEX):

```
Q1: Same preacher, same passage?
  → No: Independent sermons. Separate entries.
  → Yes: Q2

Q2: Same core outline and illustrations?
  → Yes: Same sermon, different stage.
    Label: "Version A (raw) / Version B (polished)" with slash notation
    Use format: `File1.md` / `File2.md` in same row
  → No: Q3

Q3: Same passage but different theological angle, different occasion, or different year?
  → Yes: Independent sermons on same passage.
    Separate rows. Cross-reference note: "see also [other file] — distinct sermon on same passage"
  → Unclear: Flag for human review: ⬜ COMPANION STATUS UNRESOLVED
```

**Apply to known ambiguous cases**:
- Genesis 22 (3 files): Binding of Isaac (evening sermon) / There and Back Again (transcript) / The Testing Ground (includes Gen 23) — likely 2 versions + 1 independent
- Romans 1 (2 files): `Romans 1.md` (cult-teaching format) / `Romans 1 (2024).md` (expository-anthropic format) — already documented as same row with slash notation

### 11. Handle Multiple Preachings of Same Passage

**Problem**: Romans 1 preached once in the cult series and once in the Romans series. Both must appear distinctly on the map.

**Standard**: Each preaching gets its own row. Differentiate by:
- Year in parenthetical: `Romans 1 (2024)` vs `Romans 1 (series)`
- Occasion marker in Title column: `*(cult series)*`, `*(Romans series)*`, `*(evening sermon)*`
- Cross-reference note in Subject column: `"distinct from [other entry] — different occasion/year"`

**Already partially implemented** (line 26 of sermon-map.md uses slash notation for Romans 1). Formalize and audit all cases.

---

### 12. Incomplete Manuscript Standardization

**Problem**: No consistent marker. Some say `*(raw draft)*`, some `*(incomplete)*`, some just stop mid-sentence.

**Standard marker**: `⬜ INCOMPLETE: [specific gap]`

Examples:
- `⬜ INCOMPLETE: cuts off mid-narrative at "Things kept deteriorating." No resolution, no Scripture, no gospel close.`
- `⬜ INCOMPLETE: ends at "three roles of Christ" exposition point. No gospel close.`
- `⬜ INCOMPLETE: introduction only. Cuts off at start of "Relevant Scriptures" section.`

**Apply to**: 12 known incomplete sermons from unfinished-work-tracker.md, plus any discovered during audit.

**Placement**: Title column, after the status marker: `*(raw draft)* ⬜ INCOMPLETE: [gap]`

---

### 13. Topical Sermon Passage-Secondary Marking

**Problem**: Format 3 (Topic | Passage | File | Type) treats topic and passage as co-equal. Some topical sermons use a passage as anchor text but aren't exegetical on it.

**Standard**: Add `*(anchor only)*` after the passage when it's secondary:

```
| Cultural Marxism | Romans 10:12-13 *(anchor only)* | `cultural-marxism.md` | sermon |
```

This tells the reader: the passage is referenced but the sermon isn't an exposition of it. Don't count this as "Romans 10:12-13 has been preached."

---

### 14. Format Consistency Cleanup

Three standardizations, applied across the entire sermon-map:

**A. Companion file notation** → Always slash notation in the File column: `` `File1.md` / `File2.md` ``
- Current inconsistencies: sometimes inline cross-reference notes, sometimes parenthetical sourcing
- Count to audit: 19 known companion pairs + any undiscovered

**B. Flag placement** → Always inline in the Subject column, never in separate paragraphs after the entry
- Grep for flags outside table cells and move them inline

**C. Status markers** → Always in the Title column: `*(raw draft)*`, `*(raw transcript)*`, `*(repaired draft)*`, `✓ **[polished]**`
- Audit for markers that appear in Type column or as separate rows
- Move to Title column

---

### 15. Date Map Protocol for Non-Romans Sermons

**Current state**: Future Sermons and Non-Series Sermons tables are empty.

**Protocol**:
- When a non-Romans sermon has a known preaching date: add to Non-Series Sermons table with actual date
- When a sermon's date is unknown: add to a new `### Undated Sermons` section (track, don't guess)
- **Date conflicts**: If a non-series sermon lands on a Sunday already occupied by a Romans sermon, note both in the date map. A Sunday can have two entries (AM/PM, or series + special).
- As sermons are worked on and dates discovered, move from Undated → Non-Series

---

### 16. Cross-Reference Audit (Mechanical)

**Problem**: Not all 39 Romans sermons are cited in their relevant theological-map categories.

**Procedure**:
1. For each Romans sermon, extract doctrinal claims and explicit positions
2. Check theological-map.md for whether that sermon is cited in the relevant category
3. If missing, add the citation with file reference and quote
4. Track completion (0/39 → 39/39)

This is mechanical work — no theological judgment needed, just ensuring every sermon's positions are reflected in the theological map.

---

### 17. Subject Index Density Tracker

**Purpose**: Keep the "by sermon count" index current as new sermons are added.

**Implementation**: After every INDEX or UPDATE operation, regenerate the count for affected categories. This can be a sub-step of INDEX rather than a standalone operation.

---

## Phase 5: Skill Integration

After all maps are built, update:

1. **SKILL.md** — Add Operations 8 (QUOTE) and 9 (ILLUSTRATE). Update INDEX to include companion file decision tree, incomplete manuscript markers, passage-secondary marking, and subject density tracking.
2. **skill-rules.json** — Add new map files to `fileTriggers.pathPatterns`
3. **claude.md** — Add new maps to the Reference Maps table
4. **sermon-map.md** — Apply all format standardizations

---

## Execution Order

| Step | Task | Depends On | Effort |
|------|------|-----------|--------|
| 1 | Quote Map (full text extraction) | — | Medium |
| 2 | Illustration Map (full text extraction) | — | Medium |
| 3 | People Group Registry | — | Low |
| 4 | BFM Article Index | — | Low |
| 5 | 1689 LBCF Map | — | Low-Medium |
| 6 | Subject Index by Sermon Count | — | Low |
| 7 | Incomplete Sermon Markers (12 sermons) | — | Low |
| 8 | Quote Verification Hierarchy | Step 1 | Low |
| 9 | Companion File Decision Tree + audit | — | Low |
| 10 | Multiple Preachings Standard | Step 9 | Low |
| 11 | Topical Passage-Secondary Marking | — | Low |
| 12 | Format Consistency Cleanup | Steps 9–11 | Medium |
| 13 | Date Map Non-Romans Protocol | — | Low |
| 14 | Cross-Reference Audit (39 sermons) | — | Medium |
| 15 | Passage Chain Map | — | Medium |
| 16 | Subject Density Tracker | Step 6 | Low |
| 17 | Skill Integration (SKILL.md, rules, claude.md) | Steps 1–16 | Low |

**Parallelizable**: Steps 1–7 can all run concurrently. Steps 8–13 can run concurrently after their dependencies. Step 17 is the final integration pass.

---

*Soli Deo Gloria.*
