# Fathom Workflow - Quick Start

**Get up and running in 15 minutes**

## Files You Have

1. **`fathom-cto-custom.json`** - The workflow (import into n8n)
2. **`FATHOM_CUSTOM_SETUP.md`** - Full setup guide (read if you get stuck)
3. **`fathom-test-payload.json`** - Sample data for testing
4. **`FATHOM_WORKFLOW_DELIVERY_REPORT.md`** - Complete technical documentation

## 5-Step Quick Start

### Step 1: Import Workflow (2 min)

1. Open n8n (http://localhost:5678)
2. Click "+" → Import from File
3. Upload `fathom-cto-custom.json`
4. Click Save

### Step 2: Add API Keys (5 min)

**Anthropic (Claude):**
- Get key: https://console.anthropic.com/
- Add to both "Claude Haiku" nodes
- Format: `sk-ant-...`

**Notion:**
- Get key: https://www.notion.so/my-integrations
- Add to "Create Notion Page" node
- Format: `secret_...`

**Slack:**
- Get key: https://api.slack.com/apps
- Add to "Send Slack Notification" node
- Format: `xoxb-...`

### Step 3: Configure Notion Database (3 min)

1. Create database in Notion called "Meeting Notes"
2. Add properties: Date, Participants, Action Items, Recording URL
3. Share with your integration
4. Copy database ID from URL
5. Paste into "Create Notion Page" node

### Step 4: Configure Slack (2 min)

1. Invite bot to channel: `/invite @Meeting Notes Bot`
2. Get channel ID from channel details
3. Paste into "Send Slack Notification" node

### Step 5: Test (3 min)

1. Click "Webhook - Fathom" node
2. Click "Listen for Test Event"
3. In terminal, run:

```bash
curl -X POST YOUR_WEBHOOK_URL \
  -H "Content-Type: application/json" \
  -d @fathom-test-payload.json
```

4. Watch it execute
5. Check Notion + Slack

## Done!

If it worked: Activate the workflow and start using it.

If it didn't: Check `FATHOM_CUSTOM_SETUP.md` for detailed troubleshooting.

## What's Next?

1. Record a real meeting in Fathom
2. Let the workflow process it automatically
3. Review the quality
4. Adjust prompts if needed (see FATHOM_CUSTOM_SETUP.md)
5. Share with your team

## Need Help?

**Quick issues:**
- Webhook not triggering → Check n8n is publicly accessible
- Claude errors → Verify API key and credits
- Notion fails → Check integration permissions
- Slack fails → Check bot is in channel

**Detailed help:**
- Read: `FATHOM_CUSTOM_SETUP.md` (full guide)
- Read: `FATHOM_WORKFLOW_DELIVERY_REPORT.md` (technical details)

## Cost Reminder

Your €5 Anthropic credits = **100-500 meetings** worth of processing.

Each meeting costs ~$0.01-0.05.

You're good for months or even years depending on meeting volume.

---

**Happy automating!**
