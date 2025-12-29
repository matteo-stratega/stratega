# 🎯 START HERE - Stratega OS Quick Start

**Benvenuto nel tuo sistema operativo per growth e business intelligence.**

---

## 📚 Documentazione Essenziale

### Per Te (Leggi Questi)

**1. STARTUP_QUICK_GUIDE.md** ← **Leggi prima di ogni sessione**
- Come avviare Claude in modo efficiente
- Step-by-step per startup perfetto
- Errori comuni da evitare
- **Tempo lettura: 3 minuti**

**2. CLAUDE_MANAGEMENT_GUIDE.md** ← **Leggi una volta, usa sempre**
- Best practices per gestire Claude
- Strategie di delega avanzate
- Token optimization tactics
- Troubleshooting & pattern library
- **Tempo lettura: 15 minuti**

**3. notes/daily-summaries/prep-template.md** ← **Usa ogni giorno**
- Template per prep file giornaliero
- Copia e compila ogni mattina
- **Tempo: 5 minuti/giorno**

---

## 🚀 Quick Start (Prima Sessione)

### Step 1: Setup Iniziale (una volta)
```bash
cd /Users/matteolombardi/AI-Projects/stratega

# Crea primo prep file
cp notes/daily-summaries/prep-template.md \
   notes/daily-summaries/prep-$(date +%d-%m-%y).md

# Compila top 3 priorità
nano notes/daily-summaries/prep-$(date +%d-%m-%y).md
```

### Step 2: Apri Claude Code
```bash
# Nel terminal o in Claude Code UI
# Scrivi solo:
Follow SESSION_START.md
```

### Step 3: Rispondi Conciso
Claude chiederà: "What are we working on today?"

**Rispondi in 3-5 righe:**
```
Oggi:
1. [Priority 1]
2. [Priority 2]
3. [Quick win]

Delega task heavy.
```

### Step 4: Lascia Lavorare
Claude farà tutto il resto:
- Carica solo file necessari
- Delega task pesanti
- Usa TodoWrite per tracking
- Propone commit a fine sessione

---

## 📋 Daily Routine

### Mattina (5 min)
```bash
# 1. Crea o aggiorna prep file
cp notes/daily-summaries/prep-template.md \
   notes/daily-summaries/prep-$(date +%d-%m-%y).md

# 2. Compila top 3 priorità (primi 30 righe)
# 3. Opzionale: leggi closing di ieri per context
```

### Durante Sessione (1-2h)
```
1. Apri Claude: "Follow SESSION_START.md"
2. Dai brief conciso (3-5 righe)
3. Lascia lavorare
4. Approva solo decisioni critiche
```

### Sera (5 min)
```
1. "Create closing summary and propose commit"
2. Review commit message
3. Approve push
4. Done
```

**Tempo totale overhead: 10-15 min/giorno**

---

## 🎓 Curva di Apprendimento

### Settimana 1: Basics
- [ ] Leggi STARTUP_QUICK_GUIDE.md
- [ ] Fai 3-5 sessioni con prep file
- [ ] Impara a dare brief concisi
- [ ] Lascia che Claude deleghi

**Goal:** Sessioni sotto 50K token

---

### Settimana 2: Optimization
- [ ] Leggi CLAUDE_MANAGEMENT_GUIDE.md
- [ ] Sperimenta con diversi agent
- [ ] Chiedi self-review a Claude
- [ ] Identifica pattern ricorrenti

**Goal:** Sessioni sotto 40K token

---

### Settimana 3: Mastery
- [ ] Crea template per task ricorrenti
- [ ] Usa delegation in parallelo
- [ ] Ottimizza prep file per tuo workflow
- [ ] Traccia metriche (token, quality, speed)

**Goal:** Sessioni sotto 35K token, max output

---

## 🛠 Files & Directories

### Root Directory
```
/Users/matteolombardi/AI-Projects/stratega/

├── START_HERE.md                  ← Questo file
├── STARTUP_QUICK_GUIDE.md         ← Leggi prima di ogni sessione
├── CLAUDE_MANAGEMENT_GUIDE.md     ← Best practices dettagliate
├── SESSION_START.md               ← Protocol (usato da Claude)
├── CLAUDE.md                      ← Router config (usato da Claude)
├── GEMINI.md                      ← Project config (usato da Claude)
│
├── agents/                        ← Agent definitions
│   ├── stratega-brain.md         (orchestratore)
│   ├── archivista.md             (organizer)
│   ├── content-engine.md         (writer)
│   ├── growth-hacker.md          (campaigns)
│   ├── esattore.md               (revenue)
│   └── archimede.md              (cto/code)
│
├── notes/                         ← Raw notes e thinking
│   └── daily-summaries/
│       ├── prep-template.md      ← Template giornaliero
│       ├── prep-[date].md        ← Prep files (create daily)
│       └── closing-[date].md     ← Closing (created by Claude)
│
├── docs/                          ← Final deliverables
├── research/                      ← Market analysis & ICPs
├── data/                          ← Datasets & CSV files
├── workflows/                     ← Operational processes
├── templates/                     ← Reusable frameworks
└── outputs/                       ← Generated content
```

---

## 🎯 Token Budget Guidelines

