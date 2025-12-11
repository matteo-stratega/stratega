# Google Sheets Audit Report
**Date:** 2025-11-26
**Round:** Archivista Round 2
**Total Sheets in Root:** 56 (all 173B symlinks/shortcuts)

---

## Executive Summary
- 56 Google Sheets shortcuts in root directory
- Identified 12+ suspected duplicates and redundancies
- Estimated 20-25% consolidation opportunity
- Most active: Regional market data (10 sheets)
- Most redundant: Hotel project, BIT data, Proiezioni template

---

## Category Breakdown

### 1. REGIONAL/GEOGRAPHIC PROSPECT DATA (10 sheets)
**Status:** ACTIVE - Keep all
- Lombardia.gsheet
- Centro italia.gsheet
- Sud Italia.gsheet
- Sardinia.gsheet
- Madeira.gsheet
- Portugal.gsheet
- Greece.gsheet
- Spain - NA - Smartlead.gsheet
- Swiss Li.gsheet
- Puglia 2022.gsheet

**Note:** These appear to be market research datasets by region. Keep in root for easy access.

---

### 2. STRATEGIC/INTERNAL PLANNING (5 sheets)
**Status:** KEEP - Stratega operational
- Audience Roadmap.gsheet
- Stratega - List of improvements and to do.gsheet
- Stratega - Website.gsheet
- Tracking Plan - Strategav2.gsheet
- Content ranker.gsheet

**Action:** Consider moving to `/templates/` or `/research/` if mature

---

### 3. FINANCIAL/PRICING (4 sheets)
**Status:** KEEP - Active tracking
- Payments Due.gsheet
- Price per hour.gsheet
- CD previsions.gsheet
- Treasury Managers Emea 2024-06-14T14:42:15.911Z.gsheet

**Action:** Treasury sheet may be old (2024) - verify if still active

---

### 4. EVENT/CONFERENCE LEADS (4 sheets)
**Status:** KEEP - Project data
- Event managers_MWC.gsheet
- Eventi Web Summit.gsheet
- Web Summit leads.gsheet
- Demo Day Likers.gsheet

**Note:** Web Summit appears twice - possibly different purposes. Request clarification.

---

### 5. HOTELS/HOSPITALITY PROJECT (3 sheets)
**SUSPECTED DUPLICATES - CONSOLIDATION NEEDED**
- 201F_- Hotel - 3.3-4.0s Lombardia OS Sequence Report.gsheet
- OS - Lombardia - Hotels for email - 201F - Hotel - 3.3-4.0s - w_web&email.gsheet
- Hotel Managers - Italy.gsheet

**Analysis:** First two sheets contain identical project identifiers (201F, Hotel, 3.3-4.0s, Lombardia). Likely same data with different processing/purposes.

**Recommendation:**
- Audit both sheets for content difference
- Keep one, archive or delete other
- Archive third sheet (Hotel Managers) if distinct project

---

### 6. TEMPLATE/INSTANCE PAIRS (4 sheets)
**SUSPECTED DUPLICATES**
- **Proiezioni Pistoia.gsheet** ← Instance of Proiezioni Template
- Proiezioni Template.gsheet
- Tag template.gsheet
- Template $.gsheet

**Recommendation:**
- Move Pistoia instance to `/archive/projects/` or client folder
- Keep templates in root or move to `/templates/`

---

### 7. BIT VENDOR DATA (2 sheets)
**LIKELY DUPLICATES**
- BIT Leads.gsheet
- BIT.gsheet

**Recommendation:**
- Verify if one is subset of other
- Consolidate to single file
- Archive redundant copy

---

### 8. BUSINESS ANGEL/STARTUP (2 sheets)
**POSSIBLY RELATED**
- Business Angel Scraping + Validation 2024-07-12T15:30:29.659Z.gsheet
- Business Discovery.gsheet

**Recommendation:** Review for consolidation opportunity (60% confidence)

---

### 9. AGRICULTURE/TOURISM (3 sheets)
**Status:** Project-specific data
- Agriturismi Saturnia - .gsheet
- Expoplaza-Ricettività.gsheet
- Food Truck Festivals.gsheet

**Recommendation:** Keep or move to `/archive/projects/` depending on active status

---

