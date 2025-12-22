# Session Close

Esegui il protocollo di chiusura sessione:

## Step 1: Verifica naming
1. Controlla se esiste già `task/daily-summaries/closing-DDMMYY.md`
2. Se **non esiste** → usa `closing-DDMMYY.md`
3. Se **esiste** → usa `closing-DDMMYY-2.md` (o `-3`, `-4`... incrementa)
4. Se sessione ha topic specifico → usa `closing-DDMMYY-[topic].md` (es. `closing-221225-content-engine.md`)

## Step 2: Scrivi closing report
```markdown
# Closing DD-MM-YY

## TL;DR
- **Done**: [max 3 bullet]
- **Pending**: [max 3 bullet]
- **Next**: [1 riga - prossima azione]

## Dettagli

### Done
- [bullet con contesto breve]

### Pending
- [ ] [task] - [perché importante]

### Files
- [lista file creati/modificati]

### Notes
- [opzionale]

---
**Session Status**: Completed
**Prepared by**: Basilio
```

## Step 3: Aggiorna context (se necessario)
Aggiorna `brain/context.md` se ci sono:
- Nuove decisioni chiave
- Cambi status clienti
- Cose da ricordare

## Step 4: Conferma
Conferma all'utente: "Sessione chiusa. Report: [path]"

---

**REGOLE:**
- Max 30 righe totale
- NON chiedere conferma - scrivi direttamente
- Se multiple sessioni stesso giorno → Session Closer farà merge
