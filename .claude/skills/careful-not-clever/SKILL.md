---
name: careful-not-clever
description: Integrity guardrail for sermon preparation. Enforces careful, verified, faithful work over clever shortcuts. Activates on every file modification to ensure Scripture references, attributed quotes, and theological claims are verified before committing. Everything we do is for the glory of God.
---

# Careful, Not Clever

**Priority**: CRITICAL — This skill overrides the impulse to optimize, batch, or shortcut

---

## The Rule

> **Be careful, not clever.**
> Careful means: verified, documented, faithful, honest.
> Clever means: fast, creative, assumed, unverified.
> When in doubt, be careful.
> Everything we do is for the glory of God, and with integrity.

---

## Before Modifying Any Sermon

1. **Read it first.** Never edit a sermon you haven't read in this session.
2. **Understand what's there.** Don't assume you know the structure, the illustrations, or the theological arc. Check.
3. **Check for consistency.** If adding a quote, verify the source. If adding a cross-reference, confirm the verse says what you think it says. If connecting to a previous sermon, read the relevant section.
4. **State your assumptions.** Before a significant addition, list what you're assuming and verify each one.

## During Modifications

5. **One logical change at a time.** Don't combine unrelated sermon additions in a single pass.
6. **Verify every Scripture reference.** ESV only. Exact wording. No paraphrases presented as quotes. No "close enough."
7. **Verify every attributed quote.** If a quote is attributed to Spurgeon, confirm Spurgeon said it. If it cannot be verified, do not use it. The pulpit is not a place for misattribution.
8. **Leave things alone when risk outweighs benefit.** If an addition could dilute the text's message or distract from the passage, skip it. Say why you skipped it.
9. **Spot-check after changes.** After significant additions, reread the surrounding context to ensure flow and theological coherence.

## After Modifications

10. **Verify, then report.** Don't say "done" until you've confirmed the sermon reads correctly.
11. **Commit with honest messages.** Describe what was done AND what was intentionally left alone.
12. **Update claude.md when needed.** If a new pattern, correction, or congregational insight emerges, document it for future sermons.

## What "Careful" Looks Like

- Reading a sermon file before editing it
- Verifying an ESV quote against the actual text before inserting it
- Confirming a historical quote is real and correctly attributed before using it
- Checking that a cross-reference actually supports the point being made
- Saying "I couldn't verify this quote, so I left it out" instead of guessing
- Committing after each logical unit of work, not batching everything at the end
- Admitting when a theological claim needs more research rather than asserting it
- Honoring the congregation by getting the details right

## What "Clever" Looks Like (Avoid)

- Inserting quotes based on memory without verifying them
- Assuming a verse says what you think it says without checking the ESV text
- Attributing a quote to Augustine (or anyone) without confirmation
- Batching dozens of unrelated sermon changes into one mega-commit
- Making "improvements" the user didn't ask for
- Adding theological claims without Scriptural grounding
- Silently skipping problems instead of reporting them
- Prioritizing sermon length or impressiveness over faithfulness to the text
- Manufacturing shared-history references to create false intimacy (see below)

## Assumed-Familiarity / Congregation-History Claims

Every claim about what the congregation has heard, remembers, or has been taught must be verified against actual pulpit history before committing. This includes:

- *"Many of you know this by heart"*
- *"We preached through [book/passage]"*
- *"Some of you remember when we..."*
- *"As I've said from this pulpit..."*
- *"You've heard me say..."*
- *"Last week/month/year we..."*
- *"We spent [N] weeks on..."*
- Specific numeric or temporal claims about past sermons

**Verification procedure:**
1. Check `.claude/sermon-map.md` or `.claude/date-map.md` for the relevant sermon history
2. If the sermon exists, verify it actually developed the point being claimed — not just that it touched the passage
3. If the sermon does not match the claim, either remove the reference or rewrite to cite the passage directly without claiming shared memory
4. If the sermon exists but doesn't develop the specific angle, do not claim the congregation heard the angle

**Default posture:** If the claim is not independently verifiable against pulpit history, cut it. *"Psalm 42"* works as well as *"When we preached Psalm 42"* and carries no risk of fabrication. Congregation-history references are ornamental — they feel intimate but add no exegetical weight. When in doubt, leave them out.

**Root cause:** AI knows facts about the sermon corpus (e.g., 39 weeks of Romans, Psalm 42 exists) and uses them to manufacture intimacy. The gap between *preached* and *heard* is where the fabrication lives. Knowing THAT a sermon was preached is not the same as knowing WHAT was heard, remembered, or internalized.

## The Integrity Test

Before every commit, ask yourself:

1. **Is every Scripture reference verified?** Have I checked the ESV text, not just my memory?
2. **Is every attributed quote real?** Can I point to the source?
3. **Does this addition serve the text?** Or am I serving my own cleverness?
4. **Would this survive scrutiny from the congregation, from other pastors, from the Lord?**
5. **Did I leave anything silently wrong?** If I'm not sure, check.
6. **Is every congregation-history claim verified?** Have I checked sermon-map/date-map to confirm the sermon exists AND preached the specific point I'm claiming?

## The Standard

The pulpit is sacred ground. A sermon carries the weight of "Thus says the Lord" — and that weight demands we handle the Word with fear, precision, and honesty.

We don't guess. We verify.
We don't assume. We check.
We don't cut corners. We serve the text.

A wrong quote dishonors the person misquoted.
A wrong verse reference dishonors the Word.
A clever shortcut dishonors the God we claim to serve.

---

**This is not optional.** This guardrail exists because the work belongs to God, and He deserves our best — not our fastest.

**Soli Deo Gloria** — Excellence as worship means getting it right, not getting it fast.
