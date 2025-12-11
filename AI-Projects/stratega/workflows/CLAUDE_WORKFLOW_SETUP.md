# Content Generation Workflow - Claude Edition Setup Guide

**Status:** ✅ COMPLETE AND IMPORTED INTO N8N

**Workflow Name:** `content-gen-CLAUDE-COMPLETE`

---

## What Was Fixed

### 1. **All 8 Gemini Models Replaced with Claude 3.5 Haiku**
   - `Google Gemini Chat Model3` → Claude 3.5 Haiku
   - `Google Gemini Chat Model4` → Claude 3.5 Haiku
   - `Google Gemini Chat Model6` → Claude 3.5 Haiku
   - `Google Gemini Chat Model14` → Claude 3.5 Haiku
   - `Google Gemini Chat Model2` → Claude 3.5 Haiku
   - `Google Gemini Chat Model7` → Claude 3.5 Haiku
   - `Google Gemini Chat Model` → Claude 3.5 Haiku
   - `Google Gemini Chat Model9` → Claude 3.5 Haiku

### 2. **All AI Connections Preserved**
   - 8 `ai_languageModel` connections maintained:
     - AI Agent3 (URL research and validation)
     - Information Extractor (content extraction)
     - Information Extractor1 (secondary extraction)
     - create-more-section (content generation)
     - add-short-headers (formatting)
     - normalise-output2 (normalization)
     - create-more-section1 (additional content)
     - get-insights (analysis)

### 3. **JSON Cleanup Node Added**
   - **Name:** `JSON_Cleanup`
   - **Position:** Before Information Extractor
   - **Function:** Removes markdown code block wrappers (```json...```) that cause parsing errors
   - **Connection:** `concatenate_text → JSON_Cleanup → Information Extractor`

### 4. **Supabase Job Node Disabled**
   - **Node:** `Get_job`
   - **Status:** Disabled for testing
   - **Why:** Allows manual execution without waiting for Supabase jobs

---

## Next Steps - Execute Your First Article

### Step 1: Add Anthropic API Credentials to n8n

1. Open n8n: `http://localhost:5678` (or your n8n URL)
2. Go to **Settings** → **Credentials** (or click your profile icon)
3. Click **Add Credential**
4. Search for **"Anthropic"** or **"Claude"**
5. Add your Anthropic API key
   - Get it from: https://console.anthropic.com/settings/keys
   - Your €5 credit should be active

### Step 2: Update All Claude Nodes

The workflow has been imported with 8 Claude Haiku nodes. You need to assign your Anthropic credential to each:

1. Open the workflow: `content-gen-CLAUDE-COMPLETE`
2. Look for nodes with names like:
   - `Google Gemini Chat Model3`
   - `Google Gemini Chat Model4`
   - etc. (they're now Claude nodes, names weren't changed to preserve connections)

3. For EACH of these 8 nodes:
   - Click the node
   - Under **Credential to connect with**, select your Anthropic credential
   - Click **Save**

**Important:** n8n requires credentials to be set manually after import. This is a one-time setup.

### Step 3: Provide Test Input Data

Since `Get_job` is disabled, you'll need to manually trigger the workflow with test data.

**Option A: Enable a Manual Trigger**
1. Find the node that comes after `Get_job` (likely `set_field_names`)
2. Add a **Manual Trigger** or **Webhook** node before it
3. Provide sample data matching the expected format:

```json
{
  "gpt_language": ["en"],
  "company_data": {
    "company_name": "Your Company",
    "company_url": "https://yourcompany.com",
    "company_language": "English",
    "company_competitors": ["competitor1.com", "competitor2.com"]
  },
  "blog_page": {
    "company_url": "https://yourcompany.com",
    "company_name": "Your Company",
    "topic": "Your article topic",
    "keywords": ["keyword1", "keyword2"]
  }
}
```

**Option B: Re-enable Get_job Later**
1. Click the `Get_job` node
2. Uncheck **"Disabled"**
3. Save the workflow
4. Let it run on schedule when Supabase jobs are ready

### Step 4: Execute the Workflow

1. Click **Execute Workflow** button (top right)
2. Watch the nodes light up as they execute
3. Check for errors in the **Executions** panel

### Step 5: Verify Output

- The JSON cleanup node should prevent parsing errors
- Each Claude node should process faster than Gemini (Haiku is optimized for speed)
- Final output should be your generated article content

---

## Troubleshooting

### "Missing credentials" error
- Go back to Step 2 and ensure ALL 8 Claude nodes have credentials assigned
- You'll see a red warning icon on nodes missing credentials

### "Execution timed out"
- Claude Haiku is fast, but check your timeout settings
- Go to workflow settings → increase execution timeout if needed

### "Invalid API key"
- Verify your Anthropic API key is active
- Check you have remaining credits: https://console.anthropic.com/settings/billing

### "JSON parsing error" (should be fixed now)
- The cleanup node should handle this
- If it still occurs, check the cleanup node is properly connected
- Verify the `concatenate_text → JSON_Cleanup → Information Extractor` path

### Still getting Gemini quota errors
- This shouldn't happen - all Gemini nodes were replaced
- Verify you're running the `content-gen-CLAUDE-COMPLETE` workflow
- Check no Gemini credentials are still assigned to any nodes

---

## Cost Estimation

**Claude 3.5 Haiku Pricing:**
- Input: $0.80 per million tokens
- Output: $4.00 per million tokens

**With €5 credit (~$5.30):**
- Assuming average article uses ~50k input + 10k output tokens per run
- Input cost: $0.04
- Output cost: $0.04
- **Total per article: ~$0.08**
- **Your credit covers: ~65 articles**

Much more efficient than running out of Gemini quota!

---

## Files Generated

- **Workflow file:** `/Users/matteolombardi/AI-Projects/stratega/workflows/content-gen-CLAUDE-COMPLETE.json`
- **Setup guide:** This file
- **Original workflow:** `content-gen-prod.json` (preserved as backup)

---

## Technical Details

### Nodes Modified: 11
- 8 AI model nodes (Gemini → Claude)
- 1 Supabase node (disabled)
- 1 JSON cleanup node (added)
- 1 connection rerouted

### Connections Preserved: 64
All original workflow logic maintained, only AI provider changed.

### Workflow Stats:
- Total nodes: 86
- Connection entries: 64
- AI model connections: 8

---

## Support

If you encounter any issues:

1. Check n8n execution logs (Executions panel)
2. Verify all credentials are set
3. Test with minimal input first
4. Check Anthropic console for API usage/errors

**The workflow is ready to execute. Go get your first article!** 🚀
