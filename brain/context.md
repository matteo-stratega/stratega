# Stratega Brain - Context File

**Last Updated:** 30 Dicembre 2025
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

### Completati 30 Dic
- [x] **Jubatus Discovery Call** - Prep, call, transcript analysis, follow-up
- [x] Meeting prep con FAVORITE framework
- [x] Analisi profilo Logan Para (CEO)
- [x] Follow-up email mandata con strategia 2 fasi
- [x] Sales Hub PickEat estratto in `data/sales-hub-pickeat/`

### Prossima Sessione (31 Dic / Gennaio)
- [ ] **MANDATORY: Contabilità** - Fattura Toma
- [ ] **MANDATORY: Report Duomo** - Annual report
- [ ] **Jubatus: Definire pacchetti Stratega** - Pricing proprio, non Crono
- [ ] **Jubatus: Mandare contatto persona mkt/sales** a Logan
- [ ] **Jubatus: Follow-up call** - Settimana 13 gennaio
- [ ] **Duomo GA4**: Aspetta accesso viewer da cliente, poi configurare MCP locale
- [ ] **Duomo: Trovare alternativa per slides** - Google Slides API non adatta
- [ ] **Academy: Review uTeach** - Decidere se migrare prima campagne gennaio
- [ ] Inviare reclamo commercialista (MI GESTORÍA)
- [ ] Proroga tarifa plana su IMPORTASS (deadline: 1 feb - 2 mar 2026)

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

### Jubatus Consulting (NEW)
- **Status:** Discovery done, follow-up sent
- **Client:** Logan Para (CEO) - pops.photos
- **Prodotto:** SaaS eventi sportivi, AI face recognition video
- **Need:** Sales playbook + processo prima di assumere SDR
- **Next:** Call settimana 13 gennaio per chiudere Fase 1
- **Files:** `notes/meetings/jubatus-discovery-prep-30122025.md`, `outputs/jubatus-followup-30122025.md`

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
| 30/12 | **Pacchetti Stratega separati da Crono** | Pricing e moduli propri, non dipendere da listino Crono Expert |
| 30/12 | **Jubatus: Strategia 2 fasi** | Fase 1 con founder (playbook), Fase 2 con SDR (training) |
| 29/12 | **Claude Code Guide per non-tecnici** | NetworkChuck base + Stratega OS upgrades, Build in Public asset |
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
| Metis | `stratega_brain_agent.md` | Core brain, strategy, identity |
| CTO | `cto_agent.md` | Architecture, code review, tech decisions |
| Archivista | `archivista_agent.md` | Workspace organization, git, memory |

### Execution
| Agent | File | Use Case |
|-------|------|----------|
| Archimede | `archimede_agent.md` | n8n, Supabase, coding, technical tutor |
| Content Engine | `content_engine_agent.md` | Writing, copy, editorial |
| Marketer | `marketer_agent.md` | Campaign copy, positioning, messaging |
| Build in Public | `build_in_public_agent.md` | Public content, Tool Fridays |

### Strategy
| Agent | File | Use Case |
|-------|------|----------|
| Esattore | `esattore_agent.md` | MRR accountability, revenue tracking |
| Growth Hacker | `growth_hacker_agent.md` | Experiments, campaigns, growth tactics |
| Growth Orchestrator | `growth_orchestrator_agent.md` | Campaign coordination, sequencing |
| Content Strategist | `content_strategist_agent.md` | Editorial planning, content calendar |

### Operations
| Agent | File | Use Case |
|-------|------|----------|
| Session Closer | `session_closer_agent.md` | End-of-day wrap, closing summaries |
| Matteo Voice | `matteo_voice_agent.md` | Personal brand voice |

### Project-Specific
| Agent | File | Use Case |
|-------|------|----------|
| Duomo | `duomo_agent.md` | Duomo brand + performance marketing |

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
