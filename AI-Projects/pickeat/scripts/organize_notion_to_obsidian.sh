#!/bin/bash

# Script to organize Notion workspace export into Obsidian vault structure
# Input: /tmp/notion-workspace-full.txt
# Output: Organized markdown files in obsidian-vault/

set -e

PROJECT_ROOT="$HOME/AI-Projects/pickeat"
OBSIDIAN_VAULT="$PROJECT_ROOT/obsidian-vault"
NOTION_DATA="/tmp/notion-workspace-full.txt"

echo "🗂️  Organizing Notion workspace → Obsidian vault"
echo "================================================"

# Create vault structure
mkdir -p "$OBSIDIAN_VAULT"/{00-Inbox,01-OKRs,02-Sales,03-Product,04-Marketing,05-HR,06-Events,07-Operations,08-Archive}

echo "✓ Created vault folder structure"

# Use ollama to parse and organize content
echo "⏳ Analyzing Notion structure with Ollama..."

cat << 'PROMPT' | cat - "$NOTION_DATA" | ollama run llama3.1 > "$OBSIDIAN_VAULT/00-Inbox/_workspace_structure.md" 2>&1
Analyze this Notion workspace export and create a markdown index of all pages organized by category:
- OKRs (Q4 objectives, business scoreboard)
- Sales (pipeline, prospecting, contacts)
- Product (roadmap, features)
- Marketing (campaigns, content)
- HR (team, hiring)
- Events (MWC, WebSummit, sports partnerships)
- Operations (service delivery, vendors)

Format as:
## Category Name
- [Page Title](notion://page-id) - Brief description

Data:
PROMPT

echo "✓ Generated workspace structure index"

# Create README
cat > "$OBSIDIAN_VAULT/README.md" << 'EOF'
# PickEat Knowledge Base (Obsidian Vault)

This vault contains organized knowledge from PickEat's Notion workspace.

## Structure

- `00-Inbox/` - New unprocessed content
- `01-OKRs/` - Quarterly objectives and key results
- `02-Sales/` - Pipeline, prospects, deals
- `03-Product/` - Roadmap, features, development
- `04-Marketing/` - Campaigns, content, growth
- `05-HR/` - Team, hiring, onboarding
- `06-Events/` - Conferences, partnerships
- `07-Operations/` - Service delivery, processes
- `08-Archive/` - Completed or outdated content

## Import Date

Generated: $(date)

## Source

Notion workspace export → Obsidian conversion

## Next Steps

1. Review `00-Inbox/_workspace_structure.md` for full page index
2. Move relevant pages from Inbox to appropriate folders
3. Create bidirectional links between related pages
4. Tag pages by status (active/completed/archived)
EOF

echo "✓ Created README"

# Create .obsidian config for graph view
mkdir -p "$OBSIDIAN_VAULT/.obsidian"
cat > "$OBSIDIAN_VAULT/.obsidian/app.json" << 'EOF'
{
  "defaultViewMode": "preview",
  "alwaysUpdateLinks": true,
  "showFrontmatter": false,
  "foldHeading": true,
  "foldIndent": true
}
EOF

echo "✓ Created Obsidian config"

# Summary
echo ""
echo "✅ Vault organization complete!"
echo "📂 Location: $OBSIDIAN_VAULT"
echo "📄 Pages indexed: See 00-Inbox/_workspace_structure.md"
echo ""
echo "Next: Open $OBSIDIAN_VAULT in Obsidian app"
