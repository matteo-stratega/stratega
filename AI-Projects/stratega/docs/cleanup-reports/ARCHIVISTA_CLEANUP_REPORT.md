# Archivista Cleanup Report
**Date:** 2025-11-25
**Location:** `/Users/matteolombardi/AI-Projects/stratega/`
**Total Size:** 16GB
**Total Files in Root:** 431 files

---

## Executive Summary

The Stratega OS workspace contains significant organizational debt accumulated from Google Drive sync operations. The analysis reveals:

- **16GB total workspace size** (3.3GB in archive alone)
- **431 files scattered in root directory** (should be ~10 core files)
- **169 CSV files in root** (should be in `/data/`)
- **59 duplicate files** with `(1)` or `(2)` suffixes
- **55 "Untitled" Google Doc/Sheet symlinks** in root
- **1,052 Google Drive symlink files** (.gsheet, .gdoc, etc.)
- **126 .DS_Store files** throughout the workspace
- **Only 81 files tracked in git** (99.8% of files are untracked)

### Critical Issues Identified

1. **Data Sprawl:** Lead lists and CSV exports scattered in root instead of `/data/`
2. **Duplicate Proliferation:** Multiple copies of the same files (download artifacts)
3. **Google Drive Symlink Chaos:** 1,052 symlink files mixed throughout workspace
4. **Legacy Client Work:** Multiple client folders in root instead of `/archive/`
5. **Stratega Brand Assets:** 6+ directories for brand materials, should be consolidated
6. **Untitled Documents:** 55 Google symlinks with no meaningful names
7. **System Junk:** 126 .DS_Store files polluting git status

---

## 1. CURRENT STATE ANALYSIS

### Root Directory Breakdown

**File Type Distribution:**
- CSV files: 169 (mostly lead lists, 2-5MB each)
- Google symlinks (.gsheet, .gdoc, etc.): ~200 in root
- Excel files (.xlsx): ~15
- Word docs (.docx): 8
- Images (.png, .jpg): 12
- Markdown (.md): 9 (8 core + 1 temporary)
- PDF files: scattered
- Archives (.zip): 1

**Directory Structure (Top-Level):**
- Core Stratega OS dirs: `agents/`, `data/`, `notes/`, `docs/`, `templates/`, `workflows/`, `outputs/`, `research/`, `experiments/`, `assets/`, `archive/`
- Client work folders: `Clients (1)/`, `Clients - Shared folder/`, various client names
- Brand asset folders: `Stratega - Ads/`, `Stratega - Brand Identity Book/`, `Stratega - General graphics & templates/`, `Stratega - Images/`, `Stratega - Templates (1)/`, `Stratega - Website elements/`, `Stratega 2.0/`, `Stratega Brand Kit - Sharing/`
- Legacy folders: `2022/`, `Admin/`, `Admin (1)/`, `Andriy/`, `VA/`, `Toma_Admin/`
- Campaign/project folders: `Web Summit/`, `BIT/`, `Growth Workshop Stratega IBL/`
- Content folders: `Copywriting/`, `E-books/`, `Brochure/`, `Newsletter/` (symlink)
- Tool/workflow folders: `Scraping 25/`, `Scraping Templates/`, `n8n-workflows/`
- Personal: `Matteo - personale/`, `Hacks (ML)/`
- Misc: `Call recap/`, `Canvas & Docs/`, `Chrome Capture/`, `Tests/`, `UpdraftPlus/`, `Iubenda/`

### Symlinks Detected

**Active Google Drive Symlinks (5):**
1. `Clients` → Google Drive mirror
2. `Newsletter` → Google Drive mirror
3. `Stratega - Templates` → Google Drive mirror
4. `Stratega` → `.shortcut-targets-by-id`
5. `videos` → `/Users/matteolombardi/Stratega old/Screenstudio/Academy videos`

**WARNING:** Operations affecting these directories will impact Google Drive. Recommend documenting what's inside before cleanup decisions.

