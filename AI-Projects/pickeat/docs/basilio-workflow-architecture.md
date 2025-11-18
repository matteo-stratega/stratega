# Basilio - AI Operations Architecture

**Created**: 18/11/2025
**Purpose**: Visual explanation of Basilio's workflow for PickEat automation
**Use**: LinkedIn post, documentation, team onboarding

---

## 🌿 The Challenge

PickEat needed to automate 90% of operational work to enable founder exit from day-to-day operations while maintaining quality and consistency.

---

## 🎯 The Solution: Three-Tier Architecture

### Tier 1: Source of Truth (NOTION)
**Role**: Company-wide collaboration & live data
- Q4 OKRs, Sales pipeline, Projects
- Team access & stakeholder visibility
- **Input**: Real-time business data
- **Output**: Published reports & updates

### Tier 2: AI Workspace (OBSIDIAN)
**Role**: Basilio's local working environment
- Drafts, SOPs, agent memories, playbooks
- Markdown-based, lightning-fast
- Wikilinks & graph view for context
- **Processing**: Analysis, drafting, automation

### Tier 3: Version Control (GIT)
**Role**: Audit trail & backup
- Daily automatic commits
- Full history of all changes
- Rollback capability
- **Protection**: Knowledge base security

---

## 🔄 The Workflow

```
┌──────────────────┐
│    NOTION        │  ◄── Company Source of Truth
│   (Live Data)    │
└────────┬─────────┘
         │
         │ via MCP (real-time sync)
         ▼
┌──────────────────┐
│    BASILIO       │  ◄── AI Operations Assistant
│  works in        │
│   OBSIDIAN       │
│  (Local MD)      │
└────────┬─────────┘
         │
         ├─────────────────────┐
         │                     │
         │ daily commits       │ publishes
         ▼                     ▼
┌──────────────────┐  ┌──────────────────┐
│      GIT         │  │     NOTION       │
│  (Version        │  │   (Reports &     │
│   Control)       │  │    Updates)      │
└──────────────────┘  └──────────────────┘
         │                     │
         │                     │
         ▼                     ▼
    Audit Trail          Team Visibility
```

---

## 🤖 Agent System

**Five specialized agents working in harmony**:

### 1. Sales Orchestrator 🤝
- **Mission**: Automated pipeline management
- **Output**: Follow-ups, proposals, weekly reports
- **Daily**: 9:00 AM digest (red flags + actions)

### 2. Operations Commander 🏟️
- **Mission**: Venue operations without founder
- **Output**: Pre/post-event execution, vendor coordination
- **Event-driven**: T-7 days activation

### 3. Report Factory 📊
- **Mission**: Stakeholder reporting automation
- **Output**: Vendor/team/internal reports, case studies
- **Weekly**: Friday 10-min digest

### 4. Project Manager 📋
- **Mission**: Q4 OKR tracking & deadline enforcement
- **Output**: Progress updates, red flag escalations
- **Daily**: Status checks

### 5. Archivista 📚
- **Mission**: Knowledge management & organization
- **Output**: SOPs, playbooks, documentation cleanup
- **Weekly**: Vault maintenance

---

## 💡 Key Benefits

### For Operations
- **90% automation**: Founder intervention only for strategic decisions
- **Consistency**: Same quality every time
- **Scalability**: Ready for multi-venue expansion

### For Knowledge Management
- **Fast local access**: Obsidian markdown = zero latency
- **Complete history**: Git commits = full audit trail
- **Team collaboration**: Notion = stakeholder visibility

### For Compliance
- **Traceable**: Every change logged in git
- **Recoverable**: Rollback to any previous state
- **Secure**: Credentials vault with 600 permissions

---

## 📊 Results (First 48 Hours)

**Workspace Setup**:
- 149 Notion files analyzed
- 23 knowledge areas mapped
- 6 Q4 OKRs integrated
- 5 specialized agents deployed

**Documentation Created**:
- 3 agent definitions (Sales, Ops, Reports)
- 2 event playbooks (Varese Basket, Event Debrief SOP)
- 2 agent memory systems
- 1 central knowledge brain

**Automation Coverage**:
- Sales: Pipeline sync, follow-ups, proposals
- Operations: Pre/post-event checklists, reports
- Reporting: Vendor/team reports, weekly digests

---

## 🎨 Design Philosophy

**Basilio** = Essential, not flashy
- Named after basil leaf (essential in Italian cuisine)
- Pragmatic, systematic, reliable
- Italian design meets tech-forward thinking

**Principles**:
- Execution-first (no analysis paralysis)
- Draft for approval (no auto-execute)
- Red flags escalate immediately
- Daily digests keep humans in loop

---

## 🚀 Next Steps

**Week 1** (Nov 18-22):
- HubSpot integration tested
- Git workflow automated
- First autonomous digests

**Week 2** (Nov 25-29):
- First autonomous event execution (Varese Game 5)
- First weekly Growth/Ops digest
- Case study #1 drafted

**Week 3** (Dec 1-15):
- 3 venues at "Stable" classification
- 5 contracts signed (Q4 OKR)
- Founder intervention <10%

---

## 🔧 Technical Stack

**Core**:
- Claude Code (Basilio AI engine)
- Obsidian (markdown workspace)
- Git (version control)

**Integrations**:
- Notion (via MCP) - Company data
- HubSpot (API) - Sales pipeline
- Google Drive (API) - Prospecting files
- Stripe (data export) - Payment data

**Security**:
- Credentials vault (700/600 permissions)
- Never commit secrets to git
- API keys in secure JSON files

---

## 📝 Lessons Learned

**What Works**:
1. **Complementary tools**: Notion for collaboration, Obsidian for speed, Git for safety
2. **Specialized agents**: Single responsibility = better results
3. **Human-in-loop**: Draft-for-approval prevents AI overreach
4. **Local-first**: Obsidian markdown = instant access

**What Doesn't**:
1. Trying to replace Notion entirely (it's the collaboration hub)
2. Auto-executing without approval (trust requires oversight)
3. Single monolithic agent (specialized > general)

---

## 🌍 Use Cases

This architecture works for any knowledge-intensive business needing:
- Founder exit strategy
- Operations automation
- Knowledge base management
- Team collaboration + AI efficiency
- Audit trail + version control

**Industries**:
- SaaS operations
- Professional services
- Event management
- Sales-heavy businesses
- Compliance-required sectors

---

## 👥 Team

**Created by**:
- Matteo Lombardi (PickEat Founder & CEO)
- Basilio AI (Italian AI Operations Assistant)

**For**:
- PickEat - B2B2C food ordering platform for sports venues
- Q4 2025 goal: Automate 90% of operations

---

## 📞 Questions?

This is a living architecture. It evolves daily based on:
- Real operational needs
- Agent performance
- User feedback
- Q4 OKR progress

**Philosophy**: *Build systems that work for humans, not replace them.*

---

**#AI #Automation #KnowledgeManagement #Obsidian #Notion #Git #OperationsExcellence #ItalianTech #StartupOps**

---

*Generated by Basilio 🌿*
*The pragmatic AI assistant who organizes your chaos*
