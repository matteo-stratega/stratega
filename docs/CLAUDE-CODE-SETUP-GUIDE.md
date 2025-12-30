# Guida Setup Claude Code - Sistema Completo

**Versione:** 1.0
**Data:** 29 Dicembre 2025
**Per:** Setup nuovo workspace con architettura Stratega

---

## Indice

1. [Installazione Claude Code](#1-installazione-claude-code)
2. [Creare il Progetto](#2-creare-il-progetto)
3. [Struttura Cartelle](#3-struttura-cartelle)
4. [CLAUDE.md - Il Cervello](#4-claudemd---il-cervello)
5. [Context File](#5-context-file)
6. [Comandi Personalizzati](#6-comandi-personalizzati)
7. [Agents (Opzionale)](#7-agents-opzionale)
8. [Best Practices](#8-best-practices)
9. [Troubleshooting](#9-troubleshooting)

---

## 1. Installazione Claude Code

### Prerequisiti
- macOS, Windows o Linux
- Node.js 18+ installato
- Account Anthropic con API key (oppure account Claude Pro/Max)

### Installazione

```bash
# Installa Claude Code globalmente
npm install -g @anthropic-ai/claude-code

# Verifica installazione
claude --version
```

### Primo Avvio

```bash
# Vai nella cartella del tuo progetto
cd /percorso/al/tuo/progetto

# Avvia Claude Code
claude
```

Al primo avvio ti chiederà di autenticarti con il tuo account Anthropic.

---

## 2. Creare il Progetto

### Struttura Base

```bash
# Crea la cartella principale del progetto
mkdir mio-progetto
cd mio-progetto

# Inizializza git (importante!)
git init

# Crea la struttura base
mkdir -p brain
mkdir -p notes/daily-summaries
mkdir -p docs
mkdir -p .claude/commands
```

**IMPORTANTE:** Il repository git DEVE essere nella cartella del progetto, NON nella home directory. Questo evita che Claude Code mescoli file di progetti diversi.

---

## 3. Struttura Cartelle

Ecco la struttura raccomandata:

```
mio-progetto/
├── .claude/              # Configurazione Claude Code
│   ├── commands/         # Comandi personalizzati (/start, /close)
│   └── settings.json     # Settings locali (opzionale)
├── brain/                # Stato e memoria
│   └── context.md        # File di contesto persistente
├── notes/                # Note e appunti
│   └── daily-summaries/  # Report giornalieri
├── docs/                 # Documenti finali
├── agents/               # Definizioni agenti (opzionale)
├── CLAUDE.md             # Istruzioni principali per Claude
└── .gitignore
```

### Cosa va dove

| Cartella | Contenuto |
|----------|-----------|
| `brain/` | Stato corrente, priorità, decisioni chiave |
| `notes/` | Appunti, brainstorming, note grezze |
| `docs/` | Documenti finali e polished |
| `agents/` | Definizioni di "personalità" specializzate |
| `.claude/commands/` | Comandi custom tipo `/start` |

---

## 4. CLAUDE.md - Il Cervello

Crea il file `CLAUDE.md` nella root del progetto. Questo file viene letto AUTOMATICAMENTE da Claude Code all'avvio.

### Template Base

```markdown
# CLAUDE.md

Istruzioni per Claude Code in questo progetto.

## Startup Protocol
All'avvio di ogni sessione:
1. Leggi `brain/context.md` per capire lo stato corrente
2. Chiedi cosa vuole fare l'utente oggi

## Regole Generali

1. **Non inventare dati** - Se non sai qualcosa, chiedi
2. **Rispetta la struttura cartelle** - Ogni file al suo posto
3. **Esegui in autonomia** - Chiedi solo se mancano info critiche
4. **Sii conciso** - Risposte brevi e actionable

## Struttura Progetto

```
mio-progetto/
├── brain/           # Stato e contesto
├── notes/           # Note e appunti
├── docs/            # Documenti finali
└── .claude/         # Config Claude Code
```

## Comandi Personalizzati

- `/start` - Inizia sessione di lavoro
- `/close` - Chiudi sessione con report

## Stile Output

- Usa markdown per formattare
- Bullet points per liste
- Niente emoji (a meno che non richiesto)
- Vai dritto al punto
```

### CLAUDE.md Avanzato (esempio completo)

Se vuoi un sistema più sofisticato, ecco un esempio più completo:

```markdown
# CLAUDE.md

## Router
On startup:
- Read `brain/context.md` for current state
- Follow session protocol

## Session Commands
- `/start` - Automatic session start
- `/close` - Automatic session close with report

## Token Budget
- **Startup**: 500-700 tokens MAX
- **Session total**: 25-35K tokens target

## Cose da NON Fare
1. No hallucinated data
2. No loading files "just in case"
3. No over-engineering

## Output Style
- Clear, structured formatting
- Prioritize execution over theory
- No motivational fluff
```

---

## 5. Context File

Crea `brain/context.md` - questo file mantiene lo stato tra le sessioni.

### Template

```markdown
# Context File

**Last Updated:** [data]

---

## Focus Corrente

### Questa Settimana
- [ ] Task 1
- [ ] Task 2
- [ ] Task 3

### Progetti Attivi

| Progetto | Status | Note |
|----------|--------|------|
| Progetto A | In corso | Descrizione breve |
| Progetto B | In pausa | Motivo |

---

## Decisioni Chiave

| Data | Decisione | Motivazione |
|------|-----------|-------------|
| 29/12 | Esempio | Perché |

---

## Prossime Azioni

1. Azione prioritaria 1
2. Azione prioritaria 2

---

*Aggiornare questo file a fine sessione*
```

---

## 6. Comandi Personalizzati

I comandi personalizzati permettono di automatizzare workflow ricorrenti.

### Creare il comando /start

Crea file `.claude/commands/start.md`:

```markdown
# Session Start

Esegui il protocollo di inizio sessione:

## Step 1: Load Context
1. Leggi `brain/context.md`
2. Leggi l'ultimo file in `notes/daily-summaries/closing-*.md` (se esiste)

## Step 2: Propose
Riassumi in max 5 bullet points:
- Cosa è stato fatto nell'ultima sessione
- Cosa è pending
- Focus corrente

Poi chiedi: **"Confermi queste priorità o cambiamo?"**

## Step 3: STOP
Aspetta risposta prima di procedere.
```

### Creare il comando /close

Crea file `.claude/commands/close.md`:

```markdown
# Session Close

Esegui il protocollo di chiusura:

1. **Scrivi closing report** in `notes/daily-summaries/closing-DDMMYYYY.md`:

```
# Closing [DATA]

## TL;DR
- **Done**: [cosa completato]
- **Pending**: [cosa rimane]
- **Next**: [prossima azione]

## Files Created/Modified
[lista file]

---
**Session Status**: Completed
```

2. **Aggiorna brain/context.md** se ci sono:
   - Nuove decisioni
   - Cambi di status
   - Cose da ricordare

3. **Conferma** all'utente: "Sessione chiusa. Report salvato."
```

### Come usare i comandi

```
> /start
[Claude esegue il protocollo di start]

> /close
[Claude esegue il protocollo di close]
```

---

## 7. Agents (Opzionale)

Gli "agents" sono personalità specializzate che Claude può assumere per task specifici.

### Struttura

```
agents/
├── writer.md        # Per scrittura e copy
├── analyst.md       # Per analisi dati
└── planner.md       # Per pianificazione
```

### Template Agent

Crea `agents/writer.md`:

```markdown
# Agent: Writer

## Identity
Sei un copywriter esperto. Il tuo focus è produrre testi chiari, persuasivi e ben strutturati.

## Style
- Frasi brevi e incisive
- Evita gergo tecnico
- Usa la voce attiva
- Vai dritto al punto

## When Called
Quando l'utente dice "chiama writer" o "call writer", assumi questa identità.

## Workflow
1. Chiedi il brief se non fornito
2. Proponi una struttura
3. Scrivi il draft
4. Chiedi feedback
```

### Come usare gli agents

Aggiungi in CLAUDE.md:

```markdown
## Agent Routing

Quando l'utente dice "chiama [nome]" o "call [nome]":
1. Cerca il file `agents/[nome].md`
2. Leggi le istruzioni
3. Assumi quella identità
```

---

## 8. Best Practices

### DO (Fare)

1. **Inizia sempre con /start** - Carica il contesto
2. **Chiudi sempre con /close** - Salva il progresso
3. **Aggiorna context.md** - Mantieni lo stato aggiornato
4. **Commit frequenti** - Traccia le modifiche con git
5. **Un progetto = una cartella** - Mai mischiare progetti

### DON'T (Non fare)

1. **Mai git init nella home** - Crea confusione totale
2. **Mai caricare file grandi interi** - Prima sample, poi chiedi
3. **Mai inventare dati** - Chiedi sempre se non sai
4. **Mai sessioni troppo lunghe** - Chiudi e riapri ogni 2-3 ore

### Token Efficiency

Claude Code ha un budget di token. Per ottimizzarlo:

- **Sii specifico** nelle richieste
- **Non chiedere "leggi tutto"** - Specifica cosa serve
- **Usa comandi brevi** - `/start` invece di spiegazioni lunghe
- **Chiudi sessioni lunghe** - Il context si accumula

---

## 9. Troubleshooting

### "Claude non trova i file"

```bash
# Verifica di essere nella cartella giusta
pwd

# Verifica che CLAUDE.md esista
ls -la CLAUDE.md
```

### "I comandi /start non funzionano"

```bash
# Verifica struttura
ls -la .claude/commands/

# Il file deve chiamarsi esattamente start.md (lowercase)
```

### "Claude mescola progetti diversi"

Il repository git è probabilmente nella home. Fix:

```bash
# Verifica dove è .git
git rev-parse --show-toplevel

# Se è nella home, rimuovilo e ricrea nel progetto
```

### "Claude dimentica il contesto"

- Assicurati che `brain/context.md` sia aggiornato
- Usa `/start` all'inizio di ogni sessione
- Usa `/close` alla fine per salvare lo stato

---

## Quick Start Checklist

```
[ ] Installato Claude Code (npm install -g @anthropic-ai/claude-code)
[ ] Creata cartella progetto
[ ] Inizializzato git NELLA cartella progetto
[ ] Creato CLAUDE.md
[ ] Creato brain/context.md
[ ] Creato .claude/commands/start.md
[ ] Creato .claude/commands/close.md
[ ] Testato con `claude` + `/start`
```

---

## Comandi Utili

```bash
# Avviare Claude Code
claude

# Vedere versione
claude --version

# Help
claude --help
```

Dentro Claude Code:
```
/start          # Inizia sessione
/close          # Chiudi sessione
/help           # Aiuto
/clear          # Pulisci conversazione
```

---

*Guida creata il 29/12/2025 - Basata sull'architettura Stratega OS*
