# Stratega OS - Comprehensive File Reorganization Plan

**Date:** November 14, 2025
**Analyst:** Digital Asset Manager & Information Architect
**Scope:** /Users/matteolombardi/AI-Projects/stratega (16GB, 5,367 files)

---

## Executive Summary

The Stratega OS workspace contains a substantial volume of business-critical assets (5,367 files across 70 directories, consuming 16GB) that require systematic reorganization. The analysis reveals:

- **494 files at root level** (should be ~20-30 maximum)
- **153 duplicate files** with indicators like (1), (2), (3)
- **Fragmented asset categories** spread across multiple inconsistent folder structures
- **Mixed file types** without clear categorization (353 CSVs, 745 Google Sheets, 257 Google Docs, 1,550 PNGs)
- **Empty strategic folders** (workflows/, research/, drafts/, notes/, docs/ are all empty or minimal)

**Priority Rating:** HIGH - Current structure impedes productivity and asset discovery

---

## Current State Analysis

### Root-Level Chaos (494 Files)

The root directory contains an unmanageable volume of files that should be categorized:

#### Lead Lists & Data Files (150+ files)
- 353 CSV files total, most containing lead lists from various sources
- LinkedIn Sales Navigator exports (e.g., `102_UM_-_F_-_Hotel_-_Tier_1__#_UM_-_51+...`)
- Outscraper exports (42 files: `Outscraper-20231022021003b535.csv`)
- Regional lead lists (Greece, Portugal, Italy by region)
- Hotel manager databases
- BIT trade show leads
- Apollo exports
- Multiple versions of same datasets (duplicates)

#### Google Workspace Files (1,000+ files)
- 745 Google Sheets (.gsheet) - spread throughout
- 257 Google Docs (.gdoc) - mix of templates, call recaps, client docs
- 41 Google Slides (.gslides) - presentations scattered
- 8 Google Forms (.gform) - surveys at root

#### Client Materials (Fragmented)
- Contracts: scattered (e.g., `2022_01_11_Accordo_collaborazione_Stratega_v2.docx`)
- Call recaps: both root and in `Call recap` folder
- Client-specific folders: `Clients (1)`, `Clients - Shared folder`, plus symlink

#### Marketing Assets (Highly Fragmented)
- 1,550 PNG images scattered across 10+ folders
- 562 JPG/170 JPEG files unorganized
- 199 SVG files (likely logo variations)
- Brand assets spread across:
  - `Stratega - Brand Identity Book`
  - `Stratega - General graphics & templates`
  - `Stratega - Images`
  - `Stratega - Website elements`
  - `New website Logos`
  - `Stratega Brand Kit - Sharing`

#### Templates (Inconsistent Location)
- Root level: 20+ template files
- `templates/` folder: 37 files
- `Stratega - Templates (1)` folder
- `Preventivi - Templates` folder
- Scattered Google Sheet templates

#### Documents & Reports
- 77 Excel files (.xlsx)
- 44 Word documents (.docx)
- 278 PDFs (proposals, invoices, reports)
- 63 PowerPoint files (.pptx)

### Duplicate Files Problem

**153 files** have duplicate indicators - examples:
- `102_UM_-_F_-_Hotel...(1).csv`, `(2).csv`, original
- `AtticaRegion.csv`, `AtticaRegion (1).csv`, `AtticaRegion (2).csv`
- `BIT_-_H+1...csv` through H+5 (legitimate versions vs. duplicates)
- `HM_test_-_Spain_-_test_w_domain_dropcontact (1).xlsx`

**Storage Impact:** Estimated 500MB-1GB wasted on true duplicates

### Folder Structure Issues

#### Strengths (Folders to Preserve & Enhance)
- `agents/` - Strategic OS folder (1 file only - needs development)
- `data/` - Contains 29 files, properly used
- `templates/` - 37 files, good start
- `Marketing MGMT/` - Well-organized with subfolders
- `Clients (1)` - Client work organized by project

#### Weaknesses
- `workflows/`, `research/`, `drafts/`, `notes/`, `docs/` - ALL EMPTY
- Duplicate client folders: `Clients (1)`, `Clients - Shared folder`, symlink
- Ambiguous folders: `Admin`, `Admin (1)`, `Databases`, `Lists`
- Dated folders: `2022`, `Strategy 2023`, `Scraping 25`
- Personal folders: `Matteo - personale`, `federico@stratega.co`
- Tool-specific folders scattered: `VA`, `Andriy`, `Toma_Admin`

#### Inconsistent Naming
- Spaces in folder names: "Marketing MGMT", "Canvas & Docs"
- Mixed languages: Italian and English
- Unclear abbreviations: GHM, GHWM, VA
- Inconsistent capitalization

---

## Proposed New Structure

### Tier 1: Strategic Operating System Foundation

