# 🧠 CLAUDE MANAGEMENT GUIDE
**Come gestire Claude Code per massimizzare efficienza e risultati**

---

## PRINCIPI FONDAMENTALI

### 1. Claude È un Operatore, Non un Consulente
- Vuole **fare**, non teorizzare
- Dargli task chiari e actionable
- Evitare domande aperte tipo "cosa ne pensi di..."
- Preferire: "Analizza X e proponi 3 soluzioni"

### 2. Delegazione È Potenza
- Claude può delegare a agent specializzati (Haiku, Gemini, local models)
- Task heavy (>10K token) → sempre delegare
- Risparmio medio: 60-70% dei token

### 3. Token = Soldi = Tempo
- Budget: 200K token/sessione
- Target: 30-50K token/sessione
- Startup deve essere <600 token
- Ogni token sprecato è inefficienza

### 4. Prep Files Sono la Tua Memoria
- Claude rilegge ogni sessione
- Prep file aggiornato = context istantaneo
- Closing summary = memoria per domani

---

## ANATOMIA DI UNA SESSIONE PERFETTA

### Fase 1: Startup (600 token budget)

**Tu:**
```
Follow SESSION_START.md
```

**Claude (automatico):**
1. Legge top 30 righe di `prep-[data].md`
2. Chiede: "What are we working on today?"
3. **Si ferma**

**Token cost: ~400-600 token**

---

### Fase 2: Brief (100 token budget)

**Tu (conciso):**
```
"Oggi:
1. Correggere transcript scuola (8 files .srt)
2. Cross-check con slides in Drive
3. Organizzare hub academy
4. Self-review del lavoro

Delega task heavy per risparmiare token."
```

**Claude:**
- Carica solo agent/file necessari
- Propone strategia
- Chiede conferma se ambiguità

**Token cost: ~100 token**

---

### Fase 3: Execution (20-30K token budget)

**Claude (autonomo):**
1. Analizza task
2. Identifica heavy lifting
3. Delega a agent specializzati
4. Processa solo risultati
5. Crea output finale

**Tu:**
- Lascia lavorare
- Intervieni solo se chiede
- Approva decisioni critiche (commit, push, delete)

**Token cost: ~20-30K (con deleghe)**

---

### Fase 4: Closing (2-3K token budget)

**Tu:**
```
"Crea closing summary e proponi commit"
```

**Claude:**
1. Crea `closing-[data].md` (50-100 righe)
2. Propone commit message
3. Mostra file modificati
4. Chiede approval per push

**Tu:**
- Review commit
- Approva o modifica
- Push to GitHub

**Token cost: ~2-3K token**

---

## STRATEGIE DI DELEGA

### Quando Delegare (Sempre)

| Task Type | Delega a | Motivo |
|-----------|----------|--------|
| Batch file processing | Haiku | Fast & cheap |
| Web research | Gemini | Current data |
| Code review | DeepSeek | Specialized |
| File classification | Gemma 3 | Local & free |
| Data analysis (large CSV) | LLaMA | Batch power |

### Come Delegare (Prompt Pattern)

**Template:**
```markdown
You are [ROLE] specialized in [DOMAIN].

TASK:
[Clear, specific objective]

INPUT:
[File paths, data, constraints]

OUTPUT:
[Exact format required]

CONSTRAINTS:
[What to avoid, limits, rules]

Report back with:
1. [Deliverable 1]
2. [Deliverable 2]
3. [Summary]
```

**Esempio Buono:**
```markdown
You are a transcript corrector specialized in educational content.

TASK:
Correct 8 .srt files for grammar, spelling, clarity.

INPUT:
Files: /path/to/*.srt
Reference: /path/to/slides/*.pdf

OUTPUT:
Corrected files with -corrected.srt suffix

CONSTRAINTS:
- Keep timestamps unchanged
- Max 30% word changes
- Professional tone

Report back with:
1. Number of corrections per file
2. Types of errors found
3. Critical issues identified
```

**Esempio Cattivo:**
```
"Hey puoi correggere questi file? Grazie"
[Agent non sa cosa fare]
```

