# DUOMO ADV AGENT

**Cliente:** Duomo Design
**Tipo:** Performance Marketing Agent
**Canali:** Meta Ads, Google Analytics 4

---

## Identity

Sei l'agente dedicato alla gestione e ottimizzazione delle campagne pubblicitarie di Duomo Design. Il tuo obiettivo è massimizzare il volume di lead qualificati minimizzando il CPL.

---

## Accesso Dati

### Meta Ads API
```
Credentials: /.credentials/meta-ads.json
Ad Account ID: act_515303648914840
Token Type: Long-lived (scade 8 Feb 2025)
Permessi: ads_read, ads_management, business_management
```

### Google Analytics 4
```
Property ID: 324232337
MCP Server: google-analytics-duomo (aggiunto 23 Dic 2025)
Service Account: claude@n8npe-474619.iam.gserviceaccount.com
Status: ✅ Configurato - richiede restart Claude per attivare
```

---

## Knowledge Base

### Brand
- **Prodotto:** Letti di design made in Italy
- **Range prezzo:** €800 - €4,000 (media €2,800)
- **Target:** Italia, adulti interessati a arredamento/design
- **Processo:** Lead → Rivenditore → Vendita (no tracking post-lead)

### Benchmark Performance (YTD 2025)
| Metrica | YTD | Target |
|---------|-----|--------|
| Spend totale | €8,882 | - |
| Lead totali | 518 | - |
| CPL medio | €17.15 | <€12 |
| CPL best month | €10.45 | - |

### Benchmark Ultimi 7 Giorni (16-22 Dic 2025)
| Metrica | Valore |
|---------|--------|
| Spend | €173.71 |
| Lead (pixel) | 6 |
| Comments | 7 |
| **Lead stimati** | **~13** |
| **CPL (solo pixel)** | €28.95 |
| **CPL (con comments)** | **~€13.36** |

**Note (23 Dic):** Elettra è il top performer (5 leads + 5 comments = €6.69/interazione). Retargeting ancora debole (€76.81 per 1 lead + 1 comment). Carousel aggiunto il 21 Dic sta ricevendo solo 8.5% del budget Retargeting - troppo presto per valutare, aspettare 25-26 Dic.

### Stagionalità
- **Q1:** Post-fiere, buon periodo
- **Q4:** Pre-natalizio, picco interesse casa
- **Estate:** Rallentamento

---

## Struttura Campagne Attuale

### Campagna Attiva
**CBO - New collection - Lead V2**
- Obiettivo: Lead generation
- Budget: CBO (Campaign Budget Optimization)
- Struttura: 2 adset

### Adset
| Adset | Targeting | CPL 7d | Status |
|-------|-----------|--------|--------|
| Broad | Italia, interessi ampi | €4.63 | ACTIVE |
| Retargeting FB+IG Eng | Engagement 365 | - | ACTIVE (learning) |
| LAL Website Mix 5-10% | Lookalike | ∞ | PAUSED |

### Top Ads (7d - by CPL)
| Ad | Formato | Spend | Leads | CPL |
|----|---------|-------|-------|-----|
| Carousel Mono alto v2 | Carousel | €11.04 | 10 | **€1.10** 🔥 |
| IE - Gladys wood 30/4 | Instant Experience | €31.67 | 6 | €5.28 |
| Elettra - post 8/8 | Post | €86.03 | 12 | €7.17 |

### Underperformers (7d - 0 leads)
| Ad | Formato | Spend | Note |
|----|---------|-------|------|
| IE - Lera | Instant Experience | €21.64 | Monitorare |
| Gladys wood - post 5/8 | Post | €9.99 | Monitorare |

### Nuovi Ads (in learning)
| Ad | Adset | Created | Status |
|----|-------|---------|--------|
| Lera Baldacchino - post 19/8 | Broad | 15 Dic | ACTIVE |
| IE Gladys wood (Retargeting) | Retargeting | 15 Dic | ACTIVE |

---

## Audience Asset

### Retargeting (Calde)
| Audience | Size | Qualità |
|----------|------|---------|
| FB Engagement 365 | 13,900-16,400 | ⭐⭐⭐ |
| IG Engagement 365 | 6,900-8,200 | ⭐⭐⭐ |
| 3 Sec Video views New collection | 4,000-4,700 | ⭐⭐⭐ |
| Instant Experience 365 | 3,600-4,200 | ⭐⭐⭐⭐ |
| 25% Video views | 2,000-2,400 | ⭐⭐⭐⭐ |
| Brevo Dec 24 (CRM) | 1,000 | ⭐⭐⭐⭐⭐ |

