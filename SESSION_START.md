# SESSION START PROTOCOL

## AT EVERY SESSION START - DO THIS AND NOTHING ELSE:

1. **Read weekly tasks (top 50 lines)** (300 tokens max)
   ```
   Read /task/WEEKLY_TASKS.md (limit: 50 lines)
   → Get big picture context
   ```

2. **Read latest daily prep (top 30 lines)** (300 tokens max)
   ```bash
   ls -t notes/daily-summaries/prep-*.md | head -1
   → Get today's focus
   ```

3. **Propose priorities based on both** (100 tokens)
   ```
   "From weekly tasks, I see:
   - [Big objective 1 status]
   - [Big objective 2 status]

   Today's prep suggests:
   - [Priority 1]
   - [Priority 2]

   What are we working on today?"
   ```

4. **STOP. Wait for answer.**

5. **After answer: Load ONLY relevant docs** (2-5K tokens max)
   - Working on MRR? → agents/esattore.md
   - Working on code? → agents/archimede.md
   - Working on file org? → REORGANIZATION_PLAN.md
   - Working on content? → agents/content-engine.md
   - Working on growth? → agents/growth-hacker.md

6. **Delegate heavy lifting to local models**
   - Gemma 3: fast classifications, simple tasks
   - LLaMA 3.1: batch processing, large volume
   - Gemini: web research, current data
   - DeepSeek: coding tasks

---

## NEVER DO THIS AT START:
❌ Read stratega-brain.md (you already know who you are)
❌ Read ORCHESTRATION_GUARDRAILS.md (you already know how to orchestrate)
❌ Read SESSION_STARTUP_CHECKLIST.md (it's 270 lines!)
❌ Read CLAUDE.md (router already loaded it)
❌ Read multiple files "just in case"

---

## TOKEN BUDGET PER SESSION:
- Target: 25-35K tokens TOTAL
- Startup: 600-700 tokens MAX (weekly + daily + proposal)
- Task execution: 20-30K tokens (with delegation)

---

**If you burned more than 800 tokens before asking "what are we working on?" → YOU FAILED.**
