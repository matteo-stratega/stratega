# 🧠 TASK MEMORY SYSTEM
**Come Claude mantiene memoria delle tue task e priorità**

---

## PROBLEMA RISOLTO

**Prima:** Ogni sessione Claude ripartiva da zero, dovevi rispiegare tutto.

**Adesso:** Claude ha memoria persistente attraverso 2 file:
1. **WEEKLY_TASKS.md** - Big picture, obiettivi settimanali
2. **prep-[date].md** - Focus giornaliero, task oggi

---

## COME FUNZIONA

### All'Avvio Sessione

**Tu scrivi:**
```
Follow SESSION_START.md
```

**Claude automaticamente:**

**Step 1:** Legge top 50 righe di `/task/WEEKLY_TASKS.md`
- Capisce obiettivi settimanali
- Vede cosa è pending, cosa completato
- Comprende il big picture

**Step 2:** Legge top 30 righe di `prep-[oggi].md`
- Capisce focus di oggi
- Vede priorità specifiche
- Ha context da ieri

**Step 3:** Propone priorità intelligenti
```
"From weekly tasks, I see:
- Campaign sequences: 0% complete (CRITICAL - revenue)
- Drive cleanup: 30% complete (ongoing)
- MCP/n8n: 60% complete (need testing)

Today's prep suggests:
1. Campaign DM sequences (revenue priority)
2. MCP testing + Telegram bot
3. Drive cleanup progress

What are we working on today?"
```

**Step 4:** Tu rispondi e confermi (o cambi priorità)

**Token cost:** ~700 token (efficiente!)

---

## I 2 FILES CHIAVE

### 1. WEEKLY_TASKS.md (/task/)

**Cosa contiene:**
- Big 3 objectives della settimana
- Status di ogni obiettivo (%, pending work)
- Quick wins disponibili
- Completed items
- Next week preview
- Weekly metrics

**Chi lo aggiorna:**
- Tu (fine settimana, o quando cambiano priorità)
- Claude (può suggerire updates in closing summary)

**Quando leggere:**
- Domenica sera o lunedì mattina (pianifica settimana)
- Fine settimana (review progress)

**Frequenza update:** Weekly

---

### 2. prep-[date].md (/notes/daily-summaries/)

**Cosa contiene:**
- Top 3 priorità oggi (dettagliate)
- Context da ieri (completed + pending)
- Watch out for (blockers, attenzioni)
- Files da aprire
- Agent primario da usare
- Quick wins disponibili
- Expected outcomes

**Chi lo crea:**
- Tu ogni mattina (5 min) o sera prima
- Usa template: `prep-template.md`

**Quando leggere:**
- Ogni mattina prima di aprire Claude (quick review)

**Frequenza update:** Daily

---

## WORKFLOW COMPLETO

### Domenica Sera / Lunedì Mattina (15 min)

**1. Review settimana passata:**
```bash
# Leggi weekly tasks
cat task/WEEKLY_TASKS.md
```

**2. Update weekly tasks:**
- Move completed items to "✅ COMPLETED" section
- Update status % dei big objectives
- Add new objectives if needed
- Plan next week preview

**3. Crea primo prep della settimana:**
```bash
cp notes/daily-summaries/prep-template.md \
   notes/daily-summaries/prep-$(date +%d-%m-%y).md
```

**4. Compila top 3 priorità** basate su weekly objectives

---

### Ogni Mattina (5 min)

**1. Crea prep file di oggi:**
```bash
cp notes/daily-summaries/prep-template.md \
   notes/daily-summaries/prep-$(date +%d-%m-%y).md
```

**2. Compila velocemente:**
- Top 3 priorità (guarda weekly tasks per context)
- Context da ieri (leggi closing di ieri)
- Watch out for (blockers noti)
- Files che serviranno

**3. Apri Claude:**
```
Follow SESSION_START.md
```

---

### Durante Sessione (1-2h)

**Claude ha già tutto il context:**
- Big picture (weekly)
- Focus oggi (daily)
- Propone priorità intelligenti

**Tu confermi o modifichi:**
```
"Perfetto, partiamo con priority 1"
oppure
"Oggi cambiamo, facciamo invece X"
```

