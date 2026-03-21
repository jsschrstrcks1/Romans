# Plan: Sermon Mapping Skill

## The Problem

The sermon map (`.claude/sermon-map.md`, 364KB, 1291 lines) is the connective tissue of this entire repository. Every other skill depends on it — careful-not-clever checks it for prior illustrations, like-a-human references it for voice baseline sermons, thus-says-the-lord evaluates against it, and cognitive-memory stores decisions about it.

**But there is no skill that maintains it.** The map is manually updated. When a sermon is written, revised, imported, or flagged, someone must hand-edit the map entry. This creates three risks:

1. **Stale entries** — a sermon gets repaired (flags resolved, ESV corrections applied) but the map entry still shows the old flags
2. **Missing entries** — a new sermon or teaching gets written and never added to the map
3. **Drift between maps** — the sermon map, theological map, and series trajectory fall out of sync

The reference maps (MacArthur/Sproul/Spurgeon) have automated Python scripts that rebuild from JSON metadata. The pastor's own sermons — the most important ones — have no equivalent automation or even a structured skill to guide the mapping work.

## What the Skill Does

A new skill called **`sermon-map`** that fires when sermons are created, modified, or imported. It handles six operations:

### 1. INDEX — Add a new sermon to the map

When a new sermon file is created or imported:
- Read the sermon file
- Extract structured metadata: passage, title, filename, type (raw draft / polished / transcript / sermon / bible study), key themes, illustrations used, people group, verification flags, cross-references, gospel presence
- **Detect the correct format** — the map uses six distinct formats (see Section 2); the entry must match the format of the target section
- **Scale summary density to sermon importance**: Romans series gets 500-2000 char comprehensive summaries; polished non-Romans gets moderate treatment; raw drafts/transcripts get shorter entries with more flags
- Place it in the correct Bible book section (use Grep to find section header, Read with offset to get context, Edit to insert)
- **Also place in thematic index**: evaluate which thematic categories apply (Evangelism, Faith, Five Solas, Gospel, Grace, Sovereignty, Suffering, etc.) and add bullet entries to each relevant category
- **Check for companion files**: if a related entry exists (same passage, similar title), cross-reference rather than creating a duplicate — use slash notation or "distinct from" / "archive copy of" notes matching existing patterns
- Check for duplicate entries (same passage, same title)
- Check for duplicate illustrations against the full map (two-tier: named exact match + unnamed semantic match)

### 2. UPDATE — Refresh an existing map entry

