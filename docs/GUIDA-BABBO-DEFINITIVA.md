# Guida AI nel Terminale - Setup Completo

**Video di riferimento:** https://www.youtube.com/watch?v=MsQACpcuTkU
**Tempo totale:** ~30 minuti

---

## GLOSSARIO COMANDI TERMINALE

Prima di iniziare, ecco cosa significano i comandi che userai:

| Comando | Significato | Cosa fa |
|---------|-------------|---------|
| `cd` | **C**hange **D**irectory | Entra in una cartella |
| `cd ..` | | Torna indietro di una cartella |
| `mkdir` | **M**a**k**e **Dir**ectory | Crea una nuova cartella |
| `ls` | **L**i**s**t (Mac) | Mostra i file nella cartella |
| `dir` | **Dir**ectory (Windows) | Mostra i file nella cartella |
| `npm` | **N**ode **P**ackage **M**anager | Installa programmi |
| `exit` | | Esci dal programma |

### Simboli speciali

| Simbolo | Significato | Esempio |
|---------|-------------|---------|
| `~` | La tua cartella home (Mac) | `cd ~` = vai nella home |
| `%USERPROFILE%` | La tua cartella home (Windows) | `cd %USERPROFILE%` |
| `\` | Separatore cartelle (Windows) | `notes\daily-summaries` |
| `/` | Separatore cartelle (Mac) | `notes/daily-summaries` |

### Come leggere i comandi

```
cd %USERPROFILE%\workspace
│   │              │
│   │              └── nome della cartella
│   └── dove (la tua home)
└── azione (entra nella cartella)
```

---

## FASE 0: Installa Node.js

Node.js serve per far funzionare tutti gli strumenti AI.

1. Vai su **https://nodejs.org**
2. Clicca il bottone verde **"LTS"** (quello a sinistra)
3. Scarica e installa (Next, Next, Next...)
4. **Riavvia il computer**

### Verifica
Apri il terminale:
- **Windows**: Premi `Win + R`, scrivi `cmd`, premi Invio
- **Mac**: Cerca "Terminal" in Spotlight

Scrivi:
```
node --version
```

Se vedi un numero tipo `v20.x.x` = funziona!

---

## FASE 1: Gemini CLI (Gratis)

Gemini e' l'AI di Google. E' gratis e perfetto per iniziare.

### Installa
Nel terminale:
```
npm install -g @google/gemini-cli
```

### Crea cartella progetto

**WINDOWS:**
```
cd %USERPROFILE%
mkdir workspace
cd workspace
```

**MAC:**
```
cd ~
mkdir workspace
cd workspace
```

(Questo crea la cartella nella tua home directory)

### Avvia Gemini
```
gemini
```

Al primo avvio:
- Si apre il browser
- Fai login con il tuo account Google (anche Gmail va bene)
- Torna al terminale

### Prova!
Scrivi una domanda qualsiasi, tipo:
```
Come si fa il caffe perfetto?
```

### Il comando magico: /init
Scrivi:
```
/init
```

Gemini analizza la cartella e crea un file `gemini.md` con il contesto del progetto. Ogni volta che riapri Gemini in questa cartella, lui sa gia cosa stai facendo!

### Esci
Premi `Ctrl + C` oppure scrivi `exit`

---

## FASE 2: Claude Code (Richiede abbonamento)

Claude e' piu potente di Gemini. Costa $20/mese (Claude Pro) ma vale ogni centesimo.

### Installa
```
npm install -g @anthropic-ai/claude-code
```

### Avvia (nella stessa cartella)
Se hai chiuso il terminale, torna nella cartella:

**WINDOWS:** `cd %USERPROFILE%\workspace`
**MAC:** `cd ~/workspace`

Poi:
```
claude
```

Al primo avvio:
- Si apre il browser
- Fai login con il tuo account Anthropic (claude.ai)
- Torna al terminale

### Crea il contesto
```
/init
```

Claude crea `CLAUDE.md` - il suo file di contesto.

### Comandi utili
- `/context` - Vedi quanti token hai usato
- `/agents` - Gestisci gli agenti
- `Tab` - Attiva/disattiva "thinking mode"
- `Shift + Tab` - Cambia modalita (plan mode, etc.)

---

## FASE 3: Aggiungi i File Stratega

Questi file migliorano il sistema di Chuck. Te li passo separatamente.

### Struttura finale
```
workspace/
├── CLAUDE.md          (creato da /init)
├── gemini.md          (creato da /init)
├── brain/
│   └── context.md     (FILE CHE TI PASSO)
├── notes/
│   └── daily-summaries/
├── docs/
└── .claude/
    └── commands/
        ├── start.md   (FILE CHE TI PASSO)
        └── close.md   (FILE CHE TI PASSO)
