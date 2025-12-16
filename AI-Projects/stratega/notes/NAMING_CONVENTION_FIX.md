# NAMING CONVENTION - DA SISTEMARE

**Data:** 4 Dicembre 2025
**Problema:** Naming inconsistente nei daily summaries

---

## Stato Attuale (CAOS)

```
closing-02-12-25.md          ← formato 1
session-closing-01-12-25.md  ← formato 2
closing-24-11-25.md          ← formato 1
prep-02-12-25.md             ← formato 3
session-start-02-12-25.md    ← formato 4
session-01-12-25-n8n.md      ← formato 5
```

---

## Standard Proposto

### Pattern Unico
```
{tipo}-{YYYY}-{MM}-{DD}.md
```

### Tipi Ammessi
- `prep-` → preparazione sessione
- `closing-` → chiusura sessione
- `session-` → note durante sessione (opzionale, con suffisso topic)

### Esempi Corretti
```
prep-2025-12-04.md
closing-2025-12-04.md
session-2025-12-04-n8n.md
```

### Perché YYYY-MM-DD?
- Ordinamento alfabetico = ordinamento cronologico
- Standard ISO 8601
- Niente ambiguità 02-12 vs 12-02

---

## Azione Richiesta

### Per Archivista
1. Rinominare tutti i file esistenti al nuovo formato
2. Aggiornare qualsiasi riferimento nei docs

### Per Session Closer
1. Usare SEMPRE il pattern `closing-YYYY-MM-DD.md`
2. Mai varianti tipo `session-closing-*`

### Per Stratega Brain
1. Quando crea prep/closing, usare il formato standard
2. Validare naming prima di salvare

---

## File da Rinominare

| Attuale | Nuovo |
|---------|-------|
| closing-02-12-25.md | closing-2025-12-02.md |
| closing-03-12-25.md | closing-2025-12-03.md |
| closing-24-11-25.md | closing-2025-11-24.md |
| closing-25-11-25.md | closing-2025-11-25.md |
| closing-26-11-25.md | closing-2025-11-26.md |
| closing-27-11-25.md | closing-2025-11-27.md |
| closing-28-11-25.md | closing-2025-11-28.md |
| session-closing-01-12-25.md | closing-2025-12-01.md |
| session-closing-02-12-25.md | (duplicato, merge o delete) |
| prep-02-12-25.md | prep-2025-12-02.md |
| prep-25-11-25.md | prep-2025-11-25.md |
| prep-26-11-25.md | prep-2025-11-26.md |
| prep-27-11-25.md | prep-2025-11-27.md |
| session-start-02-12-25.md | (merge in prep o delete) |
| session-01-12-25-n8n.md | session-2025-12-01-n8n.md |
| session-02-12-25.md | session-2025-12-02.md |

---

## Priorità: ALTA

Questo va fatto PRIMA della prossima sessione, altrimenti continua il caos.

---

*Segnalato da: Matteo*
*Per: Archivista, Session Closer, Stratega Brain*
