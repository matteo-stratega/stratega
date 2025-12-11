# Stratega Academy - Deployment Guide

**Version:** 1.0
**Created:** 26 November 2025
**Last Updated:** 26 November 2025

This guide provides detailed instructions for deploying Stratega Academy course materials to students and learning platforms.

---

## Table of Contents

1. [Current Status](#current-status)
2. [File Inventory & Assets](#file-inventory--assets)
3. [Deployment Checklist](#deployment-checklist)
4. [Platform-Specific Instructions](#platform-specific-instructions)
5. [Quality Assurance](#quality-assurance)
6. [Student Access Setup](#student-access-setup)
7. [Ongoing Maintenance](#ongoing-maintenance)
8. [Troubleshooting](#troubleshooting)

---

## Current Status

### What's Ready NOW
✓ **Complete:** All 8 video transcripts (original + professionally corrected)
✓ **Complete:** 7 PDF slide decks for modules 1-8
✓ **Complete:** Crono Outbound Guide supplementary resource
✓ **Complete:** Course structure and framework documentation
✓ **Complete:** Unified directory organization

### What's Missing
✗ **Video files:** 9 module video files (.mp4 or .mov) - Status: MISSING
  - Module 1: intro.mp4
  - Module 2: offering.mp4 (or m2.mp4)
  - Module 3: m3-icp.mp4
  - Module 4: m4-content.mp4
  - Module 5: m5-copy.mp4
  - Module 6: m6-tools.mp4
  - Module 7: m7-ops.mp4
  - Module 8: m8-fin.mp4
  - Module 9: final.mp4 (or m8-fin.mp4)

### What's Optional
◐ **Notion Integration:** Not yet synchronized (check if Notion workspace exists)
◐ **Downloadable Workbook:** Could be created as PDF from slides
◐ **Discussion Forum:** Not yet set up

---

## File Inventory & Assets

### Directory Location
**Primary:** `/Users/matteolombardi/AI-Projects/stratega/stratega-academy/`

### File Structure Summary
```
stratega-academy/
├── README.md (navigation & overview)
├── module-01-intro/
│   ├── transcript-original.srt (7.7 KB)
│   ├── transcript-corrected.srt (7.7 KB)
│   └── VIDEO_MISSING.txt
├── module-02-offering/
│   ├── transcript-original.srt (variable)
│   ├── transcript-corrected.srt (variable)
│   ├── slides.pdf (1.9 MB)
│   └── VIDEO_MISSING.txt
├── module-03-icp-company/
│   ├── transcript-original.srt (9.2 KB)
│   ├── transcript-corrected.srt (9.0 KB)
│   ├── slides.pdf (2.0 MB)
│   └── VIDEO_MISSING.txt
├── module-04-icp-people/
│   ├── transcript-original.srt (11 KB)
│   ├── transcript-corrected.srt (11 KB)
│   ├── slides.pdf (2.2 MB)
│   └── VIDEO_MISSING.txt
├── module-05-content/
│   ├── transcript-original.srt (12 KB)
│   ├── transcript-corrected.srt (12 KB)
│   ├── slides.pdf (1.9 MB)
│   └── VIDEO_MISSING.txt
├── module-06-copywriting/
│   ├── transcript-original.srt (13 KB)
│   ├── transcript-corrected.srt (13 KB)
│   ├── slides.pdf (1.9 MB)
│   └── VIDEO_MISSING.txt
├── module-07-tools/
│   ├── transcript-original.srt (11 KB)
│   ├── transcript-corrected.srt (11 KB)
│   ├── slides.pdf (1.9 MB)
│   ├── crono-guide.pdf (724 KB)
│   └── VIDEO_MISSING.txt
├── module-08-operations/
│   ├── transcript-original.srt (9.8 KB)
│   ├── transcript-corrected.srt (9.8 KB)
│   ├── slides.pdf (2.1 MB)
│   └── VIDEO_MISSING.txt
├── module-09-final/
│   ├── transcript-original.srt (3.9 KB)
│   ├── transcript-corrected.srt (3.9 KB)
│   └── VIDEO_MISSING.txt
├── docs/
│   ├── COURSE_STRUCTURE.md (this detailed guide)
│   ├── CORRECTION_SUMMARY.md (initial correction report)
│   ├── ENHANCED_CORRECTION_REPORT.md (detailed technical corrections)
│   ├── ENHANCEMENT_SUMMARY.txt (quick reference)
│   └── DEPLOYMENT_GUIDE.md (this file)
└── notion-sync/
    └── (ready for Notion exports if needed)
```

### Asset Sizes
- **Total Transcripts:** ~95 KB (all 16 files combined)
- **Total Slides:** ~16 MB (7 PDFs)
- **Total Crono Guide:** 724 KB
- **Video Files:** [PENDING - estimate 2-3 GB for 8-10 hours of 1080p video]
- **Documentation:** ~150 KB
- **TOTAL WITHOUT VIDEOS:** ~16.9 MB
- **TOTAL WITH VIDEOS (estimated):** ~2.5-3.5 GB

---

## Deployment Checklist

### Phase 1: Pre-Deployment Preparation (Week 1)
- [ ] Locate or acquire all 9 video files
- [ ] Verify video formats (.mp4 or .mov)
- [ ] Check video quality and resolution (minimum 1080p)
- [ ] Verify audio quality and sync with transcripts
- [ ] Review all transcripts for accuracy
- [ ] Test all PDF slides for compatibility
- [ ] Verify crono-guide.pdf accessibility
- [ ] Create backup of all materials

### Phase 2: Platform Setup (Week 2)
Choose your learning platform and follow platform-specific instructions below:
- [ ] Select LMS platform (Teachable, Kajabi, Moodle, Canvas, Blackboard, etc.)
- [ ] Create course structure in platform
- [ ] Set up user roles and permissions
- [ ] Configure student enrollment
- [ ] Create course announcements/welcome message

### Phase 3: Content Upload (Week 3)
- [ ] Upload all video files to platform (see platform-specific steps)
- [ ] Verify video playback works
- [ ] Upload PDF slides to each module
- [ ] Upload crono-guide.pdf to Module 7
- [ ] Add transcripts (SRT or converted)
- [ ] Link transcripts to videos (if supported)
- [ ] Add course README and navigation guide

### Phase 4: Configuration & Testing (Week 4)
- [ ] Configure video players (quality settings, subtitles)
- [ ] Enable/disable commenting, discussions
- [ ] Set up email notifications
- [ ] Configure progress tracking
- [ ] Test student experience
- [ ] Set up completion certificates
- [ ] Configure quiz/assessment tools (if using)

### Phase 5: Launch & Monitor (Week 5+)
- [ ] Soft launch to pilot group (5-10 students)
- [ ] Gather feedback and fix issues
- [ ] Public launch to full audience
- [ ] Monitor student engagement
- [ ] Track completion metrics
- [ ] Support student inquiries

---

## Platform-Specific Instructions

### Teachable (Recommended for most courses)

**Why Teachable?**
- Student-friendly interface
- Built-in video player and progress tracking
- Email notifications and certificates
- Student community features
- Good for courses 5-50 hours

**Setup Steps:**

1. **Create Course**
   - Log into Teachable dashboard
   - Create new course: "Stratega Academy"
   - Set course image and description
   - Configure access (free/paid)

2. **Create Module Structure**
   - Create 9 sections (Module 1-9)
   - In each section, create lesson for:
     - Video lesson
     - Transcript resource
     - Slides resource
     - Any additional materials

3. **Upload Videos**
   - In each lesson, select "Add video"
   - Upload .mp4 files (Teachable accepts up to 5GB per video)
   - Configure video quality and autoplay
   - Note: Processing can take 15-30 min per video

4. **Add Resources**
   - Under each video lesson, add section for resources
   - Upload PDF slides (slides.pdf)
   - Upload transcript (SRT format or PDF)
   - For Module 7: add crono-guide.pdf

5. **Set Up Progress Tracking**
   - Enable completion tracking by video
   - Set minimum video watch percentage (e.g., 80%)
   - Configure milestone tracking

6. **Certificate Setup**
   - Create certificate template
   - Set criteria: Complete all 9 modules
   - Enable automatic email of certificate

7. **Community & Support**
   - Enable student discussions per module
   - Pin announcements for each module
   - Create FAQ document

### Kajabi

**Setup Steps:**

1. **Course Creation**
   - New product → Course
   - Name: "Stratega Academy Growth System"
   - Set pricing and access rules

2. **Module Setup**
   - Create 9 lessons (one per module)
   - Set lesson order and dependencies
   - Configure lesson visibility

3. **Video Upload**
   - Add video lesson component
   - Upload .mp4 via Kajabi uploader
   - Configure subtitles/transcripts
   - Set autoplay and quality

4. **Resources**
   - Add downloadable resources component
   - Attach PDF slides per module
   - Attach transcript files

5. **Email Sequences**
   - Create welcome email
   - Auto-send module introduction emails
   - Send congratulations on completion

### Moodle (Open Source - for self-hosted)

**Setup Steps:**

1. **Course Creation**
   - Create new course
   - Configure course settings (enrollments, etc.)

2. **Topic Setup**
   - Create 9 topics (Module 1-9)
   - Add activity elements to each

3. **Video Embedding**
   - Add resource → Video file
   - Upload .mp4 files
   - Or embed from external host (YouTube, Vimeo)

4. **Resource Upload**
   - Add resources for PDF slides
   - Add resources for SRT transcripts
   - Configure file access

5. **Completion Tracking**
   - Enable activity completion
   - Set video watch requirements
   - Configure course completion

### Other Platforms

**Canvas (for academic institutions):**
- Use Modules for course structure
- Upload videos to Canvas Studio
- Link resources in module sections
- Configure completion requirements

**Blackboard (for enterprises):**
- Create Content Folders for each module
- Upload videos (may need encoding)
- Add resource files
- Configure grade tracking

**YouTube/Vimeo + Standalone Site:**
- Host videos on platform
- Create HTML/Markdown course guide
- Link to resources
- Use email for enrollment management

---

## Transcript Integration

### Current State
- All transcripts available in `.srt` (SubRip) format
- Both original and corrected versions available
- **Recommendation:** Use corrected transcripts for deployment

### Deployment Options

**Option 1: Platform Native (Recommended)**
If your platform supports SRT files:
1. Upload corrected SRT files directly
2. Platform auto-generates captions
3. Auto-syncs with video playback
4. Searchable transcript available to students

Supported by: Teachable, Kajabi, YouTube, Vimeo, Canvas

**Option 2: Manual Captions**
1. Upload SRT files to your video platform's caption editor
2. Review and adjust timing if needed
3. Test playback synchronization
4. Enable closed captions toggle for students

**Option 3: PDF Transcript**
For platforms without SRT support:
1. Convert SRT files to PDF
2. Upload as downloadable resource
3. Students can reference while watching
4. Provide search-friendly version

**SRT to PDF Conversion Command (Mac/Linux):**
```bash
# Simple method: use online converter or
# Python script to convert SRT to readable format
```

### Quality Standards
- ✓ All transcripts professionally corrected
- ✓ 188 total corrections applied
- ✓ Framework terminology verified
- ✓ Technical accuracy checked
- ✓ Ready for production use

---

## Student Access Setup

### Enrollment Options

**Option A: Open/Free Enrollment**
- Course publicly available
- Students sign up freely
- No payment required
- Good for: Building audience, lead generation

**Option B: Paid Enrollment**
- Set course price ($29-$99 range typical)
- Use Stripe/PayPal for payments
- Email confirmation sent on purchase
- Good for: Revenue generation, committed audience

**Option C: Closed/Cohort-Based**
- Manual enrollment only
- Assign students to cohorts
- Can batch email announcements
- Good for: Corporate training, coaching groups

**Option D: Hybrid (Recommended)**
- Free preview of Module 1
- Paid enrollment for full course
- Includes support and community
- Includes certificate

### User Roles & Permissions

**Admin/Instructor**
- Can upload content
- Can edit course materials
- Can view all student progress
- Can send communications

**Teaching Assistant**
- Can monitor student progress
- Can answer questions
- Cannot edit course content
- Cannot delete students

**Student**
- Can watch videos
- Can download resources
- Can see progress
- Can access discussion community (if enabled)

### Welcome Email Template

```
Subject: Welcome to Stratega Academy!

Hi [Student Name],

Welcome to Stratega Academy - the complete growth infrastructure system!

You now have access to 9 modules designed to teach you how to systematize lead generation, build detailed customer profiles, and scale your growth operations.

Here's what you'll learn:
Module 1: Introduction to the Stratega Framework
Module 2: Positioning Your Offering
Module 3: Building Company ICP
Module 4: Building People ICP
Module 5: Content Strategy
Module 6: Copywriting & Persuasion
Module 7: Growth Tools & Automation
Module 8: Building Growth Systems
Module 9: Implementation & Scaling

Getting Started:
1. Start with Module 1: Introduction
2. Watch the video and review the slides
3. Take notes on frameworks you want to apply
4. Move through modules sequentially

Each module includes:
- Video lesson (15-20 minutes)
- PDF slides for reference
- Corrected transcript
- Additional resources

Expected Completion: 4-6 weeks at 5-10 hours/week

Questions? Reply to this email or check out our FAQ [link].

Let's build your growth infrastructure together!

Best,
[Your Name]
Stratega Academy
```

---

## Quality Assurance

### Pre-Launch Checklist

**Video Quality**
- [ ] All 9 videos uploaded and play without errors
- [ ] Audio is clear and levels are consistent
- [ ] Video resolution is minimum 1080p
- [ ] Captions/subtitles sync correctly
- [ ] No buffering or streaming issues in test

**Content Accuracy**
- [ ] All transcripts spell-checked
- [ ] Framework names match official terminology
- [ ] No broken links or references
- [ ] Slides are readable at full zoom
- [ ] PDF files open without errors

**Platform Functionality**
- [ ] Progress tracking works correctly
- [ ] Email notifications send properly
- [ ] Certificates generate on completion
- [ ] Discussion/comments function (if enabled)
- [ ] Mobile viewing is responsive
- [ ] Student can download resources

**User Experience**
- [ ] Navigation is intuitive
- [ ] Load times are acceptable (<3 seconds)
- [ ] Video player is user-friendly
- [ ] Mobile experience is smooth
- [ ] No 404 errors or broken content

### Test Student Walkthrough

Create test student account and:
1. Complete enrollment process
2. Watch Module 1 completely
3. Download all resources
4. Check progress tracking
5. Submit any feedback

---

## Ongoing Maintenance

### Monthly Tasks
- [ ] Monitor student engagement and completion rates
- [ ] Check for technical issues (broken links, etc.)
- [ ] Answer student questions/feedback
- [ ] Review platform analytics

### Quarterly Tasks
- [ ] Update course if new frameworks or tools available
- [ ] Create student success stories/case studies
- [ ] Analyze which modules get most attention
- [ ] Gather comprehensive student feedback

### Annual Tasks
- [ ] Complete course refresh review
- [ ] Update slide decks if tools/terminology changes
- [ ] Create new supplementary materials based on feedback
- [ ] Plan next iteration/version of course

### Issue Tracking Template

For any issues that arise:

**Issue:** [Description]
**Affected Module:** [Module #]
**Severity:** High/Medium/Low
**Resolution:** [Steps taken]
**Date Fixed:** [Date]

---

## Troubleshooting

### Video Issues

**Problem: Video won't play**
- Check file format (.mp4 recommended)
- Verify file size (should be under 2GB)
- Try re-uploading
- Clear browser cache
- Try different browser

**Problem: Video is buffering**
- Check internet speed requirement (5 Mbps minimum)
- Reduce video quality setting
- Pause and resume to pre-cache
- Contact platform support

**Problem: Audio/video out of sync**
- Re-encode video with proper codec
- Upload again to platform
- Check transcript timing

### Transcript Issues

**Problem: Captions don't appear**
- Verify SRT file format
- Check for encoding issues (use UTF-8)
- Re-upload SRT file
- Check platform caption settings

**Problem: Captions misaligned with video**
- Verify transcript timing matches video
- Manually adjust timing in platform
- Re-encode video if timing issues persist

### Access Issues

**Problem: Student can't access course**
- Verify student is enrolled
- Check student account is active
- Clear cookies/cache
- Check access start date

**Problem: Downloadable resources don't work**
- Verify file size under platform limits
- Re-upload resources
- Use different file format if needed
- Contact platform support

### Platform Issues

**Problem: Email notifications not sending**
- Check email configuration in settings
- Verify SMTP credentials
- Check spam folder
- Contact platform support

**Problem: Progress tracking not updating**
- Check video completion threshold setting
- Clear browser cache
- Log out and log back in
- Contact platform support

---

## Next Steps & Future Enhancements

### Short Term (Next 90 Days)
1. **Locate video files** - CRITICAL PATH ITEM
2. **Launch pilot cohort** - 10-20 test students
3. **Gather feedback** - Course survey
4. **Fix issues** - Based on feedback

### Medium Term (Next 6 Months)
1. **Add interactive elements** - Quizzes, assignments
2. **Create workbook PDF** - Downloadable workbook
3. **Build community** - Discussion forum, group projects
4. **Create case studies** - Student success stories

### Long Term (Next 12 Months)
1. **Expand course** - Advanced modules, specialized tracks
2. **Create certifications** - Skills-based certificates
3. **Build community** - Cohort model, peer learning
4. **Launch Notion integration** - Unified knowledge workspace

---

## Support & Questions

**For technical deployment questions:**
Contact your platform provider support

**For course content questions:**
Reference COURSE_STRUCTURE.md

**For file location questions:**
All materials stored in: `/Users/matteolombardi/AI-Projects/stratega/stratega-academy/`

---

## Appendix: Platform Comparison Matrix

| Feature | Teachable | Kajabi | Moodle | Canvas |
|---------|-----------|--------|--------|--------|
| **Ease of Use** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Video Support** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Cost (Monthly)** | $39-$199 | $119-$499 | Free (self-hosted) | $40-$500 (varies) |
| **Transcript Support** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Certificate Building** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Community Features** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Analytics & Reporting** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Mobile Experience** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **API & Integration** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

**Recommendation:** **Teachable** for most use cases - best balance of ease + features for course-based learning.

---

**Document Created:** 26 November 2025
**Status:** Complete & Ready to Follow
**Critical Path Item:** Locate video files (blocking full deployment)