```

### Crea le cartelle

**WINDOWS** (cmd):
```
mkdir brain
mkdir notes
mkdir notes\daily-summaries
mkdir docs
mkdir .claude
mkdir .claude\commands
```

**MAC** (terminal):
```
mkdir -p brain
mkdir -p notes/daily-summaries
mkdir -p docs
mkdir -p .claude/commands
```

### Metti i file
Copia i file che ti passo nelle cartelle giuste:
- `context.md` → dentro `brain/`
- `start.md` → dentro `.claude/commands/`
- `close.md` → dentro `.claude/commands/`

---

## FASE 4: Obsidian (Opzionale ma consigliato)

Obsidian ti fa vedere tutti i file in modo carino.

1. Vai su **https://obsidian.md**
2. Scarica e installa
3. Apri Obsidian
4. Clicca **"Open folder as vault"**
5. Seleziona la cartella `workspace`

Ora vedi tutti i file markdown in modo bello!

---

## COME USARLO OGNI GIORNO

### Mattina - Inizio lavoro

**WINDOWS:**
```
cd %USERPROFILE%\workspace
claude
```

**MAC:**
```
cd ~/workspace
claude
```

Poi scrivi:
```
/start
```

Claude legge il contesto e ti dice dove eri rimasto.

### Durante il giorno
Chiedi quello che vuoi:
- "Scrivimi una email per..."
- "Fammi un riassunto di..."
- "Organizza questi appunti..."

Claude puo creare file, modificarli, cercare sul web.

### Sera - Fine lavoro
```
/close
```

Claude salva un report di cosa hai fatto. La prossima volta sa da dove riprendere.

---

## COMANDI RAPIDI

| Comando | Cosa fa |
|---------|---------|
| `/start` | Inizia sessione, carica contesto |
| `/close` | Chiudi sessione, salva report |
| `/init` | Crea file di contesto |
| `/context` | Vedi token usati |
| `/help` | Aiuto |
| `Ctrl + C` | Interrompi |
| `exit` | Esci |

---

## RIASSUNTO COMANDI INSTALLAZIONE

### Tutti i sistemi
```
# Node.js: scarica da nodejs.org

# Gemini (gratis)
npm install -g @google/gemini-cli

# Claude (richiede Claude Pro)
npm install -g @anthropic-ai/claude-code
```

### Crea cartelle - WINDOWS
```
cd %USERPROFILE%
mkdir workspace
cd workspace
mkdir brain
mkdir notes
mkdir notes\daily-summaries
mkdir docs
mkdir .claude
mkdir .claude\commands
```

### Crea cartelle - MAC
```
cd ~
mkdir workspace
cd workspace
mkdir -p brain
mkdir -p notes/daily-summaries
mkdir -p docs
mkdir -p .claude/commands
```

---

## TROUBLESHOOTING

### "npm non trovato"
Node.js non installato. Reinstalla e riavvia il PC.

### "gemini/claude non trovato"
Chiudi e riapri il terminale.

### Claude non vede i file
Assicurati di essere nella cartella giusta:

**WINDOWS:** `cd %USERPROFILE%\workspace`
**MAC:** `cd ~/workspace`

### Obsidian non aggiorna
Clicca su un'altra nota e torna indietro.

---

## FILOSOFIA

Il bello di questo sistema:

1. **I tuoi dati sono tuoi** - Tutto e' nella cartella sul tuo PC
2. **Niente chat sparse** - Un progetto = una cartella
3. **Contesto persistente** - L'AI sa sempre cosa stai facendo
4. **Multi-AI** - Puoi usare Gemini E Claude nella stessa cartella

Come dice NetworkChuck: "I own my context. No vendor lock-in."

---

**Problemi? Chiama Matteo!**
