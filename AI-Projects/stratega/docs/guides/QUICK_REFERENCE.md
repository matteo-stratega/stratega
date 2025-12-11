# Stratega OS - Quick Reference Guide

## Where Do I Find...?

### Lead Data & Prospecting
| I'm looking for... | Location |
|-------------------|----------|
| Italy hotel leads (by region) | `/03-LEAD-GENERATION/lead-lists/italy/[region]/` |
| Spain/Portugal/Greece leads | `/03-LEAD-GENERATION/lead-lists/[country]/` |
| LinkedIn Sales Navigator exports | `/03-LEAD-GENERATION/scraping-exports/linkedin-navigator/` |
| Outscraper data exports | `/03-LEAD-GENERATION/scraping-exports/outscraper/` |
| Enriched/validated leads | `/03-LEAD-GENERATION/enriched-data/` |
| Email outreach templates | `/03-LEAD-GENERATION/outreach-campaigns/templates/` |
| Outreach replies tracking | `/03-LEAD-GENERATION/outreach-campaigns/replies-tracking/` |
| Lead gen experiments/tests | `/03-LEAD-GENERATION/experiments/` |

### Client Work
| I'm looking for... | Location |
|-------------------|----------|
| Active client projects | `/01-CLIENTS/active/[client-name]/` |
| Completed client work | `/01-CLIENTS/completed/[client-name]/` |
| Client contracts | `/01-CLIENTS/active/[client]/contracts/` |
| Client deliverables | `/01-CLIENTS/active/[client]/deliverables/` |
| Meeting notes & call recaps | `/01-CLIENTS/meeting-notes/` |
| Potential client materials | `/01-CLIENTS/leads-prospects/` |

### Stratega Brand & Identity
| I'm looking for... | Location |
|-------------------|----------|
| Stratega logos (all versions) | `/00-STRATEGA-CORE/brand-identity/logos/` |
| Brand guidelines & identity book | `/00-STRATEGA-CORE/brand-identity/brand-guidelines/` |
| Brand fonts & colors | `/00-STRATEGA-CORE/brand-identity/colors-fonts/` |
| Public brand kit (for sharing) | `/00-STRATEGA-CORE/brand-identity/brand-kit-public/` |
| Company contracts & legal docs | `/00-STRATEGA-CORE/legal-admin/` |
| Internal templates (proposals, etc.) | `/00-STRATEGA-CORE/templates-internal/` |

### Marketing & Campaigns
| I'm looking for... | Location |
|-------------------|----------|
| Enterprise Ireland campaign | `/02-MARKETING-CAMPAIGNS/campaigns/enterprise-ireland/` |
| Web Summit materials | `/02-MARKETING-CAMPAIGNS/campaigns/web-summit/` |
| Social media content | `/02-MARKETING-CAMPAIGNS/social-media/` |
| Newsletter materials | `/02-MARKETING-CAMPAIGNS/email-marketing/newsletter/` |
| Facebook ads | `/02-MARKETING-CAMPAIGNS/advertising/facebook/` |
| Case studies | `/02-MARKETING-CAMPAIGNS/case-studies/` |
| Written content library | `/02-MARKETING-CAMPAIGNS/content-library/written-content/` |
| Visual assets library | `/02-MARKETING-CAMPAIGNS/content-library/visual-assets/` |
| Marketing videos | `/02-MARKETING-CAMPAIGNS/content-library/video-audio/` |

### Templates & Tools
| I'm looking for... | Location |
|-------------------|----------|
| Google Sheets templates | `/templates/spreadsheets/` |
| Google Docs templates | `/templates/documents/` |
| Presentation templates | `/templates/presentations/` |
| Proposal templates | `/templates/proposals/` |
| Contract templates | `/templates/contracts/` |
| Marketing templates | `/templates/marketing/` |
| Scraping/data collection templates | `/templates/scraping/` |

### Stratega Products
| I'm looking for... | Location |
|-------------------|----------|
| Website design mockups | `/06-PRODUCT-ASSETS/website/design-mockups/` |
| Growth Workshop materials | `/06-PRODUCT-ASSETS/growth-workshop/` |
| Client-facing tools & templates | `/06-PRODUCT-ASSETS/tools-templates/` |
| Lead magnets | `/06-PRODUCT-ASSETS/educational-content/lead-magnets/` |
| E-books | `/06-PRODUCT-ASSETS/educational-content/e-books/` |

