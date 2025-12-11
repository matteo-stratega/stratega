# Transcript Analysis - Complete Package

**Analysis Date:** December 3, 2025
**Project:** Stratega Academy Module Transcripts
**Task:** Compare Screen Studio JSON transcripts with corrected SRT files

---

## Quick Start

**New to this analysis? Start here:**

1. **Visual Overview (2 min)** → [TRANSCRIPT_RESULTS_VISUAL.txt](./TRANSCRIPT_RESULTS_VISUAL.txt)
2. **Action Guide (5 min)** → [TRANSCRIPT_QUICK_ACTION_GUIDE.md](./TRANSCRIPT_QUICK_ACTION_GUIDE.md)
3. **Executive Summary (10 min)** → [TRANSCRIPT_ANALYSIS_SUMMARY.md](./TRANSCRIPT_ANALYSIS_SUMMARY.md)
4. **Full Report (30 min)** → [TRANSCRIPT_DISCREPANCY_REPORT.md](./TRANSCRIPT_DISCREPANCY_REPORT.md)

---

## File Structure

### 📊 Reports

| File | Size | Purpose | Best For |
|------|------|---------|----------|
| **TRANSCRIPT_RESULTS_VISUAL.txt** | 4KB | ASCII chart summary | Quick visual scan |
| **TRANSCRIPT_QUICK_ACTION_GUIDE.md** | 5.3KB | Decision framework | Knowing what to do next |
| **TRANSCRIPT_ANALYSIS_SUMMARY.md** | 5.5KB | Executive overview | Understanding the issue |
| **TRANSCRIPT_DISCREPANCY_REPORT.md** | 15KB | Complete analysis | Deep dive into each module |
| **TRANSCRIPT_ANALYSIS_INDEX.md** | This file | Navigation hub | Finding what you need |

### 🔧 Tools

| File | Size | Purpose |
|------|------|---------|
| **compare_transcripts.py** | 10KB | Python analysis script |

**Usage:**
```bash
cd /Users/matteolombardi/AI-Projects/stratega/stratega-academy
python3 compare_transcripts.py
```

---

## Key Findings Summary

### The Numbers

| Module | Similarity | Status | Action Required |
|--------|-----------|--------|-----------------|
| m2-ICP | 18.0% | 🔴 Critical | Complete review |
| m4-content | 20.8% | 🔴 Critical | Complete review |
| m6-tools | 36.6% | 🔴 Critical | Technical term review |
| m3-icp | 41.5% | ⚠️ Moderate | Spot check |
| intro | 46.5% | ⚠️ Moderate | Spot check |
| m5-copy | 51.6% | ⚠️ Moderate | Framework verification |
| m7-ops | 55.2% | ⚠️ Moderate | Business term check |
| m8-fin | 86.6% | ✅ Good | Minor review |

### The Bottom Line

**7 out of 8 modules have been significantly edited** beyond simple transcription corrections. The corrected SRT files contain:
- Paraphrasing and rewording
- Sentence restructuring
- Some changed business terminology
- Legitimate corrections mixed with editorial changes

**This is not necessarily bad**, but you need to decide if you want:
- **Verbatim accuracy** (what was actually said)
- **Editorial clarity** (improved/cleaned up version)
- **Hybrid approach** (accurate but polished)

---

## Critical Issues to Address

### 🔴 Must Fix

1. **m7-ops:** "stuff" → "staff" (completely different meaning)
2. **m3-icp:** "cs navigator" → "apollo" (different tool name)
3. **m2-ICP:** Extensive paraphrasing throughout

### ⚠️ Should Verify

4. Multiple framework name corrections (verify accuracy)
5. Technical term changes across m6-tools
6. Sentence reconstructions in m4-content

### ✅ Acceptable

7. Filler word removal (um, uh, like)
8. Contraction standardization
9. Clear transcription error fixes (copyrighted → copywriting)

---

## Recommended Workflow

### Phase 1: Assessment (30 minutes)
1. Read **TRANSCRIPT_QUICK_ACTION_GUIDE.md**
2. Review critical changes in **TRANSCRIPT_DISCREPANCY_REPORT.md**
3. Spot-check 3-5 sections against original audio
4. Decide on approach (A/B/C from Quick Action Guide)

### Phase 2: Action (1-4 hours depending on choice)
- **Option A (Verbatim):** Re-extract from JSON → 2-3 hours
- **Option B (Edited):** Review critical changes only → 1-2 hours
- **Option C (Hybrid):** Mixed approach → 3-4 hours

### Phase 3: Documentation (30 minutes)
5. Create transcript style guide for future modules
6. Document which edits are acceptable/unacceptable
7. Establish QA process

