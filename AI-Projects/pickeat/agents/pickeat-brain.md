# PickEat Brain - Basilio's Central Knowledge

**Last Updated**: 18/11/2025
**Purpose**: Central knowledge repository for all PickEat operations
**Owner**: Basilio AI

---

## 🎯 Mission & Context

**PickEat** is a B2B2C food ordering platform for sports venues and events.

**Current Phase**: Q4 2025 - Scale & Stabilize
**Exit Strategy**: Automate 90% of operations to reduce founder dependency

**Matteo's Goal**: Step back from operations, focus only on strategy (sales, product, marketing decisions)

---

## 📊 Q4 2025 OKRs (Critical Context)

### Objective 1: Convert Key Clients to Long-Term
- **Target**: 5 annual/season contracts signed
- **Sales Cycle**: ≤30 days median
- **Case Studies**: 3 published (sports, festival, ops)
- **Market Test**: 1 new segment expansion
- **Owner**: Sales Orchestrator + Matteo (strategic)

### Objective 2: Make Live Venues Stable and Founder-Light
- **Target**: 3 venues reach "Stable" classification
- **Stable Criteria**: Adoption ≥12%, Zero P0 incidents, <1% order failure, 2 consecutive events
- **Growth**: Orders/event +30% vs Q3 baseline
- **Quality**: Vendor ≥8/10, Fan NPS ≥50
- **Autonomy**: Venue runbook WITHOUT founder intervention
- **Owner**: Operations Commander

### Objective 3: Ship Revenue-Unlocking Product
- **Printing**: Live in 2 venues, <1% failures (Deadline: Nov 15) 🚨
- **Bundles & Categories**: ≤2 taps, live in 2 venues (Deadline: Nov 30) 🚨
- **Client UI v2.1**: Checkout ≤60s, LCP ≤2.5s (Deadline: Dec 10)
- **Restaurant App v2**: MVP in 3 vendors (Deadline: Dec 15)
- **Coupons/Promos**: Shipped, ≥10% redemption
- **Reliability**: 99.5% uptime, P0 MTTR <30min
- **Owner**: Product team (Matteo PM)

### Objective 4: Growth Marketing Hub
- **Analytics**: End-to-end with weekly dashboard (Nov 7 deadline passed)
- **Experiments**: 6 tests (≥2/mo), ≥2 "keep" wins
- **Content**: 3 case studies + 6 posts, ≥3 earned mentions
- **Digest**: 10-min Friday Growth/Ops digest (weekly)
- **Owner**: Report Factory + Matteo (strategic)

### Objective 5: Algorithm v0 and PickEat Index
- **Capacity Estimator**: ±20% accuracy vs 2 live events
- **PickEat Index**: 3 public charts (orders/time, sell-through, peak load)
- **Stock Prediction**: In development
- **Owner**: Product team

### Objective 6: Financing Readiness
- **Proof Pack**: 2-page traction + 60-sec reel + 1-pager architecture
- **Micro-tickets**: 10 pitched, 3 EOIs/soft-commits
- **Grants**: 2 submissions, ≥1 passes eligibility
- **Pipeline**: Weekly review with stage-move %
- **Owner**: Matteo (strategic) + Sales Orchestrator (support)

---

## 🏟️ Active Venues & Partnerships

### Varese Basket 🏀 (Serie A2 Basketball)
**Status**: Active, 1/2 events toward "Stable"
**Vendor**: Mas Que Banqueting
**Bars**: Sud (primary 15-16 orders), Est (underutilized 3-4 orders)

**Latest Performance** (Game 4 - Nov 16, 2025):
- Orders: 19 (+137% vs Game 3)
- Revenue: ~€175
- AOV: ~€9.21 (LOW - bundle issue)
- New customers: 17
- Marketing: 75 reach → 25% conversion (QR 30, Social 30, Linktree 15)
- Incidents: 0 P0

**Target Game 5**:
- Conservative: 25 orders, €300-350 revenue
- Stretch: 30+ orders, €400+ revenue
- Focus: Bundle push + Bar Est optimization

**Playbook**: `docs/playbooks/varese-basket-playbook.md`

### UYBA Volley 🏐 (Serie A Volleyball)
**Status**: Active, baseline TBD
**Next**: Collect first event data, establish metrics
**Playbook**: To be created after Game 1

---

## 💼 Business Model

**B2B2C Structure**:
- **B2B**: Partner with sports venues/events
- **B2C**: Fans order food via PickEat app
- **Revenue**: Commission on orders + partnership fees

**Key Stakeholders**:
- **Venues** (Varese, UYBA): Partnership agreements, marketing support
- **Vendors** (Mas Que): Food preparation, fulfillment
- **Fans**: End users, order placement

---

## 🤖 Agent System (Exit Strategy)

### Active Agents (Phase 1)

