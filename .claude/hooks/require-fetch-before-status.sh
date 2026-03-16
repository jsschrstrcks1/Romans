#!/bin/bash
# Iron-clad guardrail: block git status/log remote checks without a prior git fetch.
#
# Reads the Bash tool input from stdin as JSON.
# Outputs {"decision": "block", "reason": "..."} or {"decision": "approve"}.

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    print(data.get('command', ''))
except Exception:
    print('')
" 2>/dev/null)

# Does this command check remote state?
if echo "$COMMAND" | grep -qE '(git\s+status|git\s+log\s+.*origin|HEAD\.\.origin|origin\/main|git\s+branch\s+-v)'; then
    # Is a fetch also present in the same command?
    if ! echo "$COMMAND" | grep -qE 'git\s+fetch'; then
        echo "{\"decision\": \"block\", \"reason\": \"FETCH REQUIRED: You cannot check git status or compare against origin without running 'git fetch origin' first. 'git status' only reflects the local tracking ref — without fetching, you are reporting stale data as fact. Required sequence: git fetch origin && git status\"}"
        exit 0
    fi
fi

echo '{"decision": "approve"}'
exit 0