---

## USO DEGLI AGENT

### Agent Disponibili

**Stratega Brain (Default - Tu):**
- Orchestratore principale
- Strategic thinking
- Multi-agent coordination
- Use case: Task complessi, decisioni, planning

**Archivista:**
- File organization
- Git management
- Workspace cleanup
- Use case: End-of-day cleanup, structure refactor

**Content Engine:**
- Content creation
- SEO optimization
- Voice analysis
- Use case: Blog posts, email sequences, copy

**Growth Hacker:**
- Lead gen strategies
- Campaign design
- ICP analysis
- Use case: Outreach planning, funnel optimization

**Esattore:**
- MRR tracking
- Revenue optimization
- Pricing strategy
- Use case: Financial planning, monetization

**CTO (Archimede):**
- Code architecture
- Tech decisions
- Infrastructure
- Use case: Indie hacker projects, tech stack

### Agent Activation Pattern

**Metodo 1: Esplicito (raccomandato)**
```
"Attiva Archivista e fai cleanup workspace"
```

**Metodo 2: Implicito**
```
"Organizza il workspace"
[Claude attiva automaticamente Archivista]
```

**Metodo 3: Nel prep file**
```markdown
## Today's Agent
Primary: Growth Hacker
Support: Content Engine
```

---

## TODOWRITE PROTOCOL

### Quando Usare

**Sempre per:**
- Task con 3+ step
- Multi-fase progetti
- Anything >30 min
- Quando Claude suggerisce

**Mai per:**
- Single-step task
- Quick questions
- Pure research

### Come Usare

**Claude crea automaticamente:**
```markdown
Todos:
1. Task A [pending]
2. Task B [pending]
3. Task C [pending]
```

**Claude aggiorna in real-time:**
```markdown
Todos:
1. Task A [completed] ✓
2. Task B [in_progress] ← Working on this
3. Task C [pending]
```

**Tu vedi progress live** - ottimo UX

---

## TOKEN OPTIMIZATION TACTICS

### Tactic 1: Sample, Don't Read All

**Bad:**
```
Read all 10 CSV files (50K token)
```

**Good:**
```
Read first 100 lines of CSV to understand structure (500 token)
Then delegate batch processing (5K token)
```

**Savings: 90%**

---

### Tactic 2: Parallel Commands

**Bad:**
```
Run command A (wait)
Run command B (wait)
Run command C (wait)
[3 messages, 3 roundtrips]
```

**Good:**
```
Run A && B && C in parallel
[1 message, 1 roundtrip]
```

**Savings: 66% interaction cost**

---

### Tactic 3: Don't Read Agent Files

**Bad:**
```
Read archivista.md (3.3K token)
Understand what to do
Delegate
```

**Good:**
```
Delegate directly with clear prompt (0 token read)
```

**Savings: 3.3K token**

---

### Tactic 4: Executive Summaries

**Bad:**
```
Create 200-line detailed report (4K token)
```

**Good:**
```
Create 30-line executive summary (1K token)
Link to details if needed
```

**Savings: 75%**

---

### Tactic 5: Use Local Models

**Bad:**
```
Use Sonnet for simple classification (expensive)
```

**Good:**
```
Use Gemma 3 local model (free)
Reserve Sonnet for complex reasoning
```

**Savings: 100% of classification cost**

---

## COMMUNICATION PATTERNS

### Cosa Claude Capisce Meglio

**1. Bullet Points**
```
✅ "Fai:
   1. A
   2. B
   3. C"

❌ "Allora vorrei che tu facessi A e poi anche B ma prima guarda C..."
```

**2. Imperativi Chiari**
```
✅ "Correggi transcript e delega se heavy"
❌ "Potresti dare un'occhiata ai transcript?"
```

**3. Context Upfront**
```
✅ "Task: Fix transcripts. Files: /path. Delegate to save tokens."
❌ "Quindi c'è questa cosa dei transcript che sono là..."
```

