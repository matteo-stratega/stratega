# Advanced Lead Re-engagement Report Generation Model v2.0

**Objective:** Systematically identify, prioritize, and prepare high-quality context for re-engaging dormant leads, with robust data acquisition, intelligent routing, and actionable insights for advisors.

**Key Improvements in v2.0:**
- Enhanced CRM lookup with fallback strategies
- Automated "broken chain" analysis for conversation recovery
- Standardized output format for scalability
- Support for both external lists and direct CRM queries

---

## Phase 0: Initialization & Data Source Selection

**Goal:** Determine the starting point and scope for lead re-engagement.

### 1. Source Selection
Choose one of two approaches:

**Option A: External List (e.g., CSV, Google Sheets)**
- Use when you have a curated list from external research (conferences, partnerships, industry databases)
- Required fields: Entity Name, CRM Record Link/ID (optional), Context Notes

**Option B: Direct CRM Query**
- Use when targeting specific segments within your existing CRM
- Example queries:
  - "All companies in Switzerland with no activity in 90+ days"
  - "All sports venues with deal stage = 'Qualified' but no follow-up in 6 months"
  - "All leads from MWC 2024 with no closed deal"

### 2. Query Parameters (if Option B)
Define specific filters:
- **Geography:** Country, region, city
- **Industry/Category:** Sports teams, festivals, exhibition centers, food trucks
- **Time-based:** Last activity date, last contact date, deal age
- **Deal Stage:** Lead, Qualified, Proposal Sent, Negotiation, Closed-Lost
- **Custom Properties:** Event attended, product interest, budget range

---

## Phase 1: Initial Data Collection & Preparation

**Goal:** Extract and normalize core information for each target entity.

### If Starting from External List (Option A):
For each entity, extract:
1. **Entity Name** (required)
2. **CRM Record Link/ID** (if available)
3. **Context Notes** (textual summary of last interaction or status)
4. **Additional Identifiers** (optional: website, email domain, phone)

### If Starting from CRM Query (Option B):
For each entity retrieved from the query, extract:
1. **Entity Name**
2. **CRM Record ID**
3. **Relevant Properties** (industry, deal stage, last activity date, owner)
4. **Associated Contacts** (if applicable)

### Parsing & Normalization:
- Standardize entity names (remove "Inc.", "AG", "Ltd", etc. for matching)
- Extract domain names from URLs for secondary lookups
- Flag entities with incomplete data for manual review

---

## Phase 2: Data Normalization & Enrichment (Robust CRM Lookup)

**Goal:** Enrich each entity with complete CRM data using intelligent lookup strategies.

### 1. Primary CRM Lookup
- **If CRM ID provided:** Direct API call using record ID
- **If only name provided:** Search by exact entity name match

### 2. Fallback Routing Strategy (if primary lookup fails)

Execute the following lookups in sequence until a match is found:

#### **Fallback 1: Flexible Name Search**
- Use "contains" operator instead of exact match
- Remove common suffixes/prefixes (Inc, Ltd, GmbH, AG, Sport, Club)
- Search with partial name (e.g., "HC Davos" → "Davos")

#### **Fallback 2: Secondary Identifiers**
- Search by **website domain** (if available)
- Search by **phone number** (if available)
- Search by **email domain** (for contact records)

#### **Fallback 3: Custom Properties & Tags**
- Search by custom CRM fields (e.g., "team_name", "venue_name")
- Search by tags or labels
- Search by associated deals or contacts

#### **Fallback 4: Fuzzy Matching**
- Use similarity algorithms (Levenshtein distance) for close name matches
- Present top 3 matches for manual confirmation if confidence < 90%

### 3. Failure Handling
If all lookups fail:
- Mark entity as **"Not Found in CRM"**
- Create a placeholder record with available information
- Flag for manual CRM creation or verification
- Continue with external data only

