# Off the Curious Path — CTO Analysis & Architecture Report
*Generated: 25 Nov 2025*

---

## Executive Summary

**Status:** 🟢 CMS già funzionante al 70% — Serve ottimizzazione e feature mancanti critiche

**Stack:**
- Frontend: React + TypeScript + Vite + shadcn-ui
- Backend: Supabase (PostgreSQL + Auth + Storage + RLS)
- Map: Mapbox GL JS / MapLibre GL
- Deployment: Lovable (possibile migrazione ad Antigravity)

**Architettura attuale vs. Design Doc:** ✅ 7/10 match

---

## 1. COSA C'È GIÀ (Audit Completo)

### ✅ CMS Admin Panel Funzionante

**Route:** `/admin`

**Features implementate:**
1. **Places Management**
   - ✅ CRUD completo (Create, Read, Update, Delete)
   - ✅ CSV Bulk Import
   - ✅ Bulk Delete
   - ✅ Bulk Publish/Unpublish
   - ✅ Form completo con validation (Zod)
   - ✅ Preview & Edit

2. **Articles Management**
   - ✅ CRUD completo
   - ✅ Bulk operations
   - ✅ Rich text content
   - ✅ Slug auto-generation
   - ✅ Published/draft system

3. **Settings**
   - ✅ Mapbox Token configuration

### ✅ Database Schema (Supabase)

**Tables:**
```sql
places
├─ id (uuid, pk)
├─ title, slug (unique), category, cuisine
├─ lat, lng (geocoordinates)
├─ address, district, neighborhood
├─ price, rating, vibe[], tags[]
├─ comment, note, why_go, short_description
├─ image_url, instagram, website, hours
├─ is_published (boolean)
└─ created_at, updated_at

articles
├─ id (uuid, pk)
├─ title, slug (unique), excerpt, content
├─ cover_image, author, tags[]
├─ published_at
└─ created_at, updated_at

settings
├─ key (mapbox_token, etc.)
└─ value

experiences (non in uso)
user_roles, profiles (auth infrastructure, non attiva)
```

### ✅ Frontend Pages

- `/` → Homepage
- `/map` → Interactive Map with filters
- `/place/:id` → Place Detail
- `/article/:slug` → Article Detail
- `/saved` → Saved places (user feature)
- `/admin` → CMS Panel
- `/auth` → Auth page (non attiva)

### ✅ Map Features

**Mapbox Integration:**
- ✅ Clustering markers
- ✅ Custom popups
- ✅ Filters: category, district, vibe, price, rating, search
- ✅ Real-time filter sync
- ✅ Mobile responsive

---

## 2. COSA MANCA (Critical Gaps)

### 🔴 CRITICHE (Blockers per produzione)

#### 1. **Security & Authentication**
**Problema:** Le RLS policies sono pubbliche.
```sql
-- ATTUALE (pericoloso!)
CREATE POLICY "Anyone can insert articles" ON articles FOR INSERT WITH CHECK (true);
CREATE POLICY "Anyone can update articles" ON articles FOR UPDATE USING (true);
CREATE POLICY "Anyone can delete articles" ON articles FOR DELETE USING (true);
```

**Impact:** Chiunque può modificare/cancellare tutto il database.

**Soluzione richiesta:**
- Implementare Supabase Auth
- Creare ruolo `admin`
- RLS policies basate su `auth.uid()` con check ruolo
- Password-protect `/admin` route

#### 2. **Geocoding Automatico**
**Problema:** Lat/lng devono essere inseriti manualmente nel form.

**Impact:** UX terribile per chi gestisce il CMS — deve andare su Google Maps, copiare coordinate.

**Soluzione:**
- Integrare Mapbox Geocoding API
- Input "Address" → auto-fetch lat/lng
- Preview mappa nel form per verificare posizione
- Fallback manuale se geocoding fallisce

#### 3. **Image Upload System**
**Problema:** `image_url` è un campo testo — devono caricare immagini altrove e incollare URL.

**Impact:** Workflow complesso, dipendenza da servizi esterni.

**Soluzione:**
- Supabase Storage bucket `place-images/` e `article-images/`
- Drag & drop upload nel form
- Auto-resize/optimize (max 1920px, WebP conversion)
- CDN URLs

### 🟡 IMPORTANTI (UX & Product)

#### 4. **Neighborhoods Table Missing**
**Design doc richiede:**
```sql
neighborhoods
├─ id, name, slug
├─ description, image_url
```

**Attuale:** Solo campo `district` in places.

**Soluzione:** Creare table + UI per gestire quartieri come entità separate.

#### 5. **Events Section** (Fase 2 — non urgente)
Menzionato nel design ma non implementato.

#### 6. **Rich Text Editor per Articles**
**Attuale:** Textarea semplice per `content`.

**Soluzione:** Integrare Tiptap o Lexical editor con:
- Formatting (bold, italic, lists, links)
- Embed places (mention @PlaceName → auto-link)
- Image inline upload

#### 7. **SEO Meta Fields**
Mancano: `meta_description`, `og_image`, `canonical_url` per articles e places.

---

## 3. ARCHITETTURA PROPOSTA (Miglioramenti)

### Database Schema Updates

