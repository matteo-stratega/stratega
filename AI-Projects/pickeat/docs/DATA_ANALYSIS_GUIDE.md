# Data Analysis Guide

**Purpose:** Come analizzare dati PickEat (ordini, analytics, performance)

---

## Fonti Dati Disponibili

### 1. Ordini Varese
- **Location:** `clients/varese/data/`
- **Format:** CSV export da dashboard
- **Script:** `python3 scripts/analyze_varese.py`

### 2. Google Analytics
- **Access:** Matteo deve dare accesso
- **Metriche chiave:**
  - Sessions per page (/varese, /cart, /checkout)
  - Conversion funnel
  - Device breakdown (iOS vs Android)

### 3. Store Merch (Varese)
- **File:** `clients/varese/data/varese-store-merch.csv`
- **Contains:** Products, prices, availability

---

## Analisi Comuni

### Performance Partita
```python
# Input: CSV ordini partita
# Output:
# - Totale ordini
# - Revenue
# - AOV (Average Order Value)
# - Peak ordering time
# - Top products
```

### Funnel Analysis
```
/varese → /cart → /checkout → order
   ↓        ↓         ↓
  182      55        17     (example from G2-G3)

Conversion rates:
- Visit → Cart: 30%
- Cart → Checkout: 31%
- Checkout → Order: [varies by tracking]
```

### Week-over-Week
```
| Game | Orders | Revenue | AOV |
|------|--------|---------|-----|
| G1   | 10     | €180    | €18 |
| G2   | 13     | €234    | €18 |
| G3   | 8      | €144    | €18 |
```

---

## Quick Commands

### Analyze CSV
```bash
python3 scripts/analyze_varese.py clients/varese/data/orders.csv
```

### Count rows
```bash
wc -l clients/varese/data/*.csv
```

### View headers
```bash
head -1 clients/varese/data/orders.csv
```

---

## Metriche Target

### Per Partita
| Metric | Current | Target | Stretch |
|--------|---------|--------|---------|
| Orders | 10-13 | 35 | 50 |
| Revenue | €180-234 | €630 | €1,250 |
| AOV | €18 | €18 | €25 |

### Conversion Funnel
| Step | Current | Target |
|------|---------|--------|
| Visit → Cart | 30% | 40% |
| Cart → Order | ~10% | 20% |

---

## Data Requests

### Per analisi serve:
1. **Export ordini** da dashboard PickEat
2. **GA access** per funnel completo
3. **Timing data** per capire peak ordering

### Chi chiedere:
- Ordini export: Asim o dashboard
- GA: Matteo
- Varese specifico: Lorenzo

---

*Last updated: 17 Dec 2025*
