# Stratega Brain - Context File

**Last Updated:** 29 Dicembre 2025
**Purpose:** Stato corrente di Stratega, decisioni chiave, context persistente tra sessioni

---

## Focus Corrente

### Q4 2025 Priorities
1. **Stratega Academy** - Beta launch, DM outreach attivo
2. **n8n Revenue** - Decidere primo prodotto da lanciare
3. **Build in Public** - Tool Fridays, content queue

### Questa Settimana (16-22 dic)
- [ ] Academy: ENG batch upload su Crono (6 contatti)
- [ ] Academy: Follow-up DM "To complete" (11 persone)
- [ ] Academy: Follow-up DM "To sign up" (5 persone)
- [ ] n8n: Review `notes/n8n-revenue-map-dec2025.md`
- [ ] n8n: Decidere primo prodotto
- [ ] Build in Public: Tool Friday prep

### Completati 29 Dic
- [x] **Git repo separato** - Stratega ora ha repo indipendente, HOME non più git
- [x] Backup history in `~/Desktop/stratega-backup-20251229.bundle`
- [x] Duomo: Google Slides MCP configurato
- [x] Duomo: Annual Report contenuto e guida slides pronti
- [x] CTO: Decisione Service Account per Google APIs
- [x] Google Drive API abilitato su GCP
- [x] Symlink credentials per Slides MCP (`/keys/`)
- [x] Test creazione slides via API (risultato: non soddisfacente)

### Prossima Sessione (30 Dic)
- [ ] **MANDATORY: Contabilità** - Fattura Toma
- [ ] **MANDATORY: Report Duomo** - Annual report
- [ ] **Duomo GA4**: Aspetta accesso viewer da cliente, poi configurare MCP locale
- [ ] **MCP Cleanup**: Rimuovere MCP globali PickEat quando GA4 Duomo ready
- [ ] **Duomo: Trovare alternativa per slides** - Google Slides API non adatta, esplorare Pitch API / altro tool
- [ ] **Academy: Review uTeach** - Decidere se migrare o sistemare prima di campagne gennaio
- [ ] **Academy: Trovare 6 prospect** - Per completare sfida 50 (serve source file scoring)
- [ ] Inviare reclamo commercialista (MI GESTORÍA) → `notes/reclamo-migestoria-draft.md`
- [ ] Proroga tarifa plana su IMPORTASS (deadline: 1 feb - 2 mar 2026)
- [ ] Off The Path: Decisione Supabase (aspetta partner)

---

## Progetti Attivi

### Stratega Academy
- **Status:** Beta attivo
- **Focus:** DM outreach + Crono sequences
- **Contatti ENG:** 6 da caricare
- **DM pending:** 16 persone totali
- **Files:** `notes/academy/`, `data/academy/`

### n8n Revenue
- **Status:** Ideation
- **Goal:** Primo prodotto revenue-generating
- **Options:** Content Gen template, automation workflows
- **File:** `notes/n8n-revenue-map-dec2025.md`

### Off The Path (Side Project)
- **Status:** Development
- **Files:** `side-projects/off-the-path/`

---

## Side Projects

| Project | Status | Folder |
|---------|--------|--------|
| Off The Path | Active | `side-projects/off-the-path/` |
| Duomo Design | Active (ADV ongoing) | `projects/Duomo full 2025/` + `agents/duomo-adv.md` |

---

## Decisioni Chiave Recenti

| Data | Decisione | Rationale |
|------|-----------|-----------|
| 29/12 | **Git repo separato** | Stratega indipendente, backup in bundle, HOME pulito |
| 29/12 | MCP isolation per progetto | Ogni workspace ha i suoi MCP locali, evita conflitti (es. GA4) |
| 29/12 | Google Slides API non adatta per report | Troppo low-level, perde formattazione, serve alternativa (Pitch API?) |
| 29/12 | Google Slides MCP via Service Account | Stesso pattern GA4, no OAuth complexity |
| 23/12 | /close multi-tab + /daily-wrap | Workflow robusto per sessioni multiple |
| 23/12 | Memory-First Infrastructure | Implementata per Stratega, separata da PickEat |
| 23/12 | Academy: Liste pulite da VC | Rimossi 6 investor, non ICP-fit |
| 23/12 | uTeach review pending | Decidere migrazione prima campagne |
| 21/12 | Duomo: Carousel in Retargeting | Fix CPL €54 con 1 solo creative |
| 19/12 | Slash commands /start /close | Workflow automation |
| 16/12 | Academy focus su DM | Higher conversion than cold email |
| 16/12 | ENG batch via Crono | Automation per follow-up |
| 11/12 | n8n = revenue channel | Monetize automation expertise |

---

## Cose da NON Fare

1. **No hallucinated data** - Sempre chiedere dati reali
2. **No mixing projects** - Stratega ≠ PickEat
3. **No large file reads** - Sample first, then ask
4. **Revenue > Brand** - Priority a revenue-generating tasks
5. **No loading files "just in case"** - Load only what's needed

---

## Folder Structure

```
stratega/
├── agents/          # Agent definitions (15 agents)
├── brain/           # Context + memory
├── data/            # Large datasets, CSVs, exports
├── docs/            # Polished deliverables
├── drafts/          # WIP content
├── notes/           # Raw thinking, meetings
│   └── daily-summaries/  # Closing reports
├── outputs/         # Generated outputs
├── research/        # Market analysis, ICPs
├── side-projects/   # Off The Path, etc.
├── templates/       # Frameworks, SOPs
└── workflows/       # Operational blueprints
```

---

## Available Agents

### Core
| Agent | File | Use Case |
|-------|------|----------|
| Metis | `stratega-brain.md` | Core brain, strategy, identity |
| CTO | `cto.md` | Architecture, code review, tech decisions |
| Archivista | `archivista.md` | Workspace organization, git, memory |

### Execution
| Agent | File | Use Case |
|-------|------|----------|
| Archimede | `archimede.md` | n8n, Supabase, coding, technical tutor |
| Content Engine | `content-engine.md` | Writing, copy, editorial |
| Marketer | `marketer.md` | Campaign copy, positioning, messaging |
| Build in Public | `build-in-public.md` | Public content, Tool Fridays |

### Strategy
| Agent | File | Use Case |
|-------|------|----------|
| Esattore | `esattore.md` | MRR accountability, revenue tracking |
| Growth Hacker | `growth-hacker.md` | Experiments, campaigns, growth tactics |
| Growth Orchestrator | `growth-orchestrator.md` | Campaign coordination, sequencing |
| Content Strategist | `content-strategist.md` | Editorial planning, content calendar |

### Operations
| Agent | File | Use Case |
|-------|------|----------|
| Session Closer | `session-closer.md` | End-of-day wrap, closing summaries |
| Matteo Voice | `matteo-voice.md` | Personal brand voice |

### Project-Specific
| Agent | File | Use Case |
|-------|------|----------|
| Duomo Design | `duomo-design.md` | Duomo client work |
| Duomo ADV | `duomo-adv.md` | Duomo advertising |

---

## Agent Routing

**When user says "chiama [name]" or "call [name]":**
1. Search `agents/` for matching .md file
2. Read that agent file completely
3. ASSUME that agent's identity and protocol
4. Respond AS that agent

**NEVER improvise an agent. ALWAYS read the file first.**

---

## Session Protocol

### Start
Run `/start` → Loads context + closing, proposes priorities, waits for answer

### Close
Run `/close` → Writes closing report, updates this file

---

*Aggiornare questo file a fine sessione se ci sono cambi significativi*
