# Off the Curious Path
*Barcelona city guide — hidden corners & everyday wonders*

---

## Project Overview

**Type:** City guide platform with CMS
**Client:** Solo manager (content curator)
**Stack:** React + TypeScript + Supabase + Mapbox
**Status:** MVP development (70% complete)

---

## Folder Structure

```
off-the-path/
├── codebase/              # React app + Supabase backend
├── docs/                  # Strategic documents & reports
│   ├── CTO_REPORT_ANALYSIS.md
│   └── NEXT_SESSION_PLAN.md
├── notes/                 # Session summaries & raw notes
│   └── closing-25-11-25.md
├── Off_the_Curious_Path_Creative_Brand_Brief.pdf
├── 🌞 HOMEPAGE PROMPT — Off the Curious Path.pdf
├── ⭐️ PRODUCT ARCHITECTURE — MACRO SECTIONS & Structure.pdf
└── README.md             # This file
```

---

## Quick Links

**Lovable Project:** https://lovable.dev/projects/f4167f36-486e-4fcd-8f43-03ff1b511e74
**Latest Docs:** `docs/CTO_REPORT_ANALYSIS.md`
**Latest Notes:** `notes/closing-25-11-25.md`

---

## Current Phase

**Sprint:** MVP Production Prep
**Priority:** Auth + Geocoding + Image Upload
**Timeline:** 1 week to production-ready

---

## Tech Stack

| Layer | Technology | Status |
|-------|------------|--------|
| Frontend | React + TypeScript + Vite | ✅ |
| UI | shadcn-ui + Tailwind | ✅ |
| Backend | Supabase (PostgreSQL + Auth + Storage) | 🟡 |
| Map | Mapbox GL JS | ✅ |
| Deploy | Lovable | ✅ |

---

## Architecture

**3 Macro Sections:**
1. **Places** — Curated locations (restaurants, cafés, bars, shops)
2. **Editorial** — Articles, guides, lists
3. **Events** — Weekly happenings (Phase 2)

**Admin CMS:**
- Places management (CRUD, CSV import, bulk ops)
- Articles management
- Settings (Mapbox token, etc.)

---

## Development Commands

```bash
# Navigate to codebase
cd codebase/

# Install dependencies
npm install

# Start dev server
npm run dev

# Build for production
npm run build
```

---

## Critical Gaps (To Implement)

### 🔴 P0 — CRITICAL
1. **Auth & Security** — RLS policies currently public
2. **Geocoding** — Manual lat/lng input (bad UX)
3. **Image Upload** — No integrated storage

### 🟡 P1 — HIGH
4. Rich text editor for articles
5. Neighborhoods management
6. SEO meta fields

### 🟢 P2 — NICE TO HAVE
7. Events section
8. Analytics dashboard
9. PWA setup

---

## Brand Identity

**Tone:** Curious, playful, honest — "a creative local's notebook"
**Colors:**
- Solar Tangerine: `#F58E2E`
- Teal Green: `#2CA6A4`
- Light Sand: `#F6F3EF`
- Ink Charcoal: `#1D1C1A`

**Typography:**
- Headings: Canela Deck / Recoleta
- Body: Satoshi / Inter

---

## Contact

**Project Owner:** Matteo + Claude (Stratega)
**Client:** Content curator (Barcelona)
**Repository:** Local + Lovable sync

---

*Last updated: 25 Nov 2025*
