---
name: consult
description: "Quick multi-LLM second opinion. Sends a single prompt to GPT, Gemini, or Grok with a role-based system prompt and returns structured feedback."
---

# Consult — Quick Second Opinion

*One model. One question. Structured feedback.*

## Usage

```
/consult <model> <role> "prompt text"
```

### Models
- **gpt** — OpenAI GPT (strong at structure, planning)
- **gemini** — Google Gemini (strong at expansion, cross-references)
- **grok** — xAI Grok (strong at challenge, adversarial thinking)

### Roles
- **challenge** — Push back on assumptions, surface weak reasoning
- **expand** — Add context, cross-references, historical background
- **structure** — Review logical flow and organization
- **critique** — Evaluate accuracy, completeness, clarity
- **plan** — Produce structured plans with steps and risks
- **safety** — Flag risks, errors, unsafe recommendations
- **freestyle** — General-purpose response

---

## Examples

```
/consult grok challenge "This sermon argues suffering produces hope through Romans 5:3-5. What's weak?"
/consult gemini expand "What OT cross-references connect to Romans 5:1-5 on justification and peace?"
/consult gpt structure "Review this sermon outline for logical gaps"
/consult gpt plan "How should we organize a 12-week series through Romans 9-11?"
```

---

## Backend Invocation

```bash
# Install dependencies (once per session)
pip3 install -q -r /home/user/ken/orchestrator/requirements.txt

# Run consultation
python3 /home/user/ken/orchestrator/consult.py <model> <role> "prompt text"
```

**Output:** JSON response to stdout with keys: `analysis`, `proposed_update`, `risks`, `confidence`
**Usage stats:** Printed to stderr (model, tokens, cost)

**If the backend is not found:** Tell the user:
> "The orchestrator backend isn't installed on this machine. It lives in the `ken` repository at `orchestrator/`. Make sure the ken repo is cloned to `/home/user/ken/`."

---

## Context Boundaries

### SEND
- Outlines, theological claims, cross-reference requests
- Anonymized illustration concepts
- Structural questions

### NEVER SEND
- Congregation names, pastoral details, personal illustrations
- Voice profile internals
- Full sermon manuscripts (send excerpts only)

---

## After Receiving Feedback

1. **Claude evaluates** — External feedback is advisory only. Claude decides what to use.
2. **Check claims** — If the response includes `claims`, verify them before incorporating.
3. **Apply careful-not-clever** — All modifications from consultation feedback must be verified.
