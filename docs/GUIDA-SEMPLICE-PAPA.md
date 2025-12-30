# Claude Code - Guida per Non Tecnici

**3 passi e sei operativo.**

---

## PASSO 1: Installa Claude Code

Apri il **Terminale** (cerca "Terminal" in Spotlight) e copia-incolla questo comando:

```
npm install -g @anthropic-ai/claude-code
```

Premi Invio. Aspetta che finisca.

> **Errore "npm not found"?**
> Prima devi installare Node.js: vai su https://nodejs.org e scarica la versione LTS.
> Installa, poi riprova il comando sopra.

---

## PASSO 2: Esegui lo Script di Setup

Scarica questo file e salvalo sul Desktop:
**setup.sh** (te lo mando io)

Poi nel Terminale scrivi:

```
bash ~/Desktop/setup.sh
```

Lo script ti chiede come chiamare il progetto. Scrivi un nome (es: "lavoro") e premi Invio.

**Fatto!** Lo script crea tutto automaticamente.

---

## PASSO 3: Avvia Claude

Nel Terminale:

```
cd ~/lavoro
claude
```

(sostituisci "lavoro" con il nome che hai scelto)

Al primo avvio ti chiede di fare login con il tuo account Anthropic.

---

## Come Usarlo

### Inizia sessione
Quando apri Claude, scrivi:
```
/start
```
Claude legge cosa stavi facendo e ti propone le priorita'.

### Chiudi sessione
Quando hai finito, scrivi:
```
/close
```
Claude salva un report di cosa hai fatto.

### Chiedere aiuto
Scrivi semplicemente cosa vuoi fare in italiano:
- "Scrivimi una email per..."
- "Organizza questi appunti..."
- "Fammi un riassunto di..."

---

## Struttura del Progetto

Dopo il setup avrai questa struttura:

```
lavoro/
├── brain/context.md      <- Qui c'e' lo stato del progetto
├── notes/                <- Qui vanno le note
├── docs/                 <- Qui i documenti finali
└── CLAUDE.md             <- Istruzioni per Claude
```

---

## Comandi Utili

| Cosa vuoi fare | Comando |
|----------------|---------|
| Iniziare sessione | `/start` |
| Chiudere sessione | `/close` |
| Vedere aiuto | `/help` |
| Pulire chat | `/clear` |
| Uscire | `Ctrl+C` oppure scrivi "exit" |

---

## Problemi Comuni

### "command not found: claude"
Claude Code non e' installato. Ripeti il Passo 1.

### "command not found: npm"
Node.js non e' installato. Vai su https://nodejs.org e installa.

### Claude non risponde
Premi Ctrl+C per interrompere, poi scrivi `claude` per riavviare.

### Ho chiuso il terminale, come riapro?
```
cd ~/lavoro
claude
```

---

## Aggiornare Claude Code

Ogni tanto esce una nuova versione. Per aggiornare:

```
npm update -g @anthropic-ai/claude-code
```

---

**Hai problemi? Chiama Matteo!**