**Claude lavora con piena consapevolezza.**

---

### Fine Sessione (5 min)

**1. Closing summary:**
```
"Create closing summary"
```

**Claude crea:** `closing-[date].md` con:
- Cosa fatto
- Cosa rimasto pending
- Blockers trovati
- Next actions
- Suggerimenti per domani

**2. Update weekly tasks (opzionale):**
Se hai completato big objectives, aggiorna status in WEEKLY_TASKS.md

**3. Commit:**
```
"Propose commit"
[Review e approva]
```

---

## ESEMPI PRATICI

### Esempio 1: Lunedì Mattina

**WEEKLY_TASKS.md dice:**
```markdown
## BIG 3 OBJECTIVES THIS WEEK
1. Campaign sequences: 0% (CRITICAL)
2. Drive cleanup: 30% (ongoing)
3. MCP/n8n: 60% (testing needed)
```

**prep-27-11-25.md dice:**
```markdown
## Top 3 Priorità Oggi
1. Campaign DM sequences (start from 0%)
2. MCP testing
3. Drive cleanup (10 folders)
```

**Claude all'avvio propone:**
```
"This week's critical task is campaign sequences (revenue).
Today you're starting with DM creation - good priority.

Should we focus on:
1. Campaign sequences first (high revenue potential)
2. Then MCP testing (infrastructure)
3. Then drive cleanup (organization)

What are we working on today?"
```

**Tu:** "Sì, esatto quel ordine"

**Claude ha piena consapevolezza e può lavorare strategicamente.**

---

### Esempio 2: Mercoledì (Mid-Week)

**WEEKLY_TASKS.md aggiornato:**
```markdown
1. Campaign sequences: 60% ✅ (3 templates done, testing)
2. Drive cleanup: 45% 🔄 (progressing well)
3. MCP/n8n: 100% ✅ (tested, working!)
```

**prep-29-11-25.md:**
```markdown
## Top 3 Priorità Oggi
1. Test campaign sequences (first 20 prospects)
2. Finalize drive cleanup (target 70%)
3. Start next week planning
```

**Claude all'avvio:**
```
"Great progress this week:
- Campaign sequences ready for testing (60% → 100% today?)
- MCP fully working ✅
- Drive cleanup almost there (45% → 70%)

Today we're testing sequences and pushing cleanup to completion.
This could finish 2 of 3 big objectives!

What are we working on today?"
```

**Claude capisce momentum e può spingere per completare.**

---

## VANTAGGI DEL SISTEMA

### 1. Zero Spiegazioni Ripetute
**Prima:** "Allora, ieri stavamo lavorando su... e c'era anche quella cosa..."
**Adesso:** Claude già sa tutto, propone priorità intelligenti

### 2. Continuity Tra Sessioni
**Prima:** Ogni sessione ricominciava da zero
**Adesso:** Claude sa esattamente dove eravate rimasti

### 3. Big Picture Awareness
**Prima:** Focus solo su task immediato
**Adesso:** Claude capisce obiettivi settimanali e priorità strategiche

### 4. Intelligent Prioritization
**Prima:** Tu dovevi decidere tutto
**Adesso:** Claude propone basandosi su weekly + daily context

### 5. Progress Tracking
**Prima:** Nessuna memoria di % complete
**Adesso:** Weekly tasks mostra progress reale

### 6. Efficient Token Usage
**Prima:** Spiegazioni lunghe = 2K token startup
**Adesso:** Lettura strutturata = 700 token startup

---

## MAINTENANCE

### Weekly (15 min)
- [ ] Update WEEKLY_TASKS.md con progress
- [ ] Move completed items a "✅ COMPLETED"
- [ ] Plan next week objectives
- [ ] Create first prep of week

### Daily (5 min)
- [ ] Copy prep-template.md
- [ ] Fill top 3 priorities (look at weekly context)
- [ ] Add context from yesterday (read closing)
- [ ] List files needed

### Per Session (0 min)
- [ ] Just type: "Follow SESSION_START.md"
- [ ] Claude handles the rest

**Total overhead: 20 min/settimana + 5 min/giorno = ~55 min/settimana**

**ROI: Risparmio 10-20 min/sessione in spiegazioni = ~100-200 min/settimana**

