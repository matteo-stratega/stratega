# Session Report - 12 Dicembre 2025
## Duomo Design ADV - Follow-up

---

## Sommario Esecutivo

Sessione di follow-up per verificare stato audience create ieri. Identificato bug Meta: nuove engagement audience non fanno prefill storico. Decisione di usare audience vecchie (2022) che hanno size corretta. Creato adset retargeting ma pausato per rispettare regola CBO (aspettare 3-4 giorni dopo riattivazione ads).

---

## Problema Identificato

### Bug Meta Engagement Audience (Dic 2025)
Le 3 audience create ieri dal cliente non si sono popolate:

| Audience | Size Attesa | Size Attuale | Status |
|----------|-------------|--------------|--------|
| FB Page Engagement 365 - Dec 2025 | ~14,000 | 1,000 | Code 300 - Too small |
| IG Page Engagement 365 - Dec 2025 | ~7,000 | 1,000 | Code 200 - Ready |
| Instant Experience Engagement 365 - Dec 2025 | ~4,000 | 1,000 | Code 300 - Too small |

**Causa:** Meta sembra aver cambiato il comportamento di prefill. Le audience vecchie (2022) hanno i dati storici, le nuove partono da zero.

**Soluzione:** Usare le audience vecchie (2022) che hanno size corretta:
- FB Engagement 365: 13,900-16,400
- IG Engagement 365: 6,900-8,200

---

## Azioni Eseguite

1. **Creato adset Retargeting** (ID: 120239329035460471)
   - Targeting: FB + IG Engagement 365 (audience 2022)
   - Ad: IE Gladys wood 30/4
   - Status: **PAUSED**

2. **Pausato immediatamente** - Rispettare regola CBO
   - Ieri sera riattivati Elettra, Dress, IE Gladys
   - Con €25/giorno non aggiungere adset mentre altri in learning
   - Aspettare 3-4 giorni

3. **Aggiornato agent** con:
   - Nuova pianificazione scaglionata
   - Best practice CBO
   - Documentazione bug Meta audience

---

## Pianificazione Rivista

| Data | Azione | Condizione |
|------|--------|------------|
| 11 Dic | Riattivati Elettra, Dress, IE Gladys | ✅ Done |
| **15-16 Dic** | Attivare adset Retargeting | Se ads attuali stabilizzati |
| 18-19 Dic | Review performance retargeting | Se delivery OK |
| 19-20 Dic | Creare LAL 1-5% da engagement | Se retargeting funziona |
| 20-21 Dic | Attivare adset LAL 1-5% | Se retargeting stabile |
| Fine Dic | Annual Wrap-Up report | - |

---

## Best Practice Aggiunte

1. **Regola CBO con budget limitato:** Non attivare nuovi adset mentre altri sono in fase di learning. Aspettare 3-4 giorni tra modifiche significative.

2. **Verificare source audience:** Prima di creare LAL, controllare che le source audience siano state aggiornate negli ultimi 6 mesi.

3. **Bug Meta Dec 2025:** Nuove engagement audience non fanno prefill storico - usare le vecchie se disponibili.

---

## Stato Attuale

### Ads Attivi (in learning)
- Elettra - post 8/8 (x2)
- Dress 23/9 (x2) - copy aggiornato
- IE Gladys wood 30/4

### Adset Pronti (pausati)
- Retargeting FB+IG Engagement (ID: 120239329035460471)

### LAL da Creare
- LAL 1-5% da rifare dopo test retargeting (le precedenti cancellate)

---

## Prossima Sessione

**Data:** 15-16 Dicembre 2025

**Agenda:**
1. Check performance ads riattivati (Elettra, Dress, IE Gladys)
2. Se stabilizzati → Attivare adset Retargeting
3. Monitorare delivery retargeting

---

*Sessione: 12 Dicembre 2025*
*Durata: ~30 min*
*Progetto: Duomo Design ADV*
