# Technical Projects - Learn by Building for Stratega

**Purpose:** 15 hands-on projects that solve real Stratega problems while building technical skills
**Philosophy:** No toy examples. Every project produces something useful.

---

## Project Overview

| # | Project | Skills | Difficulty | Time | Track |
|---|---------|--------|------------|------|-------|
| 1 | JSON Cleaner Node | JS basics | Beginner | 2h | JS |
| 2 | Contact Deduplicator | JS arrays | Beginner | 3h | JS |
| 3 | ICP Scorer Node | JS + logic | Intermediate | 4h | JS |
| 4 | Batch Processor | JS async | Intermediate | 3h | JS |
| 5 | CSV Processor CLI | Python basics | Beginner | 3h | Python |
| 6 | LinkedIn Data Analyzer | Pandas | Intermediate | 5h | Python |
| 7 | API Enrichment Tool | Requests | Intermediate | 4h | Python |
| 8 | Web Scraper | BeautifulSoup | Intermediate | 5h | Python |
| 9 | n8n Workflow Fixer | Python + JSON | Intermediate | 3h | Python |
| 10 | Git Backup Script | Bash + Git | Beginner | 2h | DevOps |
| 11 | Docker Health Monitor | Docker + Python | Intermediate | 3h | DevOps |
| 12 | Supabase Data Loader | Python + SQL | Intermediate | 4h | Integration |
| 13 | Email Campaign Generator | Full stack | Advanced | 6h | Integration |
| 14 | Lead Scoring Pipeline | Full stack | Advanced | 8h | Capstone |
| 15 | Stratega CLI Tool | Full stack | Advanced | 10h | Capstone |

---

## Project 1: JSON Cleaner Node

### Overview
Build an n8n code node that cleans LLM output (removes markdown wrappers, parses JSON).

**Difficulty:** Beginner
**Time:** 2 hours
**Skills:** JavaScript basics, string manipulation, error handling

### Why It Matters
LLMs often return JSON wrapped in markdown code blocks. This breaks downstream nodes. A reliable cleaner is essential for any AI workflow.

### Specification

**Input:**
```json
{
  "output": "```json\n{\"name\": \"Matteo\", \"score\": 85}\n```"
}
```

**Output:**
```json
{
  "name": "Matteo",
  "score": 85
}
```

### Step-by-Step

1. **Setup** (15 min)
   - Create new n8n workflow
   - Add Code node
   - Add sample input data

2. **Basic Cleaning** (30 min)
   - Get input text
   - Remove ```json wrapper
   - Remove closing ```
   - Trim whitespace

3. **JSON Parsing** (30 min)
   - Try to parse cleaned text as JSON
   - Handle parse failures gracefully
   - Return parsed object or error

4. **Edge Cases** (30 min)
   - Handle nested code blocks
   - Handle no code blocks
   - Handle empty input

5. **Test** (15 min)
   - Test with real LLM output
   - Test edge cases

### Success Criteria
- [ ] Cleans standard markdown JSON wrappers
- [ ] Handles nested JSON
- [ ] Returns error object on parse failure
- [ ] Works with multiple input formats

### Code Template
```javascript
const items = $input.all();

return items.map(item => {
  // Get the raw output
  let text = item.json.output || item.json.text || '';

  // Your cleaning logic here
  // ...

  return { json: { /* result */ } };
});
```

### Extension Ideas
- Add support for YAML output
- Handle multiple JSON objects in one response
- Add validation against expected schema

---

## Project 2: Contact Deduplicator

### Overview
Build an n8n code node that removes duplicate contacts based on email, with smart merge of conflicting data.

**Difficulty:** Beginner
**Time:** 3 hours
**Skills:** JavaScript arrays, objects, Set/Map

### Why It Matters
Lead lists always have duplicates. A good deduplicator saves hours of manual cleanup and improves campaign deliverability.

### Specification

**Input:**
```json
[
  {"email": "alice@example.com", "name": "Alice", "score": 70},
  {"email": "ALICE@example.com", "name": "Alice Smith", "score": 85},
  {"email": "bob@example.com", "name": "Bob", "score": 60}
]
```

**Output:**
```json
[
  {"email": "alice@example.com", "name": "Alice Smith", "score": 85, "duplicates_merged": 2},
  {"email": "bob@example.com", "name": "Bob", "score": 60, "duplicates_merged": 1}
]
```

### Step-by-Step

1. **Setup** (15 min)
   - Create workflow with sample data
   - Plan deduplication strategy

2. **Basic Deduplication** (45 min)
   - Normalize emails (lowercase, trim)
   - Use Map to track unique entries
   - Keep first occurrence

3. **Smart Merge** (45 min)
   - When duplicate found, merge data
   - Keep higher score
   - Keep longer name
   - Track merge count

4. **Configuration** (30 min)
   - Add option for dedupe key (email, URL, etc.)
   - Add merge strategy options

5. **Test** (30 min)
   - Test with real contact data
   - Verify merge logic

### Success Criteria
- [ ] Removes duplicates by email (case-insensitive)
- [ ] Merges data intelligently (keeps best values)
- [ ] Tracks number of duplicates merged
- [ ] Configurable dedupe key

### Code Template
```javascript
const items = $input.all();
const seen = new Map();

