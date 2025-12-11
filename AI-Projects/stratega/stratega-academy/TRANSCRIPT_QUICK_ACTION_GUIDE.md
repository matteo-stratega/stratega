# Transcript Discrepancy - Quick Action Guide

## TL;DR

Your corrected SRT files have been significantly edited beyond simple corrections. Only **m8-fin** (86.6% match) is close to the original. The rest range from 18-55% similarity.

---

## Critical Issues Found

### 🔴 Priority 1: Requires Immediate Review

**m2-ICP (18.0% similarity)**
- Issue: Almost completely rewritten with paraphrasing
- Example: "take all this" → "do it"
- Action: Re-transcribe from original or accept edited version

**m4-content (20.8% similarity)**
- Issue: Heavily restructured sentences
- Example: "not content the" → "to have no content than"
- Action: Verify key technical points against audio

**m6-tools (36.6% similarity)**
- Issue: 69 differences, many technical terms changed
- Example: "lits" → "leads" (correct), but many others
- Action: Review all tool names and technical terms

### ⚠️ Priority 2: Moderate Review Needed

**m3-icp (41.5%)**
- Critical change: "cs navigator" → "apollo" (tool name)
- Action: Verify tool references

**intro (46.5%)**
- Changes: "experience" → "explore", "status" → "stage"
- Action: Check if meaning preserved

**m5-copy (51.6%)**
- Multiple framework corrections: "iedapas" → "aida"
- Action: Verify all marketing framework names

**m7-ops (55.2%)**
- Critical: "stuff" → "staff" (meaning change)
- Action: Verify business terms

### ✅ Priority 3: Minor Review

**m8-fin (86.6%)**
- Only 18 minor differences
- Mostly correct
- Action: Quick scan for quality assurance

---

## Decision Tree

### Option A: You Want Verbatim Transcripts
**Choose this if:** Accuracy to spoken word matters most

**Actions:**
1. Use the JSON transcripts as source of truth
2. Extract text from all JSON files
3. Apply minimal corrections (only clear mishearings)
4. Preserve filler words, hesitations, natural speech

**Time Required:** 2-3 hours to re-process all modules

---

### Option B: You Want Edited/Clean Transcripts
**Choose this if:** Professional clarity matters most

**Actions:**
1. Keep current SRT files as base
2. Review only critical semantic changes (see Priority 1 & 2)
3. Verify technical terms, tool names, frameworks
4. Accept paraphrasing if meaning preserved

**Time Required:** 1-2 hours for priority reviews

---

### Option C: Hybrid Approach (Recommended)
**Choose this if:** Balance accuracy and readability

**Actions:**
1. **High priority modules (m2, m4, m6):** Re-transcribe from JSON
2. **Medium priority (m3, intro, m5, m7):** Spot-check against audio
3. **Low priority (m8):** Accept current version
4. Apply consistent style guide for all

**Time Required:** 3-4 hours total

---

## Quick Verification Script

To spot-check specific sections against audio:

```bash
# Install ffmpeg if needed (to extract audio snippets)
brew install ffmpeg

# Example: Extract 30 seconds from module 2 at timestamp 2:30
ffmpeg -i "path/to/m2-ICP.m4a" -ss 00:02:30 -t 00:00:30 snippet.m4a
```

Then manually compare snippet to both JSON and SRT text.

---

## Common Patterns Found

### ✅ Acceptable Corrections
- "copyrighted" → "copywriting"
- "iedapas" → "aida"
- "lits" → "leads"
- Filler word removal (um, uh, like)
- Contraction standardization

### ⚠️ Questionable Edits
- "experience" → "explore"
- "messed up" → "messy"
- "status" → "stage"
- "replaced" → "a response"
- "bumped" → "bombarded"

### 🔴 Critical Changes
- "stuff" → "staff" (completely different meaning)
- "cs navigator" → "apollo" (different tool)
- "window" → "winning formula" (reconstruction)
- "getting out of our minds" → "driving ourselves crazy" (paraphrase)

---

## Files You Have

1. **TRANSCRIPT_DISCREPANCY_REPORT.md** (15KB)
   - Full detailed analysis
   - All differences listed per module
   - Timestamps where available

2. **TRANSCRIPT_ANALYSIS_SUMMARY.md** (5.5KB)
   - Executive overview
   - Recommendations by category
   - Technical methodology

3. **compare_transcripts.py** (7KB)
   - Python script to re-run analysis
   - Can be modified to adjust sensitivity
   - Reusable for future modules

4. **TRANSCRIPT_QUICK_ACTION_GUIDE.md** (This file)
   - Fastest route to decision
   - Actionable steps only

---

## Recommended Next Action

**Right now:**
1. Read the detailed report for **m2-ICP** and **m4-content**
2. Listen to 2-3 key sections from those modules
3. Decide: Do the edits help or hurt?
4. Choose Option A, B, or C above
5. Proceed accordingly

**Timeline:**
- 15 min: Review reports
- 30 min: Spot-check audio
- 15 min: Make decision
- 1-4 hours: Execute chosen option (depending on A/B/C)

---

## Questions to Answer Before Proceeding

1. **Who edited the SRTs?** (You, AI tool, transcription service?)
2. **What was the editing goal?** (Clarity, professionalism, accuracy?)
3. **Are these for subtitles or course materials?** (Different standards apply)
4. **Do students need verbatim or polished content?**
5. **Will these be used for searchable transcripts?** (Affects SEO/findability)

Your answers will determine which option (A/B/C) is optimal.

---

## Support

If you need to re-run the analysis with different parameters:

```bash
cd /Users/matteolombardi/AI-Projects/stratega/stratega-academy
python3 compare_transcripts.py
```

The script can be modified to:
- Ignore different filler words
- Adjust similarity thresholds
- Focus on specific modules only
- Export to different formats
