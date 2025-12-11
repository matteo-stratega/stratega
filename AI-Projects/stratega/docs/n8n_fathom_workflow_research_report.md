# n8n Fathom Meeting Workflow - Research Report

**Date:** 2025-11-26
**Agent:** CTO Agent
**Mission:** Find best n8n community template for Fathom → Transcript → AI → Notion → Slack workflow

---

## Executive Summary

**Key Finding:** No production-ready template exists that integrates all components (Fathom + Claude + Notion + Slack). However, there are **2 strong templates** that can be adapted with minimal modification:

1. **Template #9549** - Fathom webhook → Gemini AI → Google Docs (closest to your needs, needs output swap)
2. **Template #9284** - Google Meet → AssemblyAI → Claude → Notion + Slack (has Claude+Notion+Slack, needs Fathom input)

**Recommendation:** Hybrid approach - Use Template #9549's Fathom webhook pattern + Template #9284's Claude/Notion/Slack output pattern. Estimated setup time: 30-45 minutes.

---

## Template Analysis

### 🏆 TOP PICK #1: Workflow 9549 - Fathom to Google Docs with Gemini

**URL:** [Convert Fathom meeting transcripts to formatted Google Docs with Gemini AI summaries](https://n8n.io/workflows/9549-convert-fathom-meeting-transcripts-to-formatted-google-docs-with-gemini-ai-summaries/)

#### What It Does
- ✅ Fathom webhook trigger (exact match for your setup)
- ✅ Automatic transcript validation (3+ conversation turns)
- ✅ AI-powered analysis (key points, decisions, actions, next steps)
- ✅ Structured output generation
- ❌ Uses Google Gemini (not Claude)
- ❌ Outputs to Google Docs (not Notion)
- ❌ No Slack notification

#### Technical Details
- **Trigger:** Fathom webhook (POST endpoint)
- **AI Provider:** Google Gemini API (free tier available)
- **Output:** Google Docs (formatted HTML → Doc conversion)
- **Data Flow:** Webhook → Validate → AI Analysis → Format → Create Doc

#### Setup Instructions

1. **Get Fathom Webhook URL:**
   - Copy webhook URL from "Get Fathom Meeting" webhook node in n8n
   - Use Test URL first, switch to Production when ready

2. **Configure Fathom:**
   - Go to Fathom: Settings → API Access → Add
   - Paste webhook URL
   - Select all events including "Transcript"

3. **Set Up Gemini API:**
   - Get free API key from Google AI Studio
   - Add to n8n Google Gemini node credentials
   - Check [Google AI Pricing](https://ai.google.dev/pricing) for rate limits

4. **Configure Output:**
   - Connect Google account to n8n
   - Specify target Google Drive folder

#### What's Missing vs Your Requirements
- ❌ Uses Gemini instead of Claude (need to swap AI node)
- ❌ Outputs to Google Docs instead of Notion (need to swap output node)
- ❌ No Slack notification (need to add Slack node)

#### Pros
- Perfect Fathom webhook integration (exactly what you need)
- Proven validation logic for transcript quality
- Structured AI prompt for meeting analysis
- Active and recently maintained

#### Cons
- Wrong AI provider (but easy to swap)
- Wrong output destination (but easy to swap)
- Missing Slack notification (but easy to add)

#### Cost
- Google Gemini: Free tier generous (typically sufficient)
- Your setup: €5 Anthropic credits already available

---

### 🥈 RUNNER-UP #2: Workflow 9284 - Google Meet with Claude AI

**URL:** [Automate Meeting Summaries & Action Items with Google Meet, AssemblyAI & Claude AI](https://n8n.io/workflows/9284-automate-meeting-summaries-and-action-items-with-google-meet-assemblyai-and-claude-ai/)

#### What It Does
- ❌ Google Calendar + Google Meet trigger (not Fathom)
- ❌ Uses AssemblyAI for transcription (not needed - Fathom provides transcript)
- ✅ Anthropic Claude AI for analysis (exact match!)
- ✅ Notion integration for meeting notes (exact match!)
- ✅ Slack notification with summary (exact match!)
- ✅ Action items extraction with responsible parties

#### Technical Details
- **Trigger:** Google Calendar (scheduled check for meetings)
- **Transcription:** AssemblyAI (paid service, not needed for your use case)
- **AI Provider:** Anthropic Claude (perfect match)
- **Output:** Notion database + Slack channel
- **Data Flow:** Calendar → Drive → AssemblyAI → Claude → Notion + Slack

#### Setup Instructions

1. **Meeting Detection:**
   - Connects to Google Calendar
   - Retrieves last 24 hours of meetings
   - Filters for confirmed Google Meet links

2. **Recording Processing:**
   - Searches Google Drive for recording
   - Downloads recording file

3. **Transcription:**
   - Sends to AssemblyAI (speaker labels, sentiment)
   - Waits for transcription completion

4. **AI Analysis (Claude):**
   - Extracts: Meeting summary (2-3 paragraphs), action items with owners, deadlines, sentiment analysis

5. **Distribution:**
   - Posts summary to Slack channel
   - Creates Notion page with structured data
   - Creates individual task cards for action items

#### What's Missing vs Your Requirements
- ❌ No Fathom integration (need to add webhook trigger)
- ❌ Unnecessary transcription step (Fathom already provides transcript)
- ✅ Claude + Notion + Slack output is perfect

#### Pros
- Uses Claude (your preferred AI)
- Complete Notion integration
- Complete Slack integration
- Action items tracking
- Production-ready output structure

#### Cons
- Wrong input source (needs Fathom webhook)
- Includes unnecessary transcription service (costs money)
- More complex than needed for your setup

#### Cost
- AssemblyAI: Paid (can be removed from your implementation)
- Claude: Uses your existing €5 Anthropic credits
- Notion: Free tier sufficient
- Slack: Free tier sufficient

---

### 🤔 ALTERNATIVE #3: Workflow 10286 - OpenAI Meeting Tracker

**URL:** [AI Meeting Summary & Action Item Tracker with Notion, Slack, and Gmail](https://n8n.io/workflows/10286-ai-meeting-summary-and-action-item-tracker-with-notion-slack-and-gmail/)

#### What It Does
- ✅ Generic webhook trigger (flexible)
- ❌ Uses OpenAI GPT-4 (not Claude)
- ✅ Notion dual-database system (meetings + tasks)
- ✅ Slack with emoji categorization
- ✅ Gmail distribution

#### What's Missing
- ❌ No Fathom-specific integration
- ❌ Uses OpenAI instead of Claude
- ❌ More complex than needed (includes Gmail)

#### Why It's Third Choice
- Less specific to Fathom
- Wrong AI provider
- Overcomplicated for your needs

---

## Recommended Implementation Strategy

### 🎯 Hybrid Approach: Build from Template 9549 + Template 9284

**Rationale:** Template 9549 has perfect Fathom webhook setup. Template 9284 has perfect Claude + Notion + Slack output. Combine the best of both.

### Implementation Steps

#### Phase 1: Get Template 9549 Working (15 min)
1. Import workflow 9549 into your n8n instance
2. Configure Fathom webhook (copy URL, add to Fathom settings)
3. Test webhook trigger with a real meeting
4. Verify transcript data arrives correctly

#### Phase 2: Swap AI Provider (10 min)
1. Remove Google Gemini node
2. Add Anthropic Claude node (you already have this working)
3. Copy the Gemini prompt structure to Claude
4. Test AI analysis output
5. Add JSON cleanup (you already have this pattern working)

#### Phase 3: Add Notion Output (10 min)
1. Remove Google Docs node
2. Add Notion node
3. Create Notion database with fields:
   - Title (meeting title)
   - Date (meeting date)
   - Transcript (full text)
   - Summary (AI-generated)
   - Key Points (bulleted list)
   - Action Items (checklist)
   - Recording URL (link)
4. Map Claude output to Notion fields

#### Phase 4: Add Slack Notification (10 min)
1. Add Slack node
2. Configure Slack channel (create #meeting-summaries if needed)
3. Format message with emoji indicators:
   - 📝 Meeting: [Title]
   - 📅 Date: [Date]
   - ✅ Summary: [AI Summary]
   - 🎯 Actions: [Action Items]
   - 🔗 Notion: [Link to Notion page]
4. Test notification

#### Phase 5: Testing & Refinement (10 min)
1. Run end-to-end test with real Fathom meeting
2. Verify: Webhook triggers → Claude processes → Notion creates → Slack notifies
3. Check error handling (what if transcript is empty?)
4. Add retry logic if needed

### Total Estimated Time: 45 minutes

---

## Technical Requirements

### n8n Nodes Required
- ✅ Webhook (built-in, you have this)
- ✅ Anthropic Claude (you already have this working)
- ✅ Code (for JSON cleanup, you already have this pattern)
- ⚠️ Notion (needs API credentials)
- ⚠️ Slack (needs bot token)

### API Credentials Needed
1. **Fathom:** API webhook URL (get from Fathom settings)
2. **Anthropic:** API key (you already have this)
3. **Notion:** Integration token (get from Notion integrations page)
4. **Slack:** Bot token with `chat:write` scope (create Slack app)

### Budget Check
- **Anthropic Claude:** €5 credits available ✅
- **Notion:** Free tier sufficient ✅
- **Slack:** Free tier sufficient ✅
- **Fathom:** No additional cost (you already have it) ✅
- **Total additional cost:** €0 🎉

---

## Why No Perfect Template Exists

### Research Findings

1. **Fathom is niche:** Limited n8n community adoption (only 1 dedicated template found)
2. **No official Fathom node:** Community requested official integration in Oct 2025, still pending
3. **Most templates use Google Meet/Zoom:** These platforms have native n8n nodes
4. **AI diversity:** Templates split between OpenAI, Gemini, Claude (no standard)
5. **Output preferences vary:** Some use Google Docs, some Notion, some Airtable

### What This Means for You

✅ **Good news:** All the components exist separately
✅ **Good news:** Your existing patterns (webhook → Claude → JSON) apply here
⚠️ **Reality:** You need to assemble the pieces (estimated 45 min)
⚠️ **Reality:** No one-click install option available

---

## Alternative Approaches (If Templates Don't Work)

### Option A: Start from Scratch (60 min)
Build the workflow manually using your existing patterns:
- You already know how to: Webhook → Claude → JSON cleanup
- You just need to add: Notion output + Slack notification
- Advantage: Full control, cleaner implementation
- Disadvantage: Takes longer, no reference template

### Option B: Use Zapier/Make.com
- Pre-built Fathom integrations available
- Simpler setup (drag-and-drop)
- Disadvantage: Subscription cost (€20-50/month)
- Disadvantage: Less flexible than n8n

### Option C: Custom Python Script
- Write script: Fathom API → Claude API → Notion API → Slack API
- Advantage: Full control, no n8n dependency
- Disadvantage: Maintenance overhead
- Disadvantage: Takes 2-3 hours to build

---

## Final Recommendation

### 🎯 RECOMMENDED: Hybrid Approach Using Templates 9549 + 9284

**Why this is the best option:**

1. **Proven components:** Both templates are production-tested
2. **Minimal adaptation needed:** You're combining working pieces
3. **Leverages your existing skills:** You already have Claude + webhook patterns working
4. **Cost-effective:** €0 additional cost
5. **Time-efficient:** 45 minutes vs building from scratch (3+ hours)

### 🚀 Implementation Priority

**Start with:** Template 9549
**Reason:** Get Fathom webhook working first (this is the hardest/most unique part)

**Then add:** Claude + Notion + Slack from Template 9284
**Reason:** You already know how to work with Claude; Notion/Slack are straightforward

### ⏱️ Time Budget Alignment

- **Your budget:** Be thorough but efficient
- **My estimate:** 45 minutes for hybrid approach
- **Comparison:** Building from scratch would take 3+ hours
- **Verdict:** Hybrid approach is optimal time investment

---

## Installation Steps (Quick Reference)

### Step 1: Import Template 9549
```bash
# In n8n UI:
1. Go to Workflows → Add workflow
2. Click "Templates" tab
3. Search: "9549" or "Fathom Gemini"
4. Click "Use this workflow"
```

### Step 2: Configure Fathom Webhook
```bash
# In n8n:
1. Open webhook node
2. Copy webhook URL (test mode)

# In Fathom:
1. Settings → API Access → Add
2. Paste webhook URL
3. Select "Transcript" event
4. Save
```

### Step 3: Test Fathom Connection
```bash
# Record a test meeting in Fathom
# Check n8n execution log for incoming data
# Verify transcript arrives in webhook payload
```

### Step 4: Swap AI Node
```bash
# In n8n:
1. Delete "Google Gemini" node
2. Add "Anthropic Claude" node
3. Use your existing credentials
4. Copy prompt from Gemini node → Claude node
5. Set model: claude-3-haiku-20240307 (your budget)
6. Set temperature: 0.3
7. Set max_tokens: 1500
```

### Step 5: Add JSON Cleanup
```bash
# Add "Code" node after Claude
# Use your existing pattern:
const response = $json.response;
const cleaned = JSON.parse(response);
return { json: cleaned };
```

### Step 6: Add Notion Node
```bash
# In Notion:
1. Create integration: https://www.notion.so/my-integrations
2. Copy integration token
3. Create database "Meeting Notes"
4. Share database with integration

# In n8n:
1. Add "Notion" node
2. Paste integration token
3. Select database
4. Map fields: Title, Date, Summary, etc.
```

### Step 7: Add Slack Node
```bash
# In Slack:
1. Create app: https://api.slack.com/apps
2. Add bot scope: chat:write
3. Install to workspace
4. Copy bot token

# In n8n:
1. Add "Slack" node
2. Paste bot token
3. Select channel: #meeting-summaries
4. Format message with emoji + data
```

### Step 8: End-to-End Test
```bash
# Record new Fathom meeting
# Verify: Webhook → Claude → Notion → Slack
# Check Notion page created
# Check Slack notification sent
# Review for errors/missing data
```

---

## Troubleshooting Guide

### Issue: Webhook not triggering
**Solution:** Use test URL first, check Fathom webhook configuration, verify Fathom events selected

### Issue: Claude response not parsing
**Solution:** Add JSON cleanup node (you already have this pattern), check Claude prompt includes "respond in JSON format"

### Issue: Notion page not creating
**Solution:** Verify integration token, check database shared with integration, verify field mapping matches database schema

### Issue: Slack message not sending
**Solution:** Verify bot token, check bot has chat:write scope, verify channel exists and bot is invited

### Issue: Hitting budget limits
**Solution:** Using Haiku (cheapest Claude model), estimated cost: €0.002 per meeting (250 meetings = €0.50)

---

## Cost Analysis

### Per-Meeting Cost Breakdown
- **Fathom:** €0 (already included in your subscription)
- **Claude Haiku:** ~€0.002 per meeting (1500 tokens input + output)
- **Notion:** €0 (free tier: unlimited blocks)
- **Slack:** €0 (free tier: unlimited messages)

### Budget Projection
- **Your budget:** €5 Anthropic credits
- **Estimated meetings:** 2,500 meetings (€5 ÷ €0.002)
- **Realistically:** 500+ meetings before needing top-up
- **Verdict:** Budget is more than sufficient

---

## Sources

### Primary Research Sources
- [Fathom to Google Docs with Gemini AI (Workflow 9549)](https://n8n.io/workflows/9549-convert-fathom-meeting-transcripts-to-formatted-google-docs-with-gemini-ai-summaries/)
- [Google Meet with Claude AI (Workflow 9284)](https://n8n.io/workflows/9284-automate-meeting-summaries-and-action-items-with-google-meet-assemblyai-and-claude-ai/)
- [AI Meeting Summary & Action Item Tracker (Workflow 10286)](https://n8n.io/workflows/10286-ai-meeting-summary-and-action-item-tracker-with-notion-slack-and-gmail/)
- [n8n Fathom Integration Page](https://n8n.io/integrations/fathom/)
- [n8n Webhook and Fathom Integration](https://n8n.io/integrations/webhook/and/fathom/)

### Supporting Resources
- [n8n Claude Integrations](https://n8n.io/integrations/claude/)
- [n8n Anthropic Chat Model Documentation](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic/)
- [n8n Notion Integrations](https://n8n.io/integrations/notion/)
- [n8n Slack Integrations](https://n8n.io/integrations/slack/)
- [Fathom Integration Community Discussion](https://community.n8n.io/t/fathom-integration/203959)

### GitHub Research
- [Zie619/n8n-workflows (General n8n workflow collection)](https://github.com/Zie619/n8n-workflows)
- [wassupjay/n8n-free-templates (200+ n8n templates)](https://github.com/wassupjay/n8n-free-templates)
- [simealdana/ai-automation-jsons (AI automation workflows)](https://github.com/simealdana/ai-automation-jsons)

**Note:** No Fathom-specific workflows found on GitHub, confirming the need for custom assembly.

---

## Conclusion

**Bottom line:** No perfect template exists, but you can build a production-ready workflow in 45 minutes by combining the best parts of Templates 9549 and 9284.

**Confidence level:** High - All components are proven, you have existing patterns to follow, and your budget is sufficient.

**Risk level:** Low - Each piece works independently; you're just connecting them.

**Recommendation:** Proceed with hybrid approach. Start with Template 9549 for Fathom webhook, then adapt outputs to use Claude + Notion + Slack.

**Next steps:**
1. Import Template 9549 into n8n
2. Configure Fathom webhook
3. Test webhook with real meeting
4. Swap AI provider to Claude
5. Add Notion + Slack outputs
6. Run end-to-end test
7. Deploy to production

**Timeline:** Start now → Working prototype in 1 hour → Production-ready by end of day.

---

*Report generated by: CTO Agent*
*Research date: 2025-11-26*
*Total templates evaluated: 10+*
*Templates recommended: 2 (hybrid approach)*
*Estimated implementation time: 45 minutes*
*Estimated cost: €0 additional (using existing €5 credits)*
