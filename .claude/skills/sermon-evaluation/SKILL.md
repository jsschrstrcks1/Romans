---
name: sermon-evaluation
description: "Reformed Baptist sermon evaluation rubric. Scores sermon manuscripts on exposition, theology, gospel centrality, conscience-level application, exhortation, structure, illustration, and sermonic force using a weighted 100-point scale with fatal flaw detection, dead orthodoxy diagnostics, and cognitive load assessment. Produces diagnostic narrative with surgical fixes."
---

# Sermon Evaluation — Reformed Baptist Rubric

*Fires on request. Evaluates sermon manuscripts for faithfulness, gospel clarity, pastoral force, and sermonic quality.*

> A good sermon is a text-governed proclamation of God's Word that faithfully explains the passage, clearly presents Christ and the gospel, searches the conscience, gives specific application, exhorts a real response, and equips the church for holiness and witness.

The sermon must be judged first by faithfulness to the text, then by gospel clarity, then by how deeply it presses the hearer toward repentance, faith, and obedience.

**Relationship to other skills:**
- **sermon-evaluation** assesses *quality* — is this sermon faithful, sharp, and pastoral?
- **voice-audit** assesses *authenticity* — does this sound like the preacher or like a machine?
- **careful-not-clever** guards *integrity* — are the references verified and the quotes real?
- **like-a-human** shapes *voice* — during writing, not after.

**Recommended workflow:**
1. Write with `like-a-human` + `careful-not-clever` active
2. Run `sermon-evaluation` on the completed draft
3. Revise based on surgical fixes
4. Run `voice-audit` before committing
5. Commit

---

## A. The Berean Gate (Non-Negotiable)

Before scoring anything, answer two questions:

1. **Is the main point of the sermon the main point of the text?**
2. **Does the preacher stand under the Word as a herald, or above it as an editor?**

If either answer is no — evaluation stops. No score assigned. Report:

> "This sermon is not text-driven. The main point of the sermon does not arise from the main point of the passage. No score is assigned. The sermon must be rebuilt from the text, not decorated with it."

This is not harsh. It is merciful. A sermon that doesn't say what the text says is not a sermon — it is a lecture using the Bible as a springboard. And a preacher who stands above the text as editor — selecting what to keep, softening what offends, reframing what is plain — has ceased to be a herald.

**The Scopus Test**: Can you state the sermon's thesis in one sentence that demonstrably arises from the passage's own argument? If you cannot, the sermon fails the gate.

**The Authority Test**: Does the preacher submit to the text's claims, including the uncomfortable ones? Or does the sermon quietly edit the passage — omitting the hard parts, softening the declarations, reframing plain speech into palatable advice?

---

## B. Fatal Flaw Flags (Score Cap System)

If any of the following are present, the score is **capped at 69** regardless of other strengths. These are non-negotiable failures:

1. **No clear gospel presentation** — Christ's finished work is absent or assumed, never proclaimed
2. **Main point does not equal text's point** — passed the gate loosely but drifts from the passage's argument
3. **Christ is absent or unnecessary** — the sermon could survive intact without Jesus
4. **Application is entirely generic** — no specific call, no differentiated address, no conscience pressed
5. **No actual exhortation** — the sermon explains and applies but never calls for response. Did the preacher tell the people what they must now believe, repent of, obey, or pursue?
6. **Inaccessible to ordinary hearers** — the sermon requires seminary training to follow; the single mother, the high schooler, and the new believer are lost

A sermon with a fatal flaw flag cannot score above "Concerning gaps." The flag must be reported prominently in the evaluation output.

---

## C. Weighted Scoring Framework (100 points + 5 bonus)