### 4. Data Enrichment
Once record is found, retrieve:
- **Core Properties:**
  - `hs_last_sales_activity_date`
  - `notes_last_contacted`
  - `hs_lead_status`
  - `hs_pipeline_stage`

- **Associated Records:**
  - Primary contact (name, title, email, phone)
  - Deal(s) associated with the company
  - Recent activities (emails, calls, meetings, notes)

- **Custom Properties (if available):**
  - Event attended
  - Product interest
  - Budget/revenue range
  - Venue capacity (for sports/events)

---

## Phase 3: Entity Categorization (Hot/Cold)

**Goal:** Prioritize leads based on historical engagement signals.

### Classification Logic

Analyze textual notes (from initial source + CRM) and enriched properties using keyword detection and sentiment analysis.

#### **Hot List Criteria (Priority 1)**
Entities showing **positive engagement signals**:

**Strong Signals (Auto-Hot):**
- Keywords: "interested", "yes", "meeting scheduled", "demo requested", "call next week", "send proposal", "wants to talk", "deck sent and opened", "replied positively"
- Deal stage: "Qualified", "Proposal Sent", "Negotiation"
- Recent activity within 60 days

**Medium Signals (Manual Review):**
- Keywords: "spoke with", "forwarded to team", "evaluating", "considering", "timeline TBD"
- Deal stage: "Lead" with multiple touchpoints
- Last activity 61-180 days ago

#### **Cold List Criteria (Priority 2)**
Entities showing **negative or neutral signals**:

**Strong Negative Signals:**
- Keywords: "not interested", "no budget", "do not contact", "unsubscribed", "competitor chosen", "bad timing", "rejected"
- Deal stage: "Closed-Lost", "Disqualified"
- Explicit opt-out or blacklist

**Neutral Signals:**
- Keywords: "no response", "never replied", "no activity", "never contacted", "no CRM record"
- Deal stage: "New", "Attempted to Contact"
- Last activity > 180 days ago or never contacted

### Output
- **Hot List:** High-priority entities requiring personalized re-engagement
- **Cold List:** Low-priority entities for generic outreach or future nurturing

---

## Phase 4: CRM Deep Dive & "Broken Chain" Analysis (Hot List Only)

**Goal:** Identify why the conversation stalled and craft a recovery strategy.

### 1. Retrieve Associated Activities
Use CRM API to pull:
- All notes chronologically
- All emails (sent + received)
- All calls (logged with summaries)
- All meetings (scheduled + completed)

### 2. Chronological Analysis
Order activities from **most recent to oldest**:
```
2024-10-15: Note - "WhatsApp follow-up sent"
2024-10-01: Meeting - "Discussed demo for November event"
2024-09-20: Email - "Proposal sent via email"
2024-09-15: Call - "Initial discovery call, very interested"
```

### 3. Identify "Broken Chain"
Analyze the **last 3-5 activities** to determine:

**A) What was the last significant interaction?**
- Example: "Proposal sent on 09/20"

**B) What was the expected next step?**
- Example: "Awaiting feedback on proposal by end of September"

**C) Why did the conversation stall?**
Use pattern recognition:
- **Awaiting response from lead:** "Sent follow-up, no reply"
- **Internal blocker at lead:** "Waiting on budget approval", "POS system in progress"
- **Our side dropped the ball:** "Follow-up scheduled but never sent"
- **External event:** "Renovating stadium for 2 years", "Season ended"
- **Ambiguous:** "Last contact unclear, no explicit next step"

### 4. Generate Operational Brief
Create a **2-3 sentence summary** with this structure:

```
**Last Interaction:** [Date] - [What happened]
**Expected Next Step:** [What should have happened]
**Stall Reason:** [Why it didn't happen]
**Suggested Action:** [How to recover]
```

