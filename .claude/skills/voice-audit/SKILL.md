---
name: voice-audit
description: "Post-draft diagnostic for sermon and book writing. Scans for machine tells, assesses authenticity risk, checks voice continuity against the author's sermon corpus. Fires after writing is complete or when reviewing existing drafts. For during-writing standards, see like-a-human."
---

# Voice Audit — Post-Draft Diagnostics

*Fires after writing. Evaluates what was produced.*

**Relationship to other guardrails:**
- **like-a-human** shapes the *writing* — voice markers, rhythms, vocabulary, theological precision.
- **voice-audit** reviews the *output* — scanning for drift, flagging machine tells, assessing authenticity.
- **careful-not-clever** guards the *content* — verified Scripture, real quotes, grounded theology.

When drift is detected, the response is **restoration, not rewriting.** A few targeted edits to bring the prose back to the author's voice — not a wholesale rewrite that introduces new machine patterns.

---

## Machine Tell Scan

Run this scan against any draft that has been written or edited with AI assistance. These are the specific fingerprints AI leaves.

### Structural tells
- [ ] Uniform sentence length throughout — mid-length sentences with no spikes or drops
- [ ] Paragraph template loops: thesis line → 2-3 supports → tidy restatement, repeated section after section
- [ ] Visible symmetry: every section the same length, every list the same number of items
- [ ] The sandwich: intro promises what it will say, body says it, conclusion summarizes what it said

### Transition tells
- [ ] "Moreover," "Furthermore," "Additionally," "It's worth noting," "In conclusion," "In today's world," "At its core," "In essence," "Let's dive in"
- [ ] Any transition smoother than a gear grind — this voice uses hard pivots: "Now —" "And then Paul pivots." "But here's the thing."

### Word-level tells
- [ ] Hedging stacks: "It's important to note that," "One might argue," "It's worth considering," "It seems like," "Perhaps"
- [ ] Adverb inflation: "truly remarkable," "deeply profound," "incredibly powerful"
- [ ] Thesaurus syndrome: three words where one would do
- [ ] AI-overrepresented vocabulary: *robust, comprehensive, landscape, realm, leveraging, framework, holistic, narrative, nuanced, multifaceted, foster, delve, tapestry, pivotal, navigate, unpack, resonate*
- [ ] Vague moral swaps: "brokenness" for sin, "issues" for wrath, "challenges" for idolatry, "struggles" for repentance, "disconnect" for judgment, "fresh start" for justification, "realign" for repent

### Rhythm tells
- [ ] Even sentence length from start to finish
- [ ] Fragment stacking every time emphasis is needed (occasional = human; constant = machine)
- [ ] False variation: complex/simple alternation in a mechanical pattern

### Substance tells
- [ ] Everything important, nothing specific: "This powerful passage reveals deep truths about the human condition"
- [ ] Interchangeable illustrations that could be swapped into any other sermon
- [ ] Correct but bloodless exposition: text explained, sinner never cornered, heart never pierced
- [ ] No rough edges: every paragraph resolves cleanly, every transition is smooth
- [ ] Comfort arrives before conviction has had time to land

### Seam detection
- [ ] One or more paragraphs shift to a more abstract, polished, or consultant-like register while the rest sounds like the preacher
- [ ] Paragraphs whose sentences all open the same way when the author's pattern uses varied openings
- [ ] A section that feels "inserted" rather than grown from the surrounding argument

---

## Voice Continuity Check

Compare the draft against the author's existing sermon corpus. The baseline voice (established in Romans 13b through Romans 15a and the thief on the cross sermon) has these markers:

### Must be present
- **Compressed declarative chains:** "Same crimes. Same sentence. Same nails. Same slow suffocation."
- **Antithetical parallelism:** "Not correction. Not condescension. Not rolling our eyes… We owe them *weight-bearing*."
- **Text-first orbit:** Quote → unpack → re-quote. The prose doesn't leave the passage for long.
- **Gear-shift markers:** "Now —" "Hear me:" "And here's the thing:" "Let me say this gently:"
- **Direct pastoral address:** "Some of you..." tied to concrete, plausible lives — the addict, the estranged parent, the diagnosis, the war-zone marriage.
- **Shrinking sentences at climax:** "Today. With me. Paradise." "Cast it off."
- **Pause-and-pivot after intensity:** "Something else was happening. Someone was opening his eyes."
- **The refrain:** "The night is far gone. The day is at hand." woven organically.

