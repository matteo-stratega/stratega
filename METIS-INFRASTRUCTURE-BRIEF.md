# Metis Infrastructure Brief

**From:** Basilio (PickEat Brain)
**To:** CTO Agent @ Metis
**Date:** 23 Dec 2025
**Purpose:** Replicate Memory-First infrastructure from PickEat

---

## What We Built

A "Memory-First" system that gives Claude persistent memory across sessions. After several iterations (and killing a bad v1), this is the working setup.

### Core Components

| Component | Purpose | Status |
|-----------|---------|--------|
| Memory MCP | Persistent knowledge graph | ✅ Working |
| 2 Hooks | Enforcement + auto-save | ✅ Working |
| Closing protocol | Structured session handoff | ✅ Working |

---

## 1. Memory MCP Setup

### Config Location
Global: `~/.claude.json` (shared across projects)

### Add to mcpServers:
```json
"memory": {
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-memory"
  ],
  "env": {
    "MEMORY_FILE_PATH": "/Users/matteolombardi/AI-Projects/metis/.memory/knowledge-graph.jsonl"
  }
}
```

### Permissions
In `.claude/settings.local.json`:
```json
{
  "permissions": {
    "allow": [
      "mcp__memory__*"
    ]
  }
}
```

### Directory
```bash
mkdir -p .memory
echo ".memory/" >> .gitignore
```

---

## 2. Hooks Setup

### Directory Structure
```
.claude/
├── hooks/
│   ├── memory-auto-save.py    # SessionEnd - forces memory save
│   └── agent-call-enforcer.py # UserPromptSubmit - forces agent file read
└── settings.local.json        # Hook registration
```

### Hook 1: memory-auto-save.py
Triggers on SessionEnd. Reminds Claude to save facts to Memory MCP.

```python
#!/usr/bin/env python3
import json
import sys

def main():
    hook_input = json.loads(sys.stdin.read())

    # Only trigger on session end
    if hook_input.get("hook_type") != "SessionEnd":
        print(json.dumps({"continue": True}))
        return

    # Remind to save memory
    result = {
        "continue": True,
        "message": "BEFORE CLOSING: Save any new facts to Memory MCP using mcp__memory__add_observations or mcp__memory__create_entities"
    }
    print(json.dumps(result))

if __name__ == "__main__":
    main()
```

### Hook 2: agent-call-enforcer.py
Triggers on UserPromptSubmit. When user says "chiama [agent]", forces reading the agent file.

```python
#!/usr/bin/env python3
import json
import sys
import re

def main():
    hook_input = json.loads(sys.stdin.read())
    message = hook_input.get("message", "").lower()

    # Check for agent call patterns
    patterns = [
        r"chiama\s+(\w+)",
        r"call\s+(\w+)",
        r"usa\s+(\w+)\s+agent"
    ]

    for pattern in patterns:
        match = re.search(pattern, message)
        if match:
            agent_name = match.group(1)
            result = {
                "continue": True,
                "message": f"REQUIRED: Read agents/{agent_name}.md before responding. Do NOT improvise agent behavior."
            }
            print(json.dumps(result))
            return

    print(json.dumps({"continue": True}))

if __name__ == "__main__":
    main()
```

### Register Hooks
In `.claude/settings.local.json`:
```json
{
  "hooks": {
    "SessionEnd": [
      {
        "command": "python3 .claude/hooks/memory-auto-save.py"
      }
    ],
    "UserPromptSubmit": [
      {
        "command": "python3 .claude/hooks/agent-call-enforcer.py"
      }
    ]
  }
}
```

---

## 3. Session Protocol

### Start Command (`.claude/commands/start.md`)
Key addition - Step 0 Memory Recovery:
```markdown
## Step 0: Memory Recovery
**PRIMA DI TUTTO**, recupera contesto persistente:
mcp__memory__read_graph()
```

### Close Command (`.claude/commands/close.md`)
Key additions:
1. APPEND to existing closing file (no `-2, -3` naming)
2. Facts section that gets saved to Memory MCP
3. Structured format with TL;DR, Done, Pending, Files

---

## 4. Files to Create/Adapt

| File | Purpose | Copy from PickEat? |
|------|---------|-------------------|
| `.claude/hooks/memory-auto-save.py` | Auto-save reminder | Yes, adapt paths |
| `.claude/hooks/agent-call-enforcer.py` | Agent enforcement | Yes, as-is |
| `.claude/settings.local.json` | Hook registration | Merge with existing |
| `.claude/commands/start.md` | Session start | Adapt for Metis |
| `.claude/commands/close.md` | Session close | Adapt for Metis |
| `brain/context.md` | Persistent context | Create Metis version |
| `templates/closing-template.md` | Report format | Optional |

---

## 5. What We Killed (Don't Replicate)

❌ **knowledge-router.py** - Forced search before every response. Too noisy.
❌ **knowledge-gap-logger.py** - Logged corrections. Created friction.
❌ **Multiple UserPromptSubmit hooks** - Slowed down every interaction.

**Lesson:** Fewer hooks = better. Only hook what's critical.

---

## 6. Verification Steps

After setup:
1. Restart Claude Code (required to load MCP)
2. Test Memory MCP: `mcp__memory__read_graph()` should return empty or existing data
3. Test agent hook: Say "chiama cto" and check if it forces file read
4. Test closing: Run `/close` and verify it prompts for memory save

---

## Questions?

The CTO agent on Metis should be able to implement this. Key principle: **Memory-First means Claude saves facts automatically, not searches for them.**

If issues arise, check:
1. `~/.claude.json` syntax (JSON validity)
2. File permissions on hooks (`chmod +x`)
3. Python3 available in PATH
