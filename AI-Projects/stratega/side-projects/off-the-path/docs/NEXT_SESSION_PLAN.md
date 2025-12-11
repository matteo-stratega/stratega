# Off the Curious Path — Next Session Plan
*Prep per sessione 26 Nov 2025*

---

## Context Recap

**Progetto:** Barcelona city guide — "creative local's notebook"
**Cliente:** Lei gestisce CMS, noi gestiamo backend/automazioni
**Stack:** React + Supabase + Mapbox
**Stato:** CMS 70% funzionante, mancano 3 feature critiche per produzione

---

## Priority Queue (Ordine di implementazione)

### 🔴 P0 — CRITICAL (Questa settimana)

#### 1. Security & Auth System
**Problema:** DB pubblicamente modificabile da chiunque
**Soluzione:**
- Supabase Auth (Magic Link email-based)
- Admin role table
- RLS policies con auth check
- Protected route `/admin`

**Stima:** 1-2 giorni
**Owner:** Noi (Matteo + Claude)

---

#### 2. Geocoding Automatico
**Problema:** Deve copiare lat/lng manualmente da Google Maps
**Soluzione:**
- Mapbox Geocoding API
- Input address → auto-fetch coordinates
- Preview map nel form admin
- Fallback manual override

**Stima:** 1 giorno
**Owner:** Noi

---

#### 3. Image Upload System
**Problema:** Deve uppare immagini altrove e incollare URL
**Soluzione:**
- Supabase Storage buckets (`place-images/`, `article-images/`)
- Drag & drop component nel form
- Auto-resize + WebP conversion
- CDN URLs

**Stima:** 1 giorno
**Owner:** Noi

---

### 🟡 P1 — HIGH (Prossime 2 settimane)

#### 4. Rich Text Editor per Articles
**Attuale:** Textarea semplice
**Target:** Tiptap editor con:
- Formatting (bold, italic, headings, lists)
- Link insertion
- Image inline upload
- Place mention/embed (@PlaceName)

**Stima:** 2 giorni

---

#### 5. Neighborhoods Management
**Attuale:** Solo campo `district` in places
**Target:**
- Neighborhoods come entità separate
- UI per CRUD neighborhoods
- Relazione `places.neighborhood_id`
- Homepage "Explore by Neighborhood" cards

**Stima:** 1-2 giorni

---

#### 6. SEO Meta Fields
**Mancanti:**
- `meta_description`
- `og_image`
- `og_title`
- Canonical URLs

**Stima:** 0.5 giorni

---

### 🟢 P2 — NICE TO HAVE (Fase 2)

7. Events section (design già pronto)
8. Analytics dashboard (Plausible/Fathom)
9. Bulk image upload
10. Admin audit log
11. Mobile PWA setup

---

## Tech Decisions Made

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **Auth** | Supabase Auth Magic Link | Zero-friction per utente singolo |
| **Map** | Mapbox (free tier) | Già integrato, 50K loads/mese gratis |
| **Storage** | Supabase Storage | Integrated, CDN, auto-scaling |
| **Editor** | Tiptap | React-first, extensible |
| **Deploy** | Lovable (per ora) | Fast iteration, migration path open |

---

## Session 26 Nov — Proposed Agenda

**Opzione A: Quick Win Path** (Recommended)
1. Implementa Image Upload (1h)
2. Implementa Geocoding (1.5h)
3. Test end-to-end del flusso CMS
4. Deploy preview per feedback cliente

**Opzione B: Security First Path**
1. Implementa Supabase Auth (2h)
2. RLS policies (1h)
3. Protected routes (0.5h)
4. Test auth flow

**Opzione C: Full Stack Sprint**
1. Auth (mattina)
2. Geocoding (pomeriggio)
3. Image upload (sera)
4. Deploy & test

**Raccomandazione:** Opzione A — quick wins visibili per la cliente, poi security.

---

## Files da Caricare Next Session

```
/side-projects/off-the-path/
├── CTO_REPORT_ANALYSIS.md (questo)
├── NEXT_SESSION_PLAN.md (questo)
├── codebase/
│   ├── src/pages/AdminPage.tsx
│   ├── src/components/admin/PlaceFormDialog.tsx
│   └── supabase/migrations/*.sql
```

---

## Quick Commands Reference

**Start dev server:**
```bash
cd /Users/matteolombardi/AI-Projects/stratega/side-projects/off-the-path/codebase
npm run dev
```

**Supabase local:**
```bash
npx supabase start
npx supabase db reset
```

**Check Mapbox usage:**
→ https://account.mapbox.com/

---

## Questions for Client (quando testa)

1. Come preferisci uploadare immagini? Drag & drop o click to browse?
2. Vuoi auto-save drafts mentre scrivi articles?
3. Serve preview before publish per places/articles?
4. Come vuoi gestire duplicati quando importi CSV?

---

## Links

- **Lovable Project:** https://lovable.dev/projects/f4167f36-486e-4fcd-8f43-03ff1b511e74
- **Design Docs:** `side-projects/off-the-path/*.pdf`
- **CTO Report:** `CTO_REPORT_ANALYSIS.md`

---

**Ready to ship.** 🚀

Domani partiamo da dove preferisci — io suggerisco Opzione A (quick wins).
