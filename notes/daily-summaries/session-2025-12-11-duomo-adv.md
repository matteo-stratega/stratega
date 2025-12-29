# Session Report - 11 Dicembre 2025
## Duomo Design ADV Setup & Optimization

---

## Sommario Esecutivo

Prima sessione operativa completa sull'account Meta Ads di Duomo Design. Configurato accesso API, eseguita analisi YTD, creato agent dedicato, e avviata ottimizzazione campagne. Identificato problema con audience stale (2022) - risolto con creazione nuove audience da parte del cliente.

---

## Azioni Completate

### 1. Setup Infrastruttura
- [x] **Meta Ads API** - Token long-lived creato (scade 8 Feb 2025)
- [x] **Google Analytics** - Service account creato, in attesa accesso Editor da Duomo
- [x] **Agent creato** - `/agents/duomo-adv.md` con knowledge base completa
- [x] **Content Tracker** - `/projects/Duomo full 2025/CONTENT_TRACKER.md`

### 2. Analisi YTD
- **Spend totale:** €8,903
- **Lead totali:** 520
- **CPL medio:** €17.12
- **Trend:** Miglioramento drastico da Q1 (€118 CPL) a Q4 (€7-12 CPL)
- **Top performer:** IE Gladys wood (€6.69 CPL)
- **Worst performer:** Atlante (€20.04 CPL)

### 3. Ottimizzazioni Eseguite
- [x] **Pausa Atlante** (2 ads) - underperformer
- [x] **Riattivato Elettra** (2 ads) - top performer
- [x] **Riattivato Dress** con copy aggiornato (2 varianti)

### 4. Audience Work
- [x] Creato 4 LAL 1-5% (IE, FB Eng, IG Eng, Video 25%)
- [x] Creato adset Retargeting con IE Gladys wood
- [x] Attivato adset Retargeting → **ROLLBACK**
- [x] **Problema identificato:** Source audience del 2022 mai aggiornate
- [x] **Cancellate** 4 LAL create
- [x] **Pausato** adset retargeting
- [x] **Cliente ha creato** 3 nuove audience fresche:
  - FB Page Engagement 365 - Dec 2025
  - IG Page Engagement 365 - Dec 2025
  - Instant Experience Engagement 365 - Dec 2025

### 5. Audit Pixel
- Pixel attivo ma audience website tutte ~20 persone
- **Causa:** Consent banner + iOS 14.5 + manca CAPI
- **Soluzione:** Implementare Conversion API (backlog)

---

## Problemi Identificati

| Problema | Impatto | Soluzione | Status |
|----------|---------|-----------|--------|
| Audience 2022 stale | LAL su dati vecchi | Ricreate nuove | In popolamento |
| Pixel website ~20 persone | No retargeting website | CAPI da implementare | Backlog |
| LAL 5-10% troppo ampie | Performance = Broad | Sostituite con 1-5% | Da rifare domani |

---

## Best Practice Appresa

> **Prima di creare LAL, verificare che le source audience siano state aggiornate negli ultimi 6 mesi. Se >6 mesi, ricrearle.**

Da aggiungere all'agent.

---

## Stato Attuale Campagne

| Ad | Adset | Status | Note |
|----|-------|--------|------|
| Elettra - post 8/8 (x2) | Broad + LAL | ACTIVE | Top performer riattivato |
| Dress 23/9 (x2) | Broad + LAL | ACTIVE | Copy aggiornato |
| IE Gladys wood 30/4 | Broad | ACTIVE | Top performer |
| Atlante (x2) | Broad + LAL | PAUSED | Worst performer |
| Retargeting adset | - | PAUSED | In attesa audience nuove |

---

## Prossimi Step (Domani)

1. [ ] Verificare che le 3 audience siano popolate (~14k FB, ~7k IG, ~4k IE)
2. [ ] Creare LAL 1-5% da source fresche
3. [ ] Riattivare adset Retargeting con audience nuove
4. [ ] Check performance notturna ads attivi
5. [ ] Preparare card per nuova Instant Experience (Lera Soft)

---

## File Modificati/Creati

- `/agents/duomo-adv.md` - Agent ADV con reportistica e best practice
- `/projects/Duomo full 2025/CONTENT_TRACKER.md` - Tracker contenuti per modello
- `/projects/Duomo full 2025/Brief.md` - Aggiunto backlog task
- `/.credentials/meta-ads.json` - Credenziali Meta API
- `/.credentials/google-analytics-duomo.json` - Credenziali GA4

---

## Note per Prossima Sessione

- Audience in popolamento (alcune ore)
- Token Meta scade 8 Feb 2025 - reminder a fine Gennaio
- Annual Wrap-Up da fare fine Dicembre
- Integrazione Calendar in roadmap per reminder automatici

---

*Sessione: 11 Dicembre 2025*
*Durata: ~2 ore*
*Progetto: Duomo Design ADV*
