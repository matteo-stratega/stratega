# Session Closing - 16 Dicembre 2025 (session 4)
**Focus:** Academy Platform Review

---

## Pain Points Documentati (uTeach)

| Issue | Severity | Impact |
|-------|----------|--------|
| SMTP non funziona | Alto | No email automation |
| UX admin pessima | Alto | Landing page difficile da modificare |
| Supporto non attivo | Medio | Nessun aiuto quando serve |
| Integrazioni limitate | Medio | Mancano Zapier, Pabbly |
| Video buffering | Critico | Studente non riesce a vedere contenuto |
| UX studenti confusa | Alto | Login/iscrizione poco chiari |

**Status:** 7 corsi, 40 studenti registrati, LTD già pagata

---

## Discussione Build vs Buy

### Opzione Custom Stack (CTO Assessment)
```
Frontend:    Next.js / Astro (gratis)
Auth:        Supabase / Firebase (free tier)
Payments:    Stripe Checkout
Video:       YouTube unlisted / Bunny.net
Email:       Resend / Loops
```
**Effort stimato:** ~10 giorni lavoro
**Costo fisso:** €0-20/mese

### Decisione
Pending - raccogliere più learnings prima di switch

---

## Issue Risolto

### Video Buffering
- **Problema:** Studente con endless buffering su un modulo
- **Diagnosi:** Funziona per Matteo, non per studente → problema CDN/cache uTeach
- **Fix proposto:** Export da Screen Studio → YouTube unlisted → link diretto
- **Video trovati:** Tutti i 9 moduli in `/Users/matteolombardi/Screen Studio Projects/`

---

## Learnings Operativi

I pain points vissuti con uTeach sono **dati reali**, non fallimenti:
- Ogni "non funziona" = requisito per sistema futuro
- Chi teorizza non ha questi dati
- La frustrazione operativa ha valore strategico

**Nota Metis:** Includere riconoscimento learnings operativi nei closing, non solo task list.

---

## Pending

- [ ] Debug video buffering per studente (troubleshooting o YouTube workaround)
- [ ] Raccogliere recensioni sul contenuto (separato da platform UX)
- [ ] Creare onboarding chiaro per studenti (Loom + email)
- [ ] Testare Systeme.io in parallelo quando c'è tempo

---

## Asset Identificato

Video Academy tutti presenti in Screen Studio:
- `intro.screenstudio`
- `M1-Offering.screenstudio`
- `mod2-ICP.screenstudio`
- `m3-icp.screenstudio`
- `m4-content.screenstudio`
- `m5-copy.screenstudio`
- `m6-tools.screenstudio`
- `m7-ops.screenstudio`
- `m8-fin.screenstudio`

---

*Sessione: ~25 min*
*Produttiva: Sì - pain points documentati, video localizzati, direzione chiara*
