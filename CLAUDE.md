# Claude Code — Standing Instructions for This Repository

## Git Status Checks

**ALWAYS run `git fetch origin` before answering any question about:**
- Whether the branch is up to date
- Whether there are conflicts to resolve
- Whether a pull or merge is needed
- The state of the remote

`git status` only compares against the local tracking ref. Without fetching first, it is stale data. Reporting stale data as fact is a lie. Do not do it.

**Required sequence before any git status answer:**
```
git fetch origin
git status
```

No exceptions.

---

## Scripture Integrity

- Never quote Scripture from memory. Always verify against ESV text.
- Never cite a specific verse unless it has been confirmed from a primary or reliable secondary source.
- "The third chapter of Romans" is defensible when the specific verse is unconfirmed. A verse number is not defensible until verified.

## Attributed Quotes

- Never fabricate or paraphrase a quote and present it as verbatim.
- If a quote cannot be verified to a source, flag it with ⚠️ in the sermon file and illustration file.

## General

- Careful beats clever. Always.
- Soli Deo Gloria.
