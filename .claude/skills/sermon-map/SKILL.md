---
name: sermon-map
description: "Sermon mapping and indexing skill. Maintains sermon-map.md, theological-map.md, series-trajectory.md, and date-map.md. Fires when sermons are created, modified, or imported. Provides gap analysis, illustration deduplication, and cross-map integrity checks."
---

# Sermon Map Skill

**Priority**: HIGH — The sermon map is the connective tissue of this repository. Every other skill depends on it.

---

## Purpose

This skill maintains `.claude/sermon-map.md` as the single source of truth for the sermon inventory. It also maintains cross-references to `.claude/theological-map.md`, `.claude/series-trajectory.md`, and `.claude/date-map.md`.

Ten operations: **INDEX**, **UPDATE**, **AUDIT**, **CONNECT**, **GAP**, **DEDUP**, **DATE**, **QUOTE**, **ILLUSTRATE**, **COVERAGE**.

### Relationship to Other Skills

| Skill | Relationship |
|-------|-------------|
| careful-not-clever | sermon-map fires AFTER careful-not-clever verifies content; map entries include verification status |
| like-a-human | sermon-map references voice baseline sermons identified in like-a-human |
| voice-audit | sermon-map records authenticity risk assessments from voice-audit |
| thus-says-the-lord | sermon-map records evaluation scores from thus-says-the-lord |
| cognitive-memory | sermon-map updates are encoded as memories for cross-session continuity |

---

## Map Entry Formats

The sermon map uses **eight distinct formats**. Every operation must detect the correct format and match it precisely.

### Format 1: Sermon Series Tables

Used by: Romans Primary, Romans Supporting, Special Messages, Five Solas, Doctrines of Grace, BFM Series.

```
| Passage | Title | File | Subject |
|---|---|---|---|
```

The 4th column is **Subject**, not Summary. Density varies by sermon importance:

- **Romans primary**: 500–2000 chars. Point-by-point exposition, Greek terms, illustrations, cross-references, verification flags. Example:

```
| Romans 4:1-8 | In Christ Alone: Where Justice Meets Grace | `Romans 4 - In Christ Alone- Where Justice Meets Grace.md` | Abraham justified before Law and circumcision; faith as empty hand; ledger metaphor (debt cancelled, righteousness credited); *logizomai* word study... |
```

- **Supporting files**: 150–400 chars. Key themes, companion file notes.
- **Special messages**: Varies widely. Some polished entries run 1000+ chars.

**Status markers in Title column**: `*(raw draft)*`, `*(raw transcript)*`, `*(repaired draft)*`, `✓ **[polished]**`

### Format 2: Archive Sermons by Bible Book

```
| Passage | Subject | File | Type |
|---|---|---|---|
```

Note column order differs: Subject before File, Type replaces Title.

Type values: `sermon`, `memorial`, `sermon (raw)`, `bible study`, `notes`, `sunday school`, `teaching`, `polished draft`, `raw draft`, `raw transcript`.

Example:
```
| Genesis 1–2 | Gap Theory refuted; Hebrew chiasm in creation week; creation reflects God; Sabbath; beautiful but not safe | `Gen 1-2 - beautiful but not safe.txt` | sermon |
```

### Format 3: Topical / Doctrinal Sermons

```
| Topic | Passage | File | Type |
|---|---|---|---|
```

First column is **Topic** (not Passage). Type column carries the full description payload, sometimes 1000+ chars.

### Format 4: Memorial Services

```
| Person | Passage | File |
|---|---|---|
```

**Three columns only.** No Subject or Type.

### Format 5: Ordination Services

```
| Person | Passage | File | Subject |
|---|---|---|---|
```

Four columns. Person replaces Passage as first column.

### Format 6: Non-Sermon Files

```
| File | Contents |
|---|---|
```

Two columns only.

### Format 7: Studies, Notes, & Bible Studies

```
| File | Subject | Type |
|---|---|---|
```

Three columns. File first.

### Format 8: Subject Index

Bullet-list format, not a table. Grouped by 32+ topic categories.