### Must be absent
- Stacked intensifier adverbs
- AI-overrepresented vocabulary (see Machine Tell Scan)
- "Moreover / Furthermore / In conclusion" transitions
- Road-map paragraphs that announce what's coming
- Hedged assertions where the text speaks declaratively
- Therapeutic vocabulary substituting for biblical terms

### Drift indicators
If three or more of the "must be present" markers are missing, or two or more of the "must be absent" items appear, the draft has drifted from the author's voice. Flag specific locations and suggest minimal restoration edits.

---

## Conviction Check

For each major movement of the sermon, ask:

1. **What sin or unbelief is this confronting?** If the answer is only "we're all broken / busy / distracted," conviction has been flattened. Replace with text-shaped names.

2. **Is there a clear call?** Repent, come, confess, forgive, flee, put on, cast off. If a section only explains but never summons, it has lost its edge.

3. **Is there direct pastoral address?** At least once per major movement, the sermon should look at someone specific: "Some of you who..." If "we" is doing all the work, conviction has been averaged out.

4. **Has the conditional voice crept in?** Scan for "might," "could," "may," "tends to" where the author would say "is," "does," "will." Keep conditionals only where the text itself frames hypotheticals.

5. **Does comfort arrive too early?** The law should have time to land before the gospel relieves it. If conviction and comfort share a paragraph, the tension has been collapsed.

---

## Cadence Check

Identify the 1-2 moments in the sermon that should be the hottest points. At those spots, check:

1. **Are sentences actually shorter?** If the climax has the same sentence length as the setup, it has been flattened.

2. **Is there anaphora or antithesis?** "He didn't... He didn't... He didn't..." or "Not... Not... Not... But..." If absent at key moments, the author's native rhythm has been smoothed.

3. **Is there a pause-and-pivot?** After the peak, does one quiet sentence pull the room close? If the high moment rolls straight into explanation, a native move has been lost.

4. **Do gear-shift markers appear?** "Now —" "Hear me:" before or after key transitions? If not, the draft reads like an essay, not a sermon.

5. **Does the breath test pass?** Can each paragraph be read aloud in one or two breaths? If not, it was built for silent reading, not preaching.

---

## Doctrinal Sharpness Check

1. **Biblical vocabulary present?** Where the text says sin, wrath, judgment, repentance, justification, adoption, sanctification — are those words on the page? Or have they been swapped for therapeutic equivalents?

2. **Contrasts drawn?** For every key doctrinal statement, is there a "not... but..." antithesis? If you can't form one, the doctrine may be too vague.

3. **TED talk test.** Take the biggest claim in the sermon. Could it be the centerpiece of a secular leadership talk with zero offense? If yes, either anchor it explicitly to the text or replace it with something that cannot survive outside the world of Romans, cross, resurrection, judgment.

4. **Corporate retreat test.** Could a paragraph be read unchanged at a corporate retreat with nods and no discomfort? If yes, it has been flattened.

5. **Text tethering.** For every doctrinal claim, is there a clear "Look at verse..." or a direct quotation? If doctrine floats free of the passage, pull it back.

---

## Authenticity Risk Assessment

After completing all checks, assign an overall rating:

**Authenticity Risk: Low / Medium / High**

Evaluate based on:
- Machine tell density (how many items flagged in the scan)
- Voice continuity (how many markers are present/absent)
- Conviction integrity (does the sermon corner and summon, or only explain?)
- Cadence integrity (does the sermon build and breathe, or flatline?)
- Doctrinal precision (sharp biblical words or vague therapeutic ones?)
- Sermonic cliché density ("friends," "beloved," "here's the thing")
- Emotional register accuracy (does anger sound like anger, or like disappointment?)

**High risk if:**
- More than 5 machine tells flagged
- Three or more voice markers missing
- No direct pastoral address in the entire sermon
- Climactic moments have the same sentence length as setup
- Biblical terms consistently replaced with therapeutic language
- The piece has no seams — no place where the author changed direction or left a tension unresolved
- The prose could survive in a secular context with no Bible reference

**Output:** Flag specific locations. Suggest 3-5 minimal restoration edits. Do not rewrite the sermon. Restore the voice.

*This assessment is internal and never published.*