### Design & Creative
| I'm looking for... | Location |
|-------------------|----------|
| PSD working files | `/07-CREATIVE-STUDIO/working-files/psd/` |
| Adobe Illustrator files | `/07-CREATIVE-STUDIO/working-files/ai/` |
| InDesign files | `/07-CREATIVE-STUDIO/working-files/indd/` |
| Final exported designs | `/07-CREATIVE-STUDIO/final-exports/` |
| Photography library | `/07-CREATIVE-STUDIO/photography/` |
| Video projects | `/07-CREATIVE-STUDIO/video-projects/` |

### Operations & Admin
| I'm looking for... | Location |
|-------------------|----------|
| Event materials (BIT, Web Summit, etc.) | `/05-OPERATIONS/events/[event-name]/` |
| Workshop materials | `/05-OPERATIONS/events/workshops/` |
| Partnership documents | `/05-OPERATIONS/partnerships/` |
| Team management files | `/05-OPERATIONS/team-management/` |
| VA work & tasks | `/05-OPERATIONS/team-management/va-work/` |
| Invoices & financial docs | `/05-OPERATIONS/admin/financial/` |
| Strategic planning docs | `/05-OPERATIONS/strategy-planning/` |

### Analytics & Data
| I'm looking for... | Location |
|-------------------|----------|
| Performance reports | `/04-DATA-ANALYTICS/reports/` |
| Tracking plans (GA4, etc.) | `/04-DATA-ANALYTICS/tracking-plans/` |
| Dashboard exports | `/04-DATA-ANALYTICS/dashboards/` |
| Market research | `/04-DATA-ANALYTICS/research/` |

### System & Archives
| I'm looking for... | Location |
|-------------------|----------|
| AI agents | `/agents/` |
| Automated workflows | `/workflows/` |
| Work-in-progress docs | `/drafts/` |
| Notes & ideas | `/notes/` |
| Research materials | `/research/` |
| Agent outputs | `/outputs/` |
| Old campaigns (2022-2023) | `/archive/[year]/` |
| Deprecated files | `/archive/deprecated/` |
| Personal files | `/archive/personal/` |
| Files pending deletion review | `/archive/duplicates-review/` |

---

## File Naming Standards

### Lead Lists
```
leads_[country]_[region]_[segment]_[date-scraped].csv
```
**Examples:**
- `leads_italy_lombardia_hotels-3star_2023-10-24.csv`
- `leads_spain_catalonia_hotels-luxury_2024-02-13.csv`
- `leads_greece_attica_all-hotels_2024-01-15.csv`

### Client Deliverables
```
[client-code]_[deliverable-type]_[description]_[version].[ext]
```
**Examples:**
- `LAY_report_q4-analytics_v2.pdf`
- `DOT_proposal_seo-strategy_final.docx`
- `KLO_presentation_growth-plan_v1.pptx`

### Marketing Assets
```
[campaign]_[asset-type]_[variant]_[date].[ext]
```
**Examples:**
- `enterprise-ireland_social-post_carousel-1_2023-06-15.png`
- `web-summit_email-banner_variant-a_2024-03-01.jpg`
- `newsletter_header-image_december_2024-12-01.png`

### Templates
```
template_[category]_[description].[ext]
```
**Examples:**
- `template_proposal_saas-startup.docx`
- `template_spreadsheet_competitor-analysis.gsheet`
- `template_email_cold-outreach-v1.gdoc`

### Date Format
**ALWAYS use:** `YYYY-MM-DD`
- ✅ Correct: `2024-03-15`
- ❌ Wrong: `15-03-2024`, `03_15_2024`, `15.03.24`

---

## Most Common Tasks

### Finding a Lead List
1. Go to `/03-LEAD-GENERATION/lead-lists/`
2. Choose country folder
3. Choose region/city folder
4. Find your CSV

**Time: 15-20 seconds**

### Finding a Client Project
1. Go to `/01-CLIENTS/active/` (or `/completed/`)
2. Choose client folder
3. Navigate to subfolder (deliverables, contracts, etc.)

**Time: 20 seconds**