```
/stratega/
├── 00-STRATEGA-CORE/              [Brand assets, company essentials]
│   ├── brand-identity/            [Logos, guidelines, colors, fonts]
│   ├── templates-internal/        [Company templates for proposals, contracts]
│   ├── legal-admin/              [Contracts, NDAs, company docs]
│   └── company-assets/           [Core marketing materials]
│
├── 01-CLIENTS/                    [All client work consolidated]
│   ├── active/                   [Current active projects]
│   │   ├── [client-name]/
│   │   │   ├── deliverables/
│   │   │   ├── meetings-notes/
│   │   │   ├── contracts/
│   │   │   └── assets/
│   ├── completed/                [Archived client projects]
│   └── leads-prospects/          [Potential client materials]
│
├── 02-MARKETING-CAMPAIGNS/        [Marketing operations]
│   ├── content-library/          [Blog posts, social media, newsletters]
│   │   ├── written-content/
│   │   ├── visual-assets/
│   │   └── video-audio/
│   ├── campaigns/                [Campaign-specific folders]
│   │   ├── enterprise-ireland/
│   │   ├── web-summit/
│   │   ├── wmf-rimini/
│   │   └── archived-campaigns/
│   ├── advertising/              [FB ads, Google ads, paid media]
│   ├── social-media/             [SMM strategy, content calendar]
│   ├── email-marketing/          [Newsletter, outreach]
│   └── case-studies/             [Success stories, testimonials]
│
├── 03-LEAD-GENERATION/            [All lead data & outreach]
│   ├── lead-lists/               [Raw lead databases]
│   │   ├── italy/               [By geography]
│   │   │   ├── lombardia/
│   │   │   ├── puglia/
│   │   │   ├── sicily/
│   │   │   └── other-regions/
│   │   ├── spain/
│   │   ├── portugal/
│   │   ├── greece/
│   │   └── other-countries/
│   ├── enriched-data/            [Processed, validated lists]
│   ├── scraping-exports/         [Outscraper, LinkedIn exports]
│   │   ├── linkedin-navigator/
│   │   ├── outscraper/
│   │   └── other-tools/
│   ├── outreach-campaigns/       [Email sequences, replies]
│   │   ├── active-sequences/
│   │   ├── replies-tracking/
│   │   └── templates/
│   └── experiments/              [A/B tests, outreach experiments]
│
├── 04-DATA-ANALYTICS/             [Business intelligence]
│   ├── reports/                  [Performance reports, analytics]
│   ├── tracking-plans/           [GA4, tracking configurations]
│   ├── dashboards/               [Links to BI tools, exports]
│   └── research/                 [Market research, competitor analysis]
│
├── 05-OPERATIONS/                 [Business operations]
│   ├── team-management/          [VA work, contractors]
│   ├── partnerships/             [Partner materials]
│   ├── events/                   [Trade shows, workshops]
│   ├── admin/                    [Invoices, transactions, admin]
│   └── strategy-planning/        [Strategic documents, OKRs]
│
├── 06-PRODUCT-ASSETS/             [Stratega product materials]
│   ├── website/                  [Website designs, elements]
│   ├── growth-workshop/          [Workshop materials]
│   ├── tools-templates/          [Client-facing templates]
│   └── educational-content/      [E-books, guides, lead magnets]
│
├── 07-CREATIVE-STUDIO/            [Design source files]
│   ├── working-files/            [PSDs, AIs, INDDs]
│   ├── final-exports/            [Production-ready assets]
│   ├── photography/              [Photo library]
│   └── video-projects/           [Video files, edits]
│
├── agents/                        [AI agents (preserve)]
├── workflows/                     [Automated workflows]
├── templates/                     [Enhanced template library]
├── data/                         [Enhanced data storage]
├── docs/                         [Documentation]
├── drafts/                       [WIP documents]
├── notes/                        [Meeting notes, ideas]
├── research/                     [Research repository]
├── outputs/                      [Agent outputs]
├── experiments/                  [Testing area]
└── archive/                      [Historical files]
    ├── 2022/
    ├── 2023/
    ├── 2024/
    └── deprecated/
```

---

## Detailed File Movement Plan

### Phase 1: Lead Lists & Data (Priority 1)

**Rationale:** These are the most numerous files at root (150+) and critical for business operations.

#### Italy Lead Lists
**Destination:** `/03-LEAD-GENERATION/lead-lists/italy/`

Move files like:
- `201A_- Hotel - 3s Lombardia Lead List.csv` → `/lombardia/`
- `202A - Puglia 3 stars Hotel Lead List.csv` → `/puglia/`
- `203A - Sicily 3 Stars Hotels Lead List.csv` → `/sicily/`
- `204A_- Emilia Romagna - Strutture Alberghiere Lead List.csv` → `/emilia-romagna/`
- `205A_- Toscana - All facilities Lead List.csv` → `/toscana/`

**Action:** Create regional subfolders, move 50+ Italy-specific CSVs

#### Spain/Portugal/Greece Lists
**Destination:** `/03-LEAD-GENERATION/lead-lists/[country]/`

- `301A_- CAT- Hotels 3+ Lead List.csv` → `/spain/catalonia/`
- `302A_- MAN - Hotels 3+ Lead List.csv` → `/spain/manchester/` [verify location]
- `Lisboa.csv`, `Braga.csv`, `Madeira.csv` → `/portugal/`
- `AtticaRegion.csv`, `CreteRegion.csv`, etc. → `/greece/`

**Files affected:** 60+ geographic lead lists

#### LinkedIn Sales Navigator Exports
**Destination:** `/03-LEAD-GENERATION/scraping-exports/linkedin-navigator/`

