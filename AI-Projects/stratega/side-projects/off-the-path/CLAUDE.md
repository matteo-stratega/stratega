# CLAUDE.md — Off the Curious Path

This file provides guidance to Claude Code when working on this side project.

---

## Project Identity

**Name:** Off the Curious Path
**Type:** Barcelona city guide platform (CMS + frontend)
**Client:** Solo content curator (she manages content, we manage tech)
**Mission:** "A creative local's notebook" — authentic Barcelona, anti-touristy

---

## Folder Structure

This side project follows a **mini Stratega structure**:

```
off-the-path/
├── codebase/              # React app (don't modify without asking)
├── docs/                  # Strategic documents, reports, specs
├── notes/                 # Session summaries, raw thoughts
├── *.pdf                  # Design briefs (read-only)
└── README.md             # Project overview
```

**Golden Rule:** Keep session summaries in `notes/`, strategic docs in `docs/`.

---

## Operating Context

### Tech Stack
- **Frontend:** React + TypeScript + Vite + shadcn-ui
- **Backend:** Supabase (PostgreSQL + Auth + Storage + RLS)
- **Map:** Mapbox GL JS (free tier, 50K loads/mese)
- **Deploy:** Lovable (https://lovable.dev/projects/f4167f36-486e-4fcd-8f43-03ff1b511e74)

### Current Status
- CMS Admin: 70% complete
- Security: ⚠️ Not production-ready (RLS pubbliche)
- MVP Target: 1 week to production

### Critical Gaps
1. Auth + Security (Supabase Auth + RLS)
2. Geocoding automatico (Mapbox API)
3. Image Upload (Supabase Storage)

---

## Working Principles

### 1. CMS UX First
The client manages content through `/admin`. Every feature must be:
- **Simple** — She's not technical
- **Visual** — Show previews, not raw data
- **Forgiving** — Auto-save, clear errors, undo options

### 2. Backend = Our Domain
- Automations, API integrations, complex logic → We handle
- She should never see Supabase console
- Abstract complexity behind clean UI

### 3. Mapbox Strategy
- Free tier covers 50K loads/mese
- If we hit limits → Pivot to MapLibre + Maptiler
- Don't over-engineer for scale yet

### 4. Documentation Style
- Keep `docs/` for strategic deliverables (reports, specs)
- Keep `notes/` for session summaries, daily work
- Use clear headers, bullet points, decision logs
- Link to Lovable project when relevant

---

## Code Modification Rules

**BEFORE touching `codebase/`:**
1. Ask Matteo if unsure about architecture changes
2. Read latest `docs/CTO_REPORT_ANALYSIS.md` for context
3. Check `docs/NEXT_SESSION_PLAN.md` for priorities
4. Test locally before deploy

**When implementing:**
- Follow existing patterns (React Query, Zod validation, shadcn-ui)
- Keep forms simple and accessible
- Add loading states and error handling
- Document new API integrations

---

## Brand Guidelines (Reference Only)

**Tone:** Curious, playful, honest — never formal or touristy
**Colors:**
- Solar Tangerine: `#F58E2E` (primary accent)
- Teal Green: `#2CA6A4` (secondary)
- Light Sand: `#F6F3EF` (background)
- Ink Charcoal: `#1D1C1A` (text)

**Copy style:**
- Short sentences, contractions (you'll, we're)
- Avoid clichés ("hidden gems", "must-see")
- Feel: editorial yet relaxed

---

## Session Workflow

**At session start:**
1. Load `README.md` for project context
2. Check latest `notes/closing-*.md` for what we did last
3. Check `docs/NEXT_SESSION_PLAN.md` for priorities
4. Ask Matteo what we're working on today

**At session end:**
1. Create `notes/closing-DD-MM-YY.md` with summary
2. Update `docs/NEXT_SESSION_PLAN.md` if priorities changed
3. Update `README.md` status if milestones reached

---

## Decision Log (Key Choices)

| Date | Decision | Rationale |
|------|----------|-----------|
| 25 Nov 2025 | Supabase Auth Magic Link | Zero-friction for solo user |
| 25 Nov 2025 | Keep Mapbox free tier | Already integrated, monitor usage |
| 25 Nov 2025 | Stay on Lovable for MVP | Fast iteration, migration path later |
| 25 Nov 2025 | Tiptap for rich text editor | React-native, extensible |

---

## Quick Commands

**Navigate to project:**
```bash
cd /Users/matteolombardi/AI-Projects/stratega/side-projects/off-the-path
```

**Start dev server:**
```bash
cd codebase/
npm run dev
```

**Check Mapbox usage:**
Visit: https://account.mapbox.com/

---

## Common Tasks

### Creating a session summary
```bash
# Location
notes/closing-DD-MM-YY.md

# Template
## Session Closing — [Date]
**Focus:** [What we worked on]
**Deliverables:** [Files created/modified]
**Decisions:** [Key choices made]
**Next:** [What's next]
```

### Creating strategic docs
```bash
# Location
docs/[DESCRIPTIVE_NAME].md

# Examples
docs/CTO_REPORT_ANALYSIS.md
docs/NEXT_SESSION_PLAN.md
docs/AUTH_IMPLEMENTATION_SPEC.md
```

---

## Links

- **Lovable Project:** https://lovable.dev/projects/f4167f36-486e-4fcd-8f43-03ff1b511e74
- **Mapbox Account:** https://account.mapbox.com/
- **Supabase Dashboard:** (check codebase/.env for project URL)

---

## Notes for Archivista

When this project is referenced from main Stratega workspace:
- Session summaries stay in `side-projects/off-the-path/notes/`
- Don't duplicate in main `notes/` folder
- Link from main daily summaries when relevant

---

*This is a living document. Update when key decisions are made.*
