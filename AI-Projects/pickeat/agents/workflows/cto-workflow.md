# CTO Workflow - Technical Decision Making

**Quando chiamare questo workflow:** Decisioni tecniche, review architettura, priorità dev, valutazione feature

---

## Workflow: Technical Decision

### Input richiesto
- Problema/domanda tecnica
- Context (cosa esiste già, vincoli)
- Urgenza (now/soon/later)

### Steps

```
1. UNDERSTAND
   └─ Qual è il problema reale? (non la soluzione proposta)
   └─ Chi è impattato? (utente, vendor, admin)
   └─ Qual è il costo di non fare nulla?

2. OPTIONS
   └─ Genera 2-3 opzioni
   └─ Per ogni opzione:
      - Effort (hours/days/weeks)
      - Risk (low/medium/high)
      - Dependencies
      - Trade-offs

3. RECOMMEND
   └─ Una raccomandazione chiara
   └─ Reasoning in 2-3 bullet
   └─ "If I'm wrong, the worst case is..."

4. DECISION RECORD
   └─ Salva in docs/decisions/[YYYYMMDD]-[topic].md
```

### Decision Record Template
```markdown
# Decision: [Title]
**Date:** [YYYY-MM-DD]
**Status:** Proposed / Accepted / Rejected

## Context
[Perché questa decisione è necessaria]

## Options Considered
1. [Option A] - [Pro/Con summary]
2. [Option B] - [Pro/Con summary]

## Decision
[Cosa abbiamo deciso]

## Consequences
- [Cosa cambia]
- [Cosa dobbiamo fare dopo]
```

---

## Workflow: Feature Prioritization

### Framework: RICE
```
Reach × Impact × Confidence / Effort = Score

Reach: Quanti utenti/settimana? (1-1000)
Impact: Quanto migliora? (0.25 = minimal, 3 = massive)
Confidence: Quanto sei sicuro? (0.5 = low, 1 = high)
Effort: Person-weeks (0.5 = few days, 5 = months)
```

### Steps
```
1. List features/requests
2. Score each with RICE
3. Sort by score
4. Reality check: dependencies? blockers?
5. Output: prioritized backlog
```

---

## Workflow: Bug Triage

### Severity Levels
```
P0 - Critical: Users can't order, payments broken
     → Fix NOW, drop everything

P1 - High: Major feature broken, workaround exists
     → Fix today

P2 - Medium: Feature degraded, not blocking
     → This sprint

P3 - Low: Cosmetic, edge case
     → Backlog
```

### Steps
```
1. Reproduce
2. Identify scope (who's affected?)
3. Assign severity
4. If P0/P1: immediate escalation to Asim
5. Document in bug tracker
```

---

## Tech Stack Reference

### Frontend
- React/Next.js
- Deployed on Vercel

### Backend
- Node.js
- Database: [TBD - check with Asim]

### Integrations
- Payments: Stripe
- Notifications: WhatsApp (in progress), Email
- Analytics: GA4

### Constraints
- Asim è l'unico dev → capacity limitata
- iOS/Safari = maggioranza utenti → priorità testing
- Multi-tenant: ogni venue ha config separata

---

## Output Locations

- Decisions: `docs/decisions/`
- Tech specs: `docs/tech/`
- Bug reports: [External tracker]