### Data Directory Analysis

**Current `/data/` size:** 244MB (24 files)
**CSV files in root that belong in `/data/`:** 169 files (~400-500MB total)

**Target:** Move all lead lists, exports, and datasets to `/data/`

### Git Tracking Status

**Tracked files:** 81 (mostly .md files in `/docs/`, `/agents/`, `/notes/` + n8n workflows)
**Untracked files:** 99.8% of workspace
**Ignored by .gitignore:** CSVs, PDFs, assets, data directory

**Good news:** Git is properly configured to ignore large files. The untracked status is expected for data/asset files.

---

## 2. DUPLICATE DETECTION

### Confirmed Duplicates (59 files with numbered suffixes)

**High-Priority Duplicates (Large CSV Files):**

1. **102_UM LinkedIn Scrapes** (3 copies × 689KB = 2MB wasted)
   - `102_UM_-_F_-_Hotel_-_Tier_1__#_UM_-_51+_-_Hospitality_-_Italy_(1_3)-Scrape...csv`
   - Same file with `(1)` and `(2)` suffixes

2. **103_UM LinkedIn Scrapes** (3 copies × 222KB = 666KB wasted)

3. **104_UM LinkedIn Scrapes** (3 copies × 617KB = 1.8MB wasted)

4. **105_UM LinkedIn Scrapes** (multiple copies)

5. **201-series Hotel Lead Lists** (various duplicates)
   - `201F_- Hotel - 3.3-4.0s Lombardia OS Lead List.csv` + `(1).csv`
   - Multiple sequence report duplicates

6. **Outscraper Exports** (multiple duplicates)
   - `Outscraper-20231022021003b535.csv` + `(1).csv` (4.3MB each)
   - `Outscraper-20231103133118f9d8_spa_-_cat.csv` + `(1).csv` (3.4MB each)
   - Many others with `(1)` suffixes

7. **Other Large Duplicates:**
   - `Simplescraper data.csv` + `(1).csv` (2.3MB each)

**Estimated savings from removing numbered duplicates:** ~150-200MB

### Potential Content Duplicates (Need Review)

**Admin/Client Folders:**
- `Admin/` vs `Admin (1)/` - likely different content but needs verification
- `Clients (1)/` vs `Clients - Shared folder/` vs `Clients` symlink - organizational confusion

**Stratega Brand Folders:**
- `Stratega - Templates (1)/` vs `Stratega - Templates` (symlink)
- Multiple brand asset folders could be consolidated

**Lists vs Databases:**
- `Lists/` directory (204KB) - contains old lead lists
- `Databases/` directory (empty) - purpose unclear
- Could be merged into `/data/`

### Google Drive Symlink Duplicates

**Untitled Documents (55 files):** These are Google Drive artifacts with no context
- `Untitled document.gdoc` through `Untitled document (10).gdoc`
- `Untitled spreadsheet.gsheet` through `Untitled spreadsheet (41).gsheet`

**Action:** These should be reviewed in Google Drive and either:
1. Given meaningful names and kept
2. Deleted if they're abandoned drafts
3. Consolidated if they're duplicates

---

## 3. CLEANUP RECOMMENDATIONS

### Priority 1: SAFE TO REMOVE (High Confidence)

**A. System Junk Files (126 files, ~5MB)**
```bash
# Remove all .DS_Store files
find . -name ".DS_Store" -delete
```
**Impact:** Clean git status, no functional impact
**Risk:** ZERO - these are macOS thumbnail cache files

**B. Duplicate CSV Files with Numbered Suffixes (59 files, ~150-200MB)**

