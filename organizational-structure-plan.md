# Romans Repository — Organizational Plan

*Updated March 24, 2026 — rewritten around how a pastor uses this data.*

---

## What This Repository Is For

You come here to do five things:

1. **Write a sermon** — from blank page to manuscript
2. **Find something you've already preached** — by passage, date, topic, or series
3. **Pull supporting material** — theologian quotes, cross-references, illustrations
4. **Prepare a non-sermon service** — funeral, wedding, prayer service, special event
5. **Study** — theology papers, seminary reference, Bible study notes

Everything in this plan serves those five activities. If a change doesn't make one of them easier, we don't make it.

---

## How You Find Things Today

| I want to... | How it works now | What's broken |
|---|---|---|
| Find a sermon by passage | Search sermon-map.md or grep the root | Works — but 464 files in root makes browsing impossible |
| Find a sermon by date | Search date-map.md | Works |
| See what I've preached from a book | Check sermon-map.md under that book | Works |
| Find a quote from Sproul | Browse `quotes-and-references/sproul/` | Works well — already organized |
| Find a funeral service | Grep root for "funeral" | Buried among 464 other files |
| Find a raw draft | Grep for "(raw draft)" | Scattered across root and Other-Sermons/ |
| Find seminary work | Check sebts-reference/ ... which one? | Two copies in two places, different contents |
| Check if I've used an illustration | Search sermon-map.md subject column | Works, but only if the map entry captured it |

**The maps are doing the heavy lifting.** The folder structure isn't helping — it's just a pile. The goal is to make the folders match the way you already think about the content.

---

## Proposed Structure

```
Romans/
│
├── sermons/
│   ├── ot/                        # Old Testament sermons, by book
│   │   ├── genesis/
│   │   ├── psalms/
│   │   ├── isaiah/
│   │   └── ...
│   ├── nt/                        # New Testament sermons, by book
│   │   ├── romans/                # "Night Is Far Gone" series lives here
│   │   ├── john/
│   │   ├── 1-peter/
│   │   └── ...
│   └── topical/                   # Not passage-primary (titled sermons, series)
│       ├── Sermon - The Watching World.md
│       ├── Sermon - Legacies.md
│       └── ...
│
├── services/                      # Non-Sunday-morning occasions
│   ├── funerals/
│   ├── weddings/
│   ├── prayer-services/
│   └── special-events/
│
├── teaching/                      # Non-sermon instruction
│   ├── sunday-school/
│   ├── bible-studies/
│   └── notes/
│
├── theology/                      # Doctrinal papers and studies
│
├── pastoral-resources/            # Church admin, policy, community resources
│
├── sebts-reference/               # Seminary work (consolidated from both copies)
│
├── quotes-and-references/         # Already organized — don't touch
│
├── personal/                      # Pandemic journal, personal reflections
│
├── A journey in grace/            # Book study photos — don't touch
│
└── .claude/                       # Maps and skills — auto-regenerated
```

### Why per-book folders under sermons/?

Romans isn't a special case — it's just another book. `sermons/nt/romans/` sits alongside `sermons/nt/john/` and `sermons/ot/psalms/`. No special decisions needed. When you want to see everything you've preached from Psalms, you open one folder.

### Where do drafts go?

**Next to their finals.** A raw draft of Romans 5 lives in `sermons/nt/romans/` alongside the polished version. The `(raw draft)` or `(raw transcript)` tag in the filename already distinguishes it. Separating drafts into their own tree orphans them from the sermons they belong to.

### What about Other-Sermons/?

Sort its contents into the new structure, then delete it. It was a staging area, not a category.

---

## Decisions (Resolved)

Based on GPT and Gemini consultation feedback:

| Decision | Answer | Rationale |
|---|---|---|
| Romans placement | `sermons/nt/romans/` | Per-book folders make it consistent, not special |
| OT/NT split | Yes — `sermons/ot/` and `sermons/nt/` with book subfolders | You think in books. Folders should match that |
| Draft handling | Keep next to finals | Drafts are versions of a sermon, not a separate category |
| Other-Sermons/ | Sort and delete | It's a junk drawer, not a category |
| Naming convention | Normalize gradually | New files follow `[Book] [Chapter] - [Title].md`. Old files keep their names |
| Move files or just plan? | Move — but in phases, with commits between each | Use `.git-blame-ignore-revs` to preserve blame history |