```
### Adoption (Theology of)
- `adoption - gal 3.md` — Galatians 3:23–29 — Law, faith, and adoption; dumb laws hook; debtors' prison; *huios*/*huion* word study
- `Sermon - Every Little Girl Needs a Daddy.md` — Galatians 3:27–4:7 — **Polished version**; Lily/Mercedes story; penal substitution + adoption as sons
```

Pattern: `` - `filename.md` — Passage — Description ``

Uses backtick-wrapped filenames and em-dash (`—`) separators.

### Flag Vocabulary

The full flag system — not just three symbols:

| Symbol | Meaning |
|--------|---------|
| ⚠️ | Unverified claim, needs checking. Severity varies: "verify before pulpit use" vs. "do not attribute from pulpit" |
| ❌ | Error found AND corrected. Marks what was wrong, with correction noted inline |
| ✅ / ✓ | Verified correct |
| ⬜ | Placeholder/TODO (e.g., "pew Bible page number") |
| *(Month Year)* | Date-stamped correction |
| **[polished]** | State marker for completion level |
| `corrected from X → Y` | Inline correction notation |
| `raw → flagged → repaired` | Multi-stage tracking |

---

## Operation 1: INDEX — Add a New Sermon to the Map

**Trigger**: A new sermon file is created or imported.

### Step-by-Step Procedure

1. **Read the entire sermon file.** Not just the title. A sermon's actual content is rarely predictable from its first paragraph. This is a firm rule.

2. **Extract structured metadata:**
   - Passage (book, chapter, verses)
   - Title (from the sermon itself, not the filename)
   - Filename (exact, for backtick reference)
   - Type: raw draft / polished / transcript / sermon / bible study
   - Key themes (semicolon-separated list)
   - Illustrations used (named: Bannockburn, Corrie ten Boom, etc.)
   - People group (**REQUIRED** — every sermon must have a People Group of the Week. If missing, flag: `⚠️ MISSING PEOPLE GROUP — source from Joshua Project before next preach`)
   - Verification flags (⚠️ for unverified claims, ✅ for verified)
   - Cross-references to other Scripture
   - Gospel presence (is there a gospel close?)
   - Greek/Hebrew terms used

3. **Detect the correct format.**
   - Is this a Romans series sermon? → Format 1 (Passage | Title | File | Subject)
   - Is this a non-Romans sermon by Bible book? → Format 2 (Passage | Subject | File | Type)
   - Is this topical/doctrinal? → Format 3 (Topic | Passage | File | Type)
   - Is this a memorial service? → Format 4 (Person | Passage | File)
   - Is this an ordination? → Format 5 (Person | Passage | File | Subject)
   - Is this a study/notes? → Format 7 (File | Subject | Type)

4. **Scale Subject/description density by importance:**
   - Romans series: comprehensive (500–2000 chars) — every point, every Greek word, every illustration, every flag
   - Polished non-Romans: moderate (200–600 chars) — key themes, flags, notable illustrations
   - Raw transcripts/drafts: shorter (100–300 chars) with more flags — basic metadata, verification warnings

5. **Check for companion files.** Before creating a new entry:
   - Grep the map for the same passage and similar titles
   - If a related entry exists, apply the **Companion File Decision Tree**:

   ```
   Q1: Same preacher, same passage?
     → No: Independent sermons. Separate entries.
     → Yes: Q2

   Q2: Same core outline and illustrations?
     → Yes: Same sermon, different stage.
       Label: slash notation in same row: `File1.md` / `File2.md`
       Add status markers: *(raw)* / *(polished)*
     → No: Q3

   Q3: Same passage but different theological angle, different occasion, or different year?
     → Yes: Independent sermons on same passage.
       Separate rows. Cross-reference: "see also [other file] — distinct sermon on same passage"
     → Unclear: Flag for human review: ⬜ COMPANION STATUS UNRESOLVED
   ```

   - **Multiple preachings of the same passage**: Each preaching gets its own row. Differentiate by year in parenthetical (`Romans 1 (2024)` vs `Romans 1 (series)`), occasion marker in Title column (`*(cult series)*`, `*(Romans series)*`, `*(evening sermon)*`), and cross-reference note in Subject column (`"distinct from [other entry] — different occasion/year"`).
   - **Companion file notation standard**: Always use slash notation in the File column: `` `File1.md` / `File2.md` ``. No inline cross-reference notes or parenthetical sourcing as alternatives.
   - Never silently overwrite an existing entry