---

## How to Use the Python Script

### Basic Usage
```bash
python3 compare_transcripts.py
```

### Modify for Custom Analysis

The script can be adjusted to:
- Focus on specific modules only
- Change similarity calculation method
- Adjust which filler words to ignore
- Export results in different formats
- Include/exclude certain types of changes

See comments in **compare_transcripts.py** for modification points.

---

## Source Files Analyzed

### JSON Transcripts (Original - Source of Truth)
Located in: `/Users/matteolombardi/Screen Studio Projects/`

- `intro.screenstudio/recording/channel-2-microphone-0.m4a-transcript.json`
- `mod2-ICP.screenstudio/recording/channel-2-microphone-0.m4a-transcript.json`
- `m3-icp.screenstudio/recording/channel-2-microphone-0.m4a-transcript.json`
- `m4-content.screenstudio/recording/channel-2-microphone-0.m4a-transcript.json`
- `m5-copy.screenstudio/recording/channel-2-microphone-0.m4a-transcript.json`
- `m6-tools.screenstudio/recording/channel-2-microphone-0.m4a-transcript.json`
- `m7-ops.screenstudio/recording/channel-2-microphone-0.m4a-transcript.json`
- `m8-fin.screenstudio/recording/channel-2-microphone-0.m4a-transcript.json`

### SRT Files (Corrected - Under Review)
Located in: `/Users/matteolombardi/AI-Projects/stratega/stratega-academy/school transcripts/`

- `intro-corrected.srt`
- `m2-ICP-corrected.srt`
- `m3-icp-corrected.srt`
- `m4-content-corrected.srt`
- `m5-copy-corrected.srt`
- `m6-tools-corrected.srt`
- `m7-ops-corrected.srt`
- `m8-fin-corrected.srt`

---

## Technical Notes

### Comparison Methodology
- **Normalization:** Lowercase, punctuation removed, whitespace normalized
- **Filler filtering:** Common words like "um", "uh", "like" automatically excluded
- **Similarity algorithm:** Python's SequenceMatcher (difflib)
- **Threshold:** No arbitrary cutoff; all differences reported
- **Focus:** Word-level semantic changes, not styling

### Limitations
- Cannot assess tone, emphasis, or delivery quality
- May flag acceptable variations as differences
- Context-dependent changes require manual review
- Timestamps from JSON not perfectly aligned with SRT in report

---

## Questions & Decisions Needed

Before proceeding, answer these:

1. **Who made the edits to the SRT files?**
   - You manually?
   - AI transcription service?
   - Automated tool?

2. **What was the goal of the corrections?**
   - Fix transcription errors only?
   - Improve readability?
   - Make content more professional?

3. **What is the intended use?**
   - Video subtitles?
   - Course materials?
   - Searchable transcripts?
   - Study guides?

4. **What standard do you want going forward?**
   - Verbatim accuracy?
   - Polished clarity?
   - Something in between?

5. **How much time can you invest?**
   - Quick fix (1 hour)?
   - Thorough review (4 hours)?
   - Complete re-do (8+ hours)?

Your answers determine the optimal path forward.

---

## Support & Maintenance

### Re-running Analysis
If you get new transcript versions or want to re-analyze:
```bash
cd /Users/matteolombardi/AI-Projects/stratega/stratega-academy
python3 compare_transcripts.py
```

### Updating the Script
Key sections to modify:
- **Line 22-68:** Module definitions (add/remove modules)
- **Line 70:** Filler words list (customize what to ignore)
- **Line 143:** Similarity calculation (adjust algorithm)

### Questions or Issues?
- Check the detailed report first: **TRANSCRIPT_DISCREPANCY_REPORT.md**
- Review examples in: **TRANSCRIPT_ANALYSIS_SUMMARY.md**
- Follow decision tree in: **TRANSCRIPT_QUICK_ACTION_GUIDE.md**

---

## Deliverables Checklist

- [x] Complete discrepancy analysis
- [x] Similarity scores for all 8 modules
- [x] Detailed difference listings
- [x] Executive summary with recommendations
- [x] Quick action guide with decision framework
- [x] Visual ASCII chart summary
- [x] Reusable Python script
- [x] Navigation index (this file)

---

**Analysis completed:** December 3, 2025
**Location:** `/Users/matteolombardi/AI-Projects/stratega/stratega-academy/`
**Tools used:** Python 3, difflib, JSON parsing, SRT parsing

**Next action:** Read [TRANSCRIPT_QUICK_ACTION_GUIDE.md](./TRANSCRIPT_QUICK_ACTION_GUIDE.md) to decide how to proceed.