**Sales Orchestrator** (`agents/sales-orchestrator.md`)
- Role: Automated sales pipeline management
- Scope: HubSpot sync, follow-ups, proposals, kill/cold decisions
- Daily: 9:00 AM digest (red flags + actions)
- Target: 5 contracts Q4, ≤30 day cycle

**Operations Commander** (`agents/operations-commander.md`)
- Role: Venue operations without founder
- Scope: Pre/post-event execution, vendor coordination, reporting
- Event-driven: T-7 days activation
- Target: 3 venues "Stable", +30% orders

**Report Factory** (`agents/report-factory.md`)
- Role: Automated stakeholder reporting
- Scope: Vendor/team/internal reports, case studies, digests
- Friday: 10-min weekly digest
- Target: 3 case studies Q4

**Project Manager** (`agents/project-manager.md`)
- Role: Q4 OKR tracking, deadline enforcement
- Scope: Nov 15/30, Dec 10/15 critical deadlines
- Daily: Progress updates

**Archivista** (`agents/archivista.md`)
- Role: Knowledge management, file organization
- Scope: Documentation cleanup, SOP extraction
- Weekly: Vault maintenance

### Active Agents (Phase 2 - Activated Nov 18, 2025)

**Content Engine** (`agents/content-engine.md`)
- Role: Blog posts, case studies, SEO, social content
- Scope: 3 case studies + 6 posts (Q4 OKR)
- Connected: Notion SEO, Content Calendar, Social Media Management
- Target: All content by Dec 31

**Product Coordinator** (`agents/product-coordinator.md`)
- Role: Backlog, specs, bug triage, Q4 deadlines
- Scope: Obj 3 tracking (Nov 30, Dec 10, Dec 15)
- Daily: 9:00 AM digest (product status)
- Target: All 6 KRs delivered

**Data Analyst** (`agents/data-analyst.md`)
- Role: Analytics dashboard, Q4 OKR metrics
- Scope: Weekly dashboard + experiment analysis
- Friday: 10-min data report
- Target: Dashboard every Friday

**Growth Experiments** (`agents/growth-experiments.md`)
- Role: Design, run, analyze experiments
- Scope: 6 experiments, ≥2 "keep" (Q4 OKR)
- Coordinate: Data Analyst for results
- Target: All experiments by Dec 31

### Agent Operation Rules
- ✅ Draft for approval (no auto-execute)
- 🚨 Red flags escalate immediately
- 📊 Daily digests at scheduled times
- 💾 Long-term memory in `agents/memory/`
- 📁 Outputs in `outputs/[agent-name]/`

---

## 📂 File Structure

```
/agents/                  # Agent definitions
  ├── 00_AGENTS_HUB.md   # Command center
  ├── sales-orchestrator.md
  ├── operations-commander.md
  ├── report-factory.md
  ├── project-manager.md
  ├── archivista.md
  └── memory/            # Long-term context
      ├── sales-orchestrator-memory.md
      └── operations-commander-memory.md

/docs/                    # Documentation
  ├── sop/               # Standard Operating Procedures
  ├── playbooks/         # Event playbooks
  │   ├── event-debrief-sop.md
  │   └── varese-basket-playbook.md
  └── processes/         # Business processes

/report/                  # Published reports
  ├── 00_REPORTS_HUB.md  # Central index
  ├── varese-game4-performance.md
  └── archivista-notion-scan-18112025.md

/sprints/                 # Sprint tracking
  ├── Sprint 17112025.md
  └── 00_SPRINTS_HUB.md

/task/                    # Daily tasks
  └── daily-summaries/

/templates/               # Report templates
  ├── sales-report-template.md
  └── game-report-template.md

/outputs/                 # Agent outputs
  ├── sales-drafts/
  └── ops-events/

/data/                    # Data sources
  └── notion-export/     # Full Notion workspace (149 files)

/Vault/                   # Secure storage
  └── .credentials/      # API keys (700 permissions)
```

---

## 🔌 Integrations

**Notion** (via MCP):
- Source of truth for all data
- Q4 OKRs, Projects, Sales pipeline
- Tools & Platforms, Vademecum
- Status: ✅ Active

**Google Drive**:
- Prospecting files (Serie B/C, Food Trucks, etc.)
- Service account: `Vault/.credentials/google-n8npe.json`
- Status: ✅ Active (read-only)

**HubSpot**:
- Sales pipeline, deals, contacts
- Integration: API (to be tested)
- Status: ⏸️ Pending test

**Crono**:
- Status: TBD

**Stripe**:
- Payment data for events
- Manual export for now
- Future: API integration

---

## 🎯 Current Priorities (Week of Nov 18-22)

**🚨 Critical**:
1. Nov 15 deadline: Printing system live (OVERDUE - check status)
2. Nov 30 deadline: Bundles & Categories (13 days remaining)
3. Varese Game 5 prep (date TBD)

