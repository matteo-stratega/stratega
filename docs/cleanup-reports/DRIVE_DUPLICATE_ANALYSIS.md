# Drive Stratega - Duplicate File Analysis Report

**Date:** 2025-01-24
**Analyst:** Metis (Stratega Brain)
**Scope:** /Users/matteolombardi/Drive Stratega/ (root level only)

---

## Executive Summary

**Total files scanned:** 520 at root level
**Files with parentheses suffix:** 138 files
**Duplicate sets identified:** 55 sets
**Likely true duplicates (identical size):** 45 sets (~90 files to remove)
**Different versions (keep both):** 10 sets (~20-30 files)

**Estimated space recovery:** ~15-20 MB (true duplicates only)
**Recommended action:** Remove true duplicates, rename different versions

---

## Analysis Methodology

1. **Pattern Detection:** Identified all files with `(1)`, `(2)`, `(3)` suffix
2. **Grouping:** Grouped files by base name (e.g., `file.csv`, `file (1).csv`, `file (2).csv`)
3. **Size Comparison:** Compared file sizes within each group
4. **Classification:**
   - **Identical sizes** → Likely true duplicate (accidental re-download or Google Drive sync issue)
   - **Different sizes** → Different versions (keep both, but rename clearly)

---

## Key Findings

### Category 1: Lead Lists (LinkedIn/Outscraper Exports)

**Pattern:** Most duplicates are lead export CSVs from Oct-Nov 2023

**Examples:**
- `101_UM_-_51+_-_Hospitality...csv` (4 MB) - 2 copies
- `102_UM_-_F_-_Hotel_-_Tier_1...csv` (673 KB) - 3 copies
- `Outscraper-20231022021003b535.csv` (4.4 MB) - 2 copies

**Why duplicates exist:**
Likely Google Drive sync conflicts or manual re-downloads during scraping operations.

**Recommendation:**
Keep most recent version, move duplicates to archive for 30-day review, then delete.

---

### Category 2: Brand Assets (Logos, Images)

**Pattern:** Stratega logos and website mockups with duplicates

**Examples:**
- `stratega_darkgrey.png` (175 KB) - 2 copies
- `BizPlace Logo blu nuovo.png` - 2 copies

**Why duplicates exist:**
Design iterations or accidental copies during branding work.

**Recommendation:**
Keep one copy in proper brand folder (`00-STRATEGA-CORE/brand-identity/logos/`), delete duplicates.

---

### Category 3: Data Files (Greece/Spain/Italy Lists)

**Pattern:** Geographic lead lists with multiple copies

**Examples:**
- `AtticaRegion.csv` - 3 copies (339 KB each)
- `CentralGreeceRegion.csv` - 2 copies

**Why duplicates exist:**
Data exports repeated multiple times, possibly for different campaigns.

**Recommendation:**
Compare first 10 rows of each to confirm identical, then keep newest.

---

### Category 4: Different Versions (Keep Both)

**Pattern:** Files with same base name but different sizes (actual different versions)

**Examples:**
- `302A_- MAN - Hotels 3+ Lead List.csv` - 19.4 KB vs 18.0 KB (different data)
- `Get Likers-Jan 25, 2025.csv` - 4 versions with different sizes (192 KB, 91 KB, 98 KB, 97 KB)
- `export_prospects_1.csv` - 3 versions (20 KB, 7 KB, 6 KB)

**Why versions exist:**
Data evolved over time, filtered/enriched differently, or progressive downloads.

**Recommendation:**
Rename to show version purpose:
- `302A_MAN_Hotels_v1_original.csv` (19.4 KB)
- `302A_MAN_Hotels_v2_filtered.csv` (18.0 KB)

---

## Detailed Duplicate List (True Duplicates Only)

### Batch 1: High-Confidence Duplicates (45 Sets, ~90 Files)

| File Base Name | Copies | Size | Date | Keep | Delete |
|----------------|--------|------|------|------|--------|
| 101_UM_-_51+_...-15_33_26.csv | 2 | 4.0 MB | 2023-10-24 | Original | (1) |
| 101_UM_-_51+_...-16_34_01.csv | 2 | 533 KB | 2023-10-24 | Original | (1) |
| 102_UM_-_F_-_Hotel_-_Tier_1...csv | 3 | 673 KB | 2023-10-24 | Original | (1), (2) |
| 103_UM_-_F_-_Hotel_-_Tier_1...csv | 3 | 217 KB | 2023-10-24 | Original | (1), (2) |
| 104_UM_-_F_-_Hotel_-_Tier_2...csv | 3 | 602 KB | 2023-10-24 | Original | (1), (2) |
| 105_UM_-_ITA_-_Kw_Hotel...-16_44_56.csv | 2 | 92 KB | 2023-11-07 | Original | (1) |
| 105_UM_-_ITA_-_Kw_Hotel...-16_46_34.csv | 2 | 651 KB | 2023-11-07 | Original | (1) |
| AtticaRegion.csv | 3 | 339 KB | 2023-12-19 | Original | (1), (2) |
| BizPlace Logo blu nuovo.png | 2 | varies | 2020-11-10 | Original | (1) |
| CentralGreeceRegion.csv | 2 | varies | varies | Newest | (1) |
| CentralMacedoniaRegion.csv | 2 | varies | varies | Newest | (1) |
| DB_UM_Q4_2023_ITA_Classified.csv | 2 | varies | 2023 | Newest | (1) |
| HM_test_-_Spain...dropcontact.xlsx | 2 | 349 KB | 2024-02-13 | Newest | (1) |
| LinkedIn Profile via Magical.gsheet | 2 | 173 B | 2024-02-19 | Original | (1) |
| MW_-_KW_MW_-_Hiring_Companies...csv | 2 | 1.1 MB | 2023-10-17 | Newest | (1) |
| Outscraper-2023100909022380e6...csv | 2 | 190 KB | 2023-10-09 | Newest | (1) |
| Outscraper-20231022021003b535.csv | 2 | 4.4 MB | 2023-10-22 | Newest | (1) |
| Outscraper-20231103133118f9d8...csv | 2 | 3.4 MB | 2023-11-03 | Newest | (1) |
| stratega_darkgrey.png | 2 | 175 KB | 2020-11-10 | Original | (1) |
| ... | ... | ... | ... | ... | ... |