Move all files matching pattern:
- `*Scrape_Linkedin_Sales_Navigator_Leads_Search_Result*.csv`
- `101_UM_-_51+_-_Hospitality_-_Italy-Scrape_Linkedin...csv`
- `Hotel_Manager-Scrape_Linkedin_Sales_Navigator...csv`
- `MW_+_KW_-_Leads-18_10_2023-18_54_47.csv`

**Files affected:** 80+ LinkedIn exports

#### Outscraper Exports
**Destination:** `/03-LEAD-GENERATION/scraping-exports/outscraper/`

Move all:
- `Outscraper-2023*.csv` (42 files)
- `Outscraper-2024*.csv`
- `Outscraper-2025*.csv`

**Naming convention:** Keep original names (contain date/time stamps)

#### Enriched/Processed Data
**Destination:** `/03-LEAD-GENERATION/enriched-data/`

Move:
- `*_dropcontact.csv` or `*_dropcontact.xlsx` (data validated/enriched)
- `DB_UM_Q4_2023_ITA_Classified (1).csv`
- `OS - Lombardia - Hotels for email - 201F - Hotel - 3.3-4.0s - w_web&email.csv`

#### BIT Trade Show Leads
**Destination:** `/05-OPERATIONS/events/bit-milan/`

Move:
- `BIT*.csv` files (10+ files)
- `BIT_-_H+1-29_02_2024-18_44_51.csv` through H+5
- `BIT Leads H+4DC (1).csv`

### Phase 2: Google Workspace Files (Priority 1)

#### Google Sheets at Root (100+ files)
**Strategy:** Categorize by purpose, then move

**Templates** → `/templates/spreadsheets/`
- `Tag template.gsheet`
- `Proiezioni Template.gsheet`
- `Copy of [Template] Hashtag Instagram .gsheet`

**Lead tracking** → `/03-LEAD-GENERATION/lead-lists/tracking/`
- `Luna's leads.gsheet`
- `Laya - Database Ranking.gsheet`
- `Hotel Managers - Italy.gsheet`

**Marketing** → `/02-MARKETING-CAMPAIGNS/tracking/`
- `Content ranker.gsheet`
- `Hashtag Instagram - Kandemic.gsheet`
- `Food Truck Festivals.gsheet`

**Analytics** → `/04-DATA-ANALYTICS/tracking-plans/`
- `Copy of Analytics Tracking Cheat Sheet.gsheet`

**Client work** → `/01-CLIENTS/[client-name]/`
- Client-specific sheets

**Events** → `/05-OPERATIONS/events/[event-name]/`
- `Demo Day Likers.gsheet`
- `Eventi Web Summit.gsheet`
- `Latitude 59 Survey.gform`

#### Google Docs at Root (80+ files)
**Call recaps** → `/01-CLIENTS/meeting-notes/` OR `/05-OPERATIONS/team-management/meeting-notes/`
- `Call Recap 09 2 2023.gdoc`
- `Call Recap 23 01 2022.gdoc`
- `Call Recap 24 01 2023.gdoc`
- `Call recap 29 7 2023.gdoc`

**Templates** → `/templates/documents/`
- `Cold email questionnaire - template.gdoc`
- `Copy of SEO Strategy Template.gdoc`

**Marketing docs** → `/02-MARKETING-CAMPAIGNS/content-library/`
- `Lead gen Campaigns Best Practices.gdoc`
- `Linkedin post - NM.gdoc`
- `Contents by Nick.gdoc`

**Contracts** → `/00-STRATEGA-CORE/legal-admin/`
- `Contratto Food Truck.gdoc`
- `CONTRATTO DI PARTNERSHIP.gdoc`

**Personal/misc** → `/archive/personal/` or DELETE
- `Ashtanga Yoga.gdoc`
- `Untitled document (8).gdoc`

#### Google Slides at Root (15+ files)
**Templates** → `/templates/presentations/`
- `STRATEGA - OMTM Canvas - Template - Sharing.gslides`
- `Copy of 6WG Growth Marketing Strategy Template.gslides`

**Client presentations** → `/01-CLIENTS/[client-name]/presentations/`

**Internal** → `/05-OPERATIONS/strategy-planning/`

### Phase 3: Marketing Assets (Priority 1)

#### Consolidate Brand Assets
**Destination:** `/00-STRATEGA-CORE/brand-identity/`

**Merge these folders:**
- `Stratega - Brand Identity Book/` → `/brand-guidelines/`
- `Stratega - General graphics & templates/Stratega - Logo/` → `/logos/`
- `New website Logos/` → `/logos/website-versions/`
- `Stratega Brand Kit - Sharing/` → `/brand-kit-public/`

**Move root logos:**
- `BizPlace Logo blu nuovo.png` → `/logos/partners/bizplace/`
- `Asset 1@4x-8.png` → categorize then move
- `ML_2_400x395.jpeg` → `/team-photos/` or archive

#### Website Assets
**Destination:** `/06-PRODUCT-ASSETS/website/`

**Consolidate:**
- `Stratega - Website elements/` → `/design-mockups/`
- `data/01 - home-d21-v10 (svg) (1).png` → `/designs/homepage/`
- `data/02 - product-d21-v4-*.png` → `/designs/product-pages/`
- `data/03 - contact-d21-v4.png` → `/designs/contact/`
- `data/04 - about-d21-v5 (3).png` → `/designs/about/`

