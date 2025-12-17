# Content Workflow - Alex Ferretti

**Quando chiamare questo workflow:** Ogni volta che devi scrivere contenuto (blog, LinkedIn, welcome post)

---

## Workflow: Blog Article

### Input richiesto
- Topic/titolo
- Lunghezza target (default: 800-1200 parole)
- Lingua (IT/EN o entrambe)
- Deadline

### Steps

```
1. RICERCA (se necessario)
   └─ Task tool con Explore agent per dati/fonti
   └─ Output: bullet points con fonti

2. DRAFT
   └─ Leggi agents/copywriter-personality.md
   └─ Scrivi in voce Alex
   └─ Salva come [DRAFT] filename.md

3. ROAST
   └─ Task tool con prompt:
      "Sei un editor critico. Valuta questo articolo 1-10:
       - Voice consistency (suona come Alex?)
       - AI tells (parole/frasi bannate?)
       - Structure (hook, flow, CTA)
       - Dai feedback specifico per migliorare"
   └─ Target: 8.5/10 minimo

4. ITERATE
   └─ Se <8.5: applica feedback, torna a step 3
   └─ Se ≥8.5: procedi

5. TRANSLATE (se richiesto)
   └─ NON tradurre letteralmente
   └─ Riscrivi come lo diresti a voce
   └─ Anglicismi OK: venue, F&B, dashboard, checkout, staff
   └─ Anglicismi da tradurre: churn, revenue

6. FINAL ROAST (Italian)
   └─ Task tool: "Valuta traduzione italiana 1-10"
   └─ Target: 8/10 minimo

7. PUBLISH READY
   └─ Rinomina [DRAFT] → [READY]
   └─ Aggiorna calendario
```

### Banned Words (hardcoded)
```
delve, realm, harness, unlock, tapestry, paradigm,
cutting-edge, revolutionize, landscape, potential,
findings, leverage, synergy, innovative, game-changer
```

### Banned Phrases
```
"Welcome to [problem]"
"In today's fast-paced world"
"Translation:"
"The 2026 reality:"
"Picture this:" (max 1x per 6 articoli)
"The pattern is clear:"
```

---

## Workflow: LinkedIn Post

### Steps
```
1. Identifica hook (prima riga, before "see more")
2. Max 200 parole
3. Engagement prompt alla fine
4. Hashtag: max 4
5. Link con UTM: ?utm_source=linkedin&utm_campaign=[campaign]
```

---

## Workflow: Welcome Post

### Steps
```
1. Verifica risposte questionario
2. Q&A format (Option A)
3. Pull quote migliore per LinkedIn
4. Verifica ruolo corretto (es. Asim = dev, NON lead)
```

---

## Quality Gates

| Gate | Minimum | Action if fail |
|------|---------|----------------|
| Roast score | 8.5/10 | Iterate |
| Italian roast | 8.0/10 | Rewrite |
| Banned words | 0 | Auto-fix |
| Word count | ±10% target | Adjust |

---

## Output Locations

- Drafts: `outputs/content-engine/blog/[DRAFT] *.md`
- Ready: `outputs/content-engine/blog/[READY] *.md`
- Archive: `outputs/content-engine/blog/archive/`
- Calendar: `outputs/content-engine/Q4-CONTENT-CALENDAR-MASTER.md`