5b. **Mark incomplete manuscripts.** If the sermon is truncated, unfinished, or missing sections:
   - Add `⬜ INCOMPLETE: [specific gap]` in the Title column after the status marker
   - Be specific: "cuts off mid-narrative at [quote]", "ends at [point]; no gospel close", "introduction only"
   - Format: `*(raw draft)* ⬜ INCOMPLETE: [gap description]`

5c. **Mark passage-secondary entries.** For Format 3 (topical) entries where the passage is an anchor text but the sermon isn't exegetical on it:
   - Add `*(anchor only)*` after the passage in the Passage column
   - This tells readers: the passage is referenced but not exposited. Don't count it as "passage X has been preached."

6. **Locate the target section.**
   - Use Grep to find the section header (e.g., `### Genesis`, `## Romans Series`)
   - Read with offset/limit to get the surrounding context (50–100 lines)
   - Insert the new entry at the correct position (alphabetical by passage within the section, or chronological for Romans series)
   - Use Edit to insert — never rewrite the whole file

7. **Place in Subject Index.**
   - Evaluate which of the 32+ thematic categories apply
   - Add bullet entries to each relevant category using Format 8
   - Match existing density and style in that category

8. **Run DEDUP check** before finalizing (see Operation 6).

9. **Run DATE** to assign a preaching date (see Operation 7).

---

## Operation 2: UPDATE — Refresh an Existing Map Entry

**Trigger**: A sermon file is modified (flags resolved, ESV corrections applied, content revised).

### Procedure

1. **Find the existing entry.** Use Grep to search for the filename (in backticks). Do NOT read the whole file.

2. **Identify what changed** in the sermon:
   - Flags resolved? Mark ⚠️ → ✅ or note correction inline
   - New content added? Update the Subject column
   - Verification status changed? Update markers
   - Score assigned by thus-says-the-lord? Note if significant

3. **Update surgically.** Use Edit on the specific entry. Do NOT rewrite from scratch. Preserve the existing structure. Add to it, don't replace it.

4. **Date-stamp updates** where appropriate: `*(March 2026)*`

5. **Sync thematic entries.** If the sermon appears in Subject Index categories, check those entries too. If flags were resolved in the by-book entry, reflect that in the thematic entries.

---

## Operation 3: AUDIT — Check Map Integrity

**Trigger**: On demand — keywords: "audit map", "check map", "map integrity"

### Scope Boundaries

- **In-scope**: Root `.md` sermon files, `Sermon - *.md`, pastor's own files in ``
- **Out-of-scope**: `quotes-and-references/`, other preachers' sermons in `Other-Sermons/`
- Without scope boundaries, AUDIT would flag 1500+ reference files as "orphans"

### Procedure

1. **Scan sermon files** on the filesystem (Glob for `*.md` in root, `Sermon - *.md`, `*.md`)
2. **Scan map entries** by Grepping for backtick-wrapped filenames in sermon-map.md (process in chunks by section)
3. **Compare and report:**
   - **Orphaned files**: pastor's own sermons with no map entry
   - **Phantom entries**: map entries pointing to files that don't exist (mark with `⚠️ FILE MISSING FROM DISK`)
   - **Stale flags**: unresolved ⚠️ flags (note age if datable)
   - **Missing verification**: entries with no ✅/⚠️/❌ status at all

---

## Operation 4: CONNECT — Cross-Reference Between Maps

**Trigger**: When a sermon touches a doctrine tracked in the theological map.

### Noise Suppression

Only suggest additions when:
1. The sermon contains a doctrinal statement **not yet reflected** in the theological map (novel position)
2. The sermon contains an explicit quote usable as evidence for an existing position **not yet cited** (novel evidence)
3. The user explicitly asks for cross-referencing

Do NOT suggest every doctrinal touchpoint. The theological map has 100+ positions and every sermon touches multiple doctrines. Surface only what's genuinely new.

### Procedure

1. After reading the sermon, identify doctrinal claims and explicit quotes
2. Grep the theological map for the relevant doctrine section
3. Check if this specific claim or quote is already cited
4. If novel, suggest an addition with the exact quote and file reference
5. Update series-trajectory.md if the sermon advances the Romans arc

