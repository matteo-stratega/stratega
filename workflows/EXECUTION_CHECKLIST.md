# Execution Checklist - From Zero to First Article

**Workflow:** `content-gen-CLAUDE-COMPLETE`
**Status:** ✅ Imported and verified in n8n
**Time to first article:** ~5 minutes

---

## Pre-Flight Checklist

- [x] 8 Gemini models replaced with Claude 3.5 Haiku
- [x] JSON cleanup node added (fixes parsing errors)
- [x] Get_job Supabase node disabled
- [x] All ai_languageModel connections preserved
- [x] Workflow imported into n8n successfully
- [x] All validation checks passed

---

## Your Action Items

### ☐ Step 1: Get Your Anthropic API Key (30 seconds)

```bash
1. Go to: https://console.anthropic.com/settings/keys
2. Click "Create Key"
3. Copy the key (starts with sk-ant-...)
4. Save it somewhere safe (you'll need it in Step 2)
```

**Check your balance:**
- Go to: https://console.anthropic.com/settings/billing
- Verify you have €5 (~$5.30) credits

---

### ☐ Step 2: Add Credentials to n8n (1 minute)

```bash
# Open n8n
1. Navigate to: http://localhost:5678

# Add Anthropic credential
2. Click profile icon (top right) → "Credentials"
3. Click "Add Credential"
4. Search for "Anthropic" in the search box
5. Click "Anthropic" from results
6. Paste your API key from Step 1
7. Give it a name: "Anthropic - Main Account"
8. Click "Save"
```

---

### ☐ Step 3: Assign Credentials to All 8 Claude Nodes (2 minutes)

```bash
# Open the workflow
1. In n8n, go to "Workflows"
2. Find and click: "content-gen-CLAUDE-COMPLETE"

# Assign credentials (repeat for ALL 8 nodes)
3. Click on: "Google Gemini Chat Model3"
   - Find "Credential to connect with" dropdown
   - Select: "Anthropic - Main Account"
   - Click outside to save

4. Repeat Step 3 for these 7 more nodes:
   ☐ Google Gemini Chat Model4
   ☐ Google Gemini Chat Model6
   ☐ Google Gemini Chat Model14
   ☐ Google Gemini Chat Model2
   ☐ Google Gemini Chat Model7
   ☐ Google Gemini Chat Model
   ☐ Google Gemini Chat Model9

5. Click "Save" (top right) to save the entire workflow
```

**Note:** These nodes still have "Gemini" in their names but are now Claude nodes. Names weren't changed to preserve all connections.

---

### ☐ Step 4: Set Up Test Execution (2 minutes)

**Option A: Manual Test (Recommended for first run)**

```bash
1. In the workflow, find the "set_field_names" node
2. Add a "Manual Trigger" node before it:
   - Click the "+" button
   - Search for "Manual Trigger"
   - Add it to the canvas
   - Connect it to "set_field_names"

3. Add test data to the Manual Trigger node:
   - Click the Manual Trigger node
   - Add this JSON in the data field:
```

```json
{
  "gpt_language": ["English"],
  "company_data": {
    "company_name": "Stratega",
    "company_url": "https://strategaco.com",
    "company_language": "English",
    "company_competitors": ["hubspot.com", "semrush.com"]
  },
  "blog_page": {
    "company_url": "https://strategaco.com",
    "company_name": "Stratega",
    "topic": "Growth Marketing Strategies for B2B SaaS",
    "keywords": ["growth marketing", "B2B SaaS", "lead generation"]
  }
}
```

**Option B: Re-enable Supabase Job (For production)**

```bash
1. Click the "Get_job" node
2. In the right panel, find "Settings" tab
3. Uncheck "Execute Once"
4. Uncheck "Disabled"
5. Click "Save"
```

---

### ☐ Step 5: Execute! (30 seconds)