#### General Images
**Destination:** `/07-CREATIVE-STUDIO/photography/` or `/02-MARKETING-CAMPAIGNS/content-library/visual-assets/`

**Strategy:** Review 1,550 PNGs - most need categorization
- Campaign graphics → `/02-MARKETING-CAMPAIGNS/campaigns/[campaign-name]/assets/`
- Stock photos → `/07-CREATIVE-STUDIO/photography/stock/`
- Screenshots → `/archive/screenshots/` or DELETE

### Phase 4: Client Materials (Priority 2)

#### Consolidate Client Folders
**Action:** Merge duplicate structures

**Current state:**
- `Clients (1)` - 24 client folders
- `Clients - Shared folder` - 39 client folders
- `Clients` - symlink to Google Drive

**Proposed:**
```
/01-CLIENTS/
├── active/
│   ├── dotacademy/
│   ├── klondike/
│   ├── laya/
│   └── [other-active]/
├── completed/
│   ├── coinrule/
│   ├── duomo-design/
│   └── [archived-projects]/
└── leads-prospects/
```

**Move client files from root:**
- `Andriy - #ICA#Stratega.docx` → `/01-CLIENTS/completed/andriy/`
- `Chatty EL#Stratega#05032023.docx` → `/01-CLIENTS/active/chatty/`
- `EL_Virtuability&Stratega#15052024.docx` → `/01-CLIENTS/active/virtuability/`

### Phase 5: Marketing MGMT Reorganization (Priority 2)

**Current:** `/Marketing MGMT/` is well-structured but needs integration

**Action:** Move into new structure

```
/Marketing MGMT/Email Outreach/ → /03-LEAD-GENERATION/outreach-campaigns/
/Marketing MGMT/Email Outreach/Leads lists/ → /03-LEAD-GENERATION/lead-lists/marketing-mgmt-archive/
/Marketing MGMT/Email Outreach/Scripts/ → /03-LEAD-GENERATION/outreach-campaigns/templates/
/Marketing MGMT/Email Outreach/Replies/ → /03-LEAD-GENERATION/outreach-campaigns/replies-tracking/

/Marketing MGMT/Case studies/ → /02-MARKETING-CAMPAIGNS/case-studies/
/Marketing MGMT/SMM Strategy/ → /02-MARKETING-CAMPAIGNS/social-media/
/Marketing MGMT/Newsletter/ → /02-MARKETING-CAMPAIGNS/email-marketing/newsletter/
/Marketing MGMT/Lead Magnets/ → /06-PRODUCT-ASSETS/educational-content/lead-magnets/
/Marketing MGMT/Facebook ads/ → /02-MARKETING-CAMPAIGNS/advertising/facebook/
/Marketing MGMT/Experiments results/ → /03-LEAD-GENERATION/experiments/
/Marketing MGMT/Strategy 2022/ → /archive/2022/marketing-strategy/
```

### Phase 6: Templates (Priority 2)

#### Consolidate All Templates
**Merge:**
- Root template files → `/templates/`
- `templates/` (current 37 files) - keep as base
- `Stratega - Templates (1)/` → merge
- `Preventivi - Templates/` → `/templates/proposals/`
- `Scraping Templates/` → `/templates/scraping/`
- `Stratega - General graphics & templates/Internal files - Templates/` → `/templates/internal/`

**Organize by type:**
```
/templates/
├── spreadsheets/        [Google Sheets templates]
├── documents/           [Google Docs templates]
├── presentations/       [Slides templates]
├── proposals/           [Client proposal templates]
├── contracts/           [Contract templates]
├── marketing/           [Marketing templates]
├── scraping/            [Data collection templates]
└── internal/            [Internal operations]
```

### Phase 7: Documents & Files (Priority 3)

#### Excel/Word/PDF Organization

**Proposals/Invoices** → `/05-OPERATIONS/admin/financial/`
- `Factura de venta_2025 12297.pdf`
- `Final_Invoice_Register.csv`
- `Transaction_Export_01.08.2024_09.56.csv`

**Contracts** → `/00-STRATEGA-CORE/legal-admin/contracts/`
- `2022_01_11_Accordo_collaborazione_Stratega_v2.docx`

**Client Excel files** → `/01-CLIENTS/[client]/`
- `EPAY_AMS_analisi uomo donna.xlsx` → `/completed/epay/`
- `EPAY_REPORTADV_MAR2020.xlsx` → `/completed/epay/`

**Analytics/Reports** → `/04-DATA-ANALYTICS/reports/`
- `Account History (2).xls`

**Presentation files** → categorize by purpose
- Client presentations → `/01-CLIENTS/[client]/`
- Internal strategy → `/05-OPERATIONS/strategy-planning/`
- Marketing → `/02-MARKETING-CAMPAIGNS/`

### Phase 8: Archive & Cleanup (Priority 3)

#### Move to Archive
```
/archive/
├── 2022/                [Move existing /2022/ folder]
├── 2023/
│   └── strategy/       [Move /Strategy 2023/]
├── deprecated/
│   ├── old-scraping/   [/Scraping 25/]
│   ├── old-workflows/  [/Workflow/]
│   └── misc/
└── personal/
    ├── matteo/         [/Matteo - personale/]
    └── federico/       [/federico@stratega.co/]
```