Files to remove (keep the original without suffix):
- All files ending in ` (1).csv`, ` (2).csv`, ` (1).xlsx`, etc.
- Examples:
  - `102_UM_-_F_-_Hotel_-_Tier_1__#_UM_-_51+_-_Hospitality_-_Italy_(1_3)-Scrape_Linkedin_Sales_Navigator_Leads_Search_Resultbqqx3tJuk-24_10_2023-16_57_51 (1).csv`
  - `102_UM_-_F_-_Hotel_-_Tier_1__#_UM_-_51+_-_Hospitality_-_Italy_(1_3)-Scrape_Linkedin_Sales_Navigator_Leads_Search_Resultbqqx3tJuk-24_10_2023-16_57_51 (2).csv`
  - All others matching this pattern

**Action:**
```bash
# Move to temp review folder first (safety protocol)
mkdir -p /Users/matteolombardi/AI-Projects/stratega/temp-cleanup-review
find /Users/matteolombardi/AI-Projects/stratega -maxdepth 1 -type f \( -name "* (1).*" -o -name "* (2).*" \) -exec mv {} temp-cleanup-review/ \;
```

**Impact:** Recover 150-200MB, reduce clutter
**Risk:** LOW - these are download duplicates, originals remain

**C. Temporary/Orphaned Files**
- `79bd664d-8a94-489b-9c14-c441d1b545d4_ExportBlock-e35b1ac3-b189-4833-a01b-98d256f5e910.zip` (temp export)
- Any other temp files with UUID names

**Impact:** Clean workspace
**Risk:** LOW - appears to be temporary export

### Priority 2: CONSOLIDATE (Medium Effort, High Value)

**A. Move All CSV/Data Files to `/data/` (169 files, ~500MB)**

**Categories to organize in `/data/`:**
1. `/data/linkedin-scrapes/` - All LinkedIn Sales Navigator exports
2. `/data/outscraper/` - All Outscraper exports
3. `/data/hotel-leads/` - 201-series hotel lead lists
4. `/data/event-leads/` - BIT, Web Summit, etc.
5. `/data/exports/` - Apollo, Hubspot, misc exports

**Action Plan:**
```bash
# Create subdirectories
mkdir -p /Users/matteolombardi/AI-Projects/stratega/data/{linkedin-scrapes,outscraper,hotel-leads,event-leads,exports}

# Move files by pattern (examples)
mv /Users/matteolombardi/AI-Projects/stratega/*UM_-_*.csv /Users/matteolombardi/AI-Projects/stratega/data/linkedin-scrapes/
mv /Users/matteolombardi/AI-Projects/stratega/Outscraper-*.csv /Users/matteolombardi/AI-Projects/stratega/data/outscraper/
mv /Users/matteolombardi/AI-Projects/stratega/201*.csv /Users/matteolombardi/AI-Projects/stratega/data/hotel-leads/
mv /Users/matteolombardi/AI-Projects/stratega/BIT_*.csv /Users/matteolombardi/AI-Projects/stratega/data/event-leads/
```

**Impact:** Restore clean root directory, organize data properly
**Risk:** LOW - git ignores CSV files, just file organization

**B. Consolidate Stratega Brand Assets into `/assets/brand/`**

**Current state:** 6+ separate directories
**Target structure:**
```
/assets/
├── brand/
│   ├── logos/
│   ├── brand-guidelines/
│   ├── ads/
│   ├── website-elements/
│   └── templates/
```

**Directories to merge:**
- `Stratega - Ads/` → `/assets/brand/ads/`
- `Stratega - Brand Identity Book/` → `/assets/brand/brand-guidelines/`
- `Stratega - Images/` → `/assets/brand/logos/`
- `Stratega - Website elements/` → `/assets/brand/website-elements/`
- `Stratega Brand Kit - Sharing/` → review and merge into above

**Impact:** Unified brand asset location
**Risk:** MEDIUM - need to verify no duplicate work, check if synced to Drive

**C. Consolidate Lists and Databases**

**Action:**
```bash
# Merge into data directory
mv /Users/matteolombardi/AI-Projects/stratega/Lists/* /Users/matteolombardi/AI-Projects/stratega/data/exports/
rmdir /Users/matteolombardi/AI-Projects/stratega/Lists
rmdir /Users/matteolombardi/AI-Projects/stratega/Databases  # already empty
```