**Example:**
```
**Last Interaction:** 2024-06-03 - HC Davos replied, interested but blocked by POS system implementation.
**Expected Next Step:** Follow up in 2-3 months after POS system completion.
**Stall Reason:** We never followed up; timeline unclear.
**Suggested Action:** Reach out asking about POS system status; offer integration support.
```

---

## Phase 5: Final Report Compilation

**Goal:** Produce a clear, actionable report for the advisor.

### Report Structure

```markdown
# Lead Re-engagement Report: [Segment Name]
**Generated:** [Date]
**Source:** [External List / CRM Query]
**Total Entities:** [X Hot / Y Cold]

---

## Priority 1: Hot List (Immediate Action Required)

### 1. [Entity Name]
- **Priority:** P1-Hot
- **CRM Link:** [URL]
- **Context:** [From initial data source]
- **Brief:** [Generated from Phase 4]
- **Recommended Action:** [Specific next step]
- **Assigned To:** [Advisor name or team]
- **Target Date:** [Suggested follow-up date]

[Repeat for each hot entity]

---

## Priority 2: Cold List (Low-Priority / Future Nurture)

### 1. [Entity Name]
- **Priority:** P2-Cold
- **CRM Link:** [URL or "Not Found"]
- **Context:** [From initial data source]
- **Status:** [Reason for cold classification]
- **Recommended Action:** [Generic nurture campaign or hold]

[Repeat for each cold entity]

---

## Summary & Next Steps
- **Hot List:** [X] entities requiring personalized outreach
- **Cold List:** [Y] entities for future consideration
- **Missing CRM Records:** [Z] entities to be created/verified
- **Recommended Timeline:** Complete hot list outreach within [N] days
```

### Export Formats
1. **Markdown** (for documentation)
2. **CSV** (for import into CRM or task management)
3. **Notion Database** (for team collaboration)
4. **Google Sheets** (for advisor access)

---

## Automation & Implementation Notes

### Tools & APIs Required
- **CRM:** HubSpot API (or Salesforce, Pipedrive, etc.)
- **Data Processing:** Python + pandas for parsing and enrichment
- **Fuzzy Matching:** fuzzywuzzy library for name matching
- **Keyword Detection:** spaCy or simple regex for signal classification
- **Report Generation:** Markdown templating with Jinja2

### Workflow Execution
1. **Manual Trigger:** Advisor requests re-engagement report for specific segment
2. **Scheduled Batch:** Weekly/monthly automated reports for key regions
3. **Event-Driven:** Post-conference lead list processing

### Quality Assurance
- **Manual Review Gates:** Hot entities with ambiguous "broken chain" flagged for human review
- **CRM Data Quality:** Flag entities with missing/outdated contact info
- **Feedback Loop:** Track success rate of re-engagement to refine classification logic

---

## Example Use Cases

### Use Case 1: Switzerland Hockey Teams (Post-Season Follow-Up)
- **Source:** External CSV from Stephane's prospecting
- **Query:** All Swiss hockey teams contacted in last 12 months
- **Output:** Hot list (7 teams with positive signals) + Cold list (10 teams with no response)

### Use Case 2: MWC 2024 Leads (6-Month Follow-Up)
- **Source:** Direct CRM query
- **Query:** All leads from MWC 2024 with no closed deal and no activity in 90+ days
- **Output:** Prioritized list for re-engagement campaign

### Use Case 3: Festival Venues (Pre-Season Outreach)
- **Source:** Combination (external list + CRM)
- **Query:** All festival venues with past engagement but no active deal
- **Output:** Targeted outreach plan for upcoming festival season

---

## Changelog

### v2.0 (2025-11-18)
- Added robust fallback CRM lookup strategies
- Enhanced "broken chain" analysis with pattern recognition
- Standardized report format for scalability
- Added automation implementation notes
- Improved classification criteria with examples

### v1.0 (2024-XX-XX)
- Initial model with basic CRM lookup and categorization

---

*Model maintained by: PickEat Growth Team*
*Last updated: 2025-11-18*
