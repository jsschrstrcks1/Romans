# Unfinished Work Tracker — Romans Repository

*Compiled from review of all 21 distinct work threads (99 merged PRs across 21 branch families), the full sermon corpus, sermon-queue.md, memory2.md, preaching-gap-analysis.md, and individual file review.*

*Date: March 13, 2026 — Last updated: March 16, 2026*

**March 16 session notes**: Resolved merge from origin/main (10 files). All 10 new files verified and mapped in sermon-map. Two new files with standing pastoral flags documented below (Deuteronomy 8, Psalm 42 — Part IV). Tracker summary counts corrected accordingly. memory2.md extractions confirmed complete. 1 Corinthians 12 polished file reviewed — clean.

---

## Summary

| Category | Count |
|----------|-------|
| Unprocessed sermons in memory2.md | ~~9~~ **0 — all complete** |
| Blocked sermons (source text missing) | 1 (Psalm 106; A Godly Home resolved) |
| Incomplete/truncated sermon manuscripts | 3 |
| Raw drafts needing polish and verification | 12 (10 prior + 2 added from March 16 merge) |
| Study papers incomplete | 2 |
| Book revision material not yet integrated | 1 |
| Sermon-map entries with verification flags (⚠️) | 46+ files |
| **Total distinct unfinished items** | **~67** |

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
- Romans 7 raw draft: Jn 15:16 corrected ✓; Lk 22:42 corrected ✓; MacArthur reworded to paraphrase ✓; standing items minor (see Part IV)
- Romans 1 - Psalm 22 raw draft: Rogers/Torrey refs substantially resolved March 2026; Psalm 22:17 cross-reference table needs one correction before printing

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

*(Updated March 2026 — all 9 extractions now complete; file paths verified against file system)*

