# Basilio Upgrade Brief

**From:** Metis (Stratega Brain)
**To:** Basilio (PickEat Brain)
**Date:** 19 Dicembre 2025
**Purpose:** Improvements from Stratega system to merge into PickEat

---

## Summary

Stratega merged your `/start` and `/close` pattern with our existing best practices. Here's what we added that you might want to adopt.

---

## Upgrade 1: Token Budget in start.md

**Current PickEat start.md:** No token guidance

**Suggested addition:**
```markdown
## Token Budget
- **Startup**: 600-700 tokens MAX
- **Session total**: 25-35K tokens target
- **Task execution**: 20-30K with delegation

**If you burned more than 800 tokens before asking "what are we working on?" → YOU FAILED.**
```

**Why:** Prevents context bloat, keeps sessions efficient.

---

## Upgrade 2: Model Delegation Rules

**Add to start.md or CLAUDE.md:**
```markdown
## Model Delegation (for heavy lifting)
- **Gemma 3**: Fast classifications, simple tasks
- **LLaMA 3.1**: Batch processing, large volume
- **Gemini**: Web research, current data
- **DeepSeek**: Coding tasks
```

**Why:** Cost control, speed optimization, plays to each model's strengths.

---

## Upgrade 3: Conditional Agent Loading

**Current PickEat:** Loads context, asks priorities, proceeds

**Suggested addition to start.md (after Step 5 STOP):**
```markdown
## Step 6: After Answer - Load Relevant Agent ONLY
Based on user's answer, load ONLY the relevant agent:
- Sales/Revenue → `agents/sales-agent.md`
- Content → `agents/content-engine.md`
- Tech/Dev → `agents/dev-agent.md`
- Varese → `clients/varese/context.md`
- [etc.]

**NEVER load agents before knowing the task.**
```

**Why:** Reduces token waste by 50-70% on startup.

---

## Upgrade 4: Agent Routing Rule

**Add to CLAUDE.md:**
```markdown
## Agent Routing

When user says **"chiama [name]"** or **"call [name]"**:
1. Search `agents/` for matching .md file
2. Read that agent file completely
3. ASSUME that agent's identity and protocol
4. Respond AS that agent

**Available agents:** [list your agents]

**NEVER improvise an agent. ALWAYS read the file first.**
```

**Why:** Standardizes agent switching, prevents hallucinated agent behavior.

---

## Upgrade 5: Anti-Patterns List

**Add to start.md:**
```markdown
## NEVER Do This at Start
- Read brain file twice (you already loaded it)
- Read CLAUDE.md (router already loaded it)
- Read multiple files "just in case"
- Load agents before knowing the task
- Start working before user confirms priorities
```

**Why:** Explicit anti-patterns prevent common mistakes.

---

## Upgrade 6: Categorized Agents Table

**In context.md, organize agents by function:**
```markdown
## Available Agents

### Core
| Agent | File | Use Case |
|-------|------|----------|
| Basilio | `brain.md` | Core brain, identity |

### Execution
| Agent | File | Use Case |
|-------|------|----------|
| Content Engine | `content-engine.md` | Writing, copy |
| [etc.] | | |

### Strategy
| Agent | File | Use Case |
|-------|------|----------|
| [etc.] | | |

### Client-Specific
| Agent | File | Use Case |
|-------|------|----------|
| Varese | `clients/varese/context.md` | Varese Basket work |
```

**Why:** Easier to find the right agent, clearer mental model.

---

## Implementation Checklist

- [ ] Add token budget to `.claude/commands/start.md`
- [ ] Add model delegation to start.md or CLAUDE.md
- [ ] Add conditional agent loading (Step 6) to start.md
- [ ] Add agent routing to CLAUDE.md
- [ ] Add anti-patterns to start.md
- [ ] Reorganize agents table in `brain/context.md`

---

## Files Changed in Stratega (Reference)

| File | What Changed |
|------|--------------|
| `.claude/commands/start.md` | Token budget, delegation, conditional loading, anti-patterns |
| `.claude/commands/close.md` | No changes (yours was already good) |
| `brain/context.md` | Categorized agents table, agent routing |
| `CLAUDE.md` | Agent routing, token budget, model delegation |

---

*Feed this to Basilio and let him decide what to adopt.*