When a sermon file is modified (flags resolved, ESV corrections applied, content revised):
- Find the existing map entry
- Identify what changed: new flags resolved? new content added? verification status changed?
- Update the entry to reflect current state
- Preserve the existing entry structure (don't rewrite from scratch — update surgically)
- Log what changed in the entry (e.g., "⚠️ flag resolved March 2026" notation pattern already used)

### 3. AUDIT — Check map integrity

On demand (keyword trigger: "audit map", "check map", "map integrity"):
- Scan sermon files in the repository — **with scope boundaries**:
  - In-scope: root `.md` sermon files, `Sermon - *.md`, pastor's own files in `Other-Sermons/Sermons/`
  - Out-of-scope: `quotes-and-references/`, other preachers' sermons in `Other-Sermons/`
  - Without scope boundaries, AUDIT would flag 1500+ reference files as "orphans"
- Compare against sermon-map.md entries (scan in sections, not full-file read)
- Report: files with no map entry, map entries pointing to missing files, entries with outdated flags, entries missing verification status
- Check for orphaned files (pastor's own sermons not in the map)
- Check for phantom entries (map entries with no corresponding file)

### 4. CONNECT — Cross-reference between maps

When a sermon touches a doctrine tracked in the theological map:
- Check if the theological-map.md has a relevant entry
- **Noise suppression**: only suggest additions when the sermon contains a doctrinal statement not yet in the theological map OR an explicit quote usable as novel evidence for an existing position. Do not suggest every doctrinal touchpoint — surface only what's genuinely new.
- Update the series trajectory if the sermon advances the Romans arc
- Cross-reference against reference maps (MacArthur/Sproul/Spurgeon) for quote verification opportunities

### 5. GAP — Identify preaching gaps

On demand (keyword trigger: "gap analysis", "what haven't we preached", "preaching gaps"):
- Survey the sermon map by Bible book
- **Distinguish "not preached" from "not mapped"**: cross-reference against actual sermon files on the filesystem, not just the map. A file matching a passage but absent from the map is "preached but unmapped" (an AUDIT finding), not a true gap.
- Report: Romans passages not yet covered, OT books with no sermons, NT books with thin coverage
- Cross-reference against the book framework in claude.md (Part I-V chapter mapping) to identify missing chapters
- Check for passages in the romans-14-16-plan.md that haven't been written yet

### 6. DEDUP — Illustration deduplication

When writing a new sermon or before committing:
- Scan the proposed sermon for illustrations
- **Two-tier deduplication**:
  - **Tier 1 (named, exact match)**: Search the map for named illustrations (Bannockburn, Hiroo Onoda, buckwheat milling, Treblinka, Corrie ten Boom, etc.). High confidence.
  - **Tier 2 (unnamed, semantic match)**: Extract illustration types (medical, legal, military, family, pastoral) and match on semantic similarity. Flag possible reuse for human review. Best-effort — false negatives acceptable.
- Flag reuse: "This illustration was used in [sermon]. Consider a fresh illustration."
- This is critical — the map already tracks illustrations for exactly this purpose

## Skill File Structure

```
.claude/skills/sermon-map/SKILL.md
```

### Metadata Block (YAML frontmatter)

```yaml
name: sermon-map
description: "Sermon mapping and indexing skill. Maintains the sermon map, theological map, and series trajectory. Fires when sermons are created, modified, or imported. Provides gap analysis, illustration deduplication, and cross-map integrity checks."
```

### Integration with Existing Skills

| Skill | Relationship |
|-------|-------------|
| careful-not-clever | sermon-map fires AFTER careful-not-clever verifies content; map entries include verification status |
| like-a-human | sermon-map references voice baseline sermons identified in like-a-human |
| voice-audit | sermon-map records authenticity risk assessments from voice-audit |
| thus-says-the-lord | sermon-map records evaluation scores from thus-says-the-lord |
| cognitive-memory | sermon-map updates are encoded as memories for cross-session continuity |

### Activation Rules (for skill-rules.json)

```json
{
  "sermon-map": {
    "enabled": true,
    "type": "domain",
    "enforcement": "suggest",
    "priority": "high",
    "description": "Maintains sermon-map.md, theological-map.md, and series-trajectory.md. Fires when sermons are created, modified, or imported. Provides gap analysis, illustration deduplication, and cross-map integrity.",
    "promptTriggers": {
      "keywords": [
        "map", "sermon map", "index", "catalog",
        "gap analysis", "preaching gaps", "what haven't we preached",
        "audit map", "check map", "map integrity",
        "illustration check", "dedup", "duplicate illustration",
        "add to map", "update map", "new sermon"
      ],
      "intentPatterns": [
        "(add|update|index|catalog|map).*?sermon",
        "(check|audit|verify).*?map",
        "(gap|missing|uncovered).*?(passage|sermon|book)",
        "(duplicate|reuse|already used).*?illustration"
      ]
    },
    "fileTriggers": {
      "pathPatterns": [
        ".claude/sermon-map.md",
        ".claude/theological-map.md",
        ".claude/series-trajectory.md"
      ],
      "contentPatterns": [
        "Sermon",
        "sermon",
        "Romans"
      ]
    },
    "toolTriggers": ["Write"],
    "autoLoad": {
      "mainFile": ".claude/skills/sermon-map/SKILL.md",
      "maxLines": 300,
      "loadOnFirstFileEdit": false
    },
    "activationMessage": "Sermon mapping active. Every sermon belongs on the map.",
    "coActivation": {
      "always_with": ["careful-not-clever"],
      "optional_with": ["cognitive-memory"],
      "note": "Map updates should always be verified (careful-not-clever) and optionally remembered (cognitive-memory)."
    }
  }
}
```

## SKILL.md Content Outline

The SKILL.md file will contain:

### Section 1: Purpose and Relationship
- What this skill does
- How it relates to other skills (the mapping layer that other skills depend on)
- The sermon-map.md is the single source of truth for sermon inventory

### Section 2: Map Entry Formats (Six Formats, Not Three)
- Document all six formats used in sermon-map.md with examples of each:
  1. **Romans primary**: `| Passage | Title | File | Summary |` — richest entries, 500-2000 character summaries with point-by-point exposition, Greek words, illustrations, cross-references, flags
  2. **Romans supporting files**: `| Passage | Title | File | Subject |` — shorter entries for companion files (raw drafts, flagged drafts, archive copies)
  3. **Special messages**: `| Passage | Title | File | Subject |` — same headers as supporting files but different content density (memorial services, ordinations, etc.)
  4. **Non-Romans by book**: `| Passage | Subject | File | Type |` — Subject column carries the real payload, varies from one word ("sermon") to 30+ lines of flags and corrections
  5. **Thematic index**: `- File — Passage — Description` — **bullet-list format, not a table** — grouped by topic (Evangelism, Faith, Five Solas, Gospel, Grace, Sovereignty, Suffering, etc.)
  6. **Memorial services**: distinct format for funeral/memorial sermon entries
- The INDEX operation must detect which section the new entry belongs in and match that section's specific format
- Flag vocabulary (full system, not just three symbols):
  - ⚠️ — unverified claim, needs checking (with severity levels: "verify before pulpit use" vs. "do not attribute from pulpit")
  - ❌ — error found AND corrected (marks what was wrong, with correction noted inline)
  - ✅ / ✓ — verified correct
  - ⬜ — placeholder/TODO (e.g., "pew Bible page number")
  - *(Month Year)* — date-stamped corrections
  - **[polished]** — state marker
  - Inline correction notation: `corrected from X → Y`
  - Multi-stage tracking: `raw → flagged → repaired`
- Verification status markers
- People group format
- Illustration tracking within entries

### Section 3: INDEX Operation
- Step-by-step for adding a new sermon
- Required fields
- **Format detection**: identify which of the six formats applies based on target section
- How to generate the summary — **density varies by sermon importance**:
  - Romans series sermons: comprehensive treatment (500-2000 chars) — point-by-point exposition, Greek terms, illustrations, cross-references, flags
  - Polished drafts of other sermons: moderate treatment — key themes, flags, notable illustrations
  - Raw transcripts and raw drafts: shorter treatment with more flags — basic metadata, verification warnings
- Placement rules (which Bible book section, sort order)
- **Thematic index placement**: every sermon must also be evaluated for thematic categories (Evangelism, Faith, Five Solas, Gospel, Grace, Sovereignty, Suffering, etc.) and added to one or more thematic sections simultaneously
- **Multi-file handling**: when a sermon has companion files (raw, flagged, repaired, archive):
  - Check if a related entry already exists (same passage, similar title)
  - If the new file is a companion to an existing entry: cross-reference with slash notation (`File1.md / File2.md`) or add a "distinct from" / "archive copy of" note — match the pattern already used in the map
  - If the new file is genuinely independent (different sermon on the same passage): create a separate entry
  - Never silently overwrite an existing entry for a companion file
- Dedup check before adding

### Section 4: UPDATE Operation
- How to find the existing entry (by filename, by passage) — **use Grep to locate, not full-file read**
- Surgical update rules (don't rewrite — modify)
- What triggers an update: flag resolution, ESV correction, content revision, score assignment
- Date-stamping updates (e.g., "*(March 2026)*")
- **Thematic sync**: when a by-book entry is updated, check if the sermon appears in thematic sections and update those entries to match (e.g., if flags are resolved in the by-book entry, reflect that in the thematic entry)

### Section 5: AUDIT Operation
- Full integrity scan procedure — **scan in sections, not full-file read** (see Section 10)
- Report format
- Orphan detection (files without map entries) — **with scope boundaries**:
  - **In-scope directories** (pastor's own sermons): root `.md` files, `Sermon - *.md` files, files explicitly referenced from sermon-map.md in `Other-Sermons/Sermons/`
  - **Out-of-scope directories** (reference material): `quotes-and-references/`, bulk files in `Other-Sermons/` that are other preachers' sermons
  - The skill must distinguish the pastor's own sermons from reference material — check the map for `Other-Sermons/` paths already referenced; only flag files in `Other-Sermons/` as orphans if they match patterns of the pastor's own work (e.g., contain "(raw draft)", "(raw transcript)", or are in the `Other-Sermons/Sermons/` subdirectory with first-person voice)
- Phantom detection (entries without files)
- Flag staleness check (unresolved flags older than 90 days)

### Section 6: CONNECT Operation
- Cross-referencing between sermon-map.md and theological-map.md
- **Noise suppression** — only suggest additions when:
  1. The sermon contains a doctrinal statement **not yet reflected** in the theological map (novel position)
  2. The sermon contains an explicit quote usable as evidence for an existing doctrinal position **not yet cited** (novel evidence)
  3. The user explicitly asks for cross-referencing
- Do NOT suggest every doctrinal touchpoint — the theological map has 100+ positions and every sermon touches multiple doctrines. Only surface what's genuinely new.
- Series trajectory updates
- Reference map cross-referencing

### Section 7: GAP Operation
- Gap analysis procedure — **must distinguish "not preached" from "not mapped"**:
  - First: check the sermon map for coverage by passage
  - Second: cross-reference against actual sermon files on the filesystem (Glob for filenames suggesting a passage)
  - Only report a passage as a true gap after confirming it's absent from BOTH the map AND the filesystem
  - If a file exists but has no map entry, report it as "preached but unmapped" (an AUDIT finding, not a GAP finding)
- Coverage report format
- Book framework alignment check
- Romans plan alignment check

### Section 8: DEDUP Operation
- **Two-tier deduplication**:
  - **Tier 1 — Named illustrations (exact match)**: Bannockburn, Hiroo Onoda, buckwheat milling, Treblinka, Augustine conversion, thief on cross, Corrie ten Boom, etc. Search the map and sermon files for exact name matches. High confidence, automated flagging.
  - **Tier 2 — Unnamed illustrations (semantic match, best-effort)**: Many illustrations are unnamed — "woman who had major surgery," "friend whose daughter was kidnapped and murdered," "man served sentence with honor, granted clemency," "operating-room light vs. living-room light." These lack stable identifiers. The skill should:
    - Extract illustration types (medical, legal, military, family, pastoral, historical, literary)
    - Match on semantic similarity within the same type
    - Flag possible reuse for **human review**, not automated rejection
    - Acknowledge this tier is best-effort — false negatives are acceptable, false positives should be rare
- Illustration extraction heuristics
- Search patterns in the sermon map
- Report format for duplicates

### Section 9: Integration with Hooks
- PostToolUse hook for Write: when a sermon file is written, suggest running INDEX or UPDATE
- Non-blocking — suggestion only
- Memory encoding after map updates

### Section 10: Large-File Operations (364KB / 1291 Lines)
- The sermon map exceeds comfortable single-read limits. **All operations must work on sections, never the whole file at once.**
- Standard operating procedure for every operation:
  1. **Grep** to locate the relevant section header or entry (by filename, passage, or section heading)
  2. **Read with offset/limit** to get the surrounding context (typically 50-100 lines around the match)
  3. **Edit** to make surgical changes to the specific entry or section
- INDEX: Grep for the target Bible book section header → Read that section → append the new entry before the next section header
- UPDATE: Grep for the filename or passage → Read the entry and surrounding context → Edit the specific lines
- AUDIT: Grep for all filenames mentioned in the map → compare against Glob results → report discrepancies (process in chunks by Bible book if needed)
- Never `Read` the entire sermon-map.md in a single call

## Implementation Steps

1. **Create** `.claude/skills/sermon-map/SKILL.md` with the full skill definition
2. **Update** `.claude/skill-rules.json` to add the sermon-map skill entry
3. **Update** `.claude/settings.json` to add a PostToolUse hint for map updates (non-blocking suggestion)
4. **Test** by running each operation against known sermons:
   - INDEX: Pick an unmapped sermon and generate its entry
   - UPDATE: Pick a sermon with resolved flags and update its entry
   - AUDIT: Run a full integrity scan
   - GAP: Generate a gap analysis
   - DEDUP: Check a recent sermon for illustration reuse
5. **Commit** all changes with clear description

## Design Principles

1. **The map is the pastor's index, not a database.** Entries are written in his voice, with his flags, his pastoral notes. The skill guides the format — it doesn't sterilize the content.

2. **Suggest, don't block.** This is a domain skill with "suggest" enforcement, not a guardrail. It helps. It doesn't prevent work.

3. **Entries follow the map's existing patterns, not a rigid rule.** The map's actual practice is richer than "one entry per file": some entries reference multiple files with slash notation (`File1.md / File2.md`), some companion files get their own entries with "archive copy of" or "distinct from" cross-references, and every sermon may appear in both a by-book section and one or more thematic sections. The skill follows these existing patterns rather than imposing a new schema.

4. **Preserve the existing format.** The sermon map has 1291 lines of carefully maintained entries. The skill works *within* that format, not against it. No schema changes. No restructuring.

5. **Flag-aware.** The flag system is the single most valuable feature of the map — and it's richer than three symbols. The full vocabulary includes ⚠️ (unverified, with severity levels), ❌ (error found and corrected), ✅/✓ (verified), ⬜ (placeholder/TODO), date-stamped corrections *(Month Year)*, state markers **[polished]**, inline correction notation (`X → Y`), and multi-stage tracking (`raw → flagged → repaired`). The skill must understand, preserve, and update all of these correctly.

6. **Soli Deo Gloria.** The map serves the preaching. The preaching serves the congregation. The congregation serves God. Every entry matters because every sermon carries the weight of "Thus says the Lord."

## Edge Cases Evaluated and Addressed

These edge cases were identified by testing the plan against the actual sermon-map.md data. Each is now addressed in the relevant section above.

| # | Edge Case | Fix | Where Addressed |
|---|-----------|-----|-----------------|
| 1 | Six formats, not three — map uses Romans primary, Romans supporting, special messages, non-Romans by book, thematic index (bullet list, not table), and memorial services | Document all six with examples; INDEX detects target format | Section 2, Section 3 |
| 2 | Multi-file entries — slash-joined files, "archive copy of," "distinct from" cross-references | Rules for when to cross-reference vs. create new entry | Section 3, Design Principle 3 |
| 3 | Thematic index is cross-cutting — same sermon in multiple categories | INDEX must also place in thematic sections; UPDATE must sync | Section 3, Section 4 |
| 4 | Summary density varies by importance — Romans gets 2000 chars, raw drafts get 20 | Codify density hierarchy by sermon type | Section 3 |
| 5 | Flag vocabulary is richer — 8+ states, not 3 | Document full flag vocabulary including ⬜, date-stamps, inline corrections, severity levels | Section 2, Design Principle 5 |
| 6 | Unnamed illustrations — semantic, not just named | Two-tier dedup: exact match + semantic best-effort for human review | Section 8 |
| 7 | Other-Sermons/ has 1800+ files, most are reference material | Scope boundaries for AUDIT: in-scope vs. out-of-scope directories | Section 5 |
| 8 | CONNECT could generate massive noise — 100+ doctrinal positions | Only suggest novel additions (new positions or new evidence) | Section 6 |
| 9 | GAP can't distinguish "not preached" from "not mapped" | Cross-reference map AND filesystem; separate true gaps from AUDIT findings | Section 7 |
| 10 | Map too large for single read (364KB / 1291 lines) | Section-based operations: Grep → Read with offset → Edit | Section 10 |