| # | Category | Weight | Rationale |
|---|---|---|---|
| 1 | Exposition & Hermeneutics | 25 pts | Center of gravity. If this collapses, everything collapses. |
| 2 | Theology & Doctrinal Integrity | 18 pts | Is the sermon truthful about God? |
| 3 | Gospel Centrality & Force | 15 pts | Where many "solid" sermons quietly fail. |
| 4 | Conscience & Applicatory Force | 15 pts | Puritan-style searching uses — presses the conscience, distinguishes hearers. |
| 5 | Exhortation & Response | 8 pts | Does the sermon actually call for response? |
| 6 | Structure & Logical Flow | 9 pts | Bad structure kills good theology. |
| 7 | Illustration & Imagination | 5 pts | Not fluff — how truth lands in the truck driver's cab. |
| 8 | Sermonic Force | 5 pts | Does this manuscript read like preaching or an essay? |
| — | **Subtotal** | **100 pts** | |
| + | Weight of Glory (bonus) | +5 pts | Does this sermon carry eternal gravity? |
| − | Cognitive Load Modifier | −3 to 0 | Could the congregation actually track this? (−3 also triggers fatal flaw) |

**Exposition + Gospel = 40 pts (40%).** A sermon can survive weak illustrations. It cannot survive weak exposition.

**Conscience + Exhortation = 23 pts (23%).** A sermon that only explains — even brilliantly — has not yet become preaching.

---

## D. Category Details

### 1. Exposition & Hermeneutics (25 pts)

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

### 2. Theology & Doctrinal Integrity (18 pts)

| Subcategory | Pts | What it measures |
|---|---|---|
| Christ-Centeredness | 7 | Not forced — organically arising from the text. *Guardrail: reward covenantal movement and organic fulfillment, not artificial "Jesus jumps" or cliche typology.* |
| Redemptive-Historical Awareness | 3 | Where does this text sit in the story of redemption? Organic placement, not forced Christology. |
| Doctrinal Precision | 4 | No theological sloppiness (especially justification, sin, grace, wrath) |
| Confessional Alignment — 1689 Pulse | 4 | *Scoped*: (1) *Negative test* — does the sermon contradict confessional theology? (2) *Positive test, where applicable* — where the text naturally engages covenant or soteriological themes, does the sermon handle them with confessional precision? Covenant of Works / Covenant of Grace distinction, Doctrines of Grace. Not every sermon will explicitly surface these — but no sermon should contradict them. |

*Diagnostic Questions:*
- Is God presented as He is, or softened for comfort?
- Is the gospel assumed (background music) or proclaimed (the melody)?
- *Redemptive-Historical guardrail*: Is the Christ-connection organic to the text's own trajectory, or bolted on? Does the connection arise from covenantal logic, typological pattern, or authorial intent — or is it an artificial leap?
- *1689 Pulse*: Where the text engages soteriological or covenantal themes, does the sermon handle them with confessional precision? Or does it drift into vague evangelicalism?

---

### 3. Gospel Centrality & Force (15 pts)

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

*The Synagogue Test:*
If a devout non-Christian — someone who believes in the Old Testament, practices moral discipline, and fears God — could sit through this sermon and not be offended by the necessity of Christ's blood, the sermon has failed its gospel clarity. The cross must be a scandal, not a decoration.

1. Could this sermon survive in a synagogue or mosque without giving offense? If yes — the gospel is missing.
2. Is obedience presented without new birth as its source?
3. Is Christ necessary to the sermon's argument — or merely decorative?

If "yes" to any → flag as moralistic drift. Major deduction.

*The Law/Gospel Dialectic (The Hammer and The Balm):*
- Was the law used to strip the hearer of self-trust? (The Hammer)
- Was the gospel used to provide the only hope? (The Balm)
- A sermon with only law is legalism. A sermon with only gospel (without conviction first) is cheap grace. Both must be present in their proper order.

---

### 4. Conscience & Applicatory Force (15 pts)

The question is not "Was this practical?" but "Did this search the heart?"

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
- Does it move from doctrine to specific *uses*?

---

### 5. Exhortation & Response (8 pts)

A sermon can be textually faithful, pastorally sensitive, and still weak if it never actually calls for response. Exhortation is the imperative edge — the moment the preacher looks the congregation in the eye and says, "Now *go*."