#### Delete or Archive Empty/Redundant Folders
- `Admin/` - review contents, likely archive
- `Admin (1)/` - merge with Admin or delete
- `Databases/` - merge into data structure
- `Lists/` - merge into lead generation
- `Chrome Capture/` - likely delete
- `UpdraftPlus/` - WordPress backup? Archive or delete

#### Compressed Archives
**Current:** 92 .zip files

**Action:**
- Extract working files from archives
- Move source .zip to `/archive/compressed-backups/`
- Examples:
  - `Documenti Workshop.zip` → extract to `/05-OPERATIONS/events/workshops/`
  - `DotAcademy_material.zip` → extract to `/01-CLIENTS/completed/dotacademy/`
  - `Loghi IBL.zip` → extract to `/06-PRODUCT-ASSETS/growth-workshop/assets/`

### Phase 9: Duplicate Resolution (Priority 3)

**Strategy:** For each duplicate set:
1. Identify the most recent/complete version
2. Compare file sizes and modification dates
3. Keep ONE version in proper location
4. Move others to `/archive/duplicates-review/` temporarily
5. After 30 days, delete confirmed duplicates

#### High-Priority Duplicates to Resolve

**Example set 1 - Attica Region leads:**
- `AtticaRegion.csv`
- `AtticaRegion (1).csv`
- `AtticaRegion (2).csv`

**Action:** Compare dates, keep most recent → `/03-LEAD-GENERATION/lead-lists/greece/attica/`

**Example set 2 - Hotel Lombardia:**
- `102_UM_-_F_-_Hotel_-_Tier_1__#_UM_-_51+...(1).csv`
- `102_UM_-_F_-_Hotel_-_Tier_1__#_UM_-_51+...(2).csv`
- `102_UM_-_F_-_Hotel_-_Tier_1__#_UM_-_51+...csv`

**Action:** Verify if these are different extracts or duplicates. Keep unique versions.

**Estimated space savings:** 500MB - 1GB

---

## File Naming Convention Standards

### Implement Consistent Naming

**Current issues:**
- Mixed languages (Italian/English)
- Inconsistent date formats
- Special characters and spaces
- Unclear abbreviations

**Proposed standards:**

#### General Format
```
[category]_[project]_[description]_[date]_[version].[ext]
```

#### Date Format
- ALWAYS use: `YYYY-MM-DD`
- Example: `2024-03-15` not `15-03-2024` or `03_15_2024`

#### Lead Lists
```
leads_[country]_[region]_[segment]_[date-scraped].csv
```
Example:
- Old: `201A_- Hotel - 3s Lombardia Lead List.csv`
- New: `leads_italy_lombardia_hotels-3star_2023-10-24.csv`

#### Client Deliverables
```
[client-code]_[deliverable-type]_[description]_[version].ext
```
Example:
- `DOT_proposal_seo-strategy_v2.docx`
- `LAY_report_q4-analytics_final.pdf`

#### Marketing Assets
```
[campaign]_[asset-type]_[variant]_[date].[ext]
```
Example:
- `enterprise-ireland_social-post_carousel-1_2023-06-15.png`
- `web-summit_email-banner_variant-a.jpg`

#### Templates
```
template_[category]_[description].ext
```
Example:
- `template_proposal_saas-startup.docx`
- `template_spreadsheet_competitor-analysis.gsheet`

---

## Priority Action Sequence

### Week 1: Critical Foundations
**Focus:** Lead data and client materials (highest business impact)

1. **Day 1-2: Lead Lists**
   - Create `/03-LEAD-GENERATION/` structure
   - Move all CSV lead files from root
   - Organize by geography
   - Handle LinkedIn exports

2. **Day 3-4: Client Consolidation**
   - Audit both client folders
   - Create `/01-CLIENTS/` unified structure
   - Move active client materials
   - Archive completed projects

3. **Day 5: Google Sheets (Lead-related)**
   - Move lead tracking sheets
   - Organize by campaign
   - Update links/references

### Week 2: Marketing & Brand
**Focus:** Marketing campaigns and brand assets

4. **Day 6-7: Brand Asset Consolidation**
   - Create `/00-STRATEGA-CORE/brand-identity/`
   - Merge 5 brand-related folders
   - Organize logos, guidelines, fonts

5. **Day 8-9: Marketing MGMT Integration**
   - Map existing structure to new
   - Move campaign materials
   - Preserve case studies

6. **Day 10: Campaign Assets**
   - Organize images by campaign
   - Move event materials
   - Categorize advertising assets

### Week 3: Documentation & Templates
**Focus:** Templates and documentation

7. **Day 11-12: Template Library**
   - Consolidate all templates
   - Organize by type
   - Create index document

8. **Day 13: Google Docs**
   - Categorize all .gdoc files
   - Move to appropriate locations
   - Archive personal docs

9. **Day 14: Documentation**
   - Create `/docs/` structure
   - Add README files
   - Document new organization

### Week 4: Cleanup & Optimization
**Focus:** Archive and optimize

10. **Day 15-16: Archive Historical**
    - Move dated folders to `/archive/`
    - Archive old campaigns
    - Organize by year

11. **Day 17-18: Duplicate Resolution**
    - Identify all duplicates
    - Compare and select versions
    - Move to temporary review folder

