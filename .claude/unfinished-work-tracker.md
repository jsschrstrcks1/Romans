# Unfinished Work Tracker — Romans Repository

*Compiled from review of all 21 distinct work threads (99 merged PRs across 21 branch families), the full sermon corpus, sermon-queue.md, memory2.md, preaching-gap-analysis.md, and individual file review.*

*Date: March 13, 2026*

---

## Summary

| Category | Count |
|----------|-------|
| Unprocessed sermons in memory2.md | 9 |
| Blocked sermons (source text missing) | 2 |
| Incomplete/truncated sermon manuscripts | 3 |
| Raw drafts needing polish and verification | 10 |
| Study papers incomplete | 2 |
| Book revision material not yet integrated | 1 |
| Sermon-map entries with verification flags (⚠️) | 46+ files |
| **Total distinct unfinished items** | **~73** |

---

## Part I: Work Thread Inventory

The repository has been developed across 21 distinct Claude Code thread families (identified by branch name pattern). Here is each thread family, its purpose, and whether work remains.

---

### Thread 1: `claude/add-sermon-repository` (branches: nJ8qS, v4xxd, X4iOX)
**Purpose**: Extract sermon manuscripts from archive .docx/.txt files, clean them, verify citations, and add as standalone .md files.
**PRs merged**: #50, #52, #53, #55, #60, #61, #62, #66, #68, #69, #71, #77, #82, #83, #86
**Status**: **Mostly complete** — over 100 sermons processed.
**Unfinished**:
- 9 sermons remain in `memory2.md` awaiting extraction (see Part II below)
- 2 sermons blocked for missing source text (Psalm 106, Exodus/Moses — see Part III)

---

### Thread 2: `claude/add-romans-sermon` (branch: Lu1XQ)
**Purpose**: Add and polish Romans series sermons.
**PRs merged**: #56, #59, #67, #73, #79
**Status**: **Substantially complete** — Romans 1–16 is fully preached and archived.
**Unfinished**:
- Romans 7 raw draft still has verification flags (⚠️ Jn 14:16 reference error, MacArthur quote unverified)
- Romans 1 - Psalm 22 raw draft has multiple unverified references (Adrian Rogers 108 OT refs, R.A. Torrey 300 OT refs)

---

### Thread 3: `claude/add-philippians-sermon` (branch: 2uEmD)
**Purpose**: Process and add Philippians series sermons.
**PRs merged**: #72, #75, #88
**Status**: **Complete** — Philippians 1, 3, 4 all processed.
**Unfinished**: None.

---

### Thread 4: `claude/add-sermon-nehemiah` (branch: hID0M)
**Purpose**: Process and add Nehemiah series sermons.
**PRs merged**: #76, #81
**Status**: **Complete** — 8+ Nehemiah sermons processed.
**Unfinished**: None.

---

### Thread 5: `claude/add-sermons-mapping` (branch: ShTCF)
**Purpose**: Build and populate sermon-map.md with comprehensive entries.
**PRs merged**: #36, #39, #40, #43, #47
**Status**: **Complete** — All 200+ sermons cataloged.
**Unfinished**:
- 46+ sermon-map entries still carry ⚠️ verification flags (see Part V)

---

### Thread 6: `claude/add-missing-sermons-maps` (branch: Zqd0d)
**Purpose**: Find sermons not yet in the map, add them, expand thin entries.
**PRs merged**: #85, #89, #90, #94
**Status**: **Complete** — all known files mapped.
**Unfinished**: None structurally, though some entries remain thin.

---

### Thread 7: `claude/plan-romans-sermon` (branch: RstXK)
**Purpose**: Plan and draft new Romans sermons (14–16).
**PRs merged**: #44, #45, #48, #80, #84
**Status**: **Complete for current needs** — Romans 14a–d, 15a–b, 16 all drafted.
**Unfinished**: None. Series is preached through.

---

