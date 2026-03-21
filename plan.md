# Sermon Evaluation Skill — Implementation Plan

## Overview

A new skill called `sermon-evaluation` that evaluates sermon manuscripts against a weighted rubric rooted in Reformed Baptist convictions. Invoked manually (not auto-firing). Produces a scored evaluation with diagnostic narrative, strengths, weaknesses, blind spots, and surgical fixes.

This is the fifth skill in the Romans project ecosystem.

---

## Thesis

> A good sermon is a text-governed proclamation of God's Word that faithfully explains the passage, clearly presents Christ and the gospel, searches the conscience, gives specific application, exhorts a real response, and equips the church for holiness and witness.

The sermon must be judged first by faithfulness to the text, then by gospel clarity, then by how deeply it presses the hearer toward repentance, faith, and obedience.

---

## Design Decisions: Four Rounds of Refinement

### Round 1 — The Original Rubric (User)

The foundation is sound: exposition, theology, Christ-centeredness, applicatory pungency, structure, illustration, delivery. The instincts are Puritan and pastoral. The categories are right. What it needed was weighting, failure detection, and a mechanism that doesn't just grade but *diagnoses*.

### Round 2 — ChatGPT Framework (RB-SES)

**Wheat kept:**
- **The non-negotiable gate** ("Berean Gate"): If the sermon is not text-driven, it fails. Full stop. This guards against everything downstream. Don't soften it.
- **Weighted scoring (100-point scale)**: Good structure. Exposition + Gospel carrying ~40% of total weight is exactly right.
- **Diagnostic questions per category**: These are the real evaluation engine. Numbers without diagnostic questions produce polite feedback. Diagnostic questions produce conviction.
- **The output format**: Score breakdown, top 3 strengths, top 3 weaknesses, blind spots, surgical fixes. Clean, actionable.
- **"Weight of Glory" bonus metric**: Captures what numbers can't — does this sermon carry eternal gravity?
- **Spiritual differentiation in application**: Distinguishing the weary saint, the self-righteous, and the unbeliever. This is Puritan pastoral theology (William Perkins, Thomas Watson) and it belongs here.

**Chaff discarded:**
- **Delivery & Authenticity (5 pts for voice/manner)**: We evaluate *manuscripts*, not live preaching. "Easy to listen to" and "distracting mannerisms" don't apply to text. Replaced with **Sermonic Force** — does it read like preaching or an essay?
- **Emoji, versioning ("v1.0"), consultantish tone**: The existing skills have gravity. This one will too.
- **Spreadsheet/form suggestions**: This is a Claude Code skill, not a Google Form.

### Round 3 — Gemini/ChatGPT Critique

**Wheat kept:**
- **Fatal Flaw Flags (score cap system)**: If any of 4 non-negotiables are present, the score is capped at 69 regardless of other strengths. This prevents polished but hollow sermons from scoring well. Excellent innovation. Adopted.
- **Cognitive Load Index**: A sermon can be theologically rich, textually faithful, and pastorally overwhelming. The congregation must be able to track it. Added as a modifier (-3 to 0).
- **"Illusion of Strength" and "Missed Opportunity" in output**: Where the sermon *felt* strong but wasn't, and where the text offered depth the preacher ignored. Sharp additions to the surgical report.
- **Moralism Alarm expansion**: Three questions instead of one — "Could this sermon comfort a moral atheist?" / "Is obedience presented without new birth?" / "Is Christ necessary or just helpful?" Sharper. Adopted.
- **Redemptive-Historical guardrails**: Valid concern. Bad evaluators reward artificial "Jesus jumps" and cliche Christ connections. The rubric must reward *organic fulfillment and covenantal movement*, not forced typology. Guardrail added.
- **Law/Gospel concern**: Valid. A standalone 20% Law/Gospel category imports a Lutheran central grid into a Reformed Baptist framework. Not every passage is structured around law/gospel contrast. Law/Gospel dynamics absorbed into the Gospel Centrality category rather than standing alone.