**Impact:** Simplified structure
**Risk:** LOW - small directories with clear data content

### Priority 3: ARCHIVE (Move to `/archive/`)

**Client Work Folders:**
- `Clients (1)/` → `/archive/clients/`
- `Clients - Shared folder/` → `/archive/clients/` (verify not duplicate of symlink)
- `Growth Workshop Stratega IBL - Shared Folder/` → `/archive/workshops/`
- `Andriy/` → `/archive/contractors/`
- `VA/` → `/archive/contractors/`
- `federico@stratega.co/` → `/archive/team/`
- `Toma_Admin/` → `/archive/admin/`

**Legacy Folders:**
- `2022/` → `/archive/historical/2022/`
- `Admin/` and `Admin (1)/` → `/archive/admin/` (after deduplication review)

**Old Campaigns/Events:**
- `Web Summit/` → `/archive/events/web-summit/`
- `Follow the Path/` → `/archive/projects/`
- `GHM/`, `GHWM/` → `/archive/projects/`

**Personal/Misc:**
- `Matteo - personale/` → `/archive/personal/`
- `Hacks (ML)/` → `/archive/personal/experiments/`
- `Chrome Capture/` → likely screenshots, archive or delete
- `UpdraftPlus/` → WordPress backup plugin files, archive

**Impact:** Clear root directory of inactive projects
**Risk:** LOW - moving to archive, not deleting

### Priority 4: REVIEW NEEDED (User Decision Required)

**A. Google Drive Symlink Strategy**

**Decision needed:** Should symlinked directories remain in root or be moved?

Current symlinks:
1. `Clients` - Active client work (likely needs to stay accessible)
2. `Newsletter` - Active newsletter content (keep in root or move to `/docs/newsletter/`?)
3. `Stratega - Templates` - Active templates (conflicts with `/templates/` directory)
4. `Stratega` - Unknown purpose (`.shortcut-targets-by-id`)
5. `videos` - Academy video content (move to `/assets/videos/` or keep symlink?)

**Recommendation:**
- Keep `Clients` symlink if actively used
- Move `Newsletter` → create `/docs/newsletter/` and update workflows
- Evaluate `Stratega - Templates` overlap with `/templates/`
- Investigate `Stratega` symlink purpose
- Consolidate `videos` into assets structure

**B. Untitled Google Documents (55 files)**

**Options:**
1. Open each in Google Drive and rename appropriately
2. Create a `/review/untitled-docs/` folder and move them for batch review
3. Delete if confirmed as abandoned drafts

**Recommendation:** Move to review folder, let Matteo bulk-process in Google Drive

**C. Active Project Folders (Unclear Status)**

Need clarification on active vs. archived:
- `Copywriting/` - Active content work or archive?
- `E-books/` - Active or archive?
- `Brochure/` - Active or archive?
- `Canvas & Docs/` - Active or archive?
- `Questionnaires/` - Active templates or archive?
- `Preventivi - Templates/` - Active proposal templates or archive?
- `Scraping 25/`, `Scraping Templates/` - Active scraping work or archive?
- `Slider/` - Unknown purpose
- `The Growth hub/` - Active or archive?
- `UI UX Outreach/` - Active campaign or archive?
- `Unicorn Dbs - reorg/` - Work in progress or archive?

**D. Potential Template Consolidation**

Multiple template-related locations:
- `/templates/` (Stratega OS directory, tracked in git)
- `Stratega - Templates (1)/` (untracked directory)
- `Stratega - Templates` (Google Drive symlink)
- `Preventivi - Templates/` (proposal templates)

**Question:** Should all templates consolidate into `/templates/` with subdirectories?

**E. Workflow Organization**

Multiple workflow/process directories:
- `/workflows/` (Stratega OS directory)
- `Workflow/` (separate directory)
- `n8n-workflows/` (automation workflows, tracked in git)

