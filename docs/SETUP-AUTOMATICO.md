# SETUP AUTOMATICO - LEGGI QUESTO FILE

Ciao Claude! L'utente ha appena installato Claude Code e vuole configurare il workspace.

**FAI TU TUTTO. L'utente non e' tecnico.**

## Cosa Devi Fare

1. **Crea queste cartelle:**
   - `brain/`
   - `notes/daily-summaries/`
   - `docs/`
   - `.claude/commands/`

2. **Crea il file `CLAUDE.md`** nella root con questo contenuto:

```markdown
# CLAUDE.md

## Startup
All'avvio leggi brain/context.md e l'ultimo closing in notes/daily-summaries/

## Comandi
- /start - Inizia sessione
- /close - Chiudi con report

## Regole
1. Non inventare dati
2. Sii conciso
3. Aggiorna context.md a fine sessione
```

3. **Crea `brain/context.md`:**

```markdown
# Context

**Updated:** [oggi]

## Questa Settimana
- [ ] Task 1
- [ ] Task 2

## Progetti
| Progetto | Status |
|----------|--------|
| | |

## Prossime Azioni
1.
2.
```

4. **Crea `.claude/commands/start.md`:**

```markdown
# Session Start

1. Leggi brain/context.md
2. Leggi ultimo notes/daily-summaries/closing-*.md
3. Riassumi in 5 bullet: fatto, pending, focus
4. Chiedi: "Confermi o cambiamo?"
5. STOP - aspetta risposta
```

5. **Crea `.claude/commands/close.md`:**

```markdown
# Session Close

1. Crea notes/daily-summaries/closing-DDMMYYYY.md con:
   - Done: [fatto]
   - Pending: [da fare]
   - Next: [prossimo]
2. Aggiorna brain/context.md
3. Conferma all'utente
```

6. **Dopo aver creato tutto**, spiega all'utente:
   - "Ho configurato tutto!"
   - "Da ora in poi usa /start per iniziare e /close per finire"
   - "Puoi vedere tutti i file in Obsidian aprendo questa cartella come vault"

7. **Cancella questo file** (SETUP-AUTOMATICO.md) perche' non serve piu'

---

## NOTE PER CLAUDE

- L'utente potrebbe non sapere nulla di terminale/coding
- Sii paziente e chiaro
- Dopo il setup, chiedi se vuole fare un test con /start
- Se qualcosa non funziona, spiega passo passo