### 10. VENDOR/LEAD FOLLOW-UP (2 sheets)
**Status:** Active tracking
- WS Leads.gsheet
- WMF Follow Up.gsheet

**Recommendation:** Keep (distinct purposes)

---

### 11. DATA EXPORTS/RESEARCH (3 sheets)
**Status:** Historical data
- DB_enriched_raw_PJ_SIB.gsheet (with timestamp)
- Outscraper search.gsheet
- Startup KW IT - Nerual Text.gsheet

**Recommendation:** Consider moving to `/data/` directory

---

### 12. OLD/TEST DATA (2 sheets)
**Status:** ARCHIVE CANDIDATES
- LinkedIn Profile via Magical.gsheet (test/old)
- startup-it-it-suggestions-answerthepublic.gsheet (old research)

**Recommendation:** Move to `/archive/` if not actively used

---

### 13. ENTERTAINMENT/MISC (4 sheets)
**Status:** Project-specific
- Ac Dc.gsheet
- Basket - Ita - A.gsheet
- Hashtag Instagram - Kandemic.gsheet
- IS - Renewable energy.gsheet

**Recommendation:** Keep if active, archive if not

---

### 14. MARKETING/SEO/PARTNER (4 sheets)
**Status:** Project-specific
- SEO Content Strategy USA.gsheet
- Partner form Ita.gsheet
- BYD - Changes to do.gsheet
- Influencer lists.gsheet
- Orari per campagne.gsheet
- WSUProfiles.gsheet

**Recommendation:** Keep if active, move to `/templates/` if reusable

---

### 15. CLIENT PROPOSALS (1 sheet)
**Status:** Historical
- Stratega for Total Stunts Ireland - Business Proposal (Draft final).gsheet

**Recommendation:** Move to `/archive/projects/clients/` or relevant project folder

---

## Duplicate Candidates Summary

| Priority | Duplicate Pair | Confidence | Action |
|----------|---|---|---|
| HIGH | Proiezioni Pistoia vs Template | 100% | Archive Pistoia → projects/ |
| HIGH | 201F Hotel sheets (2) | 95% | Consolidate to 1, archive other |
| MEDIUM | BIT Leads vs BIT | 70% | Consolidate to 1 |
| MEDIUM | Business Angel vs Discovery | 60% | Audit then consolidate |
| LOW | Web Summit leads vs Eventi | 50% | May have different purposes |

---

## Recommended Actions

### Immediate (do not delete, just organize):
1. **Move to `/archive/projects/`:**
   - Proiezioni Pistoia.gsheet
   - Hotel manager sheets (if distinct from 201F project)
   - Client proposal sheets
   - Old test sheets (LinkedIn Profile via Magical, startup-it-it...)

2. **Move to `/templates/` (if mature/reusable):**
   - Proiezioni Template.gsheet
   - Tag template.gsheet
   - Template $.gsheet

3. **Consolidate (review then archive duplicate):**
   - BIT Leads.gsheet + BIT.gsheet → keep one
   - 201F Hotel sheets (2) → keep one
   - Business Angel + Business Discovery → optional

### Secondary (after review):
1. Move data exports to `/data/` if consolidating
2. Create project-based organization structure
3. Update project trackers if sheets reorganized

---

## Questions for Matteo

1. **201F Hotel sheets:** Are these two sheets for same project with different purposes, or complete duplicates? → Archive or consolidate?

2. **Web Summit data:** Do `Web Summit leads` and `Eventi Web Summit` serve different purposes, or are they redundant?

3. **Old sheets:** Are `LinkedIn Profile via Magical` and `startup-it-it-suggestions-answerthepublic` actively used?

4. **BIT data:** Are `BIT Leads` and `BIT` different, or can they be consolidated?

5. **Project-based org:** Would you like regional sheets moved to a `/data/market-research/` folder?

---

## Next Steps

**Round 2 Actions:**
- Archive identified old/test sheets
- Consolidate BIT sheets (user decision)
- Consolidate hotel sheets (user decision)
- Create `/projects/` folder structure for client/project data

**Impact:**
- Current: 56 sheets in root
- Target: 40-45 sheets (15-20% reduction)
- New structure: Regional data in root, projects in folders, old data archived

---

**Generated:** 2025-11-26
**Status:** Ready for review + action