12. **Day 19: Final Cleanup**
    - Remove empty folders
    - Organize remaining misc files
    - Update symlinks

13. **Day 20: Documentation & Training**
    - Create folder structure guide
    - Document naming conventions
    - Create quick-reference guide

---

## Detailed New Structure with File Counts

### Estimated File Distribution (Post-Reorganization)

```
/00-STRATEGA-CORE/ (250 files)
├── brand-identity/ (180 files)
│   ├── logos/ (100 PNGs, SVGs)
│   ├── brand-guidelines/ (2 PDFs)
│   ├── colors-fonts/ (27 font files)
│   └── brand-kit-public/ (50 assets)
├── templates-internal/ (25 files)
├── legal-admin/ (30 files)
│   └── contracts/ (10 DOCX)
└── company-assets/ (15 files)

/01-CLIENTS/ (800 files)
├── active/ (400 files)
│   └── [15 client folders]
├── completed/ (350 files)
│   └── [20 client folders]
└── leads-prospects/ (50 files)

/02-MARKETING-CAMPAIGNS/ (1,200 files)
├── content-library/ (600 files)
│   ├── written-content/ (100 docs)
│   ├── visual-assets/ (450 images)
│   └── video-audio/ (50 files)
├── campaigns/ (400 files)
│   ├── enterprise-ireland/ (150 files)
│   ├── web-summit/ (80 files)
│   └── [other campaigns]
├── advertising/ (50 files)
├── social-media/ (100 files)
├── email-marketing/ (40 files)
└── case-studies/ (10 files)

/03-LEAD-GENERATION/ (900 files)
├── lead-lists/ (400 CSV files)
│   ├── italy/ (200 files)
│   ├── spain/ (50 files)
│   ├── portugal/ (30 files)
│   ├── greece/ (50 files)
│   └── other-countries/ (70 files)
├── enriched-data/ (80 files)
├── scraping-exports/ (250 files)
│   ├── linkedin-navigator/ (150 files)
│   ├── outscraper/ (80 files)
│   └── other-tools/ (20 files)
├── outreach-campaigns/ (150 files)
│   ├── active-sequences/
│   ├── replies-tracking/
│   └── templates/
└── experiments/ (20 files)

/04-DATA-ANALYTICS/ (100 files)
├── reports/ (50 files)
├── tracking-plans/ (30 files)
├── dashboards/ (10 files)
└── research/ (10 files)

/05-OPERATIONS/ (300 files)
├── team-management/ (50 files)
├── partnerships/ (40 files)
├── events/ (150 files)
│   ├── bit-milan/ (40 files)
│   ├── web-summit/ (30 files)
│   └── workshops/ (60 files)
├── admin/ (40 files)
│   └── financial/ (20 invoices/reports)
└── strategy-planning/ (20 files)

/06-PRODUCT-ASSETS/ (500 files)
├── website/ (300 files)
│   └── design-mockups/ (large PNGs)
├── growth-workshop/ (100 files)
├── tools-templates/ (80 files)
└── educational-content/ (20 files)

/07-CREATIVE-STUDIO/ (400 files)
├── working-files/ (80 files - PSDs, AIs)
├── final-exports/ (200 files)
├── photography/ (100 files)
└── video-projects/ (20 files)

/templates/ (100 files)
├── spreadsheets/ (40 gsheets)
├── documents/ (30 gdocs)
├── presentations/ (15 gslides)
└── [other categories]

/data/ (150 files - enhanced)
/agents/ (5 files)
/workflows/ (TBD - will be populated)
/docs/ (20 files - new documentation)
/archive/ (1,000 files)
├── 2022/ (200 files)
├── 2023/ (150 files)
├── deprecated/ (500 files)
├── duplicates-review/ (150 files - temporary)
└── personal/ (50 files)

ROOT LEVEL: ~20 files maximum
- README.md
- CLAUDE.md (existing)
- GEMINI.md (existing)
- REORGANIZATION_PLAN.md (this document)
- .gitignore
- .DS_Store (system)
- Essential symlinks only
```

---

## Risk Assessment & Mitigation

### Identified Risks

#### 1. Broken Links/References
**Risk:** Google Drive links in documents may break
**Mitigation:**
- Document all file moves in spreadsheet
- Use "Find & Replace" in key documents
- Keep symlinks for critical paths initially
- Test major document links after moves

#### 2. Lost Files
**Risk:** Files accidentally deleted or misplaced
**Mitigation:**
- **DO NOT DELETE** anything initially
- Move to `/archive/` instead
- Create backup before starting
- Use version control for structure
- Review archive after 30 days before deletion

#### 3. Duplicate Uncertainty
**Risk:** Deleting a "duplicate" that's actually different
**Mitigation:**
- Use file comparison tools (diff, Beyond Compare)
- Check file sizes and dates
- Move to review folder, don't delete
- Keep for 30 days minimum

#### 4. Workflow Disruption
**Risk:** Team can't find files during transition
**Mitigation:**
- Communicate plan before starting
- Phase implementation by priority
- Create "Quick Find" guide
- Maintain old structure temporarily if needed
- Add README in old locations pointing to new

#### 5. Google Drive Sync Issues
**Risk:** Symlinked folders (`Clients`, `Newsletter`) need special handling
**Mitigation:**
- Identify all symlinks before moving
- Document Google Drive folder IDs
- Consider keeping symlinks in root with clear names
- Test sync after any symlink changes