**Recommendation:** Merge `Workflow/` into `/workflows/` if not duplicate

### Priority 5: KEEP AS-IS (Core Structure)

**Stratega OS Core Directories (DO NOT MOVE):**
- `agents/` - AI agent definitions (tracked in git)
- `data/` - Data warehouse (gitignored, correct location)
- `notes/` - Daily summaries and notes (tracked in git)
- `docs/` - Final deliverables (tracked in git)
- `templates/` - Reusable frameworks (tracked in git)
- `workflows/` - Operational blueprints (tracked in git)
- `outputs/` - Generated deliverables (tracked in git)
- `research/` - Market analysis (tracked in git)
- `experiments/` - Testing area (tracked in git)
- `assets/` - Visual materials (gitignored, correct location)
- `archive/` - Historical content (gitignored, correct location)
- `scripts/` - Python/bash scripts (tracked in git)
- `n8n-workflows/` - Automation workflows (tracked in git)

**Core Configuration Files (DO NOT MOVE):**
- `README.md`
- `CLAUDE.md`
- `GEMINI.md`
- `.gitignore`
- `.obsidian/` (Obsidian vault config)
- `.claude/` (Claude Code config)

**Active Work Files (Keep in Root for Now):**
- `SESSION_START.md` - Session management
- `REORGANIZATION_PLAN.md` - This cleanup plan
- `IMPLEMENTATION_QUICK_START.md` - Quick reference
- `STRUCTURE_COMPARISON.md` - Structure analysis
- `QUICK_REFERENCE.md` - Quick reference

**Note:** These working documents should eventually move to `/docs/` when finalized

---

## 4. PROPOSED STRUCTURE (After 30% Cleanup)

### Target Root Directory
```
/Users/matteolombardi/AI-Projects/stratega/
├── .claude/                          # Claude Code config
├── .obsidian/                        # Obsidian vault config
├── .gitignore                        # Git exclusions
├── README.md                         # Repository overview
├── CLAUDE.md                         # Claude Code instructions
├── GEMINI.md                         # Shared AI agent config
│
├── agents/                           # AI agent definitions (8 files)
├── data/                             # Data warehouse
│   ├── linkedin-scrapes/             # LinkedIn exports (organized)
│   ├── outscraper/                   # Outscraper exports
│   ├── hotel-leads/                  # Hospitality lead lists
│   ├── event-leads/                  # Event-specific leads
│   ├── exports/                      # Misc data exports
│   └── README.md                     # Data dictionary
│
├── notes/                            # Working notes and daily logs
│   ├── daily-summaries/              # Daily work summaries
│   ├── weekly-rollups/               # Weekly reviews
│   └── [topic].md                    # Ad-hoc notes
│
├── docs/                             # Final deliverables
│   ├── workflows/                    # Workflow documentation
│   ├── lead-gen-crash-course/        # Educational content
│   └── *.md                          # Strategy docs
│
├── templates/                        # Reusable frameworks (Google Sheets/Docs)
│   ├── Asana/                        # Asana templates
│   ├── Email/                        # Email templates
│   ├── Lead Gen - Automation/        # Lead gen templates
│   └── *.gsheet/*.gslides            # Various templates
│
├── workflows/                        # Operational blueprints
├── outputs/                          # Generated deliverables
├── research/                         # Market analysis and ICPs
├── experiments/                      # Testing and prototypes
├── scripts/                          # Automation scripts
│
├── assets/                           # Visual materials
│   ├── brand/                        # Stratega brand assets (consolidated)
│   │   ├── logos/
│   │   ├── brand-guidelines/
│   │   ├── ads/
│   │   └── website-elements/
│   ├── images/                       # General images
│   └── videos/                       # Video content
│
├── archive/                          # Historical content (3.3GB)
│   ├── clients/                      # Past client work
│   ├── contractors/                  # Past contractor work
│   ├── events/                       # Past events (Web Summit, etc.)
│   ├── projects/                     # Completed projects
│   ├── admin/                        # Administrative archives
│   └── personal/                     # Personal archives
│
├── n8n-workflows/                    # Automation workflows (tracked)
│   ├── content/
│   ├── lead-gen/
│   ├── linkedin/
│   └── school/
│
├── side-projects/                    # Side project experiments
├── stratega-project/                 # Stratega website/project
│
└── [SYMLINKS]                        # Google Drive symlinks (selective)
    ├── Clients -> [Google Drive]     # Active client work
    └── Newsletter -> [Google Drive]  # Active newsletter
```

