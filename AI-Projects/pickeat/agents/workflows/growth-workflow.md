# Growth Workflow - Experiment Design & Execution

**Quando chiamare questo workflow:** Design esperimenti, analisi risultati, decisioni growth

---

## Workflow: Experiment Design

### Input richiesto
- Obiettivo (cosa vuoi migliorare?)
- Vincoli (budget, tempo, tech)
- Contesto (venue, evento, timing)

### Steps

```
1. HYPOTHESIS
   └─ "Se [facciamo X], allora [metrica Y] migliorerà del [Z%]
       perché [reasoning]"

2. METRICS
   └─ Primary: una metrica chiave
   └─ Secondary: 2-3 metriche di supporto
   └─ Guardrail: cosa NON deve peggiorare

3. DESIGN
   └─ Control (A): stato attuale
   └─ Treatment (B): cosa cambia
   └─ Sample size: quanti utenti/ordini servono?
   └─ Duration: quante partite/giorni?

4. IMPLEMENTATION
   └─ Tech requirements
   └─ Ops requirements
   └─ Comunicazione (social, speaker, etc.)

5. SUCCESS CRITERIA
   └─ Keep: [threshold for success]
   └─ Iterate: [threshold for "promising"]
   └─ Kill: [threshold for failure]

6. DOCUMENT
   └─ Salva in outputs/growth-experiments/designs/
```

### Experiment Template
```markdown
# Experiment: [Name]

**Hypothesis:** If we [X], then [Y] will [improve/increase] by [Z%] because [reason]

**Type:** Acquisition / Activation / Retention / Revenue

**Metrics:**
- Primary: [metric]
- Secondary: [metrics]
- Guardrail: [metric that must not degrade]

**Variants:**
- Control (A): [current state]
- Treatment (B): [what changes]

**Duration:** [X events/days]
**Sample:** [N users/orders needed]

**Success Criteria:**
- Keep: Primary ≥ [X]
- Iterate: Primary [range]
- Kill: Primary < [X]

**Status:** Design / Running / Complete
```

---

## Workflow: Results Analysis

### Steps

```
1. COLLECT DATA
   └─ Primary metric: control vs treatment
   └─ Secondary metrics
   └─ Guardrails check

2. STATISTICAL CHECK
   └─ Is difference significant? (p < 0.05)
   └─ Sample size reached?
   └─ Any confounders? (weather, opponent, etc.)

3. DECISION
   └─ Keep: implement for all
   └─ Iterate: modify and retest
   └─ Kill: archive, document learnings

4. DOCUMENT
   └─ Results in outputs/growth-experiments/results/
   └─ Update experiment log
   └─ Add learnings to brain/context.md
```

---

## Experiment Ideas Backlog

### Acquisition
- QR placement optimization
- Speaker announcement timing
- Social content A/B
- Referral program

### Activation
- First-order discount
- WhatsApp login vs email
- Simplified menu
- Social proof ("X fans ordered")

### Retention
- Loyalty program
- Push notifications
- Email re-engagement

### Revenue
- Bundle pricing
- Upsell prompts
- Dynamic pricing
- Minimum order threshold

---

## Prioritization: ICE Score

```
Impact (1-10): How much will this move the needle?
Confidence (1-10): How sure are we it'll work?
Ease (1-10): How easy to implement?

ICE = (Impact + Confidence + Ease) / 3
```

### Quick Reference
| ICE | Priority |
|-----|----------|
| 8+ | Do now |
| 6-8 | This month |
| 4-6 | Backlog |
| <4 | Skip |

---

## Current Experiments

### Running
- Varese Xmas Voucher (21 dic)
  - Hypothesis: Voucher €10 per ≥€25 aumenta ordini 50%
  - Metrics: ordini, AOV, revenue
  - Status: Approved, awaiting execution

### Completed
[Add as experiments complete]

### Backlog
[Prioritized list from above]

---

## Output Locations

- Designs: `outputs/growth-experiments/designs/`
- Results: `outputs/growth-experiments/results/`
- Log: `outputs/growth-experiments/log.md`