| Session Type | Target | Max | Notes |
|--------------|--------|-----|-------|
| **Startup** | 400-600 | 600 | Critical! |
| **Simple Task** | 5-10K | 15K | Direct work |
| **Complex Task** | 20-30K | 50K | With delegation |
| **Self-Review** | 20-30K | 40K | Periodic only |
| **Full Session** | 30-50K | 80K | Target zone |

**Se superi 80K → rivedi strategia**

---

## ⚡ Quick Wins

### Migliora Startup (5 min)
Ogni mattina aggiorna prep file top 3 priorità.
**Risultato:** Claude ha context immediato, zero token sprecati

### Usa TodoWrite (0 min)
Claude lo fa automatico su task complessi.
**Risultato:** Vedi progress live, migliore UX

### Delega Heavy Tasks (0 min)
Dì "delega task heavy" nel brief.
**Risultato:** 60-70% risparmio token

### Template per Task Ricorrenti (15 min setup)
Crea template in `/templates/` per task ripetitivi.
**Risultato:** Pay once, reuse forever

### Closing Summary Sempre (2 min)
Fine sessione: "Create closing summary"
**Risultato:** Memoria perfetta per domani

---

## 🆘 Troubleshooting

### "Non so come iniziare"
→ Apri STARTUP_QUICK_GUIDE.md, segui step by step

### "Claude legge troppi file"
→ Prep file troppo vago, sii più specifico nelle priorità

### "Sessione costa troppo"
→ Check: startup >600? Deleghi abbastanza? Report troppo lunghi?

### "Claude non capisce cosa voglio"
→ Brief più conciso e bullet points, evita rambling

### "Non so quale agent usare"
→ Vedi CLAUDE_MANAGEMENT_GUIDE.md sezione "Agent Disponibili"

---

## 📊 Success Metrics

**Settimana 1:**
- ✓ 5 sessioni completate
- ✓ Prep file usato ogni volta
- ✓ Startup <600 token

**Settimana 2:**
- ✓ Avg session <50K token
- ✓ Claude delega automaticamente
- ✓ TodoWrite usato su task complessi

**Settimana 3:**
- ✓ Avg session <40K token
- ✓ 1-2 commit/giorno
- ✓ Workflow fluido e naturale

**Mese 1:**
- ✓ ROI positivo (time saved vs cost)
- ✓ Template creati per task ricorrenti
- ✓ Zero sessioni >80K token

---

## 🎓 Resources

### Documentation
- **STARTUP_QUICK_GUIDE.md** - Quick reference per avvio sessione
- **CLAUDE_MANAGEMENT_GUIDE.md** - Guida completa gestione
- **SESSION_START.md** - Protocol per Claude (auto-loaded)
- **CLAUDE.md** - Repo overview & router logic
- **agents/*.md** - Agent definitions (load on demand)

### Templates
- **prep-template.md** - Daily prep file template
- **/templates/** - Task-specific templates (build over time)

### Learning
- **docs/SELF_REVIEW_*.md** - Self-reviews per learning
- **docs/SESSION_REPORT_*.md** - Session summaries
- **notes/daily-summaries/** - Daily memory

---

## 💡 Pro Tips

1. **Prep File è Oro** - 5 min al mattino valgono 30 min risparmiati
2. **Brief Conciso Vince** - 3-5 righe > 3-5 paragrafi
3. **Delega Aggressivamente** - Se >10K token → delega
4. **TodoWrite Sempre** - Su task complessi, no excuses
5. **Review Commit** - Mai auto-approve, sempre check
6. **Self-Review Periodico** - Ogni 5-10 sessioni per imparare
7. **Track Metrics** - Token usage trend rivela inefficienze
8. **Template Reuse** - Crea una volta, usa sempre
9. **Parallel Execution** - Task indipendenti → launch together
10. **Local Models** - Gemma/LLaMA per simple tasks = free

---

## 🚦 Your First Session Checklist

Pronto per iniziare? Segui questo:

- [ ] **Leggi** STARTUP_QUICK_GUIDE.md (3 min)
- [ ] **Crea** primo prep file da template (5 min)
- [ ] **Compila** top 3 priorità di oggi
- [ ] **Apri** Claude Code
- [ ] **Scrivi** "Follow SESSION_START.md"
- [ ] **Rispondi** in 3-5 righe cosa fare
- [ ] **Lascia lavorare** Claude
- [ ] **Fine sessione** chiedi closing summary
- [ ] **Review** e approva commit
- [ ] **Done!** 🎉

---

## 📞 Support

**Hai domande durante sessione?**
```
"Spiega [topic] da management guide"
[Claude ti aiuta]
```

**Vuoi migliorare il tuo workflow?**
```
"Analizza ultima sessione e proponi miglioramenti"
[Claude fa self-review]
```

**Serve help con agent specifico?**
```
"Come funziona Archivista?"
[Claude spiega e mostra esempi]
```

---

**Obiettivo Finale:** Workflow efficiente, zero friction, massima produttività.

**Remember:** Disciplina nel setup (10 min/day) = Velocità nell'execution (10x faster).

**Ready?** Apri STARTUP_QUICK_GUIDE.md e inizia la prima sessione.

---

**Version:** 1.0
**Last Updated:** 26 November 2025
**Maintainer:** Matteo Lombardi + Claude (Stratega Brain)