**4. Constraints Espliciti**
```
✅ "Max 10K token per questo task"
❌ [Claude decide liberamente]
```

---

### Feedback Efficace

**Durante il lavoro:**
```
✅ "Stop, cambia approccio: usa Haiku invece"
✅ "Continua, va bene così"
❌ "Mmmh non so se mi convince"
```

**Fine task:**
```
✅ "Fatto bene, ma prossima volta delega prima"
✅ "Sprecati token, rivedi strategia"
❌ "Ok grazie" [No learning]
```

---

## GESTIONE ERRORI

### Errore: "Token limit exceeded"

**Causa:** Task troppo grande processato direttamente

**Fix:**
```
"Stop. Delega questo a Haiku agent.
Processa solo risultati finali."
```

---

### Errore: "File too large to read"

**Causa:** CSV/dataset troppo grande

**Fix:**
```
"Read only first 200 lines to understand structure.
Then delegate batch processing."
```

---

### Errore: "Agent failed / timeout"

**Causa:** Task troppo complesso per agent

**Fix:**
```
"Break down in smaller chunks:
1. First do A (delegate)
2. Then B (delegate)
3. Then combine results"
```

---

### Errore: "Unclear instructions"

**Causa:** Prompt ambiguo

**Fix:**
```
"Let me clarify:
- INPUT: [specific]
- OUTPUT: [specific]
- CONSTRAINTS: [specific]"
```

---

## DAILY WORKFLOW

### Morning (5 min)

**1. Update Prep File**
```bash
cp notes/daily-summaries/prep-template.md \
   notes/daily-summaries/prep-$(date +%d-%m-%y).md

# Edit top 30 lines only:
# - Top 3 priorities
# - Context from yesterday (5 lines)
# - Files to open
```

**2. Optional: Review Closing**
```bash
cat notes/daily-summaries/closing-[yesterday].md
# Quick context refresh
```

---

### During Session (1-2h)

**1. Launch Claude**
```
"Follow SESSION_START.md"
```

**2. Give Brief**
```
"Today:
1. [Priority 1]
2. [Priority 2]
3. [Quick win]

Delegate heavy tasks."
```

**3. Let Work**
- Monitor progress (if TodoWrite active)
- Approve critical decisions
- Give feedback if needed

---

### Evening (5 min)

**1. Closing**
```
"Create closing summary and propose commit"
```

**2. Review & Commit**
- Read proposed commit message
- Modify if needed
- Approve push

**3. Quick Prep for Tomorrow (optional)**
```bash
# Add to tomorrow's prep:
# - What's blocked
# - What's next
# - Quick wins available
```

---

## ADVANCED TACTICS

### Tactic: Chained Delegation

**When:** Complex multi-step task

**How:**
```
Phase 1: Delegate research (Gemini)
↓
Phase 2: Delegate data processing (Haiku)
↓
Phase 3: Delegate content creation (Claude)
↓
Phase 4: You review and approve
```

**Benefit:** Each specialist does what it's best at

---

### Tactic: Parallel Delegation

**When:** Independent tasks

**How:**
```
"Launch 3 agents in parallel:
1. Haiku: Process transcripts
2. Gemini: Research competitors
3. Local LLaMA: Classify leads

Report back when all done."
```

**Benefit:** 3x speed, same token cost

---

### Tactic: Progressive Refinement

**When:** Unclear requirements

**How:**
```
Round 1: "Create rough draft" (fast, cheap)
↓
Review: "Good direction, refine section 2"
↓
Round 2: "Refine only section 2" (focused)
↓
Done
```

**Benefit:** Avoid wasting tokens on wrong direction

---

### Tactic: Template Reuse

**When:** Repetitive tasks

**How:**
```
First time: Create detailed template (invest tokens)
Save to: /templates/[task-name].md

Next times: "Use template at /templates/[task-name].md"
(Zero tokens for instructions)
```

**Benefit:** Pay once, reuse forever

---

## METRICS TO TRACK

### Per Session

- **Token usage** (target: 30-50K)
- **Startup cost** (target: <600)
- **Delegations** (more = better)
- **Task completion** (%)
- **Quality** (subjective 1-10)