**High Priority**:
4. HubSpot API integration test
5. Sales pipeline sync (5 contracts target)
6. Weekly Growth/Ops digest (first edition)

**Medium Priority**:
7. UYBA baseline data collection
8. Case study #1 (Varese) drafting
9. Git workflow for documentation

---

## 🧠 Key Learnings Database

### Product
- **Bundle visibility critical**: Low AOV when bundles not prominent
- **2-tap maximum**: UX goal for bundle add (Nov 30 deadline)
- **Printing reliability**: <1% failure rate required for Stable classification

### Operations
- **Bar load balancing**: Monitor Sud vs Est distribution real-time
- **Marketing timing**: 3h before game (not 1h) for social posts
- **Staff training**: Active bundle suggestion increases AOV

### Sales
- **25% conversion rate**: QR + Social + Linktree = 75 reach → 19 orders (Varese)
- **Season contracts**: More valuable than one-off events
- **Case studies**: Critical for closing new deals

### Marketing
- **Multi-channel works**: QR (30) + Social (30) + Linktree (15) = consistent reach
- **Stadium announcements**: Pre-game, halftime, Q3 timing effective
- **Urgency messaging**: "Order now, skip the line" + countdown converts

---

## 📚 Knowledge Sources

**Primary**:
- Notion workspace (149 files, 23 sections)
- Q4 OKRs (live via MCP)
- Vademecum (processes, tools guides)
- Event Debrief Framework

**Secondary**:
- Prospecting files (Google Drive)
- Historical reports (Game 3, Game 4)
- Stripe payment data
- Customer registration CSVs

---

## 🚀 Exit Strategy Roadmap

**Phase 1** (Nov 18-22):
- ✅ Agent definitions complete
- ✅ Playbooks documented
- ✅ SOPs extracted
- ⏸️ HubSpot integration tested
- ⏸️ Git workflow established

**Phase 2** (Nov 25-29):
- First autonomous sales digest
- First autonomous event execution (Varese Game 5)
- First automated weekly digest
- Case study #1 drafted

**Phase 3** (Dec 1-15):
- 3 venues at Stable (Q4 OKR)
- 5 contracts signed (Q4 OKR)
- All product deadlines met
- Founder intervention <10%

**Phase 4** (Jan 2026+):
- Matteo fully strategic role only
- Agents handle 90% operations
- New team members onboarded to agent outputs

---

## 🎨 Brand & Personality

**Basilio** (me!):
- Italian AI Operations Assistant
- Visual: Basil leaf character with glasses, terracotta tie
- Personality: Pragmatic, systematic, reliable, sharp
- Tone: Professional but warm, no-bullshit
- Language: Italian for Italy ops, English for international

**PickEat**:
- Essential (like basil in Italian cuisine)
- Execution-first, not flashy
- Italian design sensibility meets tech-forward thinking

---

## 🔐 Security & Compliance

**Credentials**:
- Location: `Vault/.credentials/`
- Permissions: 700 (folder), 600 (files)
- Git: NEVER commit credentials
- Access: Basilio + Archivista only

**Data Privacy**:
- Customer data: Handled via secure APIs only
- PII: Never logged or exposed
- GDPR compliance: TBD (document requirements)

---

## 📞 Key Contacts

**Internal**:
- Matteo: Founder, strategic decisions
- [Socio]: Technical, Domain-Wide Delegation pending

**External**:
- Mas Que Banqueting: Varese vendor (Italian)
- Varese Basket: Partnership team
- UYBA Volley: Partnership team
- Stephane: Suisse sales (Switzerland market)

---

## 🔄 Continuous Improvement

**Daily**:
- Morning digest review (9:00 AM)
- Red flag escalation (immediate)
- Event-driven activations (T-7 days)

**Weekly**:
- Friday Growth/Ops digest (10-min read)
- Agent memory updates
- Sprint progress review

**Monthly**:
- Q4 OKR progress check
- Agent performance review
- Knowledge base cleanup (Archivista)

---

**This brain is living documentation. Update after every major event, learning, or context change.**

**Last Brain Update**: 18/11/2025 by Basilio
**Next Review**: After Varese Game 5 or weekly sprint

---

## System & Workflow Learnings (Updated Nov 18, 2025)

### Token Management
- **CRITICAL**: Use Gemini/Llama for research/analysis, reserve Claude Sonnet for strategic work only
- Hit token limits Wed Nov 18 - need better delegation

### Agent Delegation Protocol  
- File searches → Call Archivista agent first (don't grep manually)
- Long analysis → Gemini background processing
- Simple edits → Use Haiku model

### Daily Workflow
- Closing interview format: ddmmyy (e.g., 181125)
- Works well for tracking, continue this pattern

### Infrastructure  
- Obsidian vaults: Project root = vault root (not subfolders)
- Fixed Stratega/PickEat/Personal paths Nov 18