```bash
1. Click "Execute Workflow" button (top right, play icon)
2. Watch the magic happen:
   - Nodes will light up green as they execute
   - Each Claude node should complete in 2-10 seconds
   - JSON_Cleanup will sanitize the output
   - Total execution: ~2-5 minutes

3. Check results:
   - Click on the final output node
   - Review your generated article
   - Check for any errors in the execution panel (bottom)
```

---

## Troubleshooting Guide

### ❌ Error: "Missing credentials on node X"

**Problem:** You didn't assign Anthropic credentials to all 8 nodes

**Fix:**
```bash
1. Click the red node showing the error
2. Assign "Anthropic - Main Account" credential
3. Repeat for any other red nodes
4. Save workflow
5. Execute again
```

---

### ❌ Error: "No input data"

**Problem:** Get_job is disabled and you haven't added a manual trigger

**Fix:**
```bash
1. Follow Step 4, Option A above
2. Add Manual Trigger with test data
3. Execute again
```

---

### ❌ Error: "Invalid API key"

**Problem:** Your Anthropic API key is wrong or inactive

**Fix:**
```bash
1. Go to: https://console.anthropic.com/settings/keys
2. Generate a new key
3. Go to n8n Credentials
4. Edit "Anthropic - Main Account"
5. Paste new key
6. Save
7. Execute workflow again
```

---

### ❌ Error: "Rate limit exceeded"

**Problem:** You're making too many requests too fast

**Fix:**
```bash
1. Wait 60 seconds
2. Execute again
3. If it persists, add a "Wait" node between steps
```

---

### ❌ Error: "JSON parsing error"

**Problem:** Cleanup node might not be working properly

**Fix:**
```bash
1. Check JSON_Cleanup node is connected
2. Verify the connection: concatenate_text → JSON_Cleanup → Information Extractor
3. Check the cleanup code is present (should be ~30 lines)
4. If still failing, check the actual output from concatenate_text
```

---

## Success Indicators

✅ **You've succeeded when:**

1. Workflow executes without errors (all nodes green)
2. Each Claude node completes in 2-10 seconds
3. JSON_Cleanup processes without errors
4. Final output contains your generated article
5. n8n execution panel shows "Success"
6. Anthropic console shows API usage increasing

---

## Cost Tracking

**After your first article:**

```bash
1. Go to: https://console.anthropic.com/settings/billing
2. Check "Usage" section
3. Calculate remaining budget:
   - Starting: €5.00 (~$5.30)
   - Per article: ~$0.08
   - Remaining articles = (Balance / 0.08)
```

**Example:**
- After 1 article: $5.22 remaining = ~65 more articles
- After 10 articles: $4.50 remaining = ~56 more articles

---

## Next Steps After First Success

1. **Test different topics** - Verify quality across content types
2. **Adjust prompts** - Customize output to your needs
3. **Re-enable Get_job** - Connect to production Supabase
4. **Monitor costs** - Track usage daily
5. **Scale up** - If quality is good, run more articles

---

## Files Reference

- **Workflow:** `/Users/matteolombardi/AI-Projects/stratega/workflows/content-gen-CLAUDE-COMPLETE.json`
- **This checklist:** `/Users/matteolombardi/AI-Projects/stratega/workflows/EXECUTION_CHECKLIST.md`
- **Setup guide:** `/Users/matteolombardi/AI-Projects/stratega/workflows/CLAUDE_WORKFLOW_SETUP.md`
- **Quick start:** `/Users/matteolombardi/AI-Projects/stratega/workflows/QUICK_START.md`
- **Verification:** `/Users/matteolombardi/AI-Projects/stratega/workflows/VERIFICATION_REPORT.txt`

---

## Support

**If all else fails:**

1. Check n8n logs: Docker logs for n8n-production container
2. Check Anthropic status: https://status.anthropic.com
3. Verify Claude 3.5 Haiku availability in your region
4. Check n8n langchain version supports Anthropic

---

**You're ready. Open n8n and execute your first article!** 🚀

Last updated: 2025-11-26