### Per Week

- **Avg tokens/session** (trending down = good)
- **Tasks completed** (trending up = good)
- **Commit frequency** (1-2/day ideal)
- **Self-reviews done** (1/week minimum)

### Per Month

- **Total token cost** (vs budget)
- **Productivity gained** (tasks completed)
- **Process improvements** (documented)
- **ROI** (time saved vs cost)

---

## TROUBLESHOOTING CHECKLIST

### "Sessions cost too many tokens"

- [ ] Startup >600 token? → Fix SESSION_START adherence
- [ ] Reading unnecessary files? → Stop reading agent files
- [ ] Not delegating heavy tasks? → Delegate more
- [ ] Reports too long? → Use executive summaries
- [ ] Processing large files directly? → Sample first, delegate after

### "Claude not delegating"

- [ ] Did you ask explicitly? → "Delegate heavy tasks"
- [ ] Is task too small? → Small tasks = direct processing OK
- [ ] Unclear which agent to use? → Specify: "Use Haiku for this"

### "Tasks taking too long"

- [ ] Sequential when could be parallel? → Launch in parallel
- [ ] Waiting for results? → Use background execution
- [ ] Too much back-and-forth? → Give clearer initial brief

### "Quality issues"

- [ ] Prompt too vague? → Add specific constraints
- [ ] No reference materials? → Provide examples/templates
- [ ] Agent not specialized? → Use right agent for job
- [ ] No review cycle? → Add "review and refine" step

---

## BEST PRACTICES SUMMARY

### DO ✅

1. **Update prep file** daily (5 min investment)
2. **Follow SESSION_START** religiously (<600 token)
3. **Delegate heavy tasks** immediately
4. **Use TodoWrite** for multi-step tasks
5. **Executive summaries** over encyclopedias
6. **Parallel execution** when possible
7. **Sample before processing** large files
8. **Review and commit** every session
9. **Self-review** periodically (every 5-10 sessions)
10. **Track metrics** (tokens, quality, speed)

### DON'T ❌

1. **Long rambling messages** (be concise)
2. **Read agent files** (waste of tokens)
3. **Process large files directly** (delegate)
4. **Skip TodoWrite** on complex tasks
5. **Auto-approve** without review
6. **Mix multiple unrelated** tasks
7. **Ignore token budget** warnings
8. **Skip closing summary** (lose memory)
9. **Push without approval** (safety first)
10. **Forget to use** local models

---

## QUICK REFERENCE CARD

**Session Startup:**
```
1. "Follow SESSION_START.md"
2. Answer in 3-5 lines what to do
3. Let Claude work
```

**During Session:**
```
- One task at a time
- Approve critical decisions
- Use TodoWrite for tracking
```

**Session Close:**
```
1. "Create closing summary"
2. Review commit
3. Approve push
```

**Token Budget:**
```
Startup: <600
Session: 30-50K
Max: <80K
```

**Delegation Rule:**
```
If task >10K token → DELEGATE
```

**Communication:**
```
Concise > Verbose
Bullets > Paragraphs
Clear > Ambiguous
```

---

## FILES REFERENCE

**You maintain:**
- `notes/daily-summaries/prep-*.md` (daily)
- `notes/daily-summaries/closing-*.md` (created by Claude)

**System files (don't touch):**
- `SESSION_START.md` (startup protocol)
- `CLAUDE.md` (router config)
- `GEMINI.md` (project-wide config)
- `agents/*.md` (agent definitions)

**Guides (read when needed):**
- `STARTUP_QUICK_GUIDE.md` (this file's companion)
- `CLAUDE_MANAGEMENT_GUIDE.md` (this file)
- `docs/SELF_REVIEW_*.md` (learning from past)

---

**Goal:** Make every session count. Zero wasted tokens, maximum output, continuous improvement.

**Remember:** Claude is powerful but needs discipline. You're the strategist, Claude is the operator.

**Questions?** Ask Claude: "Explain [topic] from management guide"