| # | Sermon | Primary Text | Status |
|---|--------|-------------|--------|
| 1 | Paul's Final Letter | 2 Timothy 1:1-2 | ~~Extracted~~ → `2 Timothy 1 1-2 - Paul's Final Letter (raw draft).md` ✓ |
| 2 | Cultural Marxism / CRT | Romans 10:12-13 | ~~Raw in memory2.md~~ → `Other-Sermons/Sermons/Cultural Marxism.md` → `Cultural Marxism - CRT - Romans 10 (raw draft).md` → **`Sermon - Cultural Marxism.md` ✓ polished & verified** (all Scripture ESV ✓; David Brooks sourced ✓; Hitler "half Jewish" removed ✓; Deut 10:17 corrected to ESV ✓; Dhund geography corrected ✓; sermon-map + theological-map updated ✓) |
| 3 | Bless the Lord / Thanksgiving & Hesed Love | Psalm 103 | ~~Raw in memory2.md~~ → `Psalm 103 - Bless the Lord - Hesed Love (raw draft).md` ✓ — Scripture refs corrected March 2026; ⚠️ JFB quote unverified |
| 4 | The Covenants — God's Unfolding Plan | Ephesians 3:3-6 | ~~Partially extracted~~ → `Other-Sermons/Sermons/Eph 3 - The Covenants.md` ✓ (complete Integrity Log present, 6 Scripture corrections + 3 factual notes applied) |
| 5 | Quilted Together in Love / Gratitude as Guardian | Colossians 2:1-8 | ~~Raw in memory2.md~~ → `Other-Sermons/Sermons/Col 2 - thanksigiving.md` ✓ |
| 6 | Prayer | Colossians 4:2-4 | ~~Raw in memory2.md~~ → `Other-Sermons/Sermons/col 4 - prayer.md` (full version) + `Other-Sermons/Sermons/prayer col 4.md` (prayer service version) ✓ |
| 7 | Church Membership / Body of Christ | 1 Corinthians 12:12-27 | ~~Raw in memory2.md~~ → `Other-Sermons/Sermons/Commitment to the church body 1 cor 12.md` ✓ |
| 8 | Sowing and Reaping | Galatians 6:7-10 | ~~Raw in memory2.md~~ → `Galatians 6 - Sowing and Reaping (raw draft).md` ✓ — Flood story corrected March 2026; Toplady ✓, Spurgeon ✓, Luther ✓ verified March 2026; Lawson wording confirmed, no primary source located; Sindhi Samas verified (Joshua Project — ~1.63M, Frontier/Unengaged); Titanic illustration researched — current version embellished/unattributed (real Peuchen kernel exists but woman/casino details are not historical) |
| 9 | Angels, Demons, Etcetera | Ephesians 1:3-14 | ~~Raw in memory2.md~~ → ✓ `Other-Sermons/Sermons/Eph 1 - Angels Demons Etcetera.md` is authoritative (all corrections applied, Integrity Log, Series label added). `Ephesians 1 - Angels Demons Etcetera.md` deprecated with header pointing to authoritative version. |

**All memory2.md extractions are complete.** All 9 files confirmed present on disk (March 2026). The extracted files are raw drafts — quote attribution, Scripture translation accuracy, and factual claims have not yet been verified in these files. That verification work remains for a future session.

---

## Part III: Blocked Sermons (Source Text Missing)

These sermons were cataloged in previous processing but their source text cannot be found in the repository:

| Sermon | Text | Issue |
|--------|------|-------|
| **At the Altar of Our Convenience** | Psalm 106 | No .docx or .md source file in repo. Cataloged from an earlier info dump. Source text must be re-provided to process. |
| ~~**A Godly Home**~~ | ~~Exodus / Moses~~ | ~~No .docx or .md source file in repo.~~ **RESOLVED** — Source text provided March 2026. Polished and verified manuscript saved to `Other-Sermons/Sermons/Sermon - A Godly Home.md`. Sermon-map updated (Exodus section + Marriage/Family index). Key corrections: Hiroo Onoda timeline (1974, ~29 years, age 52); ESV Scripture quotations; Patrick Henry/Rogers/Swindoll quotes verified. Two remaining ⚠️ flags: "three abortions/year" contraceptive claim (contested); silphium extinction date approximate. |

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
| `Proverbs 13 (raw draft).md` | ~~Multiple flags~~ — **All resolved** ✓. Paul Washer story verified ✓; "700%" removed → "small fraction" ✓; Edwin Starr / Lockheed Martin story CUT (confirmed false) ✓; screen time corrected to 5–9 hrs (Common Sense Media) ✓; "3 hrs Puritan scripture" reframed ✓; Newton ref corrected ✓; "spare the rod" paraphrase flagged in body with real ESV verse ✓. ⬜ Pew Bible page number — fill before Sunday (pastor's task) |
| `Psalm 2 (raw draft).md` | ~~11 flags~~ — **All resolved** ✓ (Heb 13:3 ESV, Edwards Q2 fixed, LORD/Lord corrected incl. v.4 Adonai, IDOP first Sunday, 7 duplicate lines removed); ⚠️ "53 countries" and "Russia in Revelation" remain as noted interpretive/dated-data flags |
| `Psalm 8 - Hebrews 2 (raw draft).md` | ~~4 flags~~ — **Duplicates resolved** ✓ (4 partial lines removed); ESV corrections applied ✓; J.C. Ryle verified ✓; "How He Loves" / McMillan corrected ✓; Caño Cristales corrected ✓. ⚠️ David Platt cab driver story unverified (no indexed source); ⚠️ Edwards "just the sin" quote not in Yale critical edition (possibly misattributed); ⚠️ MacArthur "serve righteousness as slaves" — paraphrase of Rom 6:18-19, not confirmed direct quote — all three flagged inline in draft |
| `Psalm 119 161-168 (raw draft).md` | ~~10 flags~~ — **8 resolved** ✓ (Fenn corrections, US population, Brother Andrew prayer/Romania verified); ⚠️ Florida "more than rest of country combined" (opiates/Xanax) — directionally accurate for pill-mill era, exact phrase unverified; update with sourced stats before reprising |
| `Psalm 68 Part 2 (raw draft).md` | ~~7 flags~~ — **All resolved** ✓ (Prov 27:17 ESV, 1 Kgs 18 LORD, prophet count 850, Elijah timeline, duplicate line removed) |
| `1 Thess 5 - Rejoice Always (raw draft).md` | ~~7 flags~~ — **All resolved** ✓ (Spurgeon verified Sermon #2483, "3 million" → ~1.3M, "Communists defeated" corrected, duplicate line removed) |
| `Philippians 4 (raw draft).md` | ~~16 flags~~ — **11 resolved** ✓ (CT Studd wording corrected, Spurgeon verified #1178, semnos confirmed, prosphilēs NT hapax confirmed, LXX Ps 84 claim corrected to ἀγαπητά, Samuel Sey description corrected). ⚠️ Samuel Sey quote unverified; ⚠️ Richard Baxter full passage unverified (closing sentence confirmed — Practical Works II:884-885); ⚠️ Mo-Jer-Hai not in indexed sources; ⬜ pew Bible page number |
| `Romans 1 - Psalm 22 (Prophecy raw draft).md` | ~~8 flags~~ — **All resolved** ✓ (Rogers "108" verified Sermon #2299 LWF; Torrey "300" corrected — actual lists 61-79; "68%" corrected to 65% with Joyner/Morningstar attribution; prophecy table Ps 22:17 → Ps 34:20 for bones-not-broken; Deut 18:20-22 and Rom 10:9 ESV previously corrected). ⚠️ Remaining Psalm 22 fulfillment citations: verify line-by-line against ESV before printing. |
| `Romans 7.md` | ~~4 flags~~ — **2 resolved** ✓ (Jn 15:16 corrected, Phil 2:8 ESV, Lk 22:42 restored); ⚠️ Tesla story disputed; ⚠️ "3 in 5 dieters" unverified |
| `Romans 3 - antinomianism draft.md` | ~~3 flags~~ — **2 resolved** ✓; ⚠️ John Brown quote remains in Pending Verification (archive.org 403, no indexed text — cannot verify without physical copy) |
| `Deuteronomy 8 - Count Your Blessings (repaired draft).md` | **Added March 16, 2026 — from main merge.** Three pastoral flags documented inline in source notes: (1) Oatman/Johnson "Count Your Blessings" hymn story — notes describe it as invented/embellished; verify or remove before reprising. (2) Jonathan Edwards "sinners in hands" quote — sermon attributes it to Edwards but wording does not match known primary text; treat as paraphrase or remove attribution. (3) Col 3:6 cited as support for "God's wrath falls on the disobedient" in a blessings-and-thanksgiving context — application is strained; consider removing or reframing. Sermon is usable; flags matter before reprising or print. |
| `Psalm 42 - As the Deer Pants.md` | **Added March 16, 2026 — from main merge.** Two flags in source notes: (1) Unnamed "PhD scholar" cited for the claim that deer seek water to escape predators (not to drink) — no source named; claim appears in circulation but academic origin unverified. (2) Sermon attributes the "As the Deer" chorus tune to a specific composition context — verify before any print attribution. Sermon is fully usable for preaching; flags matter for print/book use only. |

---

## Part V: Sermon-Map Verification Flags

The sermon-map.md contains **46+ entries** with ⚠️ flags indicating unverified quotes, incorrect Scripture translations, factual claims needing checking, or attribution issues. These are documented inline in the sermon-map entries. A full audit would require reading each flagged sermon and resolving the flags.

**Files with the most verification flags**:
- `Philippians 4 (raw draft).md` — 16 flags
- `Psalm 2 (raw draft).md` — 11 flags
- `Psalm 119 161-168 (raw draft).md` — 10 flags
- `Study - Joseph as a Type of Christ (typology reference).md` — partially resolved March 2026: Gen. 37:28 ESV ✓; Heb. 7:26 ESV ✓; Phil. 2:9 "new name" heading flagged as inaccurate (use Rev. 3:12 or revise heading). Standing: all quotes are KJV — convert to ESV before preaching; source/attribution unknown
- `Romans 1 - Psalm 22 (Prophecy raw draft).md` — substantially resolved March 2026; standing: Psalm 22:17/"bones not broken" cross-reference needs table correction; "68%" stat uncitable; voting intro dated
- `1 Thess 5 - Rejoice Always (raw draft).md` — 7 flags
- `Psalm 68 Part 2 (raw draft).md` — substantially resolved March 2026; 1 standing item (Elijah timeline phrasing) for print polish
- `Sermon - Faithful and God-Fearing.md` — manuscript substantially polished; major errors corrected in end notes (king succession, Xerxes-Cyrus, 50→52 days, NIV→ESV for Isa 45/Luke 12:5); standing items: (1) Gospel presentation not developed — must complete before preaching; (2) Pascal's Wager section not developed; (3) Dr. Alvin Reid quote — exact source unverified; (4) Great Wall bribery number — unverifiable, already qualified in body
- `Sermon - Sola Scriptura 2021.md` — manuscript substantially polished; standing items: (1) Trevor Noah attribution almost certainly wrong — must identify correct source before preaching (quote is evangelical theological commentary, not consistent with Trevor Noah); (2) 4 Luther quotes content-consistent but no primary LW source confirmed; Quote 2 ("Nothing helps more powerfully") traced to secondary source (Counseling Under the Cross); all other errors corrected in body/source notes (DSS "1,000 years" ✓, flat earth removed ✓, Isaiah 40:22 qualified ✓)

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
| 14 | 2 Samuel 7 | Davidic covenant — surveyed in `Eph 3 - The Covenants.md` but no dedicated expository sermon; covenant-as-primary-text gap remains |
| 15 | Galatians 5 (Fruit of the Spirit) | Referenced constantly; never primary preaching text |

**24 books of the Bible** have never been the primary preaching text (19 OT, 5 NT).

---

## Part IX: Action Items — Quick Wins

These items could be resolved in a single session each:

1. **Extract remaining memory2.md sermons** — 9 sermons need standalone file extraction, cleanup, and mapping
2. **Resolve Sola Christus 2024 incomplete draft** — needs Scripture reference and three-role exposition completed (or marked as permanently incomplete if the 2020 version is the authoritative one)
3. **Resolve Thankfulness sermon** — request remainder of transcript from pastor
4. ~~**Fix Romans 7 reference error** — Jn 14:16 should be 15:16~~ ✓ Completed March 2026; Lk 22:42 also corrected to exact ESV
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