### Finding Stratega Logo
1. Go to `/00-STRATEGA-CORE/brand-identity/logos/`
2. Choose appropriate subfolder (primary, variations, etc.)

**Time: 10 seconds**

### Finding a Template
1. Go to `/templates/`
2. Choose category (spreadsheets, documents, proposals, etc.)
3. Look for `template_` prefix

**Time: 15 seconds**

### Finding Marketing Campaign Assets
1. Go to `/02-MARKETING-CAMPAIGNS/campaigns/`
2. Choose campaign name (enterprise-ireland, web-summit, etc.)
3. Look in `/assets/` subfolder

**Time: 20 seconds**

---

## Folder Color Coding (Optional - for Finder/File Manager)

If your file manager supports folder colors, use this system:

- 🔴 **RED** - Client work (`01-CLIENTS/`)
- 🟢 **GREEN** - Lead generation (`03-LEAD-GENERATION/`)
- 🔵 **BLUE** - Marketing (`02-MARKETING-CAMPAIGNS/`)
- 🟡 **YELLOW** - Templates (`templates/`)
- 🟣 **PURPLE** - Brand core (`00-STRATEGA-CORE/`)
- 🟤 **GRAY** - Archive (`archive/`)

---

## Keyboard Shortcuts (macOS Finder)

- `Cmd + Shift + G` - Go to folder (type path directly)
- `Cmd + Up Arrow` - Go to parent folder
- `Cmd + Down Arrow` - Open selected folder
- `Cmd + F` - Search in current folder
- `Spacebar` - Quick Look preview

**Pro tip:** Bookmark frequently accessed folders in Finder sidebar!

---

## Rules to Remember

### DO:
✅ Put new lead lists immediately in correct country/region folder
✅ Name files descriptively with dates
✅ Use templates from `/templates/` folder
✅ Keep client work in client folders
✅ Archive old campaigns after 12 months

### DON'T:
❌ Save files to root directory
❌ Create files named "Untitled" or "Copy of"
❌ Use (1), (2) for versions - use proper version numbers
❌ Mix personal and business files
❌ Delete anything without moving to archive first

---

## Emergency Lookup

### "I can't find [FILE]"

**Step 1:** Check the most likely location using this guide

**Step 2:** Search using Finder/Explorer:
- Press `Cmd + F` (macOS) or `Ctrl + F` (Windows)
- Type filename or keyword
- Filter by "stratega" parent folder

**Step 3:** Check these common locations:
1. The folder category it belongs to (clients, leads, marketing)
2. Root directory (if file was recently added)
3. `/archive/` (if it's old)
4. `/data/` (if it's working data)

**Step 4:** If still not found:
- Check Google Drive (for .gsheet, .gdoc, .gslides files)
- Ask team member who last used it
- Check recent files in your editor/app

---

## Migration Period (First 30 Days)

### During transition:
- Old locations may still have files
- Use this guide for NEW file locations
- When you find old location, note it
- Gradually move files to new structure
- DON'T panic if something is still in old location

### Help the migration:
- When you open a file, check its location
- If in wrong place, move it to correct folder
- Update any links/bookmarks you have
- Share this guide with team

---

## Monthly Maintenance Checklist

### First Monday of each month:

- [ ] Check root directory - should have <20 files
- [ ] Move any strays to proper folders
- [ ] Review `/archive/duplicates-review/` - delete confirmed duplicates
- [ ] Check for new "Untitled" or "Copy of" files - rename them
- [ ] Archive completed client projects
- [ ] Archive campaigns older than 12 months
- [ ] Update this guide if new folders added

**Time required: 15-20 minutes**

---

## Questions?

### Who to ask:
- File organization questions: Check this guide first
- Can't find specific file: Ask in team chat
- Need new folder category: Discuss with team lead
- Technical issues: IT support

### Resources:
- Full reorganization plan: `REORGANIZATION_PLAN.md`
- Implementation guide: `IMPLEMENTATION_QUICK_START.md`
- Before/after comparison: `STRUCTURE_COMPARISON.md`
- This quick reference: `QUICK_REFERENCE.md`

---

## Version History

- **v1.0** (2025-11-14) - Initial quick reference created
- **v1.1** (Future) - Updates based on team feedback

---

**Print this page or bookmark it - you'll use it daily!**

**Target: Find any file in <30 seconds**