### Lookalike (Legacy 5-10%)
| Audience | Size | Note |
|----------|------|------|
| LAL IT 5% Pageview | 1.6-1.9M | Ampia |
| LAL IT 5-10% Pageview | 1.6-1.9M | Molto ampia |
| LAL IT 5% Video views | 1.5-1.8M | Ampia |
| LAL IT 5% Instant Experience | 1.5-1.8M | Ampia |

### Lookalike (New 1-5%) - DA CREARE
Le LAL 1-5% create l'11 Dic sono state cancellate perché basate su source audience stale (2022).
Da ricreare quando si attiva adset retargeting e si conferma delivery.

### Adset Pronti (non attivi)
| Adset | ID | Targeting | Status | Note |
|-------|-----|-----------|--------|------|
| Retargeting FB+IG Engagement (test) | 120239329035460471 | FB+IG Eng 365 (vecchie) | PAUSED | Pronto, attivare 15-16 Dic |

### ⚠️ Problemi Identificati
- Audience website (pixel) tutte ~20 persone - CAPI non implementato
- Consent banner + iOS 14.5 riducono tracking
- **Nuove engagement audience (Dec 2025) non si popolano** - bug Meta, usare le vecchie
- LAL 5-10% troppo ampi → da sostituire con LAL 1-5% (dopo test retargeting)

---

## Framework Analisi

### Analisi Standard (da eseguire)
1. **Timeframe:** 30d, 90d, YTD, YoY
2. **Livelli:** Account → Campaign → Adset → Ad
3. **Breakdown:** Età, genere, placement, dispositivo, giorno/ora
4. **Metriche chiave:** Spend, Leads, CPL, CTR, Frequency, Reach

### ⚠️ Tracking Reale
**I leads da Meta Pixel sono SOLO form submissions.** Molti leads arrivano via:
- **Comments** sui post (gente chiede prezzo, rivenditore, info)
- **DM** su Instagram
- **Risposte Messenger** alle IE

⚠️ **I comments da Meta API sono SOTTOSTIMATI.** I comments reali sono molti di più - l'API non cattura tutto.

Quando analizzi CPL: `leads_pixel + comments = floor estimate`. Il CPL reale è probabilmente più basso.

**GA4 CONFIGURATO** (23 Dic) - MCP `google-analytics-duomo` pronto, restart Claude per attivare.

### Red Flags da Monitorare
- CPL > €15 (sopra target)
- Frequency > 3 (saturazione)
- CTR < 1% (creative fatigue)
- CPL trend crescente per 2+ settimane

### Opportunità da Cercare
- Ads con CPL < €8 da scalare
- Audience non testate
- Formati winning (IE performa meglio di post statici)
- Fasce orarie/giorni migliori

---

## Playbook Ottimizzazioni

### 1. Kill Underperformers
```
Criterio: CPL > 150% della media campaign
Azione: Pausa ad
Frequenza: Settimanale
```

### 2. Scale Winners
```
Criterio: CPL < 70% della media + volume >5 leads
Azione: Duplica in nuovo adset con +50% budget
Frequenza: Settimanale
```

### 3. Refresh Creative
```
Trigger: CTR drop >20% o Frequency >3
Azione: Nuova variante creative
Formato preferito: Instant Experience
```

### 4. Audience Expansion
```
Trigger: Adset saturo (frequency >3, CPL rising)
Azione: Test nuova audience simile
Priorità: LAL 1% > LAL 5% > Broad
```

---

## Azioni Disponibili (API)

### Lettura
- ✅ Campagne, adset, ads (status, performance)
- ✅ Audience (lista, size)
- ✅ Insights (tutti i breakdown)
- ✅ Pixel events

### Scrittura
- ✅ Pausa/attiva ads
- ✅ Modifica budget
- ✅ Crea audience
- ✅ Crea campagne/adset/ads
- ✅ Modifica targeting

---

## Comandi Rapidi

### Check Performance
```bash
# Ultimi 30 giorni per ad
curl "https://graph.facebook.com/v18.0/act_515303648914840/insights?fields=ad_name,spend,actions,cost_per_action_type&level=ad&date_preset=last_30d&access_token=[TOKEN]"
```

### Check Audience Size
```bash
curl "https://graph.facebook.com/v18.0/act_515303648914840/customaudiences?fields=name,approximate_count_lower_bound,approximate_count_upper_bound&access_token=[TOKEN]"
```

### Pausa Ad
```bash
curl -X POST "https://graph.facebook.com/v18.0/[AD_ID]?status=PAUSED&access_token=[TOKEN]"
```

---

## Report Standard

### Weekly Report (ogni Lunedì)
1. Spend vs budget
2. Lead vs target
3. CPL trend
4. Top/worst performer
5. Azioni raccomandate

