# Stratega OS Reorganization - Quick Start Implementation Guide

## Pre-Flight Checklist

Before moving a single file:

- [ ] **BACKUP EVERYTHING** - Create full backup of `/stratega/` directory
- [ ] Read full reorganization plan: `REORGANIZATION_PLAN.md`
- [ ] Create tracking spreadsheet for file moves
- [ ] Notify team of reorganization schedule
- [ ] Test with small batch (10-20 files) first

## Phase 1: Lead Lists (Week 1, Days 1-2) - HIGHEST PRIORITY

### Why First?
- 353 CSV files cluttering root directory
- Most frequently accessed business asset
- Clear categorization rules

### Action Steps

#### Step 1: Create Lead Generation Structure
```bash
cd /Users/matteolombardi/AI-Projects/stratega

# Create the structure
mkdir -p 03-LEAD-GENERATION/lead-lists/italy/{lombardia,puglia,sicily,emilia-romagna,toscana,other}
mkdir -p 03-LEAD-GENERATION/lead-lists/{spain,portugal,greece,other-countries}
mkdir -p 03-LEAD-GENERATION/scraping-exports/{linkedin-navigator,outscraper,other-tools}
mkdir -p 03-LEAD-GENERATION/enriched-data
mkdir -p 03-LEAD-GENERATION/outreach-campaigns/{active-sequences,replies-tracking,templates}
mkdir -p 03-LEAD-GENERATION/experiments
```

#### Step 2: Move Italy Lead Lists
```bash
# Example moves (use with caution - test first!)
mv "201A_- Hotel - 3s Lombardia Lead List.csv" 03-LEAD-GENERATION/lead-lists/italy/lombardia/
mv "202A - Puglia 3 stars Hotel Lead List.csv" 03-LEAD-GENERATION/lead-lists/italy/puglia/
mv "203A - Sicily 3 Stars Hotels Lead List.csv" 03-LEAD-GENERATION/lead-lists/italy/sicily/
```

#### Step 3: Move Other Geographic Lists
```bash
# Portugal
mv Lisboa.csv 03-LEAD-GENERATION/lead-lists/portugal/
mv Madeira.csv 03-LEAD-GENERATION/lead-lists/portugal/
mv Braga.csv 03-LEAD-GENERATION/lead-lists/portugal/

# Greece
mv AtticaRegion.csv 03-LEAD-GENERATION/lead-lists/greece/
mv CreteRegion.csv 03-LEAD-GENERATION/lead-lists/greece/
mv CentralGreeceRegion.csv 03-LEAD-GENERATION/lead-lists/greece/
```

#### Step 4: Move Scraping Exports
```bash
# LinkedIn exports (80+ files)
mv *Scrape_Linkedin_Sales_Navigator*.csv 03-LEAD-GENERATION/scraping-exports/linkedin-navigator/

# Outscraper exports (42 files)
mv Outscraper-*.csv 03-LEAD-GENERATION/scraping-exports/outscraper/
```

#### Step 5: Move Enriched Data
```bash
mv *dropcontact*.csv 03-LEAD-GENERATION/enriched-data/
mv *dropcontact*.xlsx 03-LEAD-GENERATION/enriched-data/
mv DB_UM_Q4_2023_ITA_Classified*.csv 03-LEAD-GENERATION/enriched-data/
```

### Checkpoint
- [ ] All Italy lists in regional folders
- [ ] All geographic lists organized by country
- [ ] LinkedIn exports in correct folder
- [ ] Outscraper files organized
- [ ] Root directory has fewer CSVs
- [ ] Test: Can you find a Lombardia hotel list in <30 seconds?

## Phase 2: Client Materials (Week 1, Days 3-4)

### Action Steps

#### Step 1: Create Client Structure
```bash
mkdir -p 01-CLIENTS/{active,completed,leads-prospects}
mkdir -p 01-CLIENTS/meeting-notes
```

#### Step 2: Identify Active vs Completed Clients
**Active clients:** Currently working on projects (2024-2025)
**Completed clients:** No active work, projects finished

#### Step 3: Merge Client Folders
```bash
# Review both client folders
ls -la "Clients (1)/"
ls -la "Clients - Shared folder/"

# Move active client folders
# Example:
mv "Clients (1)/DotAcademy" 01-CLIENTS/active/dotacademy
mv "Clients (1)/Klondike" 01-CLIENTS/active/klondike
mv "Clients (1)/Laya" 01-CLIENTS/active/laya

# Move completed client folders
mv "Clients (1)/Coinrule" 01-CLIENTS/completed/coinrule
mv "Clients (1)/Duomo Design" 01-CLIENTS/completed/duomo-design
```