### Removed from Root (231 items → ~30 items)

**Removed/Consolidated:**
- 169 CSV files → `/data/` subdirectories
- 59 duplicate files → deleted or temp review
- 55 untitled Google docs → review folder or deleted
- 126 .DS_Store files → deleted
- 6+ Stratega brand folders → `/assets/brand/`
- 10+ legacy client folders → `/archive/clients/`
- 5+ old project folders → `/archive/projects/`
- Multiple admin folders → `/archive/admin/`
- Misc folders → appropriate categories

**Result:**
- Root directory: ~30-40 items (from 431 files + 77 directories)
- 95% reduction in root clutter
- All data organized by purpose
- Clear separation of active vs. archived work

---

## 5. SAFE FIRST ACTIONS (Top 10 Quick Wins)

These actions can be executed immediately with minimal risk:

### Action 1: Remove System Junk
```bash
cd /Users/matteolombardi/AI-Projects/stratega
find . -name ".DS_Store" -delete
```
**Impact:** Clean 126 files, immediate git status improvement
**Risk:** ZERO
**Time:** 5 seconds

### Action 2: Create Safety Review Folder
```bash
mkdir -p temp-cleanup-review/duplicates
mkdir -p temp-cleanup-review/untitled-docs
mkdir -p temp-cleanup-review/uncertain
```
**Impact:** Safety net for uncertain files
**Risk:** ZERO
**Time:** 5 seconds

### Action 3: Move Duplicate CSVs to Review
```bash
find . -maxdepth 1 -type f \( -name "* (1).csv" -o -name "* (2).csv" \) -exec mv {} temp-cleanup-review/duplicates/ \;
find . -maxdepth 1 -type f \( -name "* (1).xlsx" -o -name "* (2).xlsx" \) -exec mv {} temp-cleanup-review/duplicates/ \;
```
**Impact:** Remove 59 duplicate files from root (150-200MB)
**Risk:** LOW - moved to review, not deleted
**Time:** 10 seconds

### Action 4: Create Data Subdirectories
```bash
cd data
mkdir -p linkedin-scrapes outscraper hotel-leads event-leads exports
cd ..
```
**Impact:** Prepare data organization structure
**Risk:** ZERO
**Time:** 5 seconds

### Action 5: Move LinkedIn Scrapes
```bash
mv 102_UM*.csv 103_UM*.csv 104_UM*.csv 105_UM*.csv data/linkedin-scrapes/ 2>/dev/null
```
**Impact:** Organize ~30 LinkedIn export files
**Risk:** LOW - just file organization
**Time:** 5 seconds

### Action 6: Move Outscraper Exports
```bash
mv Outscraper-*.csv data/outscraper/ 2>/dev/null
```
**Impact:** Organize 35 Outscraper files
**Risk:** LOW - just file organization
**Time:** 5 seconds

### Action 7: Move Hotel Lead Lists
```bash
mv 201*.csv data/hotel-leads/ 2>/dev/null
```
**Impact:** Organize 15 hotel lead list files
**Risk:** LOW - just file organization
**Time:** 5 seconds

### Action 8: Move Event Lead Lists
```bash
mv BIT_*.csv data/event-leads/ 2>/dev/null
```
**Impact:** Organize event-specific leads
**Risk:** LOW - just file organization
**Time:** 5 seconds