items.forEach(item => {
  const email = item.json.email?.toLowerCase()?.trim();
  if (!email) return;

  if (seen.has(email)) {
    // Merge logic here
  } else {
    seen.set(email, item.json);
  }
});

return Array.from(seen.values()).map(contact => ({ json: contact }));
```

---

## Project 3: ICP Scorer Node

### Overview
Build a complete ICP scoring engine as an n8n code node with configurable weights and patterns.

**Difficulty:** Intermediate
**Time:** 4 hours
**Skills:** JavaScript, regex, scoring logic, data transformation

### Why It Matters
ICP scoring is core to Stratega's value proposition. A flexible, configurable scorer enables rapid iteration on scoring models.

### Specification

**Input:**
```json
{
  "firstName": "Alice",
  "lastName": "Founder",
  "position": "CEO & Co-Founder",
  "company": "TechStartup SaaS",
  "email": "alice@techstartup.com"
}
```

**Output:**
```json
{
  "firstName": "Alice",
  "lastName": "Founder",
  "position": "CEO & Co-Founder",
  "company": "TechStartup SaaS",
  "email": "alice@techstartup.com",
  "scores": {
    "seniority": 100,
    "position_fit": 100,
    "company_fit": 100,
    "total": 100
  },
  "segment": "founder",
  "tier": "A"
}
```

### Step-by-Step

1. **Define Scoring Rules** (30 min)
   - Seniority patterns (founder, director, manager, etc.)
   - Position fit patterns (growth, marketing, sales, etc.)
   - Company fit patterns (SaaS, agency, startup, etc.)

2. **Build Pattern Matcher** (45 min)
   - Function to match text against regex patterns
   - Return highest matching score
   - Handle no match (default score)

3. **Implement Scoring** (60 min)
   - Score seniority from position
   - Score position fit
   - Score company fit
   - Calculate weighted total

4. **Add Segmentation** (45 min)
   - Determine segment (founder, agency, corporate)
   - Assign tier (A, B, C) based on total score

5. **Test & Refine** (30 min)
   - Test with real LinkedIn data
   - Adjust patterns based on results

### Success Criteria
- [ ] Scores contacts accurately
- [ ] Assigns correct segments
- [ ] Configurable scoring weights
- [ ] Handles missing/null fields gracefully

---

## Project 4: Batch Processor

### Overview
Build an n8n code node that splits large datasets into batches for rate-limited API calls.

**Difficulty:** Intermediate
**Time:** 3 hours
**Skills:** JavaScript arrays, async patterns, data chunking

### Why It Matters
APIs have rate limits. Processing 5000 contacts requires batching. This node makes any workflow batch-capable.

### Specification

**Input:** Array of 5000 items
**Output:** Array of 100 batches, each containing 50 items

### Step-by-Step

1. **Basic Chunking** (45 min)
   - Split array into chunks of N size
   - Preserve item structure

2. **Add Metadata** (30 min)
   - Add batch number
   - Add total batches count
   - Add items per batch count

3. **Progress Tracking** (45 min)
   - Calculate progress percentage
   - Estimate completion time

4. **Test** (30 min)
   - Test with large dataset
   - Verify chunk boundaries

### Success Criteria
- [ ] Splits data into configurable batch sizes
- [ ] Includes batch metadata
- [ ] Handles edge cases (empty array, array smaller than batch size)

---

## Project 5: CSV Processor CLI

### Overview
Build a Python command-line tool that processes CSV files with common operations.

**Difficulty:** Beginner
**Time:** 3 hours
**Skills:** Python basics, argparse, file I/O

### Why It Matters
Quick CSV processing without opening Excel. Run from terminal, script into workflows.

### Commands

```bash
# Filter rows
python csv_tool.py filter contacts.csv --column segment --value founder

# Select columns
python csv_tool.py select contacts.csv --columns "first_name,last_name,email"

# Sort
python csv_tool.py sort contacts.csv --by score --desc

# Dedupe
python csv_tool.py dedupe contacts.csv --key email