**Chaff discarded:**
- **Restructured weighting to 30/30/15/20/5**: Too compressed. Loses illustration entirely and collapses theology with gospel in a way that obscures different failure modes. A sermon can score well on theology and still have no gospel force — the current split catches that. Keep separate categories.
- **"Perceived Divine Authority" language**: Unnecessarily abstract. "Unction and Gravity" is fine — what it needed was *operationalization* (measurable indicators), not a rebrand. Operationalized as: textual grounding density, absence of filler, Scripture-driven assertion ratio.
- **"Unction is too subjective" criticism**: Partially valid. But the solution isn't to kill the category — it's to give it measurable anchors while preserving the irreducible reality that some sermons carry weight that transcends mechanics. Both Edwards' quiet authority and Whitefield's fire qualify. Operationalized without flattening.
- **The self-congratulatory rating ("8.5/10") and dramatic warnings ("it will isolate you")**: Theater. Discarded.

### Round 4 — Perplexity/ChatGPT Convergence (Akin Layer)

Both Perplexity and ChatGPT converged on nearly identical output — which means the framework has stabilized. The new contribution is Danny Akin's emphasis on exhortation as distinct from application.

**Wheat kept:**
- **Exhortation as its own category**: This is Akin's genuine contribution. A sermon can have searching Puritan-style application — exposing the heart, distinguishing hearers — and *still never call for a response*. Application tells you where truth touches your life. Exhortation tells you what you must now *do*. These are different things. Separating them catches the sermon that is pastorally sensitive but never actually summons. Adopted as a standalone category (8 pts, carved from Application).
- **"Conscience & Applicatory Force" naming**: Better than just "Application." Makes the Puritan emphasis explicit — this is not about "practical tips" but about pressing the conscience. Adopted.
- **"No actual exhortation" as a fatal flaw**: A sermon without a call to response is a lecture. Added to the fatal flaw flags.
- **"Too dense for ordinary hearers" as a hard failure**: The cognitive load modifier already catches this at -1 and -2. At -3 (inaccessible), it should also trigger a fatal flaw flag. Promoted.
- **"Equips the church for holiness and witness"**: Good addition to the exhortation diagnostics — a sermon should not just comfort or convict, but *send*. Adopted.
- **The thesis sentence**: "A good sermon is one that faithfully expounds Scripture, displays Christ, presses the conscience, gives specific application, calls for response, and leaves the hearer more convinced of God's truth and more ready to obey it." Excellent. Adopted as the skill's governing thesis.

**Chaff discarded:**
- **Revised weighting (28/22/20/10/10/5/5)**: This collapses Theology and Gospel into one category. But a sermon can score well on theological precision and still have no gospel *force*. Those are different failure modes — one is about accuracy, the other is about proclamation. Keeping them separate catches both. Exposition stays at 25, not 28 — the 3-point difference doesn't justify restructuring.
- **Merging Structure and Illustration into one category**: Loses diagnostic precision. A sermon can have clear structure and terrible illustrations, or beautiful illustrations in a wandering structure. Keep separate.
- **Dropping the Cognitive Load modifier for a binary hard failure only**: Too coarse. A slightly dense sermon (-1) is different from an inaccessible one (-3). Keep the modifier for mild cases; the extreme case (-3) now also triggers a fatal flaw flag.
- **Moving "Gravity & Spirit Dependence" from bonus into the main 100-point scale**: The bonus mechanic is conceptually important. Gravity is *above and beyond* — it's what separates a good sermon from a great one. Keeping it as a bonus preserves that distinction.

**Structural change from Round 4:**

The old Application (20 pts) splits into:
- **Conscience & Applicatory Force (15 pts)** — Puritan searching uses, heart penetration, spiritual differentiation
- **Exhortation & Response (8 pts)** — clear call to repentance, faith, obedience, witness

This adds 3 points total. To compensate: Theology reduces from 20 to 18 (still strong — the 2-point reduction comes from Redemptive-Historical Awareness, which was borderline redundant with Christ-Centeredness and is trimmed, not eliminated). Structure reduces from 10 to 9.

### Round 5 — Gemini "Sovereign Grace Homiletic Audit" + ChatGPT Validation

