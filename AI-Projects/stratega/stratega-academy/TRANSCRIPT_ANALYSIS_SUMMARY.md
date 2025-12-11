# Transcript Analysis Summary

## Overview

Comparison analysis between Screen Studio original JSON transcripts and corrected SRT files for Stratega Academy course modules.

**Analysis Date:** December 3, 2025
**Files Analyzed:** 8 modules (intro + m2-m8)
**Method:** Semantic comparison focusing on word-level differences

---

## Key Findings

### Critical Issue Identified

**Most modules show LOW similarity scores (18% - 55%)**, indicating the corrected SRT files contain substantial edits beyond simple corrections.

### Similarity Breakdown

| Module | Score | Assessment |
|--------|-------|------------|
| m8-fin | 86.6% | GOOD - Mostly accurate |
| m7-ops | 55.2% | MODERATE - Significant edits |
| m5-copy | 51.6% | MODERATE - Significant edits |
| intro | 46.5% | LOW - Major changes |
| m3-icp | 41.5% | LOW - Major changes |
| m6-tools | 36.6% | LOW - Major changes |
| m4-content | 20.8% | VERY LOW - Extensive changes |
| m2-ICP | 18.0% | VERY LOW - Extensive changes |

---

## Analysis of Discrepancy Types

### 1. Legitimate Corrections (Expected)
- **"copyrighted" → "copywriting"** (technical term correction)
- **"kobe writing" → "copywriting"** (transcription error fix)
- **"iedapas" → "aida"** (acronym correction)
- **"atsa" → "facebook"** (mishearing correction)
- **"eta" → "email"** (abbreviation correction)
- **"le" → "lead"** (truncation fix)
- **"lits" → "leads"** (mishearing correction)

### 2. Editorial Changes (Concerning)
- **"experience" → "explore"** (word substitution)
- **"messed up" → "messy"** (tone change)
- **"status" → "stage"** (semantic change)
- **"replaced" → "a response"** (meaning alteration)
- **"bumped" → "bombarded"** (different word entirely)
- **"window" → "winning formula"** (phrase reconstruction)
- **"getting out of our minds" → "driving ourselves crazy"** (paraphrasing)
- **"stuff" → "staff"** (changes meaning completely)
- **"pose" → "a poc"** (business term correction, but POC vs pose are very different)

### 3. Structural Edits
- Removed filler words ("you know", "kind of", "like") - Expected
- Removed repeated words - Expected
- Added/removed articles (a, the, an) - Minor concern
- Changed contractions ("we are" → "we're", "you are" → "you're") - Acceptable

---

## Concerns

### Major Red Flags

1. **m2-ICP (18% similarity)** - Almost completely rewritten
   - "take all this" → "do it"
   - "getting out of our minds" → "driving ourselves crazy"
   - "one is the" → "first is"

2. **m4-content (20.8% similarity)** - Heavily edited
   - "not content the" → "to have no content than"
   - "we can just the" → "with a"
   - "position in" → "positioning"

3. **Pattern of paraphrasing** - Many instances where the SRT doesn't match what was actually spoken but conveys similar meaning in "better" language.

### Questions to Address

1. **Was this intentional?** Did someone manually edit the transcripts to improve clarity/professionalism?
2. **Source of edits?** Were these AI-enhanced transcriptions that added interpretation?
3. **Accuracy requirement?** For educational content, should we preserve exact wording or prioritize clarity?

---

## Recommendations

### Immediate Actions

1. **Review m2-ICP and m4-content urgently** - These have the most significant deviations
2. **Spot-check audio** - Listen to 3-5 key sections per module to verify which version is more accurate
3. **Decide on standard** - Determine if:
   - Verbatim accuracy is required (use JSON transcripts as source)
   - Edited clarity is acceptable (use current SRTs)
   - Hybrid approach (clean up obvious errors only)

### Module-Specific Actions

**m8-fin (86.6%)** ✅
- Approved with minor review
- Most accurate transcription
- Safe to use as-is

**m7-ops (55.2%)** ⚠️
- Review "stuff" → "staff" (critical meaning change)
- Review "pose" → "poc" (business term)
- Check "atsa" → "facebook" and "eta" → "email"

**m5-copy (51.6%)** ⚠️
- Multiple "iedapas" → "aida" corrections (verify framework name)
- Review "window" → "winning formula"

**intro (46.5%)** ⚠️
- Review "experience" → "explore"
- Check "status" → "stage"
- Verify "messed up" → "messy"

**m3-icp (41.5%)** 🔴
- Review "cs navigator" → "apollo" (tool name change)
- Check "endorse" → "emphasize"

**m6-tools (36.6%)** 🔴
- 69 differences found
- Comprehensive review needed
- Focus on technical terms

**m4-content (20.8%)** 🔴
- Requires complete review
- Extensive restructuring of sentences
- May need re-transcription

**m2-ICP (18.0%)** 🔴
- Requires complete review
- Heavily paraphrased
- Consider re-transcription from original audio

---

## Technical Notes

### Methodology
- Normalized text (lowercase, removed punctuation)
- Filtered out common filler words automatically
- Used SequenceMatcher for similarity calculation
- Focused on word-level semantic differences

### Limitations
- Cannot assess tone, emphasis, or delivery
- May flag acceptable variations as differences
- Context-dependent changes hard to evaluate automatically

---

## Next Steps

1. **Decision point:** Verbatim vs. edited transcripts?
2. **Spot-check audio:** Sample 5 sections to verify accuracy
3. **If verbatim required:** Re-extract from JSON transcripts
4. **If edited acceptable:** Review critical meaning changes only
5. **Create style guide:** Document acceptable editing practices for future modules

---

## Files Generated

- **TRANSCRIPT_DISCREPANCY_REPORT.md** - Detailed difference analysis
- **compare_transcripts.py** - Python script for comparison
- **TRANSCRIPT_ANALYSIS_SUMMARY.md** - This executive summary
