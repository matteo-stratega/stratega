# Session Close

Esegui il protocollo di chiusura sessione:

## Step 1: Verifica file esistente
1. Controlla se esiste `task/daily-summaries/closing-DDMMYY.md`
2. Se **non esiste** → crealo con header e il tuo report
3. Se **esiste** → APPEND il tuo report sotto (come nuovo capitolo)

**IMPORTANTE:** NON creare file con `-2`, `-3`. Sempre APPEND allo stesso file del giorno.

## Step 2: Formato report

### Se file NON esiste (prima sessione del giorno):
```markdown
# Closing DD-MM-YY

---

## Session 1: [HH:MM] - [Topic/Agent]

### TL;DR
- **Done**: [max 3 bullet]
- **Pending**: [max 3 bullet]

### Files
- [lista file creati/modificati]

---
**Agent**: Basilio
```

### Se file ESISTE (append al fondo):
```markdown

---

## Session N: [HH:MM] - [Topic/Agent]

### TL;DR
- **Done**: [max 3 bullet]
- **Pending**: [max 3 bullet]

### Files
- [lista file creati/modificati]

---
**Agent**: [Nome agente]
```

## Step 3: Aggiorna context (se necessario)
Aggiorna `brain/context.md` se ci sono:
- Nuove decisioni chiave
- Cambi status clienti
- Cose da ricordare

## Step 4: Conferma
Conferma: "Sessione chiusa. Report appeso a: [path]"

---

**REGOLE:**
- SEMPRE append, MAI file separati per stesso giorno
- Session Closer farà merge finale a fine giornata
- Max 20 righe per sessione
- NON chiedere conferma - scrivi/appendi direttamente