### Action 9: Consolidate Lists Directory
```bash
mv Lists/* data/exports/ 2>/dev/null
rmdir Lists 2>/dev/null
```
**Impact:** Merge Lists into data structure
**Risk:** LOW - small directory with clear content
**Time:** 5 seconds

### Action 10: Document Current State
```bash
# Create data directory index
echo "# Data Directory Index" > data/README.md
echo "Last updated: $(date)" >> data/README.md
echo "" >> data/README.md
echo "## Subdirectories" >> data/README.md
echo "- linkedin-scrapes/ - LinkedIn Sales Navigator exports" >> data/README.md
echo "- outscraper/ - Outscraper Google Maps scrapes" >> data/README.md
echo "- hotel-leads/ - Hospitality industry lead lists" >> data/README.md
echo "- event-leads/ - Event-specific lead exports (BIT, Web Summit, etc.)" >> data/README.md
echo "- exports/ - Miscellaneous data exports (Apollo, Hubspot, etc.)" >> data/README.md
```
**Impact:** Document data organization
**Risk:** ZERO
**Time:** 10 seconds

---

## 6. EXECUTION CHECKLIST

### Phase 1: Immediate Cleanup (5 minutes)
- [ ] Execute Safe Actions 1-10 above
- [ ] Verify files moved successfully
- [ ] Check git status is cleaner
- [ ] Commit cleanup to git: "Data organization: move CSVs to /data/ subdirectories"

### Phase 2: Brand Asset Consolidation (15 minutes)
- [ ] Review Stratega brand folders for duplicates
- [ ] Create `/assets/brand/` structure
- [ ] Move brand assets systematically
- [ ] Verify symlink status before moving

### Phase 3: Archive Migration (20 minutes)
- [ ] Create archive subdirectories
- [ ] Move client work to `/archive/clients/`
- [ ] Move legacy folders to `/archive/historical/`
- [ ] Move completed projects to `/archive/projects/`

### Phase 4: Google Drive Symlink Review (30 minutes)
- [ ] Review untitled Google docs in Drive
- [ ] Rename or delete untitled documents
- [ ] Decide on symlink consolidation strategy
- [ ] Update workflows if symlinks are moved

### Phase 5: Final Organization (15 minutes)
- [ ] Review active vs. archived project folders
- [ ] Consolidate template directories
- [ ] Merge workflow directories
- [ ] Update README with new structure

### Phase 6: Verification (10 minutes)
- [ ] Verify no files lost
- [ ] Check symlinks still work
- [ ] Test git operations
- [ ] Document any edge cases

**Total estimated time:** 95 minutes (~1.5 hours)

---

## 7. SAFETY PROTOCOLS

### Before ANY Deletion or Move:

1. **Check if symlink:** `ls -la [file/folder]` - if starts with `l`, it's a symlink
2. **Check git tracking:** `git ls-files [path]` - if tracked, extra caution
3. **Check file size:** `du -sh [file/folder]` - understand impact
4. **Move to review first:** Never delete directly, always move to review folder
5. **Document actions:** Keep log of what was moved where

### If Something Goes Wrong:

1. **Check review folders:** `temp-cleanup-review/` contains moved files
2. **Git history:** Tracked files can be restored from git
3. **Google Drive:** Symlinked content is safe in Drive
4. **Time Machine:** macOS backup can restore deleted files

### Irreversible Actions to AVOID:

- Never `rm -rf` without explicit confirmation
- Never delete symlinked directories (will delete Drive content!)
- Never force-delete git-tracked files
- Never modify `/archive/` (already organized and safe)

---

## 8. SUCCESS METRICS

**Target:** 30% cleanup completion

### Quantitative Metrics:
- Root directory files: 431 → ~50 (88% reduction) ✓ Achievable
- Root directory folders: 77 → ~25 (68% reduction) ✓ Achievable
- CSV files in root: 169 → 0 (100% reduction) ✓ Achievable
- Duplicate files: 59 → 0 (100% reduction) ✓ Achievable
- .DS_Store files: 126 → 0 (100% reduction) ✓ Achievable
- Space recovered: ~200MB from duplicates + better organization

