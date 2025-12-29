# Metis Session Startup Checklist

**Purpose:** Documents to read at the start of every session to load context and operate effectively.

---

## 🎯 Priority 1: Core Identity & Mission (ALWAYS)

**Read every session without exception:**

### 1. `/agents/stratega-brain.md`
**Why:** My core identity, mission, responsibilities, operating rules
**What I get:**
- Who I am (Metis, Stratega Brain)
- My mission (make Stratega world-class)
- Core responsibilities (growth, product, research, content, OS management)
- Operating rules (folder structure, data handling, output style)

### 2. `/CLAUDE.md`
**Why:** Project-level instructions and repository overview
**What I get:**
- Repository structure and purpose
- Router instructions (always load stratega-brain.md)
- Common tasks and file management rules
- Git usage guidelines

### 3. `/GEMINI.md`
**Why:** Shared operational configuration
**What I get:**
- Identity reinforcement
- Key directives (propose improvements, execute autonomously, use real data)
- Folder architecture rules

---

## 🎯 Priority 2: Orchestration & Capabilities (ALWAYS)

### 4. `/docs/ORCHESTRATION_GUARDRAILS.md`
**Why:** How I coordinate other AI models and manage resources
**What I get:**
- Available models (local, cloud, Gemini)
- Task routing logic (who does what)
- Resource constraints (8GB RAM until Mac Mini)
- Cost optimization strategies
- Quality assurance protocols

---

## 🎯 Priority 3: Recent Context (ALWAYS)

### 5. Latest Daily Summary (`/notes/daily-summaries/[most-recent].md`)
**Why:** What happened last session, current blockers, next priorities
**What I get:**
- Completed tasks
- In-progress work
- Decisions made
- Blockers and issues
- What Matteo is working on NOW

**How to find:**
```bash
ls -t /Users/matteolombardi/AI-Projects/stratega/notes/daily-summaries/ | head -1
```

---

## 🎯 Priority 4: Active Objectives (IF RELEVANT)

**Read based on current work:**

### 6. `/agents/esattore.md` (if working on revenue/MRR)
**Why:** €500 MRR by Dec 31, 2025 is the North Star
**What I get:**
- MRR target and breakdown
- Revenue streams ranked by speed
- Current MRR status
- Asset inventory to monetize
- Fear responses and accountability protocols

### 7. `/agents/archimede.md` (if working on technical/coding tasks)
**Why:** Matteo's learning path for n8n, Supabase, SaaS development
**What I get:**
- Teaching philosophy (show, don't tell)
- Current technical skill level
- Learning paths (n8n, Supabase, full SaaS)
- Code style guide
- Common scenarios and responses

### 8. `/agents/growth-hacker.md` (if working on experiments)
**Why:** Bi-weekly growth experiments, 26/year target
**What I get:**
- Experiment framework (2-week sprints)
- Experiment ideas bank
- Current experiment status
- Success metrics

### 9. `/agents/content-engine.md` (if working on content)
**Why:** Multi-agent content production system
**What I get:**
- Sub-agent architecture
- Content workflow
- Voice and framework guidelines
- Content calendar and quotas

---

## 🎯 Priority 5: File Organization Context (IF WORKING ON REORGANIZATION)

**Read when working on Drive/file cleanup:**

### 10. `/REORGANIZATION_PLAN.md`
**Why:** Complete reorganization strategy for Drive Stratega
**What I get:**
- Current state analysis (494 files at root)
- Proposed structure (7 macro-categories)
- Phase-based approach (4 weeks)
- File movement plans
- Duplicate resolution strategy

### 11. `/QUICK_REFERENCE.md`
**Why:** Fast lookup for "where does X go?"
**What I get:**
- Quick location guide
- File naming standards
- Common tasks (find lead list, find logo, etc.)
- Rules to remember (DOs and DON'Ts)

### 12. `/STRUCTURE_COMPARISON.md`
**Why:** Before/after visualization
**What I get:**
- Current chaos vs proposed order
- Key metrics comparison
- File journey examples
- Success indicators

### 13. `/IMPLEMENTATION_QUICK_START.md`
**Why:** Step-by-step execution guide
**What I get:**
- Pre-flight checklist
- Phase 1-7 action steps
- Checkpoint criteria
- Rollback plan

---

## 🎯 Optional: Agent-Specific Context (AS NEEDED)

**Read only if directly working with these agents:**

### 14. `/agents/archivista.md` (if using file-classifier-organizer)
**Why:** File organization agent protocol
**What I get:**
- Categorization rules
- Safety protocols
- Workflow procedures

### 15. `/research/[relevant-file].md` (if continuing research work)
**Why:** Previous research context
**What I get:**
- Findings and data
- Sources and methodology

---

## 📋 Session Startup Protocol

### Standard Session Start (TOKEN-OPTIMIZED):

```
1. Read latest daily summary ONLY [500 tokens]
2. Ask: "What are we working on?" [100 tokens]
3. Load ONLY relevant docs for that task [2-5K tokens]
4. Execute with delegation (local models) [20-30K tokens]
```

### When to Read Full Context:

**ONLY if:**
- New strategic initiative (MRR planning, product launch)
- Major decision needed (architecture, agent design)
- Matteo explicitly asks "load full context"

**Otherwise:** Daily summary + on-demand docs only

### Deep Work Session (when starting major project):

```
1. Read all Priority 1-3 docs
2. Read all relevant Priority 4 docs
3. Read all Priority 5 docs (if file work)
4. Summarize current state to Matteo
5. Propose plan
```

---

## 🔄 Session Close Protocol

**At end of session, I should:**

1. **Update todo list** via TodoWrite (mark completed, update in-progress)
2. **Suggest daily summary update** (or create if end of day)
3. **Document key decisions** made during session
4. **Preview next session** priorities

---

## 📊 Context Health Check

**Signs I need to reload context:**

- ❌ I don't remember Matteo's current MRR goal
- ❌ I don't know which phase of reorganization we're in
- ❌ I don't recall recent decisions from last session
- ❌ I'm unsure which models are available
- ❌ I don't know current project priorities

**If any of these are true → re-read Priority 1-3 docs immediately**

---

## 🎯 What Matteo Can Say to Trigger Reads

**Quick prompts to help me load context:**

- "Load session context" → Read Priority 1-3
- "Load MRR context" → Read esattore.md
- "Load tech context" → Read archimede.md
- "Load file org context" → Read all Priority 5 docs
- "Load content context" → Read content-engine.md
- "Full context reload" → Read everything relevant

---

## 🧠 Memory Management

**What I remember naturally (no need to re-read):**
- Claude Code capabilities and tools
- General orchestration principles
- Coding best practices
- Strategic thinking frameworks

**What I must re-read every session:**
- Stratega-specific mission and rules
- Matteo's current priorities and blockers
- Project-specific context (MRR status, experiments, etc.)
- File organization state

---

## 📝 Maintenance

**Update this checklist when:**
- New agent added → Add to Priority 4
- New major project → Add relevant docs
- Reorganization complete → Remove Priority 5 docs from "always read"
- Mac Mini arrives → Update ORCHESTRATION_GUARDRAILS reference

---

**Version:** 1.0
**Date:** 2025-01-24
**Next Review:** When new agents/projects added

---

*This checklist ensures Metis starts every session with the right context to be maximally effective.*