**Net gain: 45-145 min/settimana**

---

## BEST PRACTICES

### Per Weekly Tasks

**DO ✅**
- Keep big 3 objectives focused (not 10)
- Update status % honestly
- Move completed to archive section
- Add context about blockers

**DON'T ❌**
- Make it too long (top 50 lines matter most)
- Add minor tasks (use daily prep for those)
- Forget to update (weekly review is key)
- Be vague on status (60% vs "almost done")

---

### Per Daily Prep

**DO ✅**
- Write top 3, not top 10
- Link to weekly objectives (context)
- Be specific on expected outcomes
- List actual file paths

**DON'T ❌**
- Write essay (bullet points win)
- Repeat info from weekly tasks
- Skip context from yesterday
- Be generic ("work on campaign" vs "create 3 DM sequences")

---

## TROUBLESHOOTING

### "Claude non propone priorità intelligenti"
→ Check che WEEKLY_TASKS.md sia aggiornato con status correnti

### "Claude propone task sbagliati"
→ Daily prep top 3 priorità sono chiare? Specifiche?

### "Claude legge troppi token all'avvio"
→ WEEKLY_TASKS troppo lungo? Solo top 50 righe contano
→ Daily prep troppo dettagliato? Max 30 righe contano

### "Non so cosa mettere in weekly vs daily"
→ Weekly = Big objectives, status %, big picture
→ Daily = Specific tasks oggi, files needed, sub-steps

### "Dimenticavo di aggiornare weekly tasks"
→ Set reminder: Domenica sera o lunedì mattina
→ Or: Claude può suggerire updates in closing summary

---

## FILES REFERENCE

**Sistema files:**
```
/task/
  └── WEEKLY_TASKS.md                    ← Big picture settimanale

/notes/daily-summaries/
  ├── prep-template.md                   ← Template per prep giornaliero
  ├── prep-27-11-25.md                   ← Prep di oggi
  ├── prep-28-11-25.md                   ← Prep di domani
  └── closing-27-11-25.md                ← Closing di oggi (created by Claude)

/docs/
  └── TASK_MEMORY_SYSTEM.md              ← Questo documento
```

**Automation (optional):**
```bash
# Crea alias per quick prep creation
alias newprep='cp notes/daily-summaries/prep-template.md notes/daily-summaries/prep-$(date +%d-%m-%y).md && nano notes/daily-summaries/prep-$(date +%d-%m-%y).md'

# Uso:
newprep
[Compili e salvi]
```

---

## NEXT LEVEL (Advanced)

### Auto-Update Weekly Tasks
Claude può auto-update WEEKLY_TASKS.md based on closing summaries:

```
"Update weekly tasks based on today's progress"

[Claude updates status %, moves completed items]
```

### Weekly Review Automation
Create script per weekly review:

```bash
#!/bin/bash
# weekly-review.sh

echo "=== WEEKLY REVIEW ==="
echo ""
echo "Last week completed:"
grep "✅" task/WEEKLY_TASKS.md | tail -10

echo ""
echo "This week pending:"
grep "⏳\|🔄" task/WEEKLY_TASKS.md

echo ""
echo "Update WEEKLY_TASKS.md now? (y/n)"
```

### Template Library
Create templates per recurring weekly objectives:

```
/templates/weekly-tasks/
  ├── growth-week-template.md
  ├── content-week-template.md
  └── infrastructure-week-template.md
```

---

## SUMMARY

**Il sistema in 3 punti:**

1. **WEEKLY_TASKS.md** = Memoria settimanale (big picture)
2. **prep-[date].md** = Focus giornaliero (cosa oggi)
3. **"Follow SESSION_START.md"** = Claude legge entrambi e propone

**Risultato:**
- Zero ripetizioni
- Context sempre presente
- Prioritization intelligente
- Token efficiency massima
- Continuity perfetta tra sessioni

**Tempo richiesto:**
- Setup iniziale: 30 min (fatto!)
- Weekly maintenance: 15 min
- Daily prep: 5 min
- **ROI: Positive da giorno 1**

---

**Ready to use. Il sistema è attivo da ora.**

**Next session: Scrivi "Follow SESSION_START.md" e vedrai la magia.** 🚀