### Thread 8: `claude/2cor-5-15-calvinism-rebuttal` (branch: mpzW1)
**Purpose**: Develop study notes rebutting the 2 Cor 5:15 objection to Definite Atonement.
**PRs merged**: #58, #65, #70
**Status**: **In progress** — study notes exist but are partial.
**Unfinished**:
- The rebuttal covers only the first argument fully. Additional arguments may be planned.

---

### Thread 9: `claude/explore-repository` (branch: xzLLO)
**Purpose**: Initial exploration and cataloging of the repository.
**PRs merged**: #54, #63
**Status**: **Complete** — exploratory work folded into other threads.
**Unfinished**: None.

---

### Thread 10: `claude/review-docs-explore-repo` (branch: tmCmE)
**Purpose**: Review documentation and explore repository structure.
**PRs merged**: #57
**Status**: **Complete**.
**Unfinished**: None.

---

### Thread 11: `claude/import-memory-skill` (branch: oflhJ)
**Purpose**: Import cognitive memory skill into the repository.
**PRs merged**: #49
**Status**: **Complete**.
**Unfinished**: None.

---

### Thread 12: `claude/import-docs-image-repo` (branch: JbkOt)
**Purpose**: Import documentation and images.
**PRs merged**: #46
**Status**: **Complete**.
**Unfinished**: None.

---

### Thread 13: `claude/review-onboarding-sermons` (branch: oPNQ7)
**Purpose**: Onboard and process initial sermon batches; build voice fingerprint.
**PRs merged**: #34, #35, #37, #38, #42, #64
**Status**: **Complete** — voice fingerprint extracted, initial sermons processed.
**Unfinished**: None.

---

### Thread 14: `claude/review-onboarding-docs`
**Purpose**: Review and understand repository documentation.
**Status**: **Complete**.
**Unfinished**: None.

---

### Thread 15: `claude/sermon-directory-docs`
**Purpose**: Documentation of sermon directory structure.
**Status**: **Complete**.
**Unfinished**: None.

---

### Thread 16: `claude/bible-study-journey-grace` (branch: SvTLL)
**Purpose**: Prepare Journey in Grace bible study materials.
**PRs merged**: #41
**Status**: **Complete** — study guide created.
**Unfinished**: None.

---

### Thread 17: `claude/prepare-bible-study` (branch: xGRxr)
**Purpose**: Prepare additional bible study materials.
**PRs merged**: #92
**Status**: **Complete** — men's bible study guide for chapters 18 and 20 created.
**Unfinished**: None.

---

### Thread 18: `claude/map-preaching-gaps` (branch: YhjkO)
**Purpose**: Comprehensive analysis of preaching gaps across the corpus.
**PRs merged**: #91, #93
**Status**: **Complete** — 11-part gap analysis produced.
**Unfinished**:
- The gap analysis identified 24 books of the Bible never preached from and 15 high-priority preaching gaps. These represent *future sermon planning work*, not unfinished documentation.

---

### Thread 19: `claude/pr51-conflict-resolution` (branch: mpzW1)
**Purpose**: Resolve merge conflicts from earlier PRs.
**PRs merged**: #74
**Status**: **Complete**.
**Unfinished**: None.

---

### Thread 20: `claude/church-hotel-policy`
**Purpose**: Church hotel assistance policy development.
**Status**: **Complete** — policy document exists at `Church Hotel Assistance Policy.md`.
**Unfinished**: None.

---

### Thread 21: `claude/review-docs-sermon-prep` (branches: wfipq, sPGup, uxX7M, EpR6A)
**Purpose**: Review documentation and prepare for sermon writing.
**PRs merged**: #95, #96, #98, #99
**Status**: **Most recent thread family** — general prep and review.
**Unfinished**: Active/ongoing as needed.

---

## Part II: Unprocessed Sermons in memory2.md

These 9 sermons remain as raw transcripts in `.claude/memory2.md` and have NOT been extracted to standalone files, cleaned, verified, or added to the sermon map:

| # | Sermon | Primary Text | Status |
|---|--------|-------------|--------|
| 1 | Paul's Final Letter | 2 Timothy 1:1-2 | ~~Extracted~~ → `2 Timothy 1 1-2 - Paul's Final Letter (raw draft).md` ✓ |
| 2 | Cultural Marxism / CRT | Romans 10:12-13 | Raw in memory2.md — needs extraction, cleanup, ESV conversion, verification |
| 3 | Bless the Lord / Thanksgiving & Hesed Love | Psalm 103 | Raw in memory2.md — needs extraction, cleanup, verification |
| 4 | The Covenants — God's Unfolding Plan | Ephesians 3:3-6 | Partially extracted (`00c1185`); verify if complete |
| 5 | Quilted Together in Love / Gratitude as Guardian | Colossians 2:1-8 | Raw in memory2.md — needs extraction, cleanup, verification |
| 6 | Prayer | Colossians 4:2-4 | Raw in memory2.md — needs extraction, cleanup, verification |
| 7 | Church Membership / Body of Christ | 1 Corinthians 12:12-27 | Raw in memory2.md — needs extraction, cleanup, verification |
| 8 | Sowing and Reaping | Galatians 6:7-10 | Raw in memory2.md — needs extraction, cleanup, verification |
| 9 | Angels, Demons, Etcetera | Ephesians 1:3-14 | Raw in memory2.md — needs extraction, cleanup, verification |

**Note**: Several of these (2 Tim 2:3-7, 2 Tim 3:14+, Titus 3:1-7, Gal 3:23+, 2 Tim 2:14-26, Matt 5:13-16) have been processed per sermon-queue.md — they exist in Other-Sermons but also remain as raw text in memory2.md. The 9 listed above are the ones still needing standalone file extraction.

---

## Part III: Blocked Sermons (Source Text Missing)

These 2 sermons were cataloged in previous processing but their source text cannot be found in the repository:

| Sermon | Text | Issue |
|--------|------|-------|
| **At the Altar of Our Convenience** | Psalm 106 | No .docx or .md source file in repo. Cataloged from an earlier info dump. Source text must be re-provided to process. |
| **A Godly Home** | Exodus / Moses | No .docx or .md source file in repo. Same situation. Source text must be re-provided. |

---

## Part IV: Incomplete and Raw Manuscripts

### Incomplete Manuscripts (truncated or unfinished)

| File | Issue |
|------|-------|
| `Sermon - Thankfulness.md` | Cuts off mid-narrative at "Things kept deteriorating." No resolution, no Scripture, no theological application. Remainder never submitted. |
| `Sermon - Sola Christus 2024.md` | Marked "INCOMPLETE DRAFT." Ends at "OK so the three roles of Christ are Prophet, Priest and King." Three roles never expounded. No gospel close. Scripture reference blank ("Our scripture will be ___"). |
| `Rapture - Study Paper (incomplete draft).md` | Introduction only. Cuts off at start of "The Relevant Scriptures" section. All Scripture analysis, position comparisons, and scholarly citations are yet to come. Pre-Wrath/Mid-Trib distinction needs clarification. |

### Raw Drafts Needing Polish and Verification

These files exist as raw drafts with known verification flags (⚠️). They are usable but need cleanup before preaching again or inclusion in a published book:

| File | Key Flags |
|------|-----------|
| `Proverbs 13 (raw draft).md` | Multiple verification flags on quotes and statistics |
| `Psalm 2 (raw draft).md` | 11 flags requiring verification: Heb 13:3 may be KJV not ESV; Edwards quote may have transcription error; "Lord" vs "LORD" in Psalm 2 quotes flagged; IDOP date and "53 countries" flagged as needing verification |
| `Psalm 8 - Hebrews 2 (raw draft).md` | 4 flags: needs ESV conversion, quote verification |
| `Psalm 119 161-168 (raw draft).md` | 10 flags: multiple quotes and cross-references unverified |
| `Psalm 68 Part 2 (raw draft).md` | 7 flags requiring verification: Prov 27:17 may be NIV not ESV; 1 Kgs 18 "Lord" vs "LORD" flagged; prophet count (~1,000 in draft vs. 850 in 1 Kings 18:19) flagged for verification |
| `1 Thess 5 - Rejoice Always (raw draft).md` | 7 flags requiring verification: Spurgeon quote source unverified; "3 million French" figure flagged as possibly overstated; "Communists defeated" claim flagged as needing historical verification |
| `Philippians 4 (raw draft).md` | 16 flags: extensive verification needed |
| `Romans 1 - Psalm 22 (Prophecy raw draft).md` | 8 flags requiring verification: Adrian Rogers "108 OT refs" claim flagged as unverified; R.A. Torrey "300 OT refs" claim flagged as unverified |
| `Romans 7.md` | 4 flags: Jn 14:16 reference error (should be 15:16); MacArthur quote unverified |
| `Romans 3 - antinomianism draft.md` | 3 flags |

---

## Part V: Sermon-Map Verification Flags

The sermon-map.md contains **46+ entries** with ⚠️ flags indicating unverified quotes, incorrect Scripture translations, factual claims needing checking, or attribution issues. These are documented inline in the sermon-map entries. A full audit would require reading each flagged sermon and resolving the flags.

**Files with the most verification flags**:
- `Philippians 4 (raw draft).md` — 16 flags
- `Psalm 2 (raw draft).md` — 11 flags
- `Psalm 119 161-168 (raw draft).md` — 10 flags
- `Study - Joseph as a Type of Christ (typology reference).md` — 10 flags
- `Romans 1 - Psalm 22 (Prophecy raw draft).md` — 8 flags
- `1 Thess 5 - Rejoice Always (raw draft).md` — 7 flags
- `Psalm 68 Part 2 (raw draft).md` — 7 flags
- `Sermon - Faithful and God-Fearing.md` — 7 flags
- `Sola Scriptura 2021.md` — 7 flags

---

## Part VI: Book Project — "The Night Is Far Gone"

The book framework is well-documented in `claude.md` with a complete chapter mapping. Unfinished book-specific work:

| Item | Status |
|------|--------|
| `Notes - Empire and Suppression (Romans 1 Book Revision).md` | Raw material for book revision of Romans 1 ("The Darkness We Chose"). Not yet integrated into the sermon/chapter. |
| Book title decision | Three options proposed; no final selection: *The Night Is Far Gone*, *Waking Up*, *From Midnight to Morning* |
| Chapter polishing for print | Sermons exist for all 16 chapters but none have been revised from "preached" format to "read" format for book publication |
| Transitions between chapters | No inter-chapter connective tissue has been written |

---

## Part VII: Study Notes and Reference Materials — Open Items

| Item | File | Status |
|------|------|--------|
| 2 Cor 5:15 Calvinism Rebuttal | `Notes - 2 Corinthians 5-15 Rebuttal (Calvinism Objection).md` | First argument developed. Additional arguments may be planned but are not written. |
| Romans 6b boulder rewrite | `Romans_6b_boulder_rewrite.md` | Short outline only (~10 lines). Companion file `Romans_6b_with_boulder.md` is more developed. Unclear if the rewrite was completed or abandoned. |
| Evangelism content survey | `evangelism-content-survey.md` | Complete as a survey document. Its purpose was to inform Romans 15b sermon prep, which is now done. No further action needed. |
| Missional Helix notes | `Notes - Missional Helix (Church Planting Strategy).md` | Strategy notes; standalone reference. No action needed unless church planting work resumes. |
| Missions bibliography | `Notes - Missions Bibliography (25 Books for Local Church).md` | Contains 5 verification flags on book descriptions. |
| Theological extraction | `theological-extraction-ecclesiology-eschatology-bibliology.md` | Comprehensive doctrinal extraction. Complete. |

---

## Part VIII: Preaching Gap Analysis — Highest Priority Future Work

From `preaching-gap-analysis.md`, the top 15 preaching gaps ranked by theological weight and pastoral relevance:

| # | Book/Passage | Why |
|---|-------------|-----|
| 1 | Jeremiah 31:31–34 | New Covenant — foundational to Romans 6–8; never preached directly |
| 2 | 1 Corinthians 15 | Bodily resurrection — most sustained NT treatment; never primary text |
| 3 | Revelation 4–5, 21–22 | Heavenly worship + new creation hope |
| 4 | Ruth | Kinsman-redeemer typology — completely absent |
| 5 | Daniel 1–6 | Faithfulness under empire — complements Romans 13 |
| 6 | Ephesians 1, 3, 6 | Election doxology, fullness of God, armor of God |
| 7 | Hebrews 9–10 | Old covenant → new covenant typological architecture |
| 8 | Esther | Providence without God's name; courage under pagan king |
| 9 | Isaiah 40, 55 | Comfort and evangelistic invitation |
| 10 | Eph 5:22–33 + Gen 2 + Song of Solomon | Biblical theology of marriage |
| 11 | Lamentations 3 + Job 38–42 | Theology of lament |
| 12 | Acts 17 (Mars Hill) | Apologetics in pagan context |
| 13 | Habakkuk | "The righteous shall live by faith" — never preached from its source |
| 14 | 2 Samuel 7 | Davidic covenant — missing link in covenantal chain |
| 15 | Galatians 5 (Fruit of the Spirit) | Referenced constantly; never primary preaching text |

**24 books of the Bible** have never been the primary preaching text (19 OT, 5 NT).

---

## Part IX: Action Items — Quick Wins

These items could be resolved in a single session each:

1. **Extract remaining memory2.md sermons** — 9 sermons need standalone file extraction, cleanup, and mapping
2. **Resolve Sola Christus 2024 incomplete draft** — needs Scripture reference and three-role exposition completed (or marked as permanently incomplete if the 2020 version is the authoritative one)
3. **Resolve Thankfulness sermon** — request remainder of transcript from pastor
4. **Fix Romans 7 reference error** — Jn 14:16 should be 15:16
5. ~~**Convert NIV/KJV quotes to ESV** in raw drafts (Psalm 2, Psalm 68 Part 2, 1 Thess 5)~~ ✓ Completed

---

## Part X: Thread Status Summary

| Thread Family | PRs | Status |
|---------------|-----|--------|
| add-sermon-repository | 15 | Active — 9 sermons remain in memory2.md |
| add-romans-sermon | 5 | Complete — verification flags remain on 2 raw drafts |
| add-philippians-sermon | 3 | Complete |
| add-sermon-nehemiah | 2 | Complete |
| add-sermons-mapping | 5 | Complete — 46+ entries have verification flags |
| add-missing-sermons-maps | 4 | Complete |
| plan-romans-sermon | 5 | Complete |
| 2cor-5-15-calvinism-rebuttal | 3 | Partial — first argument only |
| explore-repository | 2 | Complete |
| review-docs-explore-repo | 1 | Complete |
| import-memory-skill | 1 | Complete |
| import-docs-image-repo | 1 | Complete |
| review-onboarding-sermons | 6 | Complete |
| review-onboarding-docs | — | Complete |
| sermon-directory-docs | — | Complete |
| bible-study-journey-grace | 1 | Complete |
| prepare-bible-study | 1 | Complete |
| map-preaching-gaps | 2 | Complete |
| pr51-conflict-resolution | 1 | Complete |
| church-hotel-policy | — | Complete |
| review-docs-sermon-prep | 4 | Ongoing |
| **TOTAL** | **~99** | **4 threads with remaining work** |
