# Claude Code + Obsidian - Guida Completa Windows

**Per chi parte da zero. Passo per passo, con screenshot mentali.**

---

## PANORAMICA

Installeremo:
1. **Node.js** - serve per far funzionare Claude Code
2. **Claude Code** - l'assistente AI nel terminale
3. **Obsidian** - per vedere e organizzare tutti i file
4. **Git** - per tenere traccia delle modifiche (opzionale ma consigliato)

Tempo totale: ~15 minuti

---

# PARTE 1: INSTALLAZIONI

## 1.1 Installa Node.js

1. Vai su: **https://nodejs.org**
2. Clicca il bottone verde grande **"LTS"** (versione stabile)
3. Scarica il file `.msi`
4. Doppio click sul file scaricato
5. Clicca "Next" su tutto, accetta la licenza
6. **IMPORTANTE:** Quando chiede "Tools for Native Modules", metti la spunta!
7. Clicca Install, aspetta, Fine

### Verifica installazione
1. Premi `Win + R`
2. Scrivi `cmd` e premi Invio
3. Nel terminale nero scrivi:
```
node --version
```
4. Deve apparire qualcosa tipo `v20.10.0` (il numero puo' variare)

Se vedi il numero, Node e' installato!

---

## 1.2 Installa Git (Consigliato)

1. Vai su: **https://git-scm.com/download/win**
2. Scarica "64-bit Git for Windows Setup"
3. Doppio click, installa con opzioni di default
4. Clicca Next su tutto

### Verifica
Nel terminale (cmd):
```
git --version
```
Deve mostrare `git version 2.xx.x`

---

## 1.3 Installa Claude Code

1. Apri il terminale (cmd):
   - Premi `Win + R`
   - Scrivi `cmd`
   - Premi Invio

2. Scrivi questo comando e premi Invio:
```
npm install -g @anthropic-ai/claude-code
```

3. Aspetta che finisca (puo' volerci 1-2 minuti)

4. Verifica:
```
claude --version
```

---

## 1.4 Installa Obsidian

1. Vai su: **https://obsidian.md**
2. Clicca "Get Obsidian for Windows"
3. Scarica e installa
4. Apri Obsidian (non configurare ancora, lo facciamo dopo)

---

# PARTE 2: SETUP PROGETTO

## 2.1 Crea la Cartella Progetto

1. Apri **Esplora File** (icona cartella gialla nella barra)
2. Vai in `Documenti`
3. Click destro -> Nuova Cartella
4. Chiamala: `workspace` (o come preferisci)

---

## 2.2 Esegui Setup Automatico

1. Apri il terminale (cmd)
2. Vai nella cartella:
```
cd %USERPROFILE%\Documents\workspace
```

3. Copia e incolla TUTTO questo blocco e premi Invio:

```
mkdir brain && mkdir notes && mkdir notes\daily-summaries && mkdir docs && mkdir .claude && mkdir .claude\commands
```

4. Ora creiamo i file. Copia e incolla questo:

```
echo # CLAUDE.md > CLAUDE.md
```

Poi apri la cartella in Esplora File e continua con Obsidian (piu' facile).

---

## 2.3 Configura Obsidian

1. Apri **Obsidian**
2. Clicca **"Open folder as vault"**
3. Naviga fino a `Documenti\workspace`
4. Seleziona la cartella e clicca "Apri"

Ora vedi tutte le cartelle in Obsidian!

---

## 2.4 Crea i File di Configurazione

In Obsidian, crea questi file (click destro -> New note):

### File 1: `CLAUDE.md` (nella root)

```markdown
# CLAUDE.md

Istruzioni per Claude Code in questo progetto.

## Startup Protocol

All'avvio di ogni sessione:
1. Leggi `brain/context.md` per capire lo stato corrente
2. Leggi l'ultimo closing report in `notes/daily-summaries/` (se esiste)
3. Proponi le priorita e chiedi conferma

## Comandi

- `/start` - Inizia sessione di lavoro
- `/close` - Chiudi sessione con report

## Regole

1. Non inventare dati - Se non sai qualcosa, chiedi
2. Rispetta la struttura cartelle
3. Sii conciso - Risposte brevi
4. Aggiorna context.md a fine sessione

## Struttura

- brain/ - Stato e contesto
- notes/ - Appunti e note
- docs/ - Documenti finali
```

### File 2: `brain/context.md`

```markdown
# Context File

**Last Updated:** [DATA]

---

## Focus Corrente

### Questa Settimana
- [ ] Task 1
- [ ] Task 2
- [ ] Task 3

---

## Progetti Attivi

| Progetto | Status | Note |
|----------|--------|------|
| | | |

---

## Prossime Azioni

1.
2.
3.

---

*Aggiornare questo file a fine sessione*
```

### File 3: `.claude/commands/start.md`

```markdown
# Session Start

Esegui il protocollo di inizio sessione:

## Step 1: Load Context
1. Leggi brain/context.md
2. Leggi ultimo file notes/daily-summaries/closing-*.md

## Step 2: Propose
Riassumi in max 5 bullet:
- Cosa fatto ultima sessione
- Cosa pending
- Focus corrente

Poi chiedi: "Confermi queste priorita o cambiamo?"

## Step 3: STOP
Aspetta risposta prima di procedere.
```

### File 4: `.claude/commands/close.md`

```markdown
# Session Close

1. Scrivi closing report in notes/daily-summaries/closing-DDMMYYYY.md:

# Closing [DATA]

## TL;DR
- Done: [completato]
- Pending: [da fare]
- Next: [prossima azione]

## Files Modified
[lista]

---
Session Status: Completed

2. Aggiorna brain/context.md se necessario

3. Conferma: "Sessione chiusa. Report salvato."
```

---

# PARTE 3: PRIMO AVVIO

## 3.1 Avvia Claude Code

1. Apri terminale (cmd)
2. Vai nella cartella:
```
cd %USERPROFILE%\Documents\workspace
```

3. Avvia Claude:
```
claude
```

4. Al primo avvio ti chiede di fare login:
   - Si apre il browser
   - Fai login con il tuo account Anthropic
   - Torna al terminale

5. Scrivi:
```
/start
```

**Sei operativo!**

---

# PARTE 4: USO QUOTIDIANO

## Workflow Giornaliero

### Mattina - Inizio Lavoro
1. Apri terminale
2. `cd %USERPROFILE%\Documents\workspace`
3. `claude`
4. `/start`
5. Claude ti dice cosa c'e' da fare
6. Confermi o cambi priorita

### Durante il Giorno
- Chiedi a Claude quello che ti serve
- Lui puo' creare file, modificarli, organizzare
- Tu puoi vedere tutto in Obsidian in tempo reale

### Sera - Fine Lavoro
- Scrivi `/close`
- Claude salva un report di cosa hai fatto
- La prossima volta sa da dove riprendere

---

## Comandi Utili

| Comando | Cosa Fa |
|---------|---------|
| `/start` | Inizia sessione |
| `/close` | Chiudi e salva |
| `/help` | Mostra aiuto |
| `/clear` | Pulisce la chat |
| `Ctrl+C` | Interrompe Claude |
| `exit` | Esci da Claude |

---

## Obsidian Tips

- **Ctrl+P**: Cerca comandi
- **Ctrl+O**: Apri file veloce
- **Ctrl+N**: Nuovo file
- I file `.md` sono semplice testo, puoi aprirli con qualsiasi editor

---

# TROUBLESHOOTING

## "npm non riconosciuto"
Node.js non installato correttamente. Reinstalla e riavvia il PC.

## "claude non riconosciuto"
Chiudi e riapri il terminale. Se non funziona:
```
npm install -g @anthropic-ai/claude-code
```

## Claude non vede i file
Assicurati di essere nella cartella giusta:
```
cd %USERPROFILE%\Documents\workspace
dir
```
Devi vedere CLAUDE.md nella lista.

## Obsidian non vede le modifiche di Claude
Clicca su un'altra cartella e torna. Oppure premi F5.

---

# SHORTCUTS DA RICORDARE

```
Win + R, poi "cmd"     -> Apre terminale
cd Documents\workspace -> Va nella cartella
claude                 -> Avvia Claude
/start                 -> Inizia sessione
/close                 -> Chiudi sessione
```

---

**Problemi? Chiama Matteo!**
