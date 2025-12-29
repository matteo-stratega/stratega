# Stratega n8n Workflows

Automation workflows for growth operations, lead generation, and content distribution.

## 📁 Structure

```
n8n-workflows/
├── linkedin/          # LinkedIn automation (content distribution, outreach)
├── school/            # Stratega School automation (enrollment, engagement)
├── lead-gen/          # Lead enrichment and outreach sequences
├── content/           # Multi-platform content distribution
└── docs/              # Documentation and SOPs
    └── sops/          # Standard Operating Procedures
```

## 🚀 Quick Start

1. Import workflow JSON into n8n
2. Configure credentials (LinkedIn, Supabase, etc.)
3. Test with sample data
4. Activate workflow

## 📋 Workflows Available

### LinkedIn
- **content-distribution.json**: Auto-publish to LinkedIn + Twitter + Reddit
- **connection-scraper.json**: Export and segment connections

### School
- **enrollment-automation.json**: Welcome sequences for new students
- **engagement-tracking.json**: Track module completions in Supabase

### Lead Gen
- **enrichment-pipeline.json**: CSV → Dropcontact → Supabase
- **outreach-sequences.json**: Automated DM campaigns

### Content
- **repurposing-flow.json**: School content → multi-platform posts

## 🔧 Requirements

- n8n (self-hosted or cloud)
- Supabase account
- API keys: Dropcontact, LinkedIn (if available), OpenAI (optional)

## 📝 SOPs

All workflows include SOPs in `/docs/sops/` with:
- Setup instructions
- Configuration guide
- Screen recordings (when available)
- Troubleshooting

---

**Maintained by:** Stratega Team
**Last Updated:** Nov 2024