# Stats
python csv_tool.py stats contacts.csv
```

### Success Criteria
- [ ] Filter by column value
- [ ] Select specific columns
- [ ] Sort by column
- [ ] Remove duplicates
- [ ] Show basic statistics

---

## Project 6: LinkedIn Data Analyzer

### Overview
Build a Python script that analyzes LinkedIn connection data and generates insights.

**Difficulty:** Intermediate
**Time:** 5 hours
**Skills:** Pandas, data analysis, visualization

### Why It Matters
Understand your LinkedIn network. Find patterns, identify opportunities, track growth.

### Output Report

```markdown
# LinkedIn Network Analysis

## Overview
- Total connections: 4,715
- Connected this year: 892
- With email: 1,234 (26%)

## By Segment
- Founders: 1,200 (25%)
- Agency: 2,100 (45%)
- Corporate: 1,415 (30%)

## By Geography
- Italy: 1,500 (32%)
- International: 3,215 (68%)

## Top Companies
1. Google (45 connections)
2. Amazon (32 connections)
...

## Growth Trend
- 2023: +1,200 connections
- 2024: +800 connections
- 2025: +400 connections

## Recommendations
- Focus on Italian founders (high conversion potential)
- Re-engage 2023 connections (likely warm)
```

### Success Criteria
- [ ] Loads and cleans LinkedIn export
- [ ] Segments connections accurately
- [ ] Generates statistics by segment/geography
- [ ] Identifies trends over time
- [ ] Exports markdown report

---

## Project 7: API Enrichment Tool

### Overview
Build a Python tool that enriches contact data via APIs (Clearbit, Hunter, etc.).

**Difficulty:** Intermediate
**Time:** 4 hours
**Skills:** Requests, API integration, rate limiting

### Why It Matters
Raw contacts lack context. Enrichment adds company data, social profiles, and confidence scores.

### Features

```bash
# Enrich single company
python enricher.py company stratega.co

# Batch enrich from CSV
python enricher.py batch contacts.csv --output enriched.csv

# Check remaining credits
python enricher.py credits
```

### Success Criteria
- [ ] Calls enrichment API correctly
- [ ] Handles rate limits
- [ ] Caches results to avoid duplicate calls
- [ ] Gracefully handles errors
- [ ] Exports enriched data

---

## Project 8: Web Scraper

### Overview
Build a Python scraper that extracts business data from websites.

**Difficulty:** Intermediate
**Time:** 5 hours
**Skills:** BeautifulSoup, requests, data extraction

### Why It Matters
Lead generation often requires scraping. Company websites, directories, event pages all contain valuable data.

### Target: Event Speaker Pages

Extract from conference websites:
- Speaker name
- Company
- Position
- LinkedIn URL (if available)
- Bio

### Success Criteria
- [ ] Extracts structured data from HTML
- [ ] Handles multiple page formats
- [ ] Respects robots.txt
- [ ] Rate limits requests
- [ ] Exports to CSV

---

## Project 9: n8n Workflow Fixer

### Overview
Build a Python tool that analyzes and fixes common n8n workflow issues.

**Difficulty:** Intermediate
**Time:** 3 hours
**Skills:** Python, JSON manipulation, workflow understanding

### Why It Matters
n8n workflows break. Automated fixing saves debugging time.

### Features

```bash
# Analyze workflow
python n8n_fixer.py analyze workflow.json

# Fix common issues
python n8n_fixer.py fix workflow.json --output fixed.json

# Validate workflow
python n8n_fixer.py validate workflow.json
```

### Issues Detected/Fixed
- Missing node connections
- Invalid credentials references
- Deprecated node types
- Position overlaps

### Success Criteria
- [ ] Parses n8n JSON format
- [ ] Detects common issues
- [ ] Applies automatic fixes
- [ ] Validates result

---

## Project 10: Git Backup Script

### Overview
Build a bash script that backs up all Git repositories to cloud storage.

**Difficulty:** Beginner
**Time:** 2 hours
**Skills:** Bash, Git, automation

### Why It Matters
Never lose work. Automated backups provide peace of mind.

### Features

```bash
# Backup all repos in directory
./git_backup.sh ~/AI-Projects

# With compression
./git_backup.sh ~/AI-Projects --compress

# Upload to cloud
./git_backup.sh ~/AI-Projects --upload s3://bucket/backups
```

### Success Criteria
- [ ] Finds all Git repositories
- [ ] Creates dated backup
- [ ] Optionally compresses
- [ ] Works with cron for scheduling

---

## Project 11: Docker Health Monitor

### Overview
Build a Python tool that monitors Docker containers and alerts on issues.

**Difficulty:** Intermediate
**Time:** 3 hours
**Skills:** Docker API, monitoring, notifications

### Why It Matters
Know when n8n goes down before workflows fail.

### Features

```bash
# Check all containers
python docker_monitor.py status

# Watch with alerts
python docker_monitor.py watch --interval 60 --alert slack

