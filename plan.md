# Sermon Evaluation Skill — Implementation Plan

## Overview

A new skill called `sermon-evaluation` that evaluates sermon manuscripts against a weighted rubric rooted in Reformed Baptist convictions. Invoked manually (not auto-firing). Produces a scored evaluation with diagnostic narrative, strengths, weaknesses, blind spots, and surgical fixes.

This is the fifth skill in the Romans project ecosystem.

---

## Design Decisions: Three Rounds of Refinement

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

---

## Final Architecture

### Files to Create/Modify

### 1. NEW: `.claude/skills/sermon-evaluation/SKILL.md`

The main skill file. Structure follows existing skill patterns (YAML frontmatter + markdown body).

#### Frontmatter
```yaml
---
name: sermon-evaluation
description: "Reformed Baptist sermon evaluation rubric. Scores sermon manuscripts on exposition, theology, gospel centrality, application, structure, illustration, and sermonic force using a weighted 100-point scale with fatal flaw detection and cognitive load assessment. Produces diagnostic narrative with surgical fixes."
---
```

#### Body Sections

**A. The Berean Gate (Non-Negotiable)**

Before scoring anything, answer one question:

> *Is the main point of the sermon the main point of the text?*

If no — evaluation stops. No score assigned. Report:

> "This sermon is not text-driven. The main point of the sermon does not arise from the main point of the passage. No score is assigned. The sermon must be rebuilt from the text, not decorated with it."

This is not harsh. It is merciful. A sermon that doesn't say what the text says is not a sermon — it is a lecture using the Bible as a springboard.

**The Scopus Test**: Can you state the sermon's thesis in one sentence that demonstrably arises from the passage's own argument? If you cannot, the sermon fails the gate.

**B. Fatal Flaw Flags (Score Cap System)**

If any of the following are present, the score is **capped at 69** regardless of other strengths. These are non-negotiable failures:

1. **No clear gospel presentation** — Christ's finished work is absent or assumed, never proclaimed
2. **Main point does not equal text's point** — passed the gate loosely but drifts from the passage's argument
3. **Christ is absent or unnecessary** — the sermon could survive intact without Jesus
4. **Application is entirely generic** — no specific call, no differentiated address, no conscience pressed

A sermon with a fatal flaw flag cannot score above "Concerning gaps." The flag must be reported prominently in the evaluation output.

**C. Weighted Scoring Framework (100 points + 5 bonus)**

| # | Category | Weight | Rationale |
|---|---|---|---|
| 1 | Exposition & Hermeneutics | 25 pts | Center of gravity. If this collapses, everything collapses. |
| 2 | Theology & Doctrinal Integrity | 20 pts | Is the sermon truthful about God? |
| 3 | Gospel Centrality & Force | 15 pts | Where many "solid" sermons quietly fail. Absorbs law/gospel dynamics. |
| 4 | Application (Applicatory Pungency) | 20 pts | Where sermons become pastoral, not merely informational. |
| 5 | Structure & Logical Flow | 10 pts | Bad structure kills good theology. |
| 6 | Illustration & Imagination | 5 pts | Not fluff — how truth lands in the truck driver's cab. |
| 7 | Sermonic Force | 5 pts | Does this manuscript read like preaching or an essay? |
| — | **Subtotal** | **100 pts** | |
| + | Weight of Glory (bonus) | +5 pts | Does this sermon carry eternal gravity? |
| - | Cognitive Load Modifier | -3 to 0 | Could the congregation actually track this? |

**Exposition + Gospel = 40 pts (40%).** This is intentional. A sermon can survive weak illustrations. It cannot survive weak exposition.

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

**2. Theology & Doctrinal Integrity (20 pts)**

| Subcategory | Pts | What it measures |
|---|---|---|
| Christ-Centeredness | 8 | Not forced — organically arising from the text. *Guardrail: reward covenantal movement and organic fulfillment, not artificial "Jesus jumps" or cliche typology.* |
| Redemptive-Historical Awareness | 4 | Where does this text sit in the story of redemption? |
| Doctrinal Precision | 4 | No theological sloppiness (especially justification, sin, grace, wrath) |
| Confessional Alignment — 1689 | 4 | Consistent with the Second London Baptist Confession and broader Reformed orthodoxy |

