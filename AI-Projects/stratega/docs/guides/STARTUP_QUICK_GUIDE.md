# 🚀 STRATEGA OS - STARTUP QUICK GUIDE
**Come avviare una sessione con Claude in modo efficiente**

---

## STEP 1: Prepara Daily Summary (5 min)

**Se inizio giornata:**
```bash
# Crea nuovo prep file
touch notes/daily-summaries/prep-$(date +%d-%m-%y).md
```

**Template essenziale (max 100 righe):**
```markdown
# Daily Prep: [Data]

## Top 3 Priorità Oggi
1. [Task principale]
2. [Task secondario]
3. [Quick win]

## Context da Ieri (5 righe max)
- Cosa fatto
- Cosa rimasto in sospeso

## Watch Out For
- [Blockers]
- [Cose da non dimenticare]

## Files da Aprire
1. [path assoluto]
2. [path assoluto]
```

---

## STEP 2: Apri Claude Code

**Messaggio di avvio:**
```
Follow SESSION_START.md
```

**Claude farà:**
1. Legge solo top 30 righe del tuo prep file
2. Chiede: "What are we working on today?"
3. Si ferma e aspetta la tua risposta

**Budget token startup: MAX 600 token**

---

## STEP 3: Rispondi alla Domanda

**Buona risposta (concisa):**
```
"Oggi lavoriamo su:
1. Correggere transcript scuola
2. Organizzare academy hub
3. Review del lavoro fatto

Focus su deleghe per risparmiare token."
```

**Cattiva risposta (troppo lunga):**
```
"Allora, oggi vorrei che tu lavorassi sui transcript
della scuola che si trovano in questa cartella e poi
dobbiamo anche organizzare tutto l'hub dell'academy
perché è un po' in disordine e..."
[Claude brucerà 2K token solo per processare questo]
```

**Regola:** 3-5 righe MAX, bullet points preferiti

---

## STEP 4: Lascia Lavorare Claude

**Claude caricherà solo files necessari:**
- Working on MRR? → agents/esattore.md
- Working on code? → agents/archimede.md
- Working on content? → agents/content-engine.md
- Working on growth? → agents/growth-hacker.md
- Working on org? → agents/archivista.md

**Non dire a Claude cosa leggere** - lo sa già.

---

## STEP 5: Fine Sessione

**Quando finito:**
```
"Fatto. Crea closing summary e commita."
```

**Claude farà:**
1. Crea closing-[data].md
2. Propone commit con summary
3. Chiede approval per push

**Approva o modifica il commit**, poi fine.

---

## ⚠️ ERRORI COMUNI DA EVITARE

### ❌ NON FARE:

**1. Messaggi troppo lunghi all'inizio**
```
"Ciao Claude! Allora oggi volevo che lavorassimo
su questi file che ho qui nella cartella..."
[500 token sprecati]
```

**2. Chiedere di leggere file inutili**
```
"Prima leggi CLAUDE.md, poi GEMINI.md, poi..."
[Claude li conosce già]
```

**3. Dare troppe istruzioni insieme**
```
"Fai A, poi B, ma prima controlla C, e se vedi D..."
[Confusione garantita]
```

**4. Non usare il prep file**
```
[Spieghi tutto a voce ogni volta]
[Claude deve processare da zero ogni volta]
```

### ✅ FARE:

**1. Messaggio conciso**
```
"Follow SESSION_START.md"
[Claude sa cosa fare]
```

**2. Risposta bullet points**
```
"Oggi:
1. Task A
2. Task B
3. Task C"
[Chiaro e scannable]
```

**3. Prep file aggiornato**
```
[Claude legge top 30 righe e ha tutto il contesto]
```

**4. Una task alla volta**
```
"Prima A, quando finito ti dico B"
[Chiaro e sequenziale]
```

---

## 🎯 BEST PRACTICES

### Daily Prep File
- **Scrivi la sera prima** o al mattino presto
- **Max 100 righe** (Claude legge solo top 30)
- **Top 3 priorità** sempre visibili in alto
- **Files con path assoluti** (no relativi)

### Durante la Sessione
- **Un task alla volta** - non stack multipli
- **Lascia delegare** - Claude sa quando usare altri agent
- **Conferma i commit** - mai auto-push
- **Chiedi self-review** - ogni tanto per migliorare

### Fine Sessione
- **Closing summary** - sempre
- **Commit con message chiaro** - descrive il lavoro
- **Prep per domani** - se hai 2 min

---

## 📊 TOKEN BUDGET GUIDELINES

| Fase | Budget | Note |
|------|--------|------|
| Startup | 600 | Follow SESSION_START |
| Task Simple | 5-10K | Direct work |
| Task Complex | 20-30K | Con deleghe |
| Self-Review | 20-30K | Solo se richiesto |
| **Target Sessione** | **30-50K** | Con deleghe |

**Se superi 80K token → troppo, rivedi strategia**

---

## 🔧 TROUBLESHOOTING

### "Claude legge troppi file"
→ Prep file troppo generico, sii più specifico

### "Claude non delega"
→ Digli esplicitamente: "Delega task heavy, risparmia token"

### "Sessione costa troppi token"
→ Check: startup >600? Report troppo lunghi? File inutili letti?

### "Claude non usa TodoWrite"
→ Digli: "Usa TodoWrite per tracking" all'inizio del task

### "Non so che task dargli"
→ Leggi il tuo prep file, top 3 priorità

---

## 📁 FILES CHIAVE

**Per te (da leggere):**
- `STARTUP_QUICK_GUIDE.md` ← Questo file
- `CLAUDE_MANAGEMENT_GUIDE.md` ← Best practices dettagliate
- `notes/daily-summaries/prep-*.md` ← Il tuo prep giornaliero

**Per Claude (carica automaticamente):**
- `SESSION_START.md` ← Protocol startup
- `CLAUDE.md` ← Router & repo overview
- `agents/*.md` ← Agent definitions (load on demand)

---

## ⚡ QUICK REFERENCE

**Avvio sessione:**
```
1. Aggiorna prep file (5 min)
2. Apri Claude: "Follow SESSION_START.md"
3. Rispondi in 3-5 righe cosa fare oggi
4. Let it work
```

**Fine sessione:**
```
1. "Crea closing summary"
2. Review commit message
3. Approva push
4. Done
```

**Tempo totale overhead: 10 minuti/giorno**

---

**Obiettivo:** Sessioni efficienti, zero token sprecati, massima produttività.

**Remember:** Claude è uno strumento potente, ma va guidato con disciplina.