```sql
-- 1. Add geocoding cache
ALTER TABLE places ADD COLUMN geocoded_at TIMESTAMP;
ALTER TABLE places ADD COLUMN geocode_confidence FLOAT;

-- 2. Add image metadata
ALTER TABLE places ADD COLUMN image_width INT;
ALTER TABLE places ADD COLUMN image_height INT;

-- 3. Add SEO fields
ALTER TABLE articles ADD COLUMN meta_description TEXT;
ALTER TABLE articles ADD COLUMN og_image TEXT;

-- 4. Add admin audit log
CREATE TABLE admin_actions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES auth.users(id),
  action TEXT, -- 'create', 'update', 'delete'
  table_name TEXT,
  record_id UUID,
  changes JSONB,
  created_at TIMESTAMP DEFAULT now()
);

-- 5. Neighborhoods as first-class entity
CREATE TABLE neighborhoods (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  slug TEXT UNIQUE NOT NULL,
  description TEXT,
  image_url TEXT,
  bounds GEOGRAPHY(Polygon, 4326), -- GeoJSON polygon
  created_at TIMESTAMP DEFAULT now()
);

ALTER TABLE places ADD COLUMN neighborhood_id UUID REFERENCES neighborhoods(id);
```

### CMS Enhancement Roadmap

**Priority 1 (Settimana 1):**
1. ✅ Auth sistema + RLS policies
2. ✅ Geocoding automatico
3. ✅ Image upload

**Priority 2 (Settimana 2):**
4. Rich text editor (Tiptap)
5. Neighborhoods management
6. SEO meta fields

**Priority 3 (Fase 2):**
7. Events section
8. Bulk image upload
9. Analytics dashboard

---

## 4. MAPBOX WORKAROUND OPTIONS

**Opzione A: Mapbox (Attuale)**
- ✅ Già integrato
- ✅ Ottima UX
- ❌ Costo: $0 fino a 50K map loads/mese, poi $5/1K loads
- **Consiglio:** OK per MVP e primi 6 mesi

**Opzione B: MapLibre GL + Maptiler**
- ✅ Open source
- ✅ Più economico ($49/mese per 100K loads)
- ⚠️ Richiede cambio API keys
- **Consiglio:** Se scaling > 50K/mese

**Opzione C: Google Maps**
- ✅ Geocoding gratuito (fino a 40K richieste/mese)
- ❌ Map display costoso ($7/1K loads)
- **Consiglio:** No, troppo costoso

**DECISIONE:** Mantenere Mapbox per ora. Monitorare usage. Switch a MapLibre se > 40K loads/mese.

---

## 5. LOVABLE vs ANTIGRAVITY

**Lovable (Attuale):**
- ✅ Deploy automatico
- ✅ UI-first workflow
- ❌ Vendor lock-in
- ❌ Customization limitata

**Antigravity:**
- ✅ Più controllo su infrastruttura
- ✅ Git-based workflow
- ⚠️ Richiede setup iniziale

**CONSIGLIO:**
- Rimani su Lovable per MVP e test con utenti
- Migra ad Antigravity quando hai > 100 users attivi/settimana
- Setup git repository locale sin da ora per backup code

---

## 6. NEXT STEPS (Prioritized)

### Immediate (Questa settimana)
1. **Implementa Auth + RLS**
   - Supabase Auth con Magic Link
   - Admin role check
   - Protect `/admin` route

2. **Geocoding automatico**
   - Mapbox Geocoding API
   - Auto-fetch lat/lng da address input
   - Preview map in form

3. **Image Upload**
   - Supabase Storage setup
   - Drag & drop component
   - Auto WebP conversion

### Short-term (Prossime 2 settimane)
4. Neighborhoods management UI
5. Rich text editor per articles
6. SEO meta fields

### Medium-term (Prossimo mese)
7. Events section (se richiesto)
8. Analytics dashboard basic
9. Mobile app PWA setup

---

## 7. CODEBASE HEALTH CHECK

**✅ Punti di Forza:**
- TypeScript strict mode
- shadcn-ui components (ottima DX)
- React Query per data fetching
- Supabase integration pulita
- Form validation con Zod

**⚠️ Tech Debt:**
- Nessun error boundary React
- Nessun Sentry/error tracking
- Nessun analytics setup
- Manca testing suite (Vitest recommended)

**📊 Code Quality:** 7/10

---

## 8. COST ESTIMATION (Monthly)

**MVP Phase (0-500 users/mese):**
- Supabase: $0 (free tier fino a 500MB DB + 1GB storage)
- Mapbox: $0 (free tier fino a 50K loads)
- Lovable: ~$20/mese (se hosting a pagamento)
- **Total: ~$20/mese**

**Growth Phase (500-5K users/mese):**
- Supabase: $25/mese (Pro plan)
- Mapbox: ~$50/mese (100K loads stimati)
- Domain + CDN: $15/mese
- **Total: ~$90/mese**

---

## 9. DEPLOYMENT CHECKLIST

Prima di andare in produzione:
- [ ] Enable Supabase Auth
- [ ] Setup RLS policies corrette
- [ ] Configurare Mapbox production token
- [ ] Setup custom domain
- [ ] Enable HTTPS
- [ ] Setup error tracking (Sentry)
- [ ] Setup analytics (Plausible/Fathom)
- [ ] Backup strategy per DB
- [ ] Rate limiting su API endpoints
- [ ] SEO meta tags su tutte le pagine

---

## 10. CONCLUSIONI

**Stato attuale:** CMS funzionante ma non production-ready.

**Urgenza:**
1. 🔴 Security (Auth + RLS) — **CRITICAL**
2. 🟡 Geocoding + Image upload — **High impact UX**
3. 🟢 Resto può aspettare post-MVP

**Timeline realistico per produzione:**
- Con focus full-time: 1 settimana
- Con focus part-time: 2-3 settimane

**Raccomandazione finale:**
Il progetto è **ben architettato** e **75% completo**. Mancano feature critiche di sicurezza e UX ma niente di insormontabile. Con 1 settimana di lavoro mirato puoi lanciare in produzione.

---

**Prossimo step:** Vuoi che implementi le 3 feature urgenti (Auth, Geocoding, Image Upload) oppure preferisci un'altra priorità?