*Diagnostic Questions:*
- Is God presented as He is, or softened for comfort?
- Is the gospel assumed (background music) or proclaimed (the melody)?
- Would this theology survive cross-examination by Owen, Watson, or Spurgeon?
- *Redemptive-Historical guardrail*: Is the Christ-connection organic to the text's own trajectory, or bolted on? Does the connection arise from covenantal logic, typological pattern, or authorial intent — or is it an artificial leap?

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

*Moralism Alarm (3-question test):*
1. Could this sermon comfort a moral atheist without offense?
2. Is obedience presented without new birth as its source?
3. Is Christ necessary to the sermon's argument — or merely decorative?

If "yes" to any → flag as moralistic drift. Major deduction.

> *"If you leave out Christ, you have left the sun out of the day."* — Spurgeon

---

**4. Application — Applicatory Pungency (20 pts)**

This is where sermons become pastoral instead of merely informational. This is Puritan preaching at its best — William Perkins' cases of conscience, Thomas Watson's uses.

| Subcategory | Pts | What it measures |
|---|---|---|
| Heart Penetration | 6 | Convicts, comforts, confronts — reaches the affections, not just the intellect |
| Specificity | 5 | Not vague ("trust God more") — but concrete and actionable |
| Spiritual Differentiation | 5 | Distinguishes hearers: the weary saint, the self-righteous, the unbeliever, the backslider |
| Call to Response | 4 | Clear: What must I now do, believe, repent of, or cling to? |

*Diagnostic Questions:*
- Did this sermon press on the conscience — or just inform the mind?
- Did it leave different people in different places?
- Would the application land in this congregation specifically — the politically confident, the comfortable, the grieving?
- Is there a moment where a particular sinner is cornered by the text?

---

**5. Structure & Logical Flow (10 pts)**

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

1. **Berean Gate**: Pass/Fail — Is this text-driven? (With the Scopus Test sentence)
2. **Fatal Flaw Flags**: Any present? If so, score capped at 69. List which flags triggered.
3. **Score Breakdown**: Category-by-category with brief narrative justification per category
4. **Cognitive Load Modifier**: Applied with explanation
5. **Total Score**: With interpretation band
6. **Core Override Questions**: Answered
7. **Strengths (Top 3)**: Specific, with evidence from the manuscript (quote or location)
8. **Critical Weaknesses (Top 3)**: Diagnostic, not polite — with location in the sermon
9. **Blind Spots**: What the preacher likely doesn't see
10. **Illusion of Strength**: Where the sermon *felt* strong but wasn't — where confidence masked weakness
11. **Missed Opportunity**: Where the text offered depth the preacher ignored or hurried past
12. **Surgical Fixes**: Not "improve application" but specific, actionable interventions:
    - "Add direct address to the self-righteous after point 2"
    - "Clarify penal substitution in the conclusion — currently it reads as moral influence"
    - "The text's own climax is in v.8, but the sermon climaxes at v.5. Realign."
13. **Dead Orthodoxy Flag**: If triggered
14. **Weight of Glory Assessment**: One sentence

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

## What This Skill Is NOT

- It is not a replacement for the Holy Spirit's work in the preacher's heart
- It is not a mechanical pass/fail gate that reduces preaching to a score
- It is not an excuse to avoid preaching a sermon that scores 72 — the Lord has used weaker sermons than yours to save souls
- It is not personality-biased — Edwards' quiet authority and Spurgeon's fire both score well
- The numbers serve the diagnostic questions, not the other way around

The score is a mirror, not a judge. It shows the preacher what's there so he can sharpen what needs sharpening before he stands and says, "Thus says the Lord."

> A weak rubric produces polite feedback. A strong rubric produces better preachers.

*Soli Deo Gloria.*