---

## Execution Plan

Each phase is one sitting. Commit after each. Stop anywhere — later phases don't depend on earlier ones being perfect.

### Phase 0: Safety Net
- [ ] Create `.git-blame-ignore-revs` file (Claude handles this)
- [ ] Verify all maps are current before we start

### Phase 1: Clean the Junk Drawer
*~15 minutes. Low risk.*
- [ ] Merge both `sebts-reference/` directories into one at root
- [ ] Delete empty `Other-Sermons/pastoral-resources/`
- [ ] Move `Other-Sermons/_review/` contents to `_review/` at root
- [ ] Sort the 26 files in `Other-Sermons/Sermons/` — each one goes to its proper book folder or gets flagged for your review
- [ ] Delete `Other-Sermons/` once empty
- [ ] **Commit:** "Consolidate duplicates and clear Other-Sermons/"

### Phase 2: Move Non-Sermon Files Out of Root
*~20 minutes. Smallest set of files.*
- [ ] Identify and move funeral/wedding/service files → `services/`
- [ ] Identify and move Sunday school and Bible study files → `teaching/`
- [ ] Identify and move theology papers → `theology/`
- [ ] Identify and move personal files (pandemic journal, reflections) → `personal/`
- [ ] **Commit:** "Move non-sermon files to proper directories"

### Phase 3: Create Book Folders and Move Sermons
*~45 minutes. The big move.*
- [ ] Create `sermons/ot/` and `sermons/nt/` with book subfolders
- [ ] Move OT sermons to `sermons/ot/[book]/`
- [ ] Move NT sermons (non-Romans) to `sermons/nt/[book]/`
- [ ] Move topical sermons to `sermons/topical/`
- [ ] **Commit:** "Move OT and NT sermons to book folders"

### Phase 4: Move Romans
*~15 minutes. Most important, most referenced.*
- [ ] Move all Romans series files to `sermons/nt/romans/`
- [ ] Spot-check that every Romans file in the sermon-map has a match in the new location
- [ ] **Commit:** "Move Romans series to sermons/nt/romans/"

### Phase 5: Regenerate and Verify
- [ ] Run sermon-map skill to rebuild all four maps with new paths
- [ ] Spot-check 10 random sermons: can you find them by browsing?
- [ ] Spot-check 5 map entries: do the paths resolve?
- [ ] Add move commits to `.git-blame-ignore-revs`
- [ ] **Commit:** "Regenerate maps and finalize reorganization"

---

## What Claude Does vs. What You Do

| Task | Who |
|---|---|
| Create directories | Claude |
| Move files | Claude |
| Decide ambiguous cases ("is this a sermon or a study?") | You |
| Regenerate maps | Claude (sermon-map skill) |
| Spot-check results | You |
| Commit and push | Claude (after your approval) |

The only thing that requires your judgment is the ~20-30 files where the category isn't obvious. Claude will flag those and ask.

---

## What NOT to Change

- **`quotes-and-references/`** — Already well-organized. Leave it.
- **`.claude/` maps** — They regenerate automatically after moves.
- **`A journey in grace/`** — Book study photos. No change needed.
- **File contents** — This plan moves files. It does not edit sermon text.
- **Filenames of existing sermons** — Normalize gradually. Don't bulk-rename.

---

## After Reorganization: Your Workflow

| I want to... | What I do |
|---|---|
| Write a new Romans sermon | Create file in `sermons/nt/romans/`, use `/orchestrate sermon` |
| Find what I preached on Psalm 23 | Open `sermons/ot/psalms/` or check sermon-map |
| Pull a Sproul quote on justification | Search `quotes-and-references/sproul/` |
| Prepare a funeral | Check `services/funerals/` for past services |
| See preaching gaps | Run sermon-map GAP analysis |
| Check if I've used an illustration | Search sermon-map subject column or run DEDUP |
| Reference seminary Greek work | Browse `sebts-reference/` |
| Find what I preached last Easter | Check date-map.md |

*Soli Deo Gloria.*
