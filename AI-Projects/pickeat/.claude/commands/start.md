# Session Start

Esegui il protocollo di inizio sessione:

## Steps 1-5: Context Loading

1. **Leggi context**: `brain/context.md`
2. **Leggi ultimo closing**: trova il file più recente in `task/daily-summaries/closing-*.md`
3. **Riassumi** in max 5 bullet points:
   - Cosa è stato fatto nell'ultima sessione
   - Cosa è pending
   - Focus corrente da context
4. **Chiedi**: "Confermi queste priorità o cambiamo?"
5. **STOP** - Aspetta risposta prima di procedere

## Step 6: After Answer - Load Relevant Agent ONLY

Based on user's answer, load ONLY the relevant agent:

| Task Type | Agent to Load |
|-----------|---------------|
| Sales/Revenue | `agents/sales-orchestrator.md` |
| Content/Copy | `agents/content-engine.md` |
| Competitor research | `agents/competitive-intel.md` |
| Varese work | `clients/varese/` (read relevant files) |
| Session closing | `agents/session-closer.md` |
| File cleanup | `agents/archivista.md` |

**If no specific agent needed → proceed as Basilio (default brain)**

---

## Token Budget

- **Startup**: 600-700 tokens MAX
- **Session total**: 25-35K target

**If you burned more than 800 tokens before asking "what are we working on?" → YOU FAILED.**

---

## NEVER Do This at Start

- Read brain file twice (you already loaded it)
- Read CLAUDE.md (router already loaded it)
- Read multiple files "just in case"
- Load agents before knowing the task
- Start working before user confirms priorities

---

NON leggere altri file. NON caricare agenti. NON iniziare task.
