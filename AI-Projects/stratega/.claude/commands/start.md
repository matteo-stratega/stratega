# Session Start

Esegui il protocollo di inizio sessione:

## Step 1: Load Context (max 400 tokens)
1. **Leggi context**: `brain/context.md`
2. **Leggi ultimo closing**: trova il file più recente in `notes/daily-summaries/closing-*.md`

## Step 2: Propose (max 200 tokens)
Riassumi in max 5 bullet points:
- Cosa è stato fatto nell'ultima sessione
- Cosa è pending
- Focus corrente da context

Poi chiedi: **"Confermi queste priorità o cambiamo?"**

## Step 3: STOP
**Aspetta risposta prima di procedere.**

## Step 4: After Answer - Load Relevant Agent ONLY
Based on user's answer, load ONLY the relevant agent:
- MRR/Revenue → `agents/esattore.md`
- Code/Tech → `agents/archimede.md` or `agents/cto.md`
- File org/Git → `agents/archivista.md`
- Content/Copy → `agents/content-engine.md`
- Growth/Experiments → `agents/growth-hacker.md`
- Editorial planning → `agents/content-strategist.md`
- Build in Public → `agents/build-in-public.md`

---

## Token Budget
- **Startup**: 600-700 tokens MAX
- **Session total**: 25-35K tokens target
- **Task execution**: 20-30K with delegation

## Model Delegation (for heavy lifting)
- **Gemma 3**: Fast classifications, simple tasks
- **LLaMA 3.1**: Batch processing, large volume
- **Gemini**: Web research, current data
- **DeepSeek**: Coding tasks

## NEVER Do This at Start
- Read stratega-brain.md (identity already loaded)
- Read CLAUDE.md (router already loaded it)
- Read multiple files "just in case"
- Load agents before knowing the task

---

**If you burned more than 800 tokens before asking "what are we working on?" → YOU FAILED.**
