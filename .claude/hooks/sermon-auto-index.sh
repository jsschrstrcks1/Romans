#!/usr/bin/env bash
# sermon-auto-index.sh
# PostToolUse hook: fires after Write/Edit.
# If the written file is a sermon .md in the Romans root directory,
# injects a reminder to run sermon-map and thus-says-the-lord.

set -euo pipefail

# Read the full hook payload from stdin
payload=$(cat)

# Extract file path
file=$(echo "$payload" | jq -r '.tool_input.file_path // empty' 2>/dev/null)

# Nothing to do if no file path
[[ -z "$file" ]] && exit 0

# Must be a .md file directly in /home/user/Romans/ (not a subdirectory)
echo "$file" | grep -qE '^/home/user/Romans/[^/]+\.md$' || exit 0

# Exclude .claude/ files (map files, settings, hooks)
echo "$file" | grep -q '/\.claude/' && exit 0

# It's a sermon file — output additionalContext reminding Claude to run the skills
python3 - "$file" <<'PYEOF'
import json, sys
filepath = sys.argv[1]
filename = filepath.split('/')[-1]
msg = (
    f"SERMON FILE WRITTEN: {filename}\n"
    "You MUST now use the Skill tool to run these two operations before responding:\n"
    "1. sermon-map — INDEX operation: add this file to .claude/sermon-map.md, "
    ".claude/date-map.md, .claude/illustration-map.md, .claude/quote-map.md "
    "per the sermon-map skill rules\n"
    "2. thus-says-the-lord — evaluate this sermon manuscript using the full rubric\n"
    "Do not skip or defer these steps. They are required for every new sermon file."
)
output = {
    "hookSpecificOutput": {
        "hookEventName": "PostToolUse",
        "additionalContext": msg
    }
}
print(json.dumps(output))
PYEOF
