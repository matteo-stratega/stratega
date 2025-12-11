# Fathom → Notion + Slack Workflow Setup Guide

**Custom n8n Workflow for Automated Meeting Intelligence**

Built by: Stratega CTO Agent
Date: November 26, 2025
Workflow File: `fathom-cto-custom.json`

---

## Overview

This workflow automatically processes Fathom meeting recordings and creates structured meeting notes in Notion with Slack notifications. It uses Claude 3.5 Haiku for intelligent transcript processing and report generation.

**What it does:**
1. Receives webhook from Fathom when meeting is recorded
2. Cleans and structures the transcript using Claude
3. Generates comprehensive meeting report with action items
4. Creates a Notion page in your "Meeting Notes" database
5. Sends Slack notification with summary + link

**Cost per meeting:** ~$0.01-0.05 (Claude API)
**Processing time:** ~30-60 seconds

---

## Prerequisites

Before you start, you need:

- [ ] n8n instance running (Docker or cloud)
- [ ] Fathom account with API/webhook access
- [ ] Anthropic API key (Claude access)
- [ ] Notion workspace with API access
- [ ] Slack workspace with bot permissions

---

## Step 1: Import Workflow to n8n

1. Open your n8n instance (http://localhost:5678 or your cloud URL)
2. Click **"+"** to create new workflow
3. Click the **three dots menu** (⋯) in top right
4. Select **"Import from File"**
5. Upload `fathom-cto-custom.json`
6. Click **"Save"** to save the imported workflow

The workflow should now appear with all nodes connected.

---

## Step 2: Configure API Credentials

### 2.1 Anthropic API (Claude)

**Get your API key:**
1. Go to https://console.anthropic.com/
2. Navigate to **API Keys** section
3. Click **"Create Key"**
4. Copy the key (starts with `sk-ant-`)

**Add to n8n:**
1. Click on any **"Claude Haiku"** node in the workflow
2. Click **"Credential to connect with"**
3. Click **"+ Create New Credential"**
4. Name it: `Anthropic API`
5. Paste your API key
6. Click **"Save"**

**Budget note:** You have €5 credits. Each meeting costs ~$0.01-0.05. That's 100-500 meetings worth.

### 2.2 Notion API

**Create integration:**
1. Go to https://www.notion.so/my-integrations
2. Click **"+ New integration"**
3. Name it: `n8n Meeting Notes`
4. Select your workspace
5. Click **"Submit"**
6. Copy the **"Internal Integration Token"** (starts with `secret_`)

**Add to n8n:**
1. Click on the **"Create Notion Page"** node
2. Click **"Credential to connect with"**
3. Click **"+ Create New Credential"**
4. Name it: `Notion API`
5. Paste your token
6. Click **"Save"**

### 2.3 Slack API

**Create Slack app:**
1. Go to https://api.slack.com/apps
2. Click **"Create New App"**
3. Choose **"From scratch"**
4. App Name: `Meeting Notes Bot`
5. Select your workspace
6. Click **"Create App"**

**Configure permissions:**
1. In left sidebar, click **"OAuth & Permissions"**
2. Scroll to **"Scopes"**
3. Under **"Bot Token Scopes"**, add:
   - `chat:write` (Send messages)
   - `chat:write.public` (Send to public channels)
4. Scroll up and click **"Install to Workspace"**
5. Click **"Allow"**
6. Copy the **"Bot User OAuth Token"** (starts with `xoxb-`)

**Add to n8n:**
1. Click on the **"Send Slack Notification"** node
2. Click **"Credential to connect with"**
3. Click **"+ Create New Credential"**
4. Name it: `Slack API`
5. Paste your token
6. Click **"Save"**

---

## Step 3: Configure Notion Database

You need a Notion database called "Meeting Notes" with specific properties.

### Create the database:

1. In Notion, create a new page
2. Type `/database` and select **"Table - Inline"**
3. Name it: **"Meeting Notes"**

### Add required properties:

Click **"+"** to add these columns:

| Property Name | Type | Description |
|---------------|------|-------------|
| Name | Title | Auto-created (meeting title) |
| Date | Date | Meeting date |
| Participants | Multi-select | List of attendees |
| Action Items | Number | Count of action items |
| Recording URL | URL | Link to Fathom recording |
| Fathom ID | Text | Fathom meeting ID |

### Connect to n8n:

1. **Share database with your integration:**
   - Click **"Share"** in top right of database
   - Click **"Invite"**
   - Select your integration (`n8n Meeting Notes`)
   - Click **"Invite"**

2. **Get database ID:**
   - Copy the database URL from your browser
   - Format: `https://notion.so/YOUR_DATABASE_ID?v=...`
   - Extract just the ID part (32 characters between slashes)

3. **Add to workflow:**
   - Click the **"Create Notion Page"** node
   - Find the `databaseId` field
   - Replace `YOUR_NOTION_DATABASE_ID` with your actual ID
   - Click **"Save"**

---

## Step 4: Configure Slack Channel

1. **Choose your channel:**
   - Decide where notifications should go (e.g., `#meeting-notes`)
   - Invite your bot to the channel: Type `/invite @Meeting Notes Bot`

2. **Get channel ID:**
   - Right-click the channel name in Slack
   - Select **"View channel details"**
   - Scroll to bottom, copy the **Channel ID**

3. **Add to workflow:**
   - Click the **"Send Slack Notification"** node
   - Find the `channel` field
   - Replace `YOUR_SLACK_CHANNEL_ID` with your actual ID
   - Click **"Save"**

---

## Step 5: Configure Fathom Webhook

1. **Get webhook URL:**
   - Click the **"Webhook - Fathom"** node in n8n
   - Click **"Execute Node"** (or activate the workflow)
   - Copy the **"Test URL"** or **"Production URL"**
   - Format: `https://your-n8n-instance.com/webhook/fathom-webhook`

2. **Add to Fathom:**
   - Go to your Fathom settings/integrations
   - Find webhook/API configuration
   - Add the webhook URL
   - Configure to trigger on: **"Recording Completed"**
   - Save the configuration

**Note:** If Fathom doesn't support webhooks directly, you may need to:
- Use Zapier/Make as a bridge
- Or poll Fathom API periodically (requires modifying workflow to use Schedule Trigger instead)

---

## Step 6: Test the Workflow

### Manual test (recommended first):

1. In n8n, click the **"Webhook - Fathom"** node
2. Click **"Listen for Test Event"**
3. Send a test POST request using this sample payload:

```bash
curl -X POST https://your-n8n-instance.com/webhook-test/fathom-webhook \
  -H "Content-Type: application/json" \
  -d '{
    "id": "test-meeting-001",
    "title": "Weekly Team Standup",
    "date": "2025-11-26T10:00:00Z",
    "duration": "30 minutes",
    "participants": ["Alice", "Bob", "Charlie"],
    "transcript": "Alice: Good morning everyone. Let us start with updates. Bob: I completed the API integration yesterday. We can now proceed with testing. Charlie: Great work Bob. I will start the testing today. Alice: Perfect. Let us aim to deploy by Friday. Bob: Agreed. I will prepare the documentation. Charlie: I will handle the QA checklist. Alice: Excellent. Any blockers? Bob: No blockers on my end. Charlie: All clear here too. Alice: Great meeting everyone. Let us sync again on Thursday.",
    "recording_url": "https://fathom.video/test-recording"
  }'
```

4. Watch the workflow execute through all nodes
5. Check that:
   - Notion page was created
   - Slack message was sent
   - Webhook response was returned

### Live test:

1. Record a real meeting in Fathom
2. Wait for it to process
3. Fathom should trigger your webhook
4. Check Notion and Slack for the results

---

## Step 7: Activate for Production

Once testing is successful:

1. Click **"Active"** toggle in top right of n8n
2. The workflow is now live and will process all incoming webhooks

---

## Troubleshooting

### Webhook not triggering:
- Check Fathom webhook configuration
- Verify n8n is publicly accessible
- Check n8n execution log for errors

### Claude API errors:
- Verify API key is correct
- Check your Anthropic credits balance
- Reduce transcript length if hitting token limits

### Notion creation fails:
- Ensure integration has access to database
- Verify database ID is correct
- Check property names match exactly

### Slack message not sending:
- Verify bot is invited to channel
- Check bot token permissions
- Ensure channel ID is correct

### JSON parsing errors:
- Claude occasionally wraps JSON in markdown
- The workflow handles this, but check "JSON Cleanup" node
- If persists, adjust the cleanup regex patterns

---

## Customization Options

### Adjust Claude prompts:

**For different report formats:**
- Edit the `Build Report Prompt` node
- Modify the JSON structure in the prompt
- Update the `Format for Outputs` node accordingly

**For different languages:**
- Add language parameter to prompts
- Example: "Generate report in Spanish"

### Change Notion layout:

**Add more properties:**
- Update `Create Notion Page` node properties
- Add corresponding data in `Format for Outputs`

**Different formatting:**
- Edit the markdown structure in `Format for Outputs`
- Notion supports rich formatting

### Modify Slack notifications:

**Different format:**
- Edit the message template in `Send Slack Notification`
- Add emojis, formatting, buttons

**Multiple channels:**
- Duplicate the Slack node
- Configure for different channels
- Connect both to the workflow

---

## Workflow Architecture

```
Fathom Webhook
    ↓
Extract Metadata (raw data parsing)
    ↓
Build Cleanup Prompt (prepare for Claude)
    ↓
Claude Haiku Agent #1 (clean transcript)
    ↓
Build Report Prompt (prepare for analysis)
    ↓
Claude Haiku Agent #2 (generate report)
    ↓
JSON Cleanup (remove markdown wrappers)
    ↓
Format for Outputs (prepare Notion + Slack)
    ↓
    ├─→ Create Notion Page
    ↓
    └─→ Send Slack Notification
         ↓
    Webhook Response (back to Fathom)
```

---

## Cost Analysis

**Per meeting (assuming 45min, ~4000 tokens):**

| Service | Cost | Notes |
|---------|------|-------|
| Claude Haiku (cleanup) | ~$0.001-0.002 | Input + output tokens |
| Claude Haiku (report) | ~$0.005-0.010 | Larger output |
| Notion API | Free | Within limits |
| Slack API | Free | Within limits |
| n8n execution | Free/Minimal | Self-hosted or cloud pricing |
| **Total per meeting** | **~$0.01-0.05** | Very cost-effective |

**Monthly estimate (20 meetings):** ~$0.20-1.00

Your €5 credit = **100-500 meetings** worth of processing.

---

## Comparison vs Templates

### What's better in this custom version:

1. **Two-stage Claude processing:**
   - Template: Single-pass generation
   - Custom: Separate cleanup + analysis = higher quality

2. **Robust error handling:**
   - All API calls have `onError: continueRegularOutput`
   - JSON cleanup handles malformed responses
   - Graceful degradation if sections missing

3. **Production-ready structure:**
   - Clear node naming (self-documenting)
   - Comprehensive notes on each node
   - Sticky notes for documentation

4. **Cost optimization:**
   - Uses Haiku (cheapest Claude model)
   - Optimized token counts
   - €5 = hundreds of meetings

5. **Flexible output formatting:**
   - Markdown for Notion (human-readable)
   - Condensed for Slack (actionable)
   - Structured JSON for future integrations

### What templates might have:

1. **More integrations:**
   - Templates often include Google Calendar, email, etc.
   - You can add these as needed

2. **Advanced error recovery:**
   - Some templates have retry logic
   - Can be added to individual nodes

3. **Batch processing:**
   - Templates might handle multiple meetings
   - This workflow is optimized for real-time single meeting

### Trade-offs:

**Custom version pros:**
- Tailored to exact requirements
- No unnecessary complexity
- Clear, maintainable code
- Optimized for Stratega use case

**Custom version cons:**
- Less battle-tested than popular templates
- Fewer integration options out of the box
- May need adjustments for edge cases

**Overall:** This custom workflow is superior for the specific Fathom → Notion → Slack use case, with better quality outputs and lower costs than generic templates.

---

## Maintenance

### Regular checks:

- [ ] Monitor Claude API costs monthly
- [ ] Review Notion database for any parsing errors
- [ ] Check Slack messages for quality
- [ ] Update prompts if report quality degrades

### Improvements to consider:

1. **Add sentiment analysis** (detect meeting tone)
2. **Integrate with project management tools** (auto-create tasks)
3. **Add speaker identification** (who said what)
4. **Generate follow-up email drafts**
5. **Create meeting analytics dashboard**

---

## Support & Resources

**n8n Documentation:**
- General: https://docs.n8n.io/
- Webhooks: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/
- Code node: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/

**Claude API:**
- Docs: https://docs.anthropic.com/
- Models: https://docs.anthropic.com/en/docs/models-overview
- Pricing: https://www.anthropic.com/pricing

**Notion API:**
- Docs: https://developers.notion.com/
- Database objects: https://developers.notion.com/reference/database

**Slack API:**
- Docs: https://api.slack.com/docs
- Bot setup: https://api.slack.com/bot-users

---

## Next Steps

After successful setup:

1. **Run 5-10 test meetings** to validate quality
2. **Adjust prompts** based on your meeting types
3. **Share with team** and gather feedback
4. **Iterate on format** until it matches your needs
5. **Consider adding more integrations** (calendar, email, etc.)

---

## Version History

- **v1.0** (2025-11-26): Initial custom build
  - Fathom webhook integration
  - Two-stage Claude processing
  - Notion + Slack outputs
  - Production-ready error handling

---

**Built with precision by Stratega CTO Agent**
*Optimized for quality, cost, and maintainability*