#### Step 4: Move Client Files from Root
```bash
mv "Andriy - #ICA#Stratega.docx" 01-CLIENTS/completed/andriy/
mv "Chatty EL#Stratega#05032023.docx" 01-CLIENTS/active/chatty/
mv "EL_Virtuability&Stratega#15052024.docx" 01-CLIENTS/active/virtuability/
```

#### Step 5: Organize Meeting Notes
```bash
# Move all call recap files
mv "Call Recap"*.gdoc 01-CLIENTS/meeting-notes/
mv "Call recap"*.gdoc 01-CLIENTS/meeting-notes/
```

### Checkpoint
- [ ] All active clients in `/01-CLIENTS/active/`
- [ ] Completed projects in `/01-CLIENTS/completed/`
- [ ] Client files from root moved
- [ ] Meeting notes organized
- [ ] Test: Can you find Laya project files quickly?

## Phase 3: Brand Assets (Week 2, Days 6-7)

### Action Steps

#### Step 1: Create Brand Structure
```bash
mkdir -p 00-STRATEGA-CORE/brand-identity/{logos,brand-guidelines,colors-fonts,brand-kit-public}
mkdir -p 00-STRATEGA-CORE/templates-internal
mkdir -p 00-STRATEGA-CORE/legal-admin/contracts
mkdir -p 00-STRATEGA-CORE/company-assets
```

#### Step 2: Consolidate Brand Folders
```bash
# Move brand identity book
mv "Stratega - Brand Identity Book"/* 00-STRATEGA-CORE/brand-identity/brand-guidelines/

# Move logos
mv "Stratega - General graphics & templates/Stratega - Logo"/* 00-STRATEGA-CORE/brand-identity/logos/
mv "New website Logos"/* 00-STRATEGA-CORE/brand-identity/logos/website-versions/

# Move brand kit
mv "Stratega Brand Kit - Sharing"/* 00-STRATEGA-CORE/brand-identity/brand-kit-public/
```

#### Step 3: Move Fonts
```bash
# Find and move font files
find . -maxdepth 2 -name "*.ttf" -o -name "*.otf" | xargs -I {} mv {} 00-STRATEGA-CORE/brand-identity/colors-fonts/
```

#### Step 4: Move Contracts
```bash
mv "2022_01_11_Accordo_collaborazione_Stratega_v2.docx" 00-STRATEGA-CORE/legal-admin/contracts/
mv "Contratto Food Truck.gdoc" 00-STRATEGA-CORE/legal-admin/contracts/
mv "CONTRATTO DI PARTNERSHIP.gdoc" 00-STRATEGA-CORE/legal-admin/contracts/
```

### Checkpoint
- [ ] All logos in one place
- [ ] Brand guidelines accessible
- [ ] Fonts organized
- [ ] Contracts in legal folder
- [ ] Test: Can you find the Stratega logo in <10 seconds?

## Phase 4: Marketing Campaigns (Week 2, Days 8-9)

### Action Steps

#### Step 1: Create Marketing Structure
```bash
mkdir -p 02-MARKETING-CAMPAIGNS/content-library/{written-content,visual-assets,video-audio}
mkdir -p 02-MARKETING-CAMPAIGNS/campaigns/{enterprise-ireland,web-summit,wmf-rimini,archived}
mkdir -p 02-MARKETING-CAMPAIGNS/{advertising,social-media,email-marketing,case-studies}
```

#### Step 2: Move Marketing MGMT Content
```bash
# Case studies
mv "Marketing MGMT/Case studies"/* 02-MARKETING-CAMPAIGNS/case-studies/

# Social media
mv "Marketing MGMT/SMM Strategy"/* 02-MARKETING-CAMPAIGNS/social-media/

# Newsletter
mv "Marketing MGMT/Newsletter"/* 02-MARKETING-CAMPAIGNS/email-marketing/

# Facebook ads
mv "Marketing MGMT/Facebook ads"/* 02-MARKETING-CAMPAIGNS/advertising/facebook/
```

#### Step 3: Move Campaign-Specific Folders
```bash
mv "Marketing MGMT/Enterprise Ireland "/* 02-MARKETING-CAMPAIGNS/campaigns/enterprise-ireland/
mv "Marketing MGMT/WMF Rimini 2021"/* 02-MARKETING-CAMPAIGNS/campaigns/wmf-rimini/
mv "Web Summit"/* 02-MARKETING-CAMPAIGNS/campaigns/web-summit/
```