# Restart unhealthy containers
python docker_monitor.py restart --if-unhealthy
```

### Success Criteria
- [ ] Lists container status
- [ ] Detects unhealthy containers
- [ ] Sends alerts (Slack, email)
- [ ] Can auto-restart

---

## Project 12: Supabase Data Loader

### Overview
Build a Python tool that syncs CSV data to Supabase tables.

**Difficulty:** Intermediate
**Time:** 4 hours
**Skills:** Supabase client, data loading, upsert logic

### Why It Matters
Supabase is your data warehouse. Easy loading enables rapid data iteration.

### Features

```bash
# Load CSV to table
python supabase_loader.py load contacts.csv --table contacts

# With upsert (update existing)
python supabase_loader.py load contacts.csv --table contacts --upsert email

# Sync changes only
python supabase_loader.py sync contacts.csv --table contacts --key email
```

### Success Criteria
- [ ] Connects to Supabase
- [ ] Creates table from CSV schema
- [ ] Inserts data in batches
- [ ] Supports upsert logic
- [ ] Handles errors gracefully

---

## Project 13: Email Campaign Generator

### Overview
Build a system that generates personalized email sequences from contact data and templates.

**Difficulty:** Advanced
**Time:** 6 hours
**Skills:** Python, templating, n8n integration

### Why It Matters
Outbound is key to Stratega growth. Personalized at scale requires automation.

### Features

```bash
# Generate sequence
python email_gen.py generate \
  --contacts italy_founders.csv \
  --template sequences/founder_outreach.md \
  --output campaign/

# Preview emails
python email_gen.py preview campaign/ --count 5

# Export for sending tool
python email_gen.py export campaign/ --format instantly
```

### Success Criteria
- [ ] Loads contact data
- [ ] Parses template with variables
- [ ] Generates personalized emails
- [ ] Exports in sending tool format
- [ ] Supports A/B testing variants

---

## Project 14: Lead Scoring Pipeline (Capstone)

### Overview
Build a complete lead scoring system from data ingestion to scored output.

**Difficulty:** Advanced
**Time:** 8 hours
**Skills:** Python, n8n, Supabase, full integration

### Architecture

```
LinkedIn Export → Python Cleaner → Supabase → n8n Scorer → Segmented CSVs
```

### Components

1. **Data Ingestion** (Python)
   - Parse LinkedIn export
   - Clean and normalize
   - Load to Supabase

2. **Scoring Engine** (n8n)
   - Read from Supabase
   - Apply ICP scoring
   - Write scores back

3. **Segmentation** (Python)
   - Extract scored contacts
   - Segment by geography/engagement
   - Export campaign-ready CSVs

### Success Criteria
- [ ] End-to-end pipeline works
- [ ] Handles 5000+ contacts
- [ ] Produces accurate segments
- [ ] Fully automated (one command)

---

## Project 15: Stratega CLI Tool (Capstone)

### Overview
Build a unified command-line interface for all Stratega operations.

**Difficulty:** Advanced
**Time:** 10 hours
**Skills:** Python, CLI design, integration

### Commands

```bash
# Contacts
stratega contacts import connections.csv
stratega contacts score --min 70
stratega contacts export founders --format csv

# Workflows
stratega workflow list
stratega workflow run content-generator
stratega workflow logs content-generator

# Data
stratega data query "SELECT * FROM contacts WHERE segment='founder'"
stratega data backup
stratega data sync

# Campaign
stratega campaign create --name "Italian Founders Dec"
stratega campaign preview --count 5
stratega campaign export --format instantly
```

### Success Criteria
- [ ] Unified interface for common operations
- [ ] Consistent command structure
- [ ] Helpful error messages
- [ ] Tab completion support
- [ ] Documentation generated

---

## Project Progression

### Week 1-2 (Beginner)
- Project 1: JSON Cleaner
- Project 2: Contact Deduplicator
- Project 5: CSV Processor CLI
- Project 10: Git Backup Script

### Week 3-4 (Intermediate)
- Project 3: ICP Scorer Node
- Project 4: Batch Processor
- Project 6: LinkedIn Data Analyzer

### Week 5-6 (Intermediate+)
- Project 7: API Enrichment Tool
- Project 8: Web Scraper
- Project 9: n8n Workflow Fixer

### Week 7-8 (Advanced)
- Project 11: Docker Health Monitor
- Project 12: Supabase Data Loader
- Project 13: Email Campaign Generator

### Week 9-12 (Capstone)
- Project 14: Lead Scoring Pipeline
- Project 15: Stratega CLI Tool

---

## Project Completion Checklist

For each project:
- [ ] Requirements understood
- [ ] Code written and tested
- [ ] Edge cases handled
- [ ] Documentation added
- [ ] Committed to Git
- [ ] Actually used for Stratega work

---

*Projects designed for Stratega OS development - November 2025*
