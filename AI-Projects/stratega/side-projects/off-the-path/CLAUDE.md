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
├── codebase/              # React app - GitHub synced
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
- **SEO:** react-helmet-async + JSON-LD structured data
- **Hosting:** Lovable (migrating to Vercel)
- **Repo:** https://github.com/matteo-stratega/barcelona-vibe-guide

### Infrastructure (Updated 22 Dec 2025)

⚠️ **CRITICAL: There are TWO Supabase projects. Know the difference!**

| Environment | Supabase Project ID | Data | .env status |
|-------------|---------------------|------|-------------|
| **Lovable (prod)** | `casprhxtfzjlnzmfceiy` | 174 places (CSV import) | Committed in Git |
| **Our dev** | `facdxrllyilohbubdrtc` | Empty | Local only, NOT committed |

**Current state:**
- Lovable uses their Supabase (has data)
- Local dev uses our Supabase (empty)
- `.env` change is NOT committed intentionally (keeps environments separate)

**Decision pending:** Which Supabase to use for production? Options:
1. Keep Lovable's (has data, but no admin access)
2. Use ours (need to import data, but full control)
3. Export from Lovable → import to ours

### Current Status (Updated 22 Dec 2025)
- **CMS Admin:** 90% complete
- **Auth:** ⚠️ DISABLED temporarily (partner testing) - re-enable before prod
- **Geocoding:** ✅ Implemented (Mapbox API)
- **Image Upload:** ✅ Implemented (Supabase Storage)
- **SEO:** ✅ Structured (meta, sitemap, JSON-LD)
- **Branding:** ✅ Complete (Off the Curious Path)
- **Security:** ⚠️ RLS policies need review before production

### Remaining for Production
1. Configure Supabase RLS policies
2. Deploy to Vercel (migration from Lovable)
3. Connect domain `offthecuriouspath.com`
4. Add real content

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

### 4. No Vendor Lock-in
- Code is standard React/Vite — portable anywhere
- Supabase is owned separately
- Can migrate hosting anytime (Vercel recommended)

---

## Code Modification Rules

**BEFORE touching `codebase/`:**
1. Pull latest from GitHub first
2. Read this file for context
3. Check `notes/` for recent session summaries
4. Test locally before commit

**When implementing:**
- Follow existing patterns (React Query, Zod validation, shadcn-ui)
- Keep forms simple and accessible
- Add loading states and error handling
- Use SEO component for new pages

---

## Brand Guidelines

**Tone:** Curious, playful, honest — never formal or touristy

**Colors (CSS custom properties in index.css):**
- Solar Tangerine: `#F58E2E` (primary accent)
- Teal Green: `#2CA6A4` (secondary)
- Light Sand: `#F6F3EF` (background)
- Ink Charcoal: `#1D1C1A` (text)

**Copy style:**
- Short sentences, contractions (you'll, we're)
- Avoid clichés ("hidden gems", "must-see")
- Feel: editorial yet relaxed
- Tagline: "Hidden corners & everyday wonders"

---

## Key Components

### SEO (`src/components/SEO.tsx`)
- Use on every page
- Supports dynamic title, description, image
- JSON-LD for places and articles
- Example: `<SEO title="Map" description="..." />`

### Auth (`src/hooks/useAuth.tsx`)
- Magic link (primary)
- Password (fallback)
- `ProtectedRoute` wraps `/admin`

### Footer (`src/components/Footer.tsx`)
- Brand identity
- Newsletter signup (ready for integration)
- Social links

---

## Session Workflow

**At session start:**
1. Pull latest from GitHub
2. Check latest `notes/session-*.md` for context
3. Start dev server: `cd codebase && npm run dev`

**At session end:**
1. Create `notes/session-DD-MMM-YYYY.md` with summary
2. **UPDATE this CLAUDE.md if any infrastructure/architecture discoveries** (Supabase, env vars, services, etc.)
3. Commit and push to GitHub
4. Update Decision Log if major decisions made

---

## Decision Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 25 Nov 2025 | Supabase Auth Magic Link | Zero-friction for solo user |
| 25 Nov 2025 | Keep Mapbox free tier | Already integrated, monitor usage |
| 16 Dec 2025 | Migrate from Lovable to Vercel | No lock-in, free, faster deploys |
| 16 Dec 2025 | React over WordPress | Full control, better performance, AI integrations easy |
| 16 Dec 2025 | SEO with react-helmet-async | Per-page meta, JSON-LD structured data |
| 22 Dec 2025 | Disable auth temporarily | Partner needs to test /admin without login |
| 22 Dec 2025 | Document dual-Supabase situation | Lovable vs our Supabase - decision pending |

---

## Future Integrations (Easy to Add)

| Integration | Effort | Notes |
|-------------|--------|-------|
| Google Tag Manager | 5 min | Script in index.html |
| Google Analytics 4 | 5 min | Via GTM or direct |
| Meta Pixel | 5 min | Via GTM or direct |
| Newsletter (Buttondown/ConvertKit) | 30 min | Footer form ready |
| AI Chatbot (OpenAI/Claude) | 1 session | API integration |
| Recommendation Engine | 1 session | Based on tags/vibes |

---

## Quick Commands

```bash
# Navigate to project
cd /Users/matteolombardi/AI-Projects/stratega/side-projects/off-the-path

# Start dev server
cd codebase && npm run dev

# Git workflow
git pull origin feature/mvp-core-features
git add -A && git commit -m "message"
git push origin feature/mvp-core-features

# Deploy to Vercel (when ready)
npm i -g vercel && vercel
```

---

## Links

- **GitHub Repo:** https://github.com/matteo-stratega/barcelona-vibe-guide
- **Branch:** `feature/mvp-core-features`
- **Lovable (legacy):** https://lovable.dev/projects/f4167f36-486e-4fcd-8f43-03ff1b511e74
- **Mapbox Account:** https://account.mapbox.com/
- **Supabase:** https://facdxrllyilohbubdrtc.supabase.co

---

## Notes for Archivista

When this project is referenced from main Stratega workspace:
- Session summaries stay in `side-projects/off-the-path/notes/`
- Don't duplicate in main `notes/` folder
- Link from main daily summaries when relevant

---

*Last updated: 22 December 2025*