#### Step 4: Move Marketing Email Operations to Lead Gen
```bash
# These belong in lead generation
mv "Marketing MGMT/Email Outreach/Leads lists"/* 03-LEAD-GENERATION/lead-lists/marketing-mgmt-archive/
mv "Marketing MGMT/Email Outreach/Scripts"/* 03-LEAD-GENERATION/outreach-campaigns/templates/
mv "Marketing MGMT/Email Outreach/Replies"/* 03-LEAD-GENERATION/outreach-campaigns/replies-tracking/
```

### Checkpoint
- [ ] Marketing campaigns organized
- [ ] Email outreach in lead gen folder
- [ ] Case studies accessible
- [ ] Social media content organized
- [ ] Test: Can you find Enterprise Ireland graphics?

## Phase 5: Templates (Week 3, Days 11-12)

### Action Steps

#### Step 1: Create Template Structure
```bash
mkdir -p templates/{spreadsheets,documents,presentations,proposals,contracts,marketing,scraping,internal}
```

#### Step 2: Categorize Root Templates
```bash
# Google Sheets templates
mv "Proiezioni Template.gsheet" templates/spreadsheets/
mv "Tag template.gsheet" templates/spreadsheets/
mv "Copy of [Template] Hashtag Instagram .gsheet" templates/spreadsheets/

# Document templates
mv "Cold email questionnaire - template.gdoc" templates/documents/
mv "Copy of SEO Strategy Template.gdoc" templates/documents/

# Presentation templates
mv "STRATEGA - OMTM Canvas - Template - Sharing.gslides" templates/presentations/
```

#### Step 3: Move Template Folders
```bash
# Merge existing templates
cp templates/* templates/  # Existing templates folder content (review first)
mv "Preventivi - Templates"/* templates/proposals/
mv "Scraping Templates"/* templates/scraping/
mv "Stratega - Templates (1)"/* templates/  # Review and categorize
```

#### Step 4: Move Internal Templates
```bash
mv "Stratega - General graphics & templates/Internal files - Templates"/* templates/internal/
```

### Checkpoint
- [ ] All templates in `/templates/` hierarchy
- [ ] Organized by type
- [ ] No "Copy of" or "Untitled" in names
- [ ] Test: Can you find email template in <20 seconds?

## Phase 6: Archive & Cleanup (Week 4, Days 15-18)

### Action Steps

#### Step 1: Create Archive Structure
```bash
mkdir -p archive/{2022,2023,2024,deprecated,personal,duplicates-review,compressed-backups}
```

#### Step 2: Move Dated Folders
```bash
mv 2022/* archive/2022/
mv "Strategy 2023"/* archive/2023/strategy/
```

#### Step 3: Move Old Campaigns
```bash
mv "Marketing MGMT/Strategy 2022"/* archive/2022/marketing-strategy/
mv "Scraping 25"/* archive/deprecated/scraping-25/
```

#### Step 4: Archive Personal Folders
```bash
mv "Matteo - personale"/* archive/personal/matteo/
mv "federico@stratega.co"/* archive/personal/federico/
```

#### Step 5: Handle Duplicates
```bash
# Create list of duplicates
find . -type f -name "*(1)*" -o -name "*(2)*" -o -name "*(3)*" > duplicates_list.txt

# Review each duplicate manually
# Move to review folder (DON'T DELETE YET)
# Example:
mv "AtticaRegion (1).csv" archive/duplicates-review/
mv "AtticaRegion (2).csv" archive/duplicates-review/
# Keep: AtticaRegion.csv (most recent)
```

#### Step 6: Archive Compressed Files
```bash
# Move .zip files
mv *.zip archive/compressed-backups/
# Extract important ones first if needed
```

### Checkpoint
- [ ] Historical files in archive
- [ ] Personal folders moved
- [ ] Duplicates in review folder
- [ ] Compressed files archived
- [ ] Test: Root directory has <50 files?

## Phase 7: Google Workspace Files (Week 3, Day 13)

### Strategy for .gsheet, .gdoc, .gslides

**Important:** These are pointers to Google Drive files. Moving them won't break Drive links, but be careful.

#### Step 1: Categorize by Filename Review
```bash
# List all Google Sheets
find . -maxdepth 1 -name "*.gsheet" > gsheets_list.txt

# List all Google Docs
find . -maxdepth 1 -name "*.gdoc" > gdocs_list.txt

# Review each list and categorize
```

