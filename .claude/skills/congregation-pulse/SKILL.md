---
name: congregation-pulse
description: "Post-sermon and post-series reflection skill. Captures what landed, what fell flat, what needs revisiting, and what pastoral needs surfaced. Pastoral memory, not analytics."
version: 1.0.0
---

# Congregation Pulse

> *"Shepherd the flock of God that is among you."* — 1 Peter 5:2

## Purpose

After preaching, capture what the pastor sensed about the congregation's response. This is pastoral memory — not metrics, not analytics. The preacher's intuition about what connected and what didn't.

## When to Fire

- On `/pulse` command
- After finishing a sermon ("how did that go?")
- At the end of a sermon series
- When reflecting on pastoral needs

## Reflection Protocol

### After a Single Sermon

Ask these questions (the preacher answers, Claude encodes):

1. **What connected?** Which point, illustration, or moment seemed to land? Where did the room get quiet?
2. **What fell flat?** Which section felt forced, unclear, or missed? Where did attention drift?
3. **What surprised you?** Anything unexpected — a reaction, a question afterward, a conversation in the hallway?
4. **What pastoral need surfaced?** Did you see grief, conviction, confusion, hunger, resistance? In whom (categories, not names)?
5. **What should we come back to?** Is there a thread that needs its own sermon? A doctrine that needs more time?

### After a Series

Additional questions:

6. **What was the arc?** Looking back, what was the real theme — not the planned one, but the one that emerged?
7. **What would you change?** If preaching this series again, what order, emphasis, or approach would shift?
8. **What's unfinished?** What question did the series raise but not answer?

## Encoding

Each reflection gets encoded into cognitive-memory:

```bash
# After a sermon
python3 /home/user/ken/orchestrator/memory_ops.py encode romans insight \
  "Romans 8:28-30 sermon: 'golden chain' illustration connected strongly. Several people mentioned it after. The section on predestination felt rushed — need more time on that in a future sermon." \
  --tags romans8,golden-chain,predestination,congregation --protected

# After a series
python3 /home/user/ken/orchestrator/memory_ops.py encode romans pattern \
  "Romans 1-4 series: justification arc worked best when built slowly. Congregation needed more on wrath (ch 1-2) before grace (ch 3-4) could land. Don't rush the law." \
  --tags romans-series,justification,pacing,pattern --protected
```

### Linking

Link pulse observations to their sermon-map entries:
```bash
python3 /home/user/ken/orchestrator/memory_ops.py link <pulse_id> <sermon_map_id>
```

## Report Format

```
## Congregation Pulse — [Sermon Title] — [date]

**Passage:** [reference]
**Series:** [if applicable]

### What Connected
- [observation]

### What Fell Flat
- [observation]

### Pastoral Needs Surfaced
- [observation]

### Come Back To
- [topic/passage for future]

### Encoded Memories
- [memory ID]: [brief content]
```

## What This Is NOT

- Not a feedback form (no scores, no ratings)
- Not a performance review (the sermon serves God, not metrics)
- Not public (internal only, never published)
- Not about the preacher's feelings (about the congregation's needs)

## Integration

- **sermon-map** — link pulse to sermon entries
- **sermon-planner** — pulse data informs what to preach next
- **cognitive-memory** — observations persist across sessions
- **sermon-cross-reference** — "we need to come back to X" feeds future planning

---

*Soli Deo Gloria* — Shepherd attentively. Remember faithfully.
