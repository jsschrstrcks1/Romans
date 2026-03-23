# Romans — Sermon Repository

**Soli Deo Gloria.** Expository sermon manuscripts, theological study materials, and preaching resources.

This repository already has extensive Claude Code integration via `.claude/skills/` (cognitive-memory, careful-not-clever, like-a-human, voice-audit, sermon-map, thus-says-the-lord).

---

## Multi-LLM Integration

This repository has access to the multi-LLM orchestrator system. External models (GPT, Gemini, Grok) serve as **consultants only** — Claude remains lead author and decision-maker.

### Available Skills

| Skill | Usage | Purpose |
|-------|-------|---------|
| `/consult` | `/consult grok challenge "review this Romans 5 outline"` | Quick single-model second opinion |
| `/orchestrate` | `/orchestrate sermon "preach Romans 5:1-5 on suffering"` | Full multi-model pipeline |
| Cognitive Memory | Automatic on session start | Cross-session knowledge persistence |

### Mode: `sermon`
- **Lead:** Claude (author, evaluator, archivist)
- **Pipeline:** Draft (Claude) → Challenge (Grok) → Expand (Gemini) → Structure (GPT) → Integrate (Claude) → Evaluate (Claude) → Voice Audit (Claude)
- **Memory scope:** `/romans`
- **Orchestrator:** `/home/user/ken/orchestrator/`

### First-Time Setup (Per Session)

Before first use of `/consult` or `/orchestrate` in a session, install dependencies:

```bash
pip3 install -q -r /home/user/ken/orchestrator/requirements.txt
```

This is silent when already installed. If `/consult` or `/orchestrate` fails with `ModuleNotFoundError`, run this command first.

### Context Boundaries
- **SEND:** Outlines, theological claims, cross-refs, illustration concepts
- **NEVER SEND:** Congregation names, pastoral details, personal illustrations, voice internals

### Constraints
- 1689 LBCF theology
- ESV-only Scripture
- Gospel call required
- Voice profile preserved (see like-a-human skill)