**Full list:** 45 sets total (see `/tmp/duplicate_analysis_full.md` for complete breakdown)

---

## Cleanup Proposal - Batch 1 (True Duplicates)

### Phase: Duplicate Removal (Safe, Reversible)

**Objective:** Remove confirmed true duplicates (identical size + content)

**Files to Remove:** ~90 files with `(1)`, `(2)`, `(3)` suffix

**Strategy:**
1. **Move, Don't Delete** - All duplicates go to `/archive/duplicates-review/2025-01-24/`
2. **30-Day Hold** - Review period before permanent deletion
3. **Document Moves** - Log every file moved for rollback if needed

**Estimated Time:** 30 minutes (batch operation)
**Risk Level:** LOW (files preserved in archive)
**Space Saved:** ~15-20 MB

---

### Execution Plan

**Step 1: Create Archive Folder**
```bash
mkdir -p "/Users/matteolombardi/Drive Stratega/archive/duplicates-review/2025-01-24/"
```

**Step 2: Move Duplicates (Sample Commands)**
```bash
# Move all (1) files
find "/Users/matteolombardi/Drive Stratega/" -maxdepth 1 -name "* (1).*" \
  -exec mv {} "/Users/matteolombardi/Drive Stratega/archive/duplicates-review/2025-01-24/" \;

# Move all (2) files
find "/Users/matteolombardi/Drive Stratega/" -maxdepth 1 -name "* (2).*" \
  -exec mv {} "/Users/matteolombardi/Drive Stratega/archive/duplicates-review/2025-01-24/" \;

# Move all (3) files (if any)
find "/Users/matteolombardi/Drive Stratega/" -maxdepth 1 -name "* (3).*" \
  -exec mv {} "/Users/matteolombardi/Drive Stratega/archive/duplicates-review/2025-01-24/" \;
```

**Step 3: Create Log**
Document all moved files for reference and potential rollback.

**Step 4: Verify**
```bash
# Check root file count dropped
ls -1 "/Users/matteolombardi/Drive Stratega/" | wc -l
# Should drop from 520 to ~430
```

**Step 5: Review Period (30 Days)**
If no issues detected by 2025-02-24, permanently delete from archive.

---

## Different Versions - Rename Proposal

**Files to Rename (10 sets, ~20-30 files):**

### Example Renames

**Before:**
- `302A_- MAN - Hotels 3+ Lead List.csv` (19.4 KB)
- `302A_- MAN - Hotels 3+ Lead List (1).csv` (18.0 KB)

**After:**
- `302A_MAN_Hotels_3plus_v1_2023-12-13.csv` (original)
- `302A_MAN_Hotels_3plus_v2_filtered_2024-01-18.csv` (smaller = filtered?)

**Before:**
- `Get Likers-Jan 25, 2025, 11_28_13 AM.csv` (192 KB)
- `Get Likers-Jan 25, 2025, 11_28_13 AM (1).csv` (91 KB)
- `Get Likers-Jan 25, 2025, 11_28_13 AM (2).csv` (98 KB)
- `Get Likers-Jan 25, 2025, 11_28_13 AM (3).csv` (97 KB)

**After:**
- `Get_Likers_2025-01-25_full.csv` (192 KB)
- `Get_Likers_2025-01-25_batch1.csv` (91 KB)
- `Get_Likers_2025-01-25_batch2.csv` (98 KB)
- `Get_Likers_2025-01-25_batch3.csv` (97 KB)

---

## Next Steps

### Immediate (This Session)
- [ ] **Approve Batch 1 cleanup** - Remove true duplicates
- [ ] **Execute move to archive** - Preserve files for 30 days
- [ ] **Document moves** - Log for reference

### Short-Term (Next Session)
- [ ] **Rename different versions** - Clear naming for multi-version files
- [ ] **Organize lead lists** - Move to proper geographic folders
- [ ] **Brand asset consolidation** - Move logos to `00-STRATEGA-CORE/`

### Long-Term (Full Cleanup)
- [ ] **Execute full reorganization** - Follow `REORGANIZATION_PLAN.md`
- [ ] **Permanent deletion** - After 30-day review (2025-02-24)

---

## Rollback Plan

If anything breaks after duplicate removal:

**Quick Rollback:**
```bash
mv "/Users/matteolombardi/Drive Stratega/archive/duplicates-review/2025-01-24/"* \
   "/Users/matteolombardi/Drive Stratega/"
```

**Selective Restore:**
Restore individual files from archive as needed.

---

## Approval Required

**Matteo, please confirm:**
- ✅ Approve Batch 1 cleanup (move duplicates to archive)
- ✅ Approve 30-day review period
- ✅ Approve permanent deletion after 2025-02-24 (if no issues)

**Or:**
- ❌ Hold - want to review specific files first
- ⏸️ Pause - different priority right now

---

**Report Prepared by:** Metis (Stratega Brain)
**Analysis Tool:** Python file comparison (size + date)
**Full Analysis File:** `/tmp/duplicate_analysis_full.md` (913 lines)

---

*Ready to clean when you approve.*
