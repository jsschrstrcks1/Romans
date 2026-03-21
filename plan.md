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
- Generate a map entry in the format matching the existing sermon-map.md structure
- Place it in the correct Bible book section
- Check for duplicate entries (same passage, same title)
- Check for duplicate illustrations against the full map (prevent reuse)

### 2. UPDATE — Refresh an existing map entry

When a sermon file is modified (flags resolved, ESV corrections applied, content revised):
- Find the existing map entry
- Identify what changed: new flags resolved? new content added? verification status changed?
- Update the entry to reflect current state
- Preserve the existing entry structure (don't rewrite from scratch — update surgically)
- Log what changed in the entry (e.g., "⚠️ flag resolved March 2026" notation pattern already used)

### 3. AUDIT — Check map integrity

On demand (keyword trigger: "audit map", "check map", "map integrity"):
- Scan all sermon files in the repository
- Compare against sermon-map.md entries
- Report: files with no map entry, map entries pointing to missing files, entries with outdated flags, entries missing verification status
- Check for orphaned files (sermon files not in the map)
- Check for phantom entries (map entries with no corresponding file)

### 4. CONNECT — Cross-reference between maps

When a sermon touches a doctrine tracked in the theological map:
- Check if the theological-map.md has a relevant entry
- Suggest additions to the theological map where the sermon affirms or denies a doctrine not yet recorded
- Update the series trajectory if the sermon advances the Romans arc
- Cross-reference against reference maps (MacArthur/Sproul/Spurgeon) for quote verification opportunities

### 5. GAP — Identify preaching gaps

On demand (keyword trigger: "gap analysis", "what haven't we preached", "preaching gaps"):
- Survey the sermon map by Bible book
- Report: Romans passages not yet covered, OT books with no sermons, NT books with thin coverage
- Cross-reference against the book framework in claude.md (Part I-V chapter mapping) to identify missing chapters
- Check for passages in the romans-14-16-plan.md that haven't been written yet

### 6. DEDUP — Illustration deduplication

When writing a new sermon or before committing:
- Scan the proposed sermon for illustrations
- Search the full sermon map for illustrations already used
- Flag reuse: "This illustration (Bannockburn, Hiroo Onoda, buckwheat milling, etc.) was used in [sermon]. Consider a fresh illustration."
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

### Section 2: Map Entry Format
- Document the exact format used in sermon-map.md (pipe-delimited table rows)
- Three table formats:
  - **Romans series**: `| Passage | Title | File | Summary |` (the richest entries with detailed summaries, flags, cross-references)
  - **Non-Romans by book**: `| Passage | Subject | File | Type |` with detailed notes in Subject column
  - **Thematic index**: `| File | Passage | Description |` grouped by topic (Evangelism, Faith, Five Solas, etc.)
- Flag notation: ⚠️ (needs verification), ❌ (error found), ✅/✓ (verified)
- Verification status markers
- People group format
- Illustration tracking within entries

### Section 3: INDEX Operation
- Step-by-step for adding a new sermon
- Required fields
- How to generate the summary (dense, pipe-delimited, flag-aware)
- Placement rules (which Bible book section, sort order)
- Dedup check before adding

### Section 4: UPDATE Operation
- How to find the existing entry (by filename, by passage)
- Surgical update rules (don't rewrite — modify)
- What triggers an update: flag resolution, ESV correction, content revision, score assignment
- Date-stamping updates (e.g., "*(March 2026)*")

### Section 5: AUDIT Operation
- Full integrity scan procedure
- Report format
- Orphan detection (files without map entries)
- Phantom detection (entries without files)
- Flag staleness check (unresolved flags older than 90 days)

### Section 6: CONNECT Operation
- Cross-referencing between sermon-map.md and theological-map.md
- When to suggest theological map additions
- Series trajectory updates
- Reference map cross-referencing

### Section 7: GAP Operation
- Gap analysis procedure
- Coverage report format
- Book framework alignment check
- Romans plan alignment check

### Section 8: DEDUP Operation
- Illustration extraction heuristics
- Search patterns in the sermon map
- Named illustrations to track (list the recurring ones: Bannockburn, Hiroo Onoda, buckwheat milling, Treblinka, Augustine conversion, thief on cross, etc.)
- Report format for duplicates

### Section 9: Integration with Hooks
- PostToolUse hook for Write: when a sermon file is written, suggest running INDEX or UPDATE
- Non-blocking — suggestion only
- Memory encoding after map updates

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

3. **One map entry per sermon file.** Multiple files for the same sermon (raw, flagged, repaired) each get their own entry — the map tracks the state of each file, not just the passage.

4. **Preserve the existing format.** The sermon map has 1291 lines of carefully maintained entries. The skill works *within* that format, not against it. No schema changes. No restructuring.

5. **Flag-aware.** The ⚠️/❌/✅ flag system is the single most valuable feature of the map. The skill must understand, preserve, and update flags correctly.

6. **Soli Deo Gloria.** The map serves the preaching. The preaching serves the congregation. The congregation serves God. Every entry matters because every sermon carries the weight of "Thus says the Lord."