#### Step 2: Move Lead-Related Sheets
```bash
mv "Luna's leads.gsheet" 03-LEAD-GENERATION/lead-lists/tracking/
mv "Laya - Database Ranking.gsheet" 03-LEAD-GENERATION/lead-lists/tracking/
mv "Hotel Managers - Italy.gsheet" 03-LEAD-GENERATION/lead-lists/tracking/
```

#### Step 3: Move Marketing Sheets
```bash
mv "Content ranker.gsheet" 02-MARKETING-CAMPAIGNS/tracking/
mv "Hashtag Instagram - Kandemic.gsheet" 02-MARKETING-CAMPAIGNS/social-media/
```

#### Step 4: Move Event-Related Files
```bash
mv "Demo Day Likers.gsheet" 05-OPERATIONS/events/demo-day/
mv "Eventi Web Summit.gsheet" 05-OPERATIONS/events/web-summit/
mv "Web Summit Survey.gform" 05-OPERATIONS/events/web-summit/
```

#### Step 5: Archive Untitled/Personal
```bash
mv "Untitled spreadsheet"*.gsheet archive/misc/
mv "Ashtanga Yoga.gdoc" archive/personal/matteo/
```

### Checkpoint
- [ ] Lead tracking sheets organized
- [ ] Marketing sheets in campaigns
- [ ] Event materials with events
- [ ] Untitled files archived
- [ ] Test: Can you find Luna's leads?

## Final Cleanup (Week 4, Day 19)

### Root Directory Target: <20 Files

After all moves, root should contain ONLY:
- README.md
- CLAUDE.md
- GEMINI.md
- REORGANIZATION_PLAN.md
- IMPLEMENTATION_QUICK_START.md
- .DS_Store (system file)
- .gitignore (if applicable)
- Essential symlinks (label clearly)

### Remove Empty Folders
```bash
# Find empty directories
find . -type d -empty

# Remove empty folders (careful!)
find . -type d -empty -delete
```

### Create README Files
```bash
# Add README.md to major folders explaining their purpose
echo "# Lead Generation Data Repository" > 03-LEAD-GENERATION/README.md
echo "# Client Work Repository" > 01-CLIENTS/README.md
echo "# Marketing Campaigns Repository" > 02-MARKETING-CAMPAIGNS/README.md
```

## Post-Reorganization Tasks

### Documentation
- [ ] Create visual folder tree diagram
- [ ] Update any internal wikis/documentation
- [ ] Share "Where to Find" guide with team
- [ ] Document any remaining edge cases

### Verification
- [ ] Verify no files lost (compare file counts)
- [ ] Test critical file access
- [ ] Check Google Drive sync for symlinks
- [ ] Verify important document links still work

### Team Training
- [ ] Schedule team walkthrough session
- [ ] Share Quick Reference Guide
- [ ] Collect feedback on structure
- [ ] Make adjustments based on usage

### Maintenance Setup
- [ ] Schedule monthly root directory audit
- [ ] Set up duplicate detection script
- [ ] Create file naming convention checklist
- [ ] Establish archive policy (30/60/90 days)

## Rollback Plan

If something goes wrong:

1. **STOP immediately**
2. Don't delete anything
3. Restore from backup
4. Review what went wrong
5. Adjust plan
6. Test on smaller batch

## Common Issues & Solutions

### Issue: "File not found" after move
**Solution:** Check if file is in Google Drive sync folder, may need different approach

### Issue: Many files with similar names
**Solution:** Use `ls -lt` to sort by date, keep most recent

### Issue: Unsure about duplicate
**Solution:** Move ALL versions to `duplicates-review/`, compare later

### Issue: Broken link in document
**Solution:** Document in tracking sheet, update link after all moves complete

### Issue: Permission denied
**Solution:** Check file ownership: `ls -la filename`, may need `sudo` or ownership change

## Progress Tracking Template

Create a spreadsheet with columns:
- Original Path
- New Path
- File Size
- Date Moved
- Moved By
- Notes
- Status (Pending/Complete/Verified)

## Questions Before Starting?

Review these:
1. Do you have a complete backup?
2. Have you tested the process on 10 files?
3. Does the team know about the reorganization?
4. Do you have 4 hours of uninterrupted time?
5. Have you read the full REORGANIZATION_PLAN.md?

If all YES → Proceed
If any NO → Address first

---

**Good luck! Take it slow, test frequently, and don't delete anything until you're 100% sure.**

**Remember:** This is a marathon, not a sprint. Better to be thorough than fast.
