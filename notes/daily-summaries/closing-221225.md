# Closing 22/12/2025

## TL;DR
- **Fixed**: Lovable sync issue (merged feature branch → main)
- **Fixed**: Auth disabilitata per testing partner
- **Discovered**: Dual-Supabase situation (Lovable vs nostro)
- **Improved**: CLAUDE.md con infra docs + CTO session protocol
- **Duomo**: Check ads, agent file aggiornato, MCP GA4 configurato

## Off The Path - Session Details

### Problem 1: Lovable non mostrava le modifiche
**Causa**: I commit erano su `feature/mvp-core-features`, ma Lovable sincronizza solo `main`.

**Fix**: Merged feature → main (fast-forward, zero conflitti)
```
a5b560d Enable auth protection for admin routes
ce12010 Major UX refresh: Branding, SEO, Footer, Admin enhancements
```

### Problem 2: Auth bloccava /admin
**Causa**: ProtectedRoute richiedeva login, ma partner deve testare.

**Fix**: Rimosso wrapper ProtectedRoute temporaneamente. Commit: `bd07041`

### Discovery: Due Supabase diversi

| Environment | Project ID | Stato |
|-------------|------------|-------|
| Lovable (prod) | `casprhxtfzjlnzmfceiy` | 174 places |
| Nostro (dev) | `facdxrllyilohbubdrtc` | Vuoto |

**Perché**: .env locale punta al nostro, ma non è committato. Lovable usa il suo da Git.

**Pending**: Decisione su quale usare (aspetta risposta partner).

### Improvement: CTO Agent Memory
User ha fatto notare che il CTO avrebbe dovuto sapere della situazione dual-Supabase.

**Fix**: Aggiornato CLAUDE.md con:
- Sezione Infrastructure con warning ⚠️
- Protocollo sessione: "aggiorna CLAUDE.md se scopri infra"
- Decision Log aggiornato

## Files Modified
- `off-the-path/codebase/src/App.tsx` - Auth disabled
- `off-the-path/CLAUDE.md` - Infrastructure docs, session protocol

## Commits Pushed
- `bd07041` Disable auth protection on /admin (temporary)
- Merge `feature/mvp-core-features` → `main`

## Pending
- [ ] Decisione Supabase (Lovable vs nostro) - aspetta partner
- [ ] Riattivare auth prima di prod
- [ ] Inviare reclamo commercialista (da context.md)
- [ ] Proroga tarifa plana IMPORTASS

---

## Duomo ADV - Session 2 (23 Dic)

### Check Ads Performance (16-22 Dic)

| Adset | Spend | Leads (pixel) | Comments | CPL stimato |
|-------|-------|---------------|----------|-------------|
| Broad | €96.90 | 5 | 6 | ~€8.81 |
| Retargeting | €76.81 | 1 | 1 | ~€38.40 |

**Top performer:** Elettra (€66.87 → 5 leads + 5 comments = ~€6.69/interazione)

**Carousel Retargeting:** Aggiunto 21 Dic, riceve solo 8.5% del budget (€6.55). Troppo presto per valutare → re-check 25-26 Dic.

### Agent File Updates
- ✅ Aggiunta sezione "Tracking Reale" (comments = leads non tracciati da pixel)
- ✅ Nota: comments da Meta API sono sottostimati
- ✅ Benchmark aggiornato con comments inclusi
- ✅ Prossimi step aggiornati

### GA4 Configuration
- ❌ MCP GA4 puntava a PickEat, non Duomo
- ✅ Aggiunto MCP `google-analytics-duomo` (property 324232337)
- ⚠️ Richiede restart Claude per attivare

### Files Modified
- `agents/duomo-adv.md` - Tracking reale, benchmark, GA4 config

### Pending Duomo
- [ ] Re-check Carousel Retargeting (25-26 Dic)
- [ ] Test GA4 Duomo dopo restart Claude
- [ ] Annual Wrap-Up report (fine Dic)

---
**Session Status**: Completed
**Agents**: CTO → Duomo ADV
**Prepared by**: Metis