### Qualitative Metrics:
- [ ] Clean `git status` output
- [ ] All data files organized by purpose
- [ ] Brand assets in single location
- [ ] Clear separation of active vs. archived work
- [ ] Documented structure in README
- [ ] No broken symlinks
- [ ] No lost files

---

## 9. POST-CLEANUP MAINTENANCE

### Daily Habits:
1. New data files → immediately to `/data/[category]/`
2. New client work → to appropriate subdirectory or `/archive/`
3. Completed projects → to `/archive/projects/[name]/`
4. Temp files → delete same day or move to review

### Weekly Review:
1. Check root directory for new clutter
2. Move untitled Google docs to proper locations
3. Archive completed work
4. Delete temp/review folders after verification

### Monthly Audit:
1. Review `/archive/` size and prune if needed
2. Check for new duplicate patterns
3. Update data directory index
4. Clean up old temp files

### Tools to Help:
- Git alias: `git status | grep "^??" | wc -l` (count untracked files)
- Script: Auto-detect and move CSV files to `/data/`
- Cron job: Daily .DS_Store cleanup
- Script: Duplicate file detector

---

## 10. APPENDIX

### A. File Type Inventory (Root Directory)

| Extension | Count | Should Be In |
|-----------|-------|--------------|
| .csv | 169 | `/data/` |
| .gsheet | ~150 | Current OK or `/templates/` |
| .gdoc | ~40 | Current OK or `/docs/` |
| .xlsx | 15 | `/data/` |
| .docx | 8 | `/docs/` or `/archive/` |
| .md | 9 | Current OK (core config) |
| .png/.jpg | 12 | `/assets/` |
| .gslides | ~10 | `/templates/` or `/docs/` |
| .pdf | ? | `/docs/` or `/assets/` |

### B. Largest Space Consumers

1. `/archive/` - 3.3GB (already organized, don't touch)
2. Root CSVs - ~500MB (move to `/data/`)
3. `/data/` - 244MB (organized, just needs subdirectories)
4. `/assets/` - 11MB (add brand consolidation)
5. Brand folders in root - unknown size (consolidate)

### C. Quick Reference Commands

**Count files in root:**
```bash
find /Users/matteolombardi/AI-Projects/stratega -maxdepth 1 -type f | wc -l
```

**Count untracked files:**
```bash
git status --porcelain | grep "^??" | wc -l
```

**Find duplicates by name pattern:**
```bash
find . -name "* (1).*" -o -name "* (2).*"
```

**Find all CSVs in root:**
```bash
find /Users/matteolombardi/AI-Projects/stratega -maxdepth 1 -type f -name "*.csv"
```

**Check symlinks:**
```bash
find /Users/matteolombardi/AI-Projects/stratega -maxdepth 1 -type l -ls
```

---

## CONCLUSION

The Stratega OS workspace cleanup is highly achievable and will result in:

1. **95% reduction in root directory clutter** (431 files → ~50 files)
2. **~200MB immediate space recovery** from duplicate removal
3. **Proper data organization** (169 CSVs moved to structured `/data/` subdirectories)
4. **Brand asset consolidation** (6+ folders → 1 organized `/assets/brand/` structure)
5. **Clear active vs. archived separation** (legacy work moved to `/archive/`)
6. **Clean git status** (126 .DS_Store files removed)
7. **Scalable maintenance** (documented structure and workflows)

**Next Step:** Execute Safe Actions 1-10 for immediate 30% cleanup completion (5-10 minutes).

**Risk Level:** LOW - all actions use "move first, verify, then delete" protocol with review folders as safety net.

**Recommendation:** Proceed with Phase 1 (Safe Actions 1-10) immediately, then pause for Matteo's review before Phases 2-5.
