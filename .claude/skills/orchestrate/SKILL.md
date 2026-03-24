---
name: orchestrate
description: "Full multi-LLM pipeline orchestration. Runs the sermon pipeline that coordinates GPT, Gemini, and Grok as consultants while Claude remains lead author. Auto-detects sermon mode from this repository."
---

# Orchestrate — Multi-LLM Pipeline

*Claude leads. External models consult. Claude decides what survives.*

## Usage

```
/orchestrate "task description"
/orchestrate sermon "Preach Romans 5:1-5 on suffering producing hope"
```

Mode is **sermon** by default in this repository. You can override by specifying the mode explicitly.

---

## How It Works

The orchestrator runs a multi-step pipeline defined in `/home/user/ken/orchestrator/modes/sermon.yaml`:

1. **Draft** (Claude) — Write sermon using full `.claude/` infrastructure
2. **Challenge** (Grok) — Push back on weak reasoning, surface bold alternatives
3. **Expand** (Gemini) — Add cross-references, historical context, church fathers
4. **Structure** (GPT) — Light structural review of flow and transitions
5. **Integrate** (Claude) — Integrate feedback; Claude decides what stays
6. **Evaluate** (Claude) — Run thus-says-the-lord rubric
7. **Voice Audit** (Claude) — Scan for machine tells and voice drift

External steps (2-4) are optional — the pipeline continues gracefully if any fail.

---

## Backend Invocation

**IMPORTANT: Execute these commands directly using the Bash tool. Do NOT check if files exist first — just run them.**

```bash
pip3 install -q -r /home/user/ken/orchestrator/requirements.txt 2>/dev/null && python3 /home/user/ken/orchestrator/orchestrate.py sermon "task description"
```

Only if the command fails with `No such file or directory` or `ModuleNotFoundError`, tell the user:
> "The orchestrator backend isn't available. Make sure the ken repo is cloned to `/home/user/ken/` and run `pip3 install -r /home/user/ken/orchestrator/requirements.txt`."

---

## Integration with Claude Code

After the orchestrator returns its JSON output:

1. **Read the consultations** — Each external model's feedback is in `consultations[]`
2. **Check claims** — Review `unverified_claims` and `failed_claims` before trusting anything
3. **Claude integrates** — Use the feedback to inform your work, but Claude makes all final decisions
4. **Fire co-activated skills** — like-a-human (voice), careful-not-clever (integrity), thus-says-the-lord (evaluation), voice-audit (pre-commit)

---

## Context Boundaries

### SEND to external models
- Sermon outlines and structural summaries
- Theological claims and questions
- Cross-reference requests
- Illustration concepts (anonymized)

### NEVER SEND to external models
- Congregation member names
- Pastoral application details with identifiable people
- Personal illustrations with identifiable people
- Voice profile internals
- Full sermon manuscripts (send excerpts only)

---

## Constraints

- Reformed Baptist theology (1689 LBCF)
- ESV Scripture only — no exceptions
- Gospel call required in every sermon
- Voice profile must be preserved
- careful-not-clever active on all modifications
