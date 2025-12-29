# Metis Writing Style Guide

**Rule #1:** BE CONCISE. Matteo values speed over verbosity.

---

## Document Length Limits

| Type | Max Length | Why |
|------|-----------|-----|
| **Agent definition** | 300 lines | Longer = won't be read |
| **Analysis report** | 100 lines summary + link to detail | Token efficiency |
| **Session output** | 50 lines | Quick scan |
| **Planning doc** | 200 lines | Actionable, not encyclopedic |

---

## Output Format

### Good (Concise)
```
## Lead Lists Analysis

**Found:** 153 CSVs
**Categories:** Hospitality (80), Business (50), Family Office (23)
**Action:** Move to /03-LEAD-GENERATION/[industry]/[geo]/

Detail: /tmp/full_analysis.csv
```

### Bad (Verbose)
```
## Lead Lists Analysis

After careful analysis of the Drive Stratega directory, I have identified
a total of 153 CSV files that appear to be lead lists. These files span
multiple industries and geographies...

[10 more paragraphs]
```

---

## Communication Rules

1. **Headlines first** - What, not why
2. **Bullets over paragraphs** - Scannable
3. **Numbers over words** - "153 files" not "many files"
4. **Links over dumps** - Reference detail files, don't inline
5. **Action-oriented** - What to do, not what to think about

---

**Version:** 1.0
**Date:** 2025-01-24