**Wheat kept:**
- **"The Authority Test"** added to the Berean Gate: "Does the preacher stand under the Word as a herald, or above it as an editor?" Sharpens the gate from a one-question check to a two-question check. Adopted.
- **"Synagogue Test"** replaces "Moralism Alarm": "If a devout non-Christian could sit through this and not be offended by the necessity of Christ's blood, the sermon has failed." Sharper than "could this comfort a moral atheist" because it preserves the scandal of the cross. Adopted.
- **Law/Gospel Dialectic as diagnostic** (not category): "The Hammer and The Balm." Law strips self-trust, Gospel provides hope. Only Law = legalism; only Gospel = antinomianism. Better positioned as a diagnostic tool within Gospel Centrality than as a standalone weighted category. Adopted.
- **"1689 Pulse"** sharpens confessional alignment: specific reference to Covenant of Works / Covenant of Grace distinction and the Doctrines of Grace (TULIP). More specific than generic "confessional alignment." Adopted.
- **Verdict Title + 1-Sentence Summary** in output: A descriptive headline ("A Weighty Exposition" or "A Dangerous Moralism") plus a one-sentence summary makes the report immediately communicative. Adopted.
- **Tradition-grounded surgical fixes**: "Re-read the 'Use of Consolation' in Owen" as a fix. This makes the rubric distinctively Reformed rather than generically evangelical. Adopted as a principle.
- **Explicit "What We Don't Grade" section**: Polished oratory, modern relevance hooks, sermon length. Making this explicit guards against future drift. Adopted.

**Chaff discarded:**
- **Exegesis at 30%**: Too heavy. At 25 with the Berean Gate, exposition already has center of gravity. 30 crowds everything else.
- **Holy Gravity at 15%**: The Round 3 Gemini critique correctly identified this as too subjective. Now Gemini overweights it. Stays at 5 bonus.
- **Christ-Centered Necessity at 25%**: Collapses Theology and Gospel. Our split (18 + 15) catches different failure modes — a sermon can be theologically precise and still lack gospel force.
- **Structure & Exhortation merged**: Loses the Akin contribution. Exhortation is a pastoral imperative, not a structural concern.
- **"Sovereign Grace Homiletic Audit" naming, "v3.0", Pillar branding**: The skill is `sermon-evaluation`. Influences acknowledged in the thesis, not baked into category names.

**ChatGPT validation pass — one correction adopted:**
- **1689 Pulse must be scoped**: Not every sermon will explicitly surface covenant distinctions or TULIP. But it can still be fully faithful. The confessional check should be: (1) *Negative test*: Does the sermon contradict confessional theology? (2) *Positive test, where applicable*: Where the text naturally engages covenant or soteriological themes, does the sermon handle them with confessional precision? It should NOT be: "Did the sermon mention TULIP?" Scoping adopted.

---

## Final Architecture

### Files to Create/Modify

### 1. NEW: `.claude/skills/sermon-evaluation/SKILL.md`

The main skill file. Structure follows existing skill patterns (YAML frontmatter + markdown body).

#### Frontmatter
```yaml
---
name: sermon-evaluation
description: "Reformed Baptist sermon evaluation rubric. Scores sermon manuscripts on exposition, theology, gospel centrality, conscience-level application, exhortation, structure, illustration, and sermonic force using a weighted 100-point scale with fatal flaw detection, dead orthodoxy diagnostics, and cognitive load assessment. Produces diagnostic narrative with surgical fixes. Informed by Puritan pastoral theology and Danny Akin's expository priorities."
---
```

#### Body Sections

**A. The Berean Gate (Non-Negotiable)**

Before scoring anything, answer two questions:

> 1. *Is the main point of the sermon the main point of the text?*
> 2. *Does the preacher stand under the Word as a herald, or above it as an editor?*

If either answer is no — evaluation stops. No score assigned. Report:

> "This sermon is not text-driven. The main point of the sermon does not arise from the main point of the passage. No score is assigned. The sermon must be rebuilt from the text, not decorated with it."

This is not harsh. It is merciful. A sermon that doesn't say what the text says is not a sermon — it is a lecture using the Bible as a springboard. And a preacher who stands above the text as editor — selecting what to keep, softening what offends, reframing what is plain — has ceased to be a herald.

**The Scopus Test**: Can you state the sermon's thesis in one sentence that demonstrably arises from the passage's own argument? If you cannot, the sermon fails the gate.