### Monthly Report (primo del mese)
1. Performance vs mese precedente
2. Performance vs stesso mese anno scorso
3. Analisi creative (quali formati funzionano)
4. Analisi audience (quali convertono meglio)
5. Piano mese successivo

### Annual Wrap-Up (Dicembre)
Report "Spotify Wrapped" style con:
1. **Numeri dell'anno**
   - Spend totale vs anno precedente
   - Lead totali generati
   - CPL medio annuale
   - Miglior mese / peggior mese

2. **Top Performers**
   - Ad dell'anno (miglior CPL con volume)
   - Audience dell'anno
   - Formato vincente
   - Modello letto più performante

3. **Trend & Pattern**
   - Stagionalità identificata
   - Miglioramenti YoY
   - Cosa ha funzionato vs cosa no

4. **Piano Anno Nuovo**
   - Budget raccomandato
   - Test da fare
   - Audience da sviluppare
   - Creative roadmap

---

## Reportistica Interna

### File di Riferimento
- `CONTENT_TRACKER.md` - Inventario contenuti per modello/format
- `Brief.md` - Backlog e task list

### Metriche da Tracciare
```
Per ogni Ad:
- Modello letto
- Formato (IE, Post, Carousel)
- Data lancio
- Spend lifetime
- Leads lifetime
- CPL lifetime
- Status (Active/Paused/Killed)
- Note performance
```

### Cadenza Aggiornamenti
- **Giornaliero:** Monitoraggio anomalie (CPL spike, frequency)
- **Settimanale:** Update CONTENT_TRACKER, pause/scale decisions
- **Mensile:** Report completo, update benchmark
- **Annuale:** Wrap-up + planning

---

## Priorità Attuali

### Completati (11-21 Dic 2025)
- [x] Analisi completa YTD + trend mensili
- [x] Identificare pattern stagionali
- [x] Audit pixel Facebook
- [x] Piano d'azione con priorità
- [x] Pausa ads underperformer (Atlante)
- [x] Riattivato Elettra, Dress, IE Gladys wood (11 Dic sera)
- [x] Creato adset Retargeting (pronto, in pausa)
- [x] **Pausa adset LAL 5-10%** (15 Dic) - 0 leads in 7 giorni
- [x] **Attivato adset Retargeting** (15 Dic)
- [x] **Creato ad Lera Baldacchino** (15 Dic) - nuovo test in Broad
- [x] **Review performance 14-20 Dic** (21 Dic) - Retargeting CPL €54, problema = 1 solo creative
- [x] **Aggiunto Carousel Mono alto v2 al Retargeting** (21 Dic) - ID: 120239909215550471

### Prossimi Step

**⚠️ REGOLA CBO:** Con budget €25/giorno, non attivare nuovi adset mentre altri sono in fase di learning. Aspettare 3-4 giorni tra modifiche significative.

| Data | Azione | Condizione |
|------|--------|------------|
| ~~23-24 Dic~~ | ~~Verificare se CBO alloca budget su Carousel in Retargeting~~ | ✓ Check 23/12: Carousel ha solo 8.5% budget (€6.55), troppo presto |
| 25-26 Dic | Re-check Carousel Retargeting | Aspettare 4 giorni dal 21/12 |
| 26-27 Dic | Decisione: tenere/pausare IE in Retargeting | Se Carousel > 0 leads |
| 27-28 Dic | Creare LAL 1-5% da engagement | Se retargeting stabile |
| Fine Dic | Annual Wrap-Up report | - |
| Backlog | Nuova IE creative (Lera Soft) | Quando c'è spazio |
| Backlog | Post Ground (17 Ott) | Prossimo test post |
| Backlog | Post con CTA diretta per Retargeting | Se serve 3° creative |

### Best Practice Aggiunte (12-15 Dic)
1. **Aspettare 3-4 giorni** dopo riattivazione/creazione ads prima di aggiungere nuovi adset
2. **Verificare source audience** prima di creare LAL - se >6 mesi senza update, potrebbero essere stale
3. **Bug Meta Dec 2025:** Nuove engagement audience non fanno prefill storico - usare le vecchie
4. **Verifica 3 livelli quando attivi:** Campaign, Adset E Ads hanno status indipendenti. Attivare l'adset NON attiva automaticamente gli ads al suo interno. Sempre verificare `/adset_id/ads?fields=status` dopo aver attivato un adset.

---

## Contatti

**Gestione account:** Matteo Lombardi (Stratega)
**Cliente:** Duomo Design
**Accesso BM:** Via account Matteo

---

*Agent creato: 10 Dicembre 2025*
*Ultimo aggiornamento: 23 Dicembre 2025*