---

## Operation 5: GAP — Identify Preaching Gaps

**Trigger**: On demand — keywords: "gap analysis", "what haven't we preached", "preaching gaps"

### Distinguishing "Not Preached" from "Not Mapped"

1. Check the sermon map for coverage by passage
2. Cross-reference against actual sermon files on the filesystem (Glob for filenames suggesting a passage)
3. Only report a passage as a **true gap** after confirming it's absent from BOTH the map AND the filesystem
4. If a file exists but has no map entry, report it as **"preached but unmapped"** — this is an AUDIT finding, not a GAP finding

### Report Format

- Romans passages not yet covered
- OT books with no sermons
- NT books with thin coverage
- Passages in `.claude/romans-14-16-plan.md` not yet written
- Book framework alignment (Part I–V chapter mapping from `claude.md`)

---

## Operation 6: DEDUP — Illustration Deduplication

**Trigger**: When writing a new sermon or before committing.

### Two-Tier Deduplication

**Tier 1 — Named illustrations (exact match, high confidence):**
- Search the map for named illustrations: Bannockburn, Hiroo Onoda, buckwheat milling, Treblinka, Corrie ten Boom, Augustine conversion, dirty cup, dead cat, boulder, Special Olympics, etc.
- Grep sermon-map.md for the illustration name
- If found: "This illustration was used in [sermon]. Consider a fresh illustration."

**Tier 2 — Unnamed illustrations (semantic match, best-effort):**
- Many illustrations lack stable identifiers: "woman who had major surgery," "friend whose daughter was kidnapped"
- Extract illustration type: medical, legal, military, family, pastoral, historical, literary
- Match on semantic similarity within the same type
- Flag possible reuse for **human review** — not automated rejection
- False negatives acceptable. False positives should be rare.

---

## Operation 7: DATE — Assign Preaching Dates

**Trigger**: When INDEX fires for a new sermon.

### Procedure

1. Read `.claude/date-map.md` to find the last assigned date and number
2. Determine the next upcoming Sunday from the current date:
   - If today is Sunday, use today
   - If today is any other day, use the coming Sunday
3. Check if that Sunday is already occupied in the date map
   - If occupied, use the following Sunday
4. Add a new row to the appropriate table:
   - Romans series → "Romans Series" table
   - Non-series → "Non-Series Sermons" table or "Future Sermons" table
5. Format: `| # | Date | Passage | Title | File |`
6. Dates in ISO format: `YYYY-MM-DD`

### Existing Backfill

All 39 Romans sermons (Romans 1–16) have been backdated from 2026-03-15 (final sermon), one per Sunday working backwards. Series began 2025-06-22.

### Undated Sermons

When a non-series sermon has no known preaching date, add it to the `### Undated Sermons` section in date-map.md. Do not guess dates. As sermons are worked on and dates discovered, move them from Undated → Non-Series.

### Date Conflicts

A single Sunday can have two entries (AM series + PM special, or series + memorial). When a non-series sermon lands on an occupied Sunday, record both. Note the occasion: `*(AM)*`, `*(PM)*`, `*(evening)*`, `*(special service)*`. Romans series dates are immutable.

---

## Operation 8: QUOTE — Quote Map Maintenance

**Trigger**: When a sermon is indexed or updated that contains attributed quotes.

**Map file**: `.claude/quote-map.md`

### Procedure

1. **Extract all attributed quotes** from the sermon — any text in quotation marks with an author name attached.
2. **Check quote-map.md** for existing entries (Grep by author name or key phrase from the quote).
3. **If new quote**:
   - Add entry with full quote text, source work (if known), verification tier, verification chain, and sermon reference
   - Apply verification hierarchy:
     - ✅ **Green**: Exact wording confirmed against primary source (book, page, sermon number)
     - ⚠️ **Yellow**: Quote is real but exact source book/page unknown, or wording unconfirmed
     - ❌ **Red**: Unverified, disputed, or potentially fabricated; may be misattributed
   - Record verification chain: `"via MacArthur sermon #2234"`, `"confirmed ESV Ps 19:1"`, `"widely attributed, no primary found"`