---

## Tools & Utilities for Reorganization

### Recommended Tools

1. **File Comparison**
   - `diff` (built-in)
   - Beyond Compare
   - `fdupes` for finding duplicates

2. **Batch Renaming**
   - `rename` command
   - Bulk Rename Utility
   - Custom Python scripts

3. **File Analysis**
   - `tree` for directory visualization
   - `ncdu` for disk usage analysis
   - `rmlint` for finding duplicates

4. **Tracking**
   - Spreadsheet tracking all moves
   - Git for structure versioning
   - Change log document

### Example Commands

```bash
# Find all duplicates
find /path -type f -name "*(1)*" > duplicates.txt

# Compare two CSVs
diff file1.csv file2.csv

# Safe move with logging
mv source dest && echo "Moved: source -> dest" >> move_log.txt

# Find large files (>10MB)
find /path -type f -size +10M -exec ls -lh {} \; | sort -k5 -rh

# Count files by extension
find /path -type f | sed 's/.*\.//' | sort | uniq -c | sort -rn
```

---

## Quick Reference Guide (Post-Reorganization)

### Where to Find Common Assets

| I'm looking for... | Go to... |
|-------------------|----------|
| Lead lists (Italy) | `/03-LEAD-GENERATION/lead-lists/italy/[region]/` |
| Lead lists (other countries) | `/03-LEAD-GENERATION/lead-lists/[country]/` |
| LinkedIn exports | `/03-LEAD-GENERATION/scraping-exports/linkedin-navigator/` |
| Outscraper data | `/03-LEAD-GENERATION/scraping-exports/outscraper/` |
| Client project files | `/01-CLIENTS/active/[client-name]/` |
| Completed client work | `/01-CLIENTS/completed/[client-name]/` |
| Stratega logos | `/00-STRATEGA-CORE/brand-identity/logos/` |
| Brand guidelines | `/00-STRATEGA-CORE/brand-identity/brand-guidelines/` |
| Proposal templates | `/templates/proposals/` |
| Contract templates | `/templates/contracts/` |
| Google Sheets templates | `/templates/spreadsheets/` |
| Email templates | `/03-LEAD-GENERATION/outreach-campaigns/templates/` |
| Social media content | `/02-MARKETING-CAMPAIGNS/social-media/` |
| Case studies | `/02-MARKETING-CAMPAIGNS/case-studies/` |
| Newsletter materials | `/02-MARKETING-CAMPAIGNS/email-marketing/newsletter/` |
| Website designs | `/06-PRODUCT-ASSETS/website/design-mockups/` |
| Event materials | `/05-OPERATIONS/events/[event-name]/` |
| Analytics reports | `/04-DATA-ANALYTICS/reports/` |
| Meeting notes | `/01-CLIENTS/meeting-notes/` or `/05-OPERATIONS/team-management/meeting-notes/` |
| Invoices/financials | `/05-OPERATIONS/admin/financial/` |
| Old campaigns (2022-2023) | `/archive/[year]/` |
| Workshop materials | `/06-PRODUCT-ASSETS/growth-workshop/` |
| Design source files (PSD/AI) | `/07-CREATIVE-STUDIO/working-files/` |
| Photography library | `/07-CREATIVE-STUDIO/photography/` |

---

## Maintenance Best Practices

### Ongoing Organization Rules

#### 1. Root Directory Policy
- **Maximum 20 files** at root level
- Only system files and critical documentation
- Review monthly, move strays to proper folders

#### 2. Naming Convention Enforcement
- Use consistent date format: `YYYY-MM-DD`
- No spaces in folder names (use hyphens or underscores)
- Descriptive names, avoid "Untitled" or "Copy of"
- Version numbers at end: `_v1`, `_v2`, `_final`

#### 3. Duplicate Prevention
- Before uploading: search if file exists
- Use version numbers instead of (1), (2)
- Quarterly duplicate scans with `fdupes`

#### 4. Archive Policy
- Move completed projects to `/01-CLIENTS/completed/` within 30 days
- Archive campaigns older than 12 months
- Annual review of archive folder
- Delete confirmed duplicates after 90 days in review folder

#### 5. Template Updates
- Maintain single source of truth for templates
- Version templates clearly
- Deprecate old templates (move to `/archive/deprecated/`)

#### 6. Client Folder Structure
- Use consistent structure for ALL clients:
  ```
  /client-name/
  ├── deliverables/
  ├── meetings-notes/
  ├── contracts/
  ├── assets/
  └── communications/
  ```

#### 7. Lead Data Management
- Enrich raw lists before moving to `/enriched-data/`
- Tag lists with source and date
- Delete test/sample data after validation
- Quarterly review of old lead lists (archive if >18 months)

---

## Success Metrics

### How to Measure Improvement

#### Time-to-Find
- **Before:** Average 5-10 minutes to locate specific file
- **Target:** 30 seconds maximum

#### Storage Optimization
- **Before:** 16GB with duplicates
- **Target:** 14-15GB (remove 1-2GB duplicates)

#### Root Directory
- **Before:** 494 files
- **Target:** <20 files

#### Team Feedback
- Survey team on ease of navigation
- Track "where is X?" questions (should decrease)