**The Authority Test**: Does the preacher submit to the text's claims, including the uncomfortable ones? Or does the sermon quietly edit the passage — omitting the hard parts, softening the declarations, reframing plain speech into palatable advice?

**B. Fatal Flaw Flags (Score Cap System)**

If any of the following are present, the score is **capped at 69** regardless of other strengths. These are non-negotiable failures:

1. **No clear gospel presentation** — Christ's finished work is absent or assumed, never proclaimed
2. **Main point does not equal text's point** — passed the gate loosely but drifts from the passage's argument
3. **Christ is absent or unnecessary** — the sermon could survive intact without Jesus
4. **Application is entirely generic** — no specific call, no differentiated address, no conscience pressed
5. **No actual exhortation** — the sermon explains and applies but never calls for response (Akin's test: did the preacher tell the people what they must now believe, repent of, obey, or pursue?)
6. **Inaccessible to ordinary hearers** — the sermon requires seminary training to follow; the single mother, the high schooler, and the new believer are lost (triggers when Cognitive Load Modifier would be -3)

A sermon with a fatal flaw flag cannot score above "Concerning gaps." The flag must be reported prominently in the evaluation output.

**C. Weighted Scoring Framework (100 points + 5 bonus)**

| # | Category | Weight | Rationale |
|---|---|---|---|
| 1 | Exposition & Hermeneutics | 25 pts | Center of gravity. If this collapses, everything collapses. |
| 2 | Theology & Doctrinal Integrity | 18 pts | Is the sermon truthful about God? |
| 3 | Gospel Centrality & Force | 15 pts | Where many "solid" sermons quietly fail. Absorbs law/gospel dynamics. |
| 4 | Conscience & Applicatory Force | 15 pts | Puritan-style searching uses — presses the conscience, distinguishes hearers. |
| 5 | Exhortation & Response | 8 pts | Danny Akin's contribution: does the sermon actually call for response? |
| 6 | Structure & Logical Flow | 9 pts | Bad structure kills good theology. |
| 7 | Illustration & Imagination | 5 pts | Not fluff — how truth lands in the truck driver's cab. |
| 8 | Sermonic Force | 5 pts | Does this manuscript read like preaching or an essay? |
| — | **Subtotal** | **100 pts** | |
| + | Weight of Glory (bonus) | +5 pts | Does this sermon carry eternal gravity? |
| - | Cognitive Load Modifier | -3 to 0 | Could the congregation actually track this? (-3 also triggers fatal flaw) |

**Exposition + Gospel = 40 pts (40%).** This is intentional. A sermon can survive weak illustrations. It cannot survive weak exposition.

**Conscience + Exhortation = 23 pts (23%).** Application-related categories are elevated from the original 20%, reflecting the Puritan and Akin emphases. A sermon that only explains — even brilliantly — has not yet become preaching.

**D. Category Details**

Each category includes subcategories with point allocations, diagnostic questions, and scoring anchors.

---

**1. Exposition & Hermeneutics (25 pts)**

| Subcategory | Pts | What it measures |
|---|---|---|
| Textual Fidelity | 10 | Does the sermon derive its argument from the text itself? |
| Contextual Awareness | 5 | Immediate context, book flow, authorial intent |
| Exegetical Clarity | 5 | Original meaning explained clearly (Greek as unlock, not decoration) |
| Logical Faithfulness | 5 | No eisegesis, no idea-importing, no proof-texting |

*Diagnostic Questions:*
- Could a listener reconstruct the passage's argument after hearing this sermon?
- Did the preacher *discover* meaning or *impose* meaning?
- Does the sermon stay in orbit around the text, or does it launch and never return?
- Where is the longest stretch without referencing the passage? Is it too long?

---

**2. Theology & Doctrinal Integrity (18 pts)**

| Subcategory | Pts | What it measures |
|---|---|---|
| Christ-Centeredness | 7 | Not forced — organically arising from the text. *Guardrail: reward covenantal movement and organic fulfillment, not artificial "Jesus jumps" or cliche typology.* |
| Redemptive-Historical Awareness | 3 | Where does this text sit in the story of redemption? (Trimmed from 4 — organic placement, not forced Christology) |
| Doctrinal Precision | 4 | No theological sloppiness (especially justification, sin, grace, wrath) |
| Confessional Alignment — 1689 Pulse | 4 | *Scoped*: (1) Negative test — does the sermon contradict confessional theology? (2) Positive test, where applicable — where the text naturally engages covenant or soteriological themes, does the sermon handle them with confessional precision? Specifically: Covenant of Works / Covenant of Grace distinction, Doctrines of Grace. Not every sermon will explicitly surface these — but no sermon should contradict them. |

*Diagnostic Questions:*
- Is God presented as He is, or softened for comfort?
- Is the gospel assumed (background music) or proclaimed (the melody)?
- Would this theology survive cross-examination by Owen, Watson, or Spurgeon?
- *Redemptive-Historical guardrail*: Is the Christ-connection organic to the text's own trajectory, or bolted on? Does the connection arise from covenantal logic, typological pattern, or authorial intent — or is it an artificial leap?
- *1689 Pulse*: Where the text engages soteriological or covenantal themes, does the sermon handle them with confessional precision? Or does it drift into vague evangelicalism?

---

**3. Gospel Centrality & Force (15 pts)**

This is where many "solid" sermons quietly fail. Law/gospel dynamics are evaluated here — not as a Lutheran central grid, but as the natural rhythm of conviction and comfort that faithful preaching produces.

| Subcategory | Pts | What it measures |
|---|---|---|
| Clarity of the Gospel | 5 | Is justification by faith clearly articulated? |
| Necessity of Christ | 5 | Is Christ essential — or just helpful? |
| Cross-Centered Gravity | 5 | Does the sermon move toward the cross, not orbit around morality? |

*Diagnostic Questions:*
- Would an unbeliever understand how to be saved from this sermon?
- Would a believer be freshly amazed at grace?
- Does the law have time to land before the gospel relieves it, or is comfort premature?
- Does the sermon present indicatives (what God has done) before imperatives (what we must do)?

*The Synagogue Test (moralism detection):*
If a devout non-Christian — someone who believes in the Old Testament, practices moral discipline, and fears God — could sit through this sermon and not be offended by the necessity of Christ's blood, the sermon has failed its gospel clarity. The cross must be a scandal, not a decoration.

Three diagnostic questions:
1. Could this sermon survive in a synagogue or mosque without giving offense? If yes — the gospel is missing.
2. Is obedience presented without new birth as its source?
3. Is Christ necessary to the sermon's argument — or merely decorative?

If "yes" to any → flag as moralistic drift. Major deduction.

*The Law/Gospel Dialectic (The Hammer and The Balm):*
- Was the law used to strip the hearer of self-trust? (The Hammer)
- Was the gospel used to provide the only hope? (The Balm)
- A sermon with only law is legalism. A sermon with only gospel (without conviction first) is cheap grace. Both must be present in their proper order.

> *"If you leave out Christ, you have left the sun out of the day."* — Spurgeon

---

**4. Conscience & Applicatory Force (15 pts)**

This is Puritan preaching at its best — William Perkins' cases of conscience, Thomas Watson's uses. The question is not "Was this practical?" but "Did this search the heart?"

A sermon is not good merely because it is accurate. It must also search the conscience, distinguish among different hearers, and move from doctrine to specific uses. The sermon should speak differently to the believer, the doubter, the self-righteous, and the open sinner.

| Subcategory | Pts | What it measures |
|---|---|---|
| Heart Penetration | 5 | Does this expose the heart? Convicts, comforts, confronts — reaches the affections, not just the intellect |
| Specificity | 5 | Not vague ("trust God more") — but concrete, grounded in the congregation's actual lives |
| Spiritual Differentiation | 5 | Distinguishes hearers: the weary saint, the self-righteous, the unbeliever, the backslider. Does it comfort the weak? Warn the hardened? Drive the hearer to Christ? |

*Diagnostic Questions:*
- Did this sermon press on the conscience — or just inform the mind?
- Did it leave different people in different places?
- Would the application land in *this* congregation specifically — the politically confident, the comfortable, the grieving?
- Is there a moment where a particular sinner is cornered by the text?
- Does it move from doctrine to specific *uses* (Puritan sense)?

---

**5. Exhortation & Response (8 pts)**

*Danny Akin's contribution: good preaching is not just exposition, but exposition that includes illustration, application, and exhortation.* A sermon can be textually faithful, pastorally sensitive, and still weak if it never actually calls for response. Exhortation is the imperative edge — the moment the preacher looks the congregation in the eye and says, "Now *go*."

This makes the rubric more church-shaped and less academic.

| Subcategory | Pts | What it measures |
|---|---|---|
| Call to Response | 4 | Clear: What must I now believe, repent of, obey, or pursue? |
| Equipping for Holiness & Witness | 4 | Does the sermon send the church out — not just comfort them where they sit? |

*Diagnostic Questions:*
- Does the sermon move from explanation to specific application to actual exhortation?
- Is there a clear "therefore" moment — where the truth preached becomes the obedience demanded?
- Does the sermon equip the church for holiness and witness, or only for private comfort?
- Would a listener leave knowing what to *do* — not just what to *think*?

---

**6. Structure & Logical Flow (9 pts)**

Bad structure kills good theology. If the congregation can't follow it, the theology doesn't matter.

| Subcategory | Pts | What it measures |
|---|---|---|
| Clarity of Outline | 4 | Memorable, traceable — could a listener sketch it on a napkin? |
| Progression | 3 | Builds toward something — does not wander |
| Unity | 3 | One dominant idea, not five competing ones |

*Diagnostic Questions:*
- Can you summarize this sermon in one sentence?
- Did each section clearly connect to the next?
- Is there a section that could be removed without loss? If so, remove it.

---

**6. Illustration & Imagination (5 pts)**

Low weight, high impact. Illustrations aren't decoration — they're how truth lands in concrete lives.

| Subcategory | Pts | What it measures |
|---|---|---|
| Relevance | 2 | From the congregation's world (trucks, football, military, marriage, diagnosis) |
| Clarity | 2 | Illuminates the point — doesn't compete with it |
| Memorability | 1 | Will the congregation carry this image home? |

*Diagnostic Questions:*
- Did illustrations clarify — or distract?
- Could this illustration be swapped into any other sermon, or is it native to this text?
- Will this be remembered tomorrow? Next week?

---

**7. Sermonic Force (5 pts)**

*Replaces "Delivery & Authenticity" — because we evaluate manuscripts, not live preaching.* This measures whether the manuscript reads like it was written to be *preached*, not *presented*.

| Subcategory | Pts | What it measures |
|---|---|---|
| Reads as Preaching | 2 | Oral cadence, direct address, breath-length paragraphs |
| Conviction on the Page | 2 | Textual grounding density, absence of filler, Scripture-driven assertion ratio |
| Cadence and Breath | 1 | Sentence variation, climactic compression, pause-and-pivot |

*Diagnostic Questions:*
- Does this read like an essay or a sermon?
- Is there a moment where the manuscript *roars*? Does it earn that moment?
- Could a quiet, faithful man preach this with authority? (Edwards test) Could a passionate man preach this with fire? (Whitefield test) If yes to both, the sermonic force is right.

*Operationalized Unction Indicators:*
- Ratio of Scripture-grounded assertions to general statements
- Absence of filler language, hedge words, and throat-clearing
- Presence of direct address ("Some of you...") at pressure points
- Sentence length variation — shorter at climax, not uniform throughout

---

**8. Weight of Glory — Bonus (+5 pts)**

This cannot be fully operationalized. It is the irreducible remainder — what the Puritans called "unction" and what Spurgeon called "a sense of the divine presence."

| Subcategory | Pts | What it measures |
|---|---|---|
| Eternal Significance | 2 | Does this sermon feel like it matters beyond Sunday? |
| Divine Gravity | 2 | Is God weighty in this sermon — or manageable? |
| The Spurgeon Test | 1 | Would a man who has been with God weep, tremble, or rejoice? |

*This is not personality preference.* Edwards' quiet manuscript authority and Whitefield's open-air fire both qualify. The question is not "Was the preacher exciting?" but "Was God present?"

---

**9. Cognitive Load Modifier (-3 to 0 pts)**

A sermon can be theologically rich, textually faithful, and pastorally *overwhelming*. This modifier protects pastoral usefulness.

| Score | Meaning |
|---|---|
| 0 | Well-paced. The congregation can track it. |
| -1 | Slightly dense. One fewer concept would help. |
| -2 | Overloaded. Competing ideas, insufficient development time. |
| -3 | Inaccessible. The sermon requires seminary training to follow. |

*Diagnostic Question:*
- Could an average church member — not the seminary-trained elder, but the single mother, the high schooler, the new believer — follow the main argument and take home one clear truth?

---

**E. Dead Orthodoxy Detection**

A special diagnostic that fires automatically when score patterns suggest *correct but bloodless* preaching:

**Triggers:**
- Exposition scores 20+ but Application scores below 12
- Theology scores 16+ but Gospel Centrality scores below 9
- Total score is 75+ but no single diagnostic question produces a "yes, deeply" answer
- Moralism Alarm triggered despite high theology score

**Output:**
> "This sermon may be doctrinally sound but pastorally inert. Correct theology that doesn't corner sinners or comfort saints has not yet become preaching. The doctrine is right. The fire is missing. Gospel-less orthodoxy is still orthodoxy without power."

---

**F. Core Override Questions (Non-Scoring)**

These three questions override numerical scores. If the answer to all three is "no," the number is irrelevant — no matter how high:

1. Does this sermon make me think more of Christ — or myself?
2. Did I encounter God, or just ideas about Him?
3. Was I comforted, convicted, or merely informed?

---

**G. Output Format**

Every evaluation produces:

1. **Verdict Title**: A descriptive headline that immediately communicates the sermon's character (e.g., "A Weighty Exposition with a Hollow Gospel Center" or "Faithful Text Work, Missing the Conscience" or "A Dangerous Moralism in Reformed Clothing")
2. **One-Sentence Summary**: "A faithful opening of [Text] that magnified [strength] while [weakness]."
3. **Berean Gate**: Pass/Fail — Is this text-driven? (Scopus Test + Authority Test)
4. **Fatal Flaw Flags**: Any present? If so, score capped at 69. List which flags triggered.
5. **Score Breakdown**: Category-by-category with brief narrative justification per category
6. **Cognitive Load Modifier**: Applied with explanation
7. **Total Score**: With interpretation band
8. **Core Override Questions**: Answered
9. **Strengths (Top 3)**: Specific, with evidence from the manuscript (quote or location)
10. **Critical Weaknesses (Top 3)**: Diagnostic, not polite — with location in the sermon
11. **Blind Spots**: What the preacher likely doesn't see
12. **Illusion of Strength**: Where the sermon *felt* strong but wasn't — where confidence masked weakness
13. **Missed Opportunity**: Where the text offered depth the preacher ignored or hurried past
14. **Surgical Fixes**: Specific, actionable, and where possible *tradition-grounded* — pointing to the Reformed and Puritan tradition for correction, not just opinion:
    - "Add direct address to the self-righteous after point 2"
    - "Clarify penal substitution in the conclusion — currently it reads as moral influence"
    - "The text's own climax is in v.8, but the sermon climaxes at v.5. Realign."
    - "The application lacks experimental religion. Consider Watson's treatment of the uses of [doctrine] in *A Body of Divinity*."
    - "The exhortation is absent. The congregation was informed but never summoned."
15. **Dead Orthodoxy Flag**: If triggered
16. **Weight of Glory Assessment**: One sentence

**H. Score Interpretation**

| Range | Meaning |
|---|---|
| 90-105 | Rare. Exemplary exposition, pastoral heat, gospel gravity. Preach it. |
| 80-89 | Strong and faithful. Minor sharpening needed. Ready for the pulpit with targeted revisions. |
| 70-79 | Solid but lacking — usually in application or gospel force. Needs another pass. |
| 60-69 | Concerning gaps. Often the sermon explains but doesn't preach. Significant revision needed. |
| Below 60 | Fundamentally flawed. Rebuild from the text. |

*Note: A score of 69 with a fatal flaw flag is qualitatively different from a 69 without one. The flag indicates a structural problem, not just weakness.*

---

**I. Relationship to Other Skills**

| Skill | Evaluates | When |
|---|---|---|
| `sermon-evaluation` | *Quality* — faithful, sharp, pastoral? | After draft, before final revision |
| `voice-audit` | *Authenticity* — sounds like the preacher or a machine? | After revision, before commit |
| `careful-not-clever` | *Integrity* — references verified, quotes real? | During all modifications |
| `like-a-human` | *Voice* — shapes writing during composition | During writing |

**Recommended workflow:**
1. Write with `like-a-human` + `careful-not-clever` active
2. Run `sermon-evaluation` on the completed draft
3. Revise based on surgical fixes
4. Run `voice-audit` before committing
5. Commit

---

### 2. MODIFY: `.claude/skill-rules.json`

Add `sermon-evaluation` entry to the `skills` object:

```json
"sermon-evaluation": {
  "enabled": true,
  "type": "domain",
  "enforcement": "suggest",
  "priority": "high",
  "description": "Reformed Baptist sermon evaluation rubric. Scores manuscripts on a weighted 100-point scale with fatal flaw detection, cognitive load assessment, and dead orthodoxy diagnostics. Produces surgical fixes.",
  "promptTriggers": {
    "keywords": [
      "evaluate sermon",
      "sermon evaluation",
      "score sermon",
      "grade sermon",
      "rubric",
      "sermon quality",
      "how good is this sermon",
      "rate this sermon",
      "sermon review",
      "evaluate this",
      "moralism check"
    ],
    "intentPatterns": [
      "(evaluate|score|grade|rate|review|assess).*?sermon",
      "sermon.*?(evaluation|quality|score|grade|rubric)",
      "how.*?(good|strong|faithful|solid).*?sermon"
    ]
  },
  "autoLoad": {
    "mainFile": ".claude/skills/sermon-evaluation/SKILL.md",
    "maxLines": 600,
    "loadOnSessionStart": false
  },
  "activationMessage": "Sermon evaluation active. Faithful exposition, theological precision, pastoral heat. Soli Deo Gloria.",
  "coActivation": {
    "suggested_with": ["voice-audit"],
    "note": "Sermon evaluation assesses quality. Voice-audit assesses authenticity. Run both before committing a finished manuscript."
  }
}
```

Update `total_skills` from 4 to 5 in the notes section.

---

### 3. MODIFY: `claude.md`

Add a brief mention of the sermon evaluation skill to the project guidelines. One line describing what it does and when to invoke it.

---

## Implementation Order

1. Create `.claude/skills/sermon-evaluation/SKILL.md` — full skill file with all sections
2. Update `.claude/skill-rules.json` — add new skill entry, update metadata
3. Update `claude.md` — add brief reference
4. Commit and push to `claude/sermon-evaluation-skill-IeTgs`

---

## What We Don't Grade (And Why)

These are intentionally excluded to prevent the rubric from drifting toward style over substance:

- **Polished oratory**: A man can be unpolished and powerfully used. We do not grade on smoothness, but on faithfulness. The Puritans were not slick.
- **Modern relevance hooks**: We reject the need to be "cool." If the sermon is faithful to the eternal Word, it is eternally relevant. We do not reward cultural trend-chasing.
- **Sermon length**: A short sermon can be shallow; a long sermon can be a wall of text. We grade on *density of truth per unit of attention*, not minutes.
- **Entertainment value**: "Did you enjoy it?" is not a diagnostic question. "Did it corner you before Christ?" is.
- **Personality type**: Edwards was quiet. Whitefield was volcanic. Spurgeon was witty. Ryle was plain. All four are excellent. The rubric rewards faithfulness, not temperament.

---

## What This Skill Is NOT

- It is not a replacement for the Holy Spirit's work in the preacher's heart
- It is not a mechanical pass/fail gate that reduces preaching to a score
- It is not an excuse to avoid preaching a sermon that scores 72 — the Lord has used weaker sermons than yours to save souls
- It is not personality-biased — Edwards' quiet authority and Spurgeon's fire both score well
- The numbers serve the diagnostic questions, not the other way around

The score is a mirror, not a judge. It shows the preacher what's there so he can sharpen what needs sharpening before he stands and says, "Thus says the Lord."

> A weak rubric produces polite feedback. A strong rubric produces better preachers.

*Soli Deo Gloria.*