4. **If existing quote**: Increment usage count, add sermon to "Used In" column.
5. **Removed/fabricated quotes**: If a quote was cut from a sermon as fabricated, keep it in the map marked ❌ with a note. This prevents re-introduction.

### Relationship to careful-not-clever

The quote map records verification status; careful-not-clever enforces it. When careful-not-clever flags a quote as ⚠️, the quote map should reflect that status. When verification resolves, update both.

---

## Operation 9: ILLUSTRATE — Illustration Map Maintenance

**Trigger**: When a sermon is indexed or updated that contains named or significant illustrations.

**Map file**: `.claude/illustration-map.md`

### Procedure

1. **Extract all illustrations** from the sermon:
   - Named illustrations (Bannockburn, Corrie ten Boom, Mueller orphans, etc.)
   - Significant unnamed illustrations (medical, military, pastoral stories with teaching weight)
   - Recurring personal illustrations (Aunt Judy, Grace the dog, Hurricane Irma, etc.)
2. **Check illustration-map.md** for existing entries (Grep by name or descriptive identifier).
3. **If new illustration**:
   - Add entry with full text or condensed retelling (3-5 sentences preserving teaching point, emotional arc, key details)
   - Classify by type: Personal, Pastoral, Military, Medical, Historical, Biographical, Literary, Scientific, Theological, Humorous, Cultural
   - Record passage connections and sermon reference
4. **If existing illustration**: Increment usage count, add sermon to "Used In" column. Note if the same illustration is used for a different theological point.
5. **Flag reuse** for human review — same as DEDUP Tier 1, now backed by the illustration map. Two or more uses isn't necessarily wrong, but the pastor should know.

### Relationship to DEDUP

DEDUP (Operation 6) checks for illustration reuse before committing a new sermon. ILLUSTRATE (Operation 9) maintains the persistent registry. DEDUP reads the illustration map; ILLUSTRATE writes to it.

---

## Large-File Operations

The sermon map is 1291+ lines. **All operations must work on sections, never the whole file at once.**

### Standard Operating Procedure

1. **Grep** to locate the relevant section header or entry (by filename, passage, or heading)
2. **Read with offset/limit** to get surrounding context (typically 50–100 lines around the match)
3. **Edit** to make surgical changes to the specific entry or section

### Operation-Specific Patterns

| Operation | Find | Read | Edit |
|-----------|------|------|------|
| INDEX | Grep for Bible book section header | Read that section (50–100 lines) | Append new entry before next section |
| UPDATE | Grep for filename in backticks | Read entry and surrounding context | Edit specific lines |
| AUDIT | Grep for all filenames mentioned | Compare against Glob results | Report discrepancies (chunk by book) |
| CONNECT | Grep theological-map.md for doctrine | Read relevant section | Suggest addition |
| GAP | Grep sermon-map.md by book headers | Read coverage sections | Report missing passages |
| DEDUP | Grep for illustration names | Read matching entries | Flag reuse |
| DATE | Grep date-map.md for last entry | Read last 10 lines of table | Append new row |
| QUOTE | Grep quote-map.md for author/phrase | Read author section | Add/update entry |
| ILLUSTRATE | Grep illustration-map.md for name/type | Read type section | Add/update entry |

**Never `Read` the entire sermon-map.md in a single call.**

---

## Design Principles

1. **The map is the pastor's index, not a database.** Entries are written in his voice, with his flags, his pastoral notes. The skill guides the format — it doesn't sterilize the content.

2. **Suggest, don't block.** This is a domain skill with "suggest" enforcement. It helps. It doesn't prevent work.

3. **Follow existing patterns.** The map's practice is richer than "one entry per file": some entries use slash notation (`File1.md / File2.md`), some companions get cross-reference notes, every sermon may appear in both a by-book section and thematic sections. Follow these patterns.

4. **Preserve the format.** 1291 lines of carefully maintained entries. Work within the format, not against it. No schema changes. No restructuring.

5. **Flag-aware.** Understand, preserve, and update the full flag vocabulary correctly.

6. **Soli Deo Gloria.** The map serves the preaching. The preaching serves the congregation. The congregation serves God. Every entry matters because every sermon carries the weight of "Thus says the Lord."