Application tells you where truth touches your life. Exhortation tells you what you must now *do*. These are different things.

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

### 6. Structure & Logical Flow (9 pts)

Bad structure kills good theology. If the congregation can't follow it, the theology doesn't matter.

| Subcategory | Pts | What it measures |
|---|---|---|
| Clarity of Outline | 4 | Memorable, traceable — could a listener sketch it on a napkin? |
| Progression | 3 | Builds toward something — does not wander |
| Unity | 2 | One dominant idea, not five competing ones |

*Diagnostic Questions:*
- Can you summarize this sermon in one sentence?
- Did each section clearly connect to the next?
- Is there a section that could be removed without loss? If so, it should be removed.

---

### 7. Illustration & Imagination (5 pts)

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

### 8. Sermonic Force (5 pts)

*Replaces "Delivery & Authenticity" — because we evaluate manuscripts, not live preaching.* This measures whether the manuscript reads like it was written to be *preached*, not *presented*.

| Subcategory | Pts | What it measures |
|---|---|---|
| Reads as Preaching | 2 | Oral cadence, direct address, breath-length paragraphs |
| Conviction on the Page | 2 | Textual grounding density, absence of filler, Scripture-driven assertion ratio |
| Cadence and Breath | 1 | Sentence variation, climactic compression, pause-and-pivot |

*Diagnostic Questions:*
- Does this read like an essay or a sermon?
- Is there a moment where the manuscript *roars*? Does it earn that moment?
- Could a quiet, faithful man preach this with authority? Could a passionate man preach this with fire? If yes to both, the sermonic force is right.

*Operationalized Indicators:*
- Ratio of Scripture-grounded assertions to general statements
- Absence of filler language, hedge words, and throat-clearing
- Presence of direct address ("Some of you...") at pressure points
- Sentence length variation — shorter at climax, not uniform throughout

---

### 9. Weight of Glory — Bonus (+5 pts)

This cannot be fully operationalized. It is the irreducible remainder — what the Puritans called "unction."

| Subcategory | Pts | What it measures |
|---|---|---|
| Eternal Significance | 2 | Does this sermon feel like it matters beyond Sunday? |
| Divine Gravity | 2 | Is God weighty in this sermon — or manageable? |
| The Spurgeon Test | 1 | Would a man who has been with God weep, tremble, or rejoice? |

*This is not personality preference.* Edwards' quiet manuscript authority and Whitefield's open-air fire both qualify. The question is not "Was the preacher exciting?" but "Was God present?"

---

### 10. Cognitive Load Modifier (−3 to 0 pts)

A sermon can be theologically rich, textually faithful, and pastorally *overwhelming*. This modifier protects pastoral usefulness.

| Score | Meaning |
|---|---|
| 0 | Well-paced. The congregation can track it. |
| −1 | Slightly dense. One fewer concept would help. |
| −2 | Overloaded. Competing ideas, insufficient development time. |
| −3 | Inaccessible. Triggers fatal flaw flag #6. |

*Diagnostic Question:*
- Could an average church member — not the seminary-trained elder, but the single mother, the high schooler, the new believer — follow the main argument and take home one clear truth?

---

## E. Dead Orthodoxy Detection

A special diagnostic that fires automatically when score patterns suggest *correct but bloodless* preaching:

**Triggers:**
- Exposition scores 20+ but Conscience & Applicatory Force scores below 9
- Theology scores 15+ but Gospel Centrality scores below 9
- Total score is 75+ but no single diagnostic question produces a "yes, deeply" answer
- Synagogue Test triggered despite high theology score

**Output:**
> "This sermon may be doctrinally sound but pastorally inert. Correct theology that doesn't corner sinners or comfort saints has not yet become preaching. The doctrine is right. The fire is missing. Gospel-less orthodoxy is still orthodoxy without power."

---

## F. Core Override Questions (Non-Scoring)

These three questions override numerical scores. If the answer to all three is "no," the number is irrelevant — no matter how high:

1. Does this sermon make me think more of Christ — or myself?
2. Did I encounter God, or just ideas about Him?
3. Was I comforted, convicted, or merely informed?

---

## G. Output Format

Every evaluation produces:

1. **Verdict Title**: A descriptive headline that immediately communicates the sermon's character (e.g., "A Weighty Exposition with a Hollow Gospel Center" or "Faithful Text Work, Missing the Conscience" or "A Dangerous Moralism in Reformed Clothing")
2. **One-Sentence Summary**: "A faithful opening of [Text] that magnified [strength] while [weakness]."
3. **Berean Gate**: Pass/Fail (Scopus Test + Authority Test)
4. **Fatal Flaw Flags**: Any present? If so, score capped at 69. List which flags triggered.
5. **Score Breakdown**: Category-by-category with brief narrative justification
6. **Cognitive Load Modifier**: Applied with explanation
7. **Total Score**: With interpretation band
8. **Core Override Questions**: Answered
9. **Strengths (Top 3)**: Specific, with evidence from the manuscript (quote or location)
10. **Critical Weaknesses (Top 3)**: Diagnostic, not polite — with location in the sermon
11. **Blind Spots**: What the preacher likely doesn't see
12. **Illusion of Strength**: Where the sermon *felt* strong but wasn't — where confidence masked weakness
13. **Missed Opportunity**: Where the text offered depth the preacher ignored or hurried past
14. **Surgical Fixes**: Specific, actionable, and where possible tradition-grounded:
    - "Add direct address to the self-righteous after point 2"
    - "Clarify penal substitution in the conclusion — currently it reads as moral influence"
    - "The text's own climax is in v.8, but the sermon climaxes at v.5. Realign."
    - "The application lacks experimental depth. Consider the Puritan 'uses' pattern — conviction, direction, consolation."
    - "The exhortation is absent. The congregation was informed but never summoned."
15. **Dead Orthodoxy Flag**: If triggered
16. **Weight of Glory Assessment**: One sentence

---

## H. Score Interpretation

| Range | Meaning |
|---|---|
| 90–105 | Rare. Exemplary exposition, pastoral heat, gospel gravity. Preach it. |
| 80–89 | Strong and faithful. Minor sharpening needed. Ready for the pulpit with targeted revisions. |
| 70–79 | Solid but lacking — usually in application or gospel force. Needs another pass. |
| 60–69 | Concerning gaps. Often the sermon explains but doesn't preach. Significant revision needed. |
| Below 60 | Fundamentally flawed. Rebuild from the text. |

*A score of 69 with a fatal flaw flag is qualitatively different from a 69 without one. The flag indicates a structural problem, not just weakness.*

---

## I. What We Don't Grade (And Why)

These are intentionally excluded to prevent the rubric from drifting toward style over substance:

- **Polished oratory**: A man can be unpolished and powerfully used. We do not grade on smoothness, but on faithfulness.
- **Modern relevance hooks**: We reject the need to be "cool." If the sermon is faithful to the eternal Word, it is eternally relevant.
- **Sermon length**: A short sermon can be shallow; a long sermon can be a wall of text. We grade on density of truth, not minutes.
- **Entertainment value**: "Did you enjoy it?" is not a diagnostic question. "Did it corner you before Christ?" is.
- **Personality type**: Edwards was quiet. Whitefield was volcanic. Spurgeon was witty. Ryle was plain. All four are excellent. The rubric rewards faithfulness, not temperament.

---

## J. What This Evaluation Is NOT

- It is not a replacement for the Holy Spirit's work in the preacher's heart
- It is not a mechanical pass/fail gate that reduces preaching to a number
- It is not an excuse to avoid preaching a sermon that scores 72 — the Lord has used weaker sermons than yours to save souls
- The numbers serve the diagnostic questions, not the other way around

The score is a mirror, not a judge. It shows the preacher what's there so he can sharpen what needs sharpening before he stands and says, "Thus says the Lord."

A weak rubric produces polite feedback. A strong rubric produces better preachers.

*Soli Deo Gloria.*