#### Compliance
- 95% of files in correct folders within 30 days
- Zero files named "Untitled" after 60 days
- No duplicates older than 30 days

---

## Next Steps

### Immediate Actions (Before Starting)

1. **Backup Current State**
   - Full backup of `/stratega/` directory
   - Document current structure: `tree -L 3 > current_structure.txt`
   - Note existing symlinks

2. **Get Approval**
   - Review this plan with stakeholders
   - Confirm folder naming conventions
   - Identify any files that MUST NOT be moved

3. **Set Up Tracking**
   - Create spreadsheet to log all moves
   - Set up change log document
   - Create team communication channel

4. **Prepare Team**
   - Share this plan
   - Schedule training session
   - Create FAQ document

5. **Test on Small Set**
   - Test with one client folder
   - Test with one lead list batch
   - Verify no broken links
   - Adjust plan if needed

### Execution Authorization

**This plan is ready for implementation pending:**
- [ ] Stakeholder review and approval
- [ ] Full backup completed
- [ ] Team notification sent
- [ ] Tracking systems in place
- [ ] Go/No-go decision

---

## Appendix A: Folder Purpose Definitions

| Folder | Purpose | What Goes Here | What Doesn't |
|--------|---------|----------------|--------------|
| `/00-STRATEGA-CORE/` | Company identity & essentials | Logos, brand guidelines, legal docs, templates | Client work, campaigns, data |
| `/01-CLIENTS/` | All client-related work | Deliverables, contracts, meetings, assets | Internal strategy, marketing |
| `/02-MARKETING-CAMPAIGNS/` | Marketing operations | Content, campaigns, ads, social media | Lead lists (those go in 03) |
| `/03-LEAD-GENERATION/` | Lead data & outreach | CSVs, scraping exports, email campaigns | Client data, marketing assets |
| `/04-DATA-ANALYTICS/` | Business intelligence | Reports, dashboards, analytics, research | Raw lead lists |
| `/05-OPERATIONS/` | Business operations | Events, partnerships, admin, strategy | Marketing campaigns |
| `/06-PRODUCT-ASSETS/` | Stratega products | Website, workshops, tools, educational | Service delivery materials |
| `/07-CREATIVE-STUDIO/` | Design source files | PSDs, AIs, working files, photos | Final client deliverables |
| `/templates/` | Reusable templates | Any file intended for repeated use | One-off documents |
| `/archive/` | Historical files | Old campaigns, deprecated files | Anything still in use |

---

## Appendix B: File Type Distribution

| File Type | Count | Primary Locations After Reorganization |
|-----------|-------|----------------------------------------|
| PNG | 1,550 | `/02-MARKETING-CAMPAIGNS/`, `/00-STRATEGA-CORE/brand-identity/`, `/07-CREATIVE-STUDIO/` |
| Google Sheets | 745 | `/templates/spreadsheets/`, `/03-LEAD-GENERATION/`, `/04-DATA-ANALYTICS/` |
| JPG/JPEG | 732 | `/07-CREATIVE-STUDIO/photography/`, `/02-MARKETING-CAMPAIGNS/` |
| CSV | 353 | `/03-LEAD-GENERATION/lead-lists/`, `/03-LEAD-GENERATION/scraping-exports/` |
| PDF | 278 | `/00-STRATEGA-CORE/legal-admin/`, `/05-OPERATIONS/admin/`, `/01-CLIENTS/` |
| Google Docs | 257 | `/templates/documents/`, `/01-CLIENTS/`, `/05-OPERATIONS/` |
| SVG | 199 | `/00-STRATEGA-CORE/brand-identity/logos/` |
| ZIP | 92 | Extract then archive to `/archive/compressed-backups/` |
| XLSX | 77 | `/04-DATA-ANALYTICS/reports/`, `/03-LEAD-GENERATION/enriched-data/` |
| PPTX | 63 | `/01-CLIENTS/`, `/templates/presentations/` |
| DOCX | 44 | `/01-CLIENTS/`, `/00-STRATEGA-CORE/legal-admin/` |
| Google Slides | 41 | `/templates/presentations/`, `/01-CLIENTS/` |

---

## Appendix C: Duplicate Files Inventory (Sample)

Files requiring duplicate resolution:

1. **AtticaRegion set** (3 files, 1.04MB)
   - AtticaRegion.csv
   - AtticaRegion (1).csv
   - AtticaRegion (2).csv

2. **102_UM Hotel Tier 1** (3 files, 2.07MB)
   - 102_UM_-_F_-_Hotel_-_Tier_1__#_UM_-_51+...(1).csv
   - 102_UM_-_F_-_Hotel_-_Tier_1__#_UM_-_51+...(2).csv
   - 102_UM_-_F_-_Hotel_-_Tier_1__#_UM_-_51+....csv

3. **BizPlace Logo** (2 files, 50KB)
   - BizPlace Logo blu nuovo (1).png
   - BizPlace Logo blu nuovo.png

[... 150+ more duplicate sets to review]

**Action:** Create complete inventory spreadsheet with file sizes and dates for comparison.

---

## Document Version

**Version:** 1.0
**Date:** November 14, 2025
**Status:** PROPOSAL - AWAITING APPROVAL
**Next Review:** Upon stakeholder feedback

---

**END OF REORGANIZATION PLAN**
