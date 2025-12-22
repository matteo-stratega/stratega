# PickEat Brain - Context File

**Last Updated:** 22 Dicembre 2025
**Purpose:** Stato corrente dell'azienda, decisioni chiave, context persistente tra sessioni

---

## 🎯 Focus Corrente

### Q4 2025 Priorities
1. **Varese Basket** - Pilot attivo, promo Natale 21 dic
2. **New client acquisition** - 110+ target Nord Italia identificati
3. **Content Engine** - 4 articoli pronti, calendario fino a Jan 21

### Questa Settimana (16-22 dic)
- [ ] Varese: ricevere codici voucher da Lorenzo
- [ ] Varese: contenuto social pre-partita (18-20 dic)
- [ ] Varese: partita 21 dic - promo voucher €10
- [x] Content: Blog Post #1 "20-Minute Problem" → HubSpot ✅
- [ ] Content: review Post #2 (Paper Stock List)

---

## 🏀 Clienti Attivi

### Varese Basket
- **Status:** Pilot attivo
- **Partite giocate:** 6 (G1-G6)
- **G6 Results (21 dic):** 14 ordini, €219.56 revenue, AOV €15.68
- **Voucher eligibili:** 2 (Davide Macchi, Catherine Flumiani) - email pronte
- **Problemi G6:** Hot dog sold out 40 min, bar chiuso 20 min intervallo
- **Prossima partita:** 3 gen vs Napoli
- **Contatto:** Lorenzo Gaudina (marketing)
- **Files:** `clients/varese/`

### UYBA Volley
- **Status:** In standby
- **Note:** Da riattivare post-Varese

---

## 👥 Team & Ruoli

| Nome     | Ruolo            | Note                     |
| -------- | ---------------- | ------------------------ |
| Matteo   | CEO/Founder      | Decision maker           |
| Giacomo  | Co-founder/Ops   | On-site events           |
| Asim     | Developer        | Unico dev, NON tech lead |
| Stephane | Advisor (Sales)  | Welcome post pending     |
| Federico | Investor/Advisor | Welcome post pending     |

---

## 📝 Content Engine Status

### Blog Articles (4 READY)
1. The 20-Minute Problem → Dec 17 ✅ **PUBBLICATO**
2. Paper Stock List Problem → Dec 31
3. Exhibition Centers F&B → Jan 14
4. 2026 F&B Trends → Jan 21

### HubSpot Blog Integration
- **Status:** Manual (HTML copy-paste)
- **File ready:** `outputs/content-engine/blog/the-20-minute-problem-HUBSPOT-READY.html`
- **TODO:** Creare workflow automatico (n8n o API)

### Welcome Posts
- Asim → Dec 10 ✅ PUBBLICATO
- Stephane → Pending risposte
- Federico → Pending risposte

### Voice
- **Alex Ferretti** - Copywriter persona
- Style: Conversational, data-driven, ex sports journalist
- Rules: No AI words (delve, realm, harness...), Italian naturale

---

## 🎯 Sales Pipeline

### Varese Promo 21 Dic
- Budget: €300-500 (voucher)
- Meccanica: Ordine ≥€25 = Voucher €10 shop
- Status: Approvato, attesa codici da Lorenzo/Max

### New Targets (Nord Italia)
- 110+ target identificati in 6 categorie
- Focus: Mercatini, eventi food, organizzatori
- File: `outputs/NORTHERN_ITALY_EVENT_TARGETS_WINTER_2025.md`

### Music Venues
- 28 contatti in HubSpot
- Status: Pausa - email generiche non rispondono

---

## 💡 Decisioni Chiave Recenti

| Data | Decisione | Rationale |
|------|-----------|-----------|
| 22/12 | GA MCP configurato | Service account `claude@n8npe-474619`, Property ID 467442633 |
| 19/12 | Benedetto XIV renewal | €495 closed won (€99/mese fino apr) |
| 19/12 | CRM cleanup massivo | 11 deal closed lost, pipeline pulita |
| 18/12 | Asim review → fine gennaio | 6 mesi, observation period |
| 18/12 | Hiring dev #2 pausa | Budget pending (Biper/Apex/Corengers) |
| 11/12 | No hostess Varese | Tigros sponsor blocca |
| 04/12 | Cut Article 3 (Vendor Coordination) | ICP mismatch |
| 04/12 | Voucher digitali > gadget fisici | Zero logistica |
| 03/12 | Pivot target: eventi laterali | Fiere troppo lente |

---

## 🚫 Cose da NON Fare

1. **Asim NON è tech lead** - È dev, non chiamarlo lead
2. **No fake stories** - Alex non inventa esperienze personali
3. **No traduzione letterale** - Italiano naturale, non word-by-word
4. **Revenue > Brand** - Priorità a tasks revenue-generating
5. **Quando i dati non tornano → CHIEDI** - Non inventare

---

## 📁 Folder Structure

```
pickeat/
├── agents/          # Agent definitions
├── brain/           # This context + memory
├── clients/         # Client-specific work
│   └── varese/
├── docs/            # Protocols, guides
├── outputs/         # Generated outputs
│   ├── competitive-intel/
│   └── content-engine/
├── task/
│   └── daily-summaries/
└── templates/
```

---

## 🔄 Session Protocol

### Start
1. Read latest `closing-*.md`
2. Read `brain/context.md` (this file)
3. Ask: "Confermi priorità o cambiamo?"

### Close
1. Update `brain/context.md` con cambi significativi
2. Write `closing-DDMMYY.md`

---

## 📊 Key Metrics to Track

### Varese
- Ordini/partita (target: 50)
- AOV (target: €25)
- Revenue/partita (target: €1,250)

### Content
- Post pubblicati vs planned
- Engagement LinkedIn

### Sales
- Outreach sent
- Response rate
- Meetings booked

---

*Aggiornare questo file a fine sessione se ci sono cambi significativi*
