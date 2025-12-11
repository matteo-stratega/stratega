# Stratega Agent Architecture

**Version:** 1.0
**Date:** 26 November 2025
**Author:** Metis (Strategic Intelligence Architect)

---

## System Overview

The Stratega Agent Ecosystem is a three-tier architecture designed to transform manual operations into autonomous, coordinated growth execution.

```
                         ┌─────────────────────────────────────────┐
                         │          STRATEGA BRAIN (METIS)         │
                         │      Strategic Oversight & Memory       │
                         └─────────────────────┬───────────────────┘
                                               │
                    ┌──────────────────────────┼──────────────────────────┐
                    │                          │                          │
         ┌──────────▼──────────┐    ┌──────────▼──────────┐    ┌──────────▼──────────┐
         │  GROWTH ORCHESTRATOR │    │  CONTENT STRATEGIST │    │  REVENUE OPTIMIZER  │
         │   (Campaign Lead)    │    │   (Editorial Lead)  │    │   (L'Esattore 2.0)  │
         └──────────┬──────────┘    └──────────┬──────────┘    └──────────┬──────────┘
                    │                          │                          │
    ┌───────────────┼───────────────┐          │          ┌───────────────┼───────────────┐
    │               │               │          │          │               │               │
┌───▼───┐      ┌───▼───┐      ┌───▼───┐  ┌───▼───┐  ┌───▼───┐      ┌───▼───┐      ┌───▼───┐
│MARKETER│      │ DATA  │      │GROWTH │  │  SEO  │  │SOCIAL │      │ EMAIL │      │QUALITY│
│        │      │SCIENTIST│     │HACKER │  │WRITER │  │MANAGER│      │SEQUENCER│     │CONTROL│
└───┬───┘      └───┬───┘      └───┬───┘  └───┬───┘  └───┬───┘      └───┬───┘      └───┬───┘
    │               │               │          │          │               │               │
    └───────────────┴───────────────┴──────────┴──────────┴───────────────┴───────────────┘
                                               │
                    ┌──────────────────────────┼──────────────────────────┐
                    │                          │                          │
         ┌──────────▼──────────┐    ┌──────────▼──────────┐    ┌──────────▼──────────┐
         │     ARCHIVISTA      │    │      ARCHIMEDE      │    │    SESSION CLOSER   │
         │  (Workspace/Git)    │    │  (Technical Tutor)  │    │    (Daily Wrap)     │
         └─────────────────────┘    └─────────────────────┘    └─────────────────────┘
```

---

## Tier 1: Strategic Orchestrators

These agents set direction, prioritize work, and ensure alignment with €500 MRR goal.

### 1.1 Growth Orchestrator

**File:** `/agents/growth-orchestrator.md`

**Role:** Campaign coordination and sequencing across all growth initiatives.

**Responsibilities:**
- Design and sequence multi-channel campaigns
- Prioritize which ICP segments to target
- Coordinate between content, outreach, and experiments
- Report weekly on pipeline and metrics

**Input Sources:**
- `/docs/ICP_SCORING_FRAMEWORK.md` - Top 150 scored contacts
- `/outputs/linkedin_scoring_v2/` - Segmented prospect lists
- `/research/yc-b2b-growth-strategies-2023-2024.md` - Strategy playbook

**Output Deliverables:**
- Campaign execution plans
- Weekly priority lists
- Segment performance reports
- Channel allocation recommendations

**Success Metrics:**
- Campaigns launched per month: 4+
- Response rate on DM campaigns: 15%+
- Pipeline value generated: €2,000+/month

**Integration Points:**
- Receives ICP scores from Data Scientist
- Sends campaign briefs to Marketer
- Coordinates experiments with Growth Hacker
- Reports MRR contribution to Revenue Optimizer

---

### 1.2 Content Strategist

**File:** `/agents/content-strategist.md`

**Role:** Editorial planning and content calendar ownership.

**Responsibilities:**
- Create 90-day content calendars
- Define topic clusters and pillars
- Assign content to execution agents
- Balance content types (vitamins vs painkillers)

**Input Sources:**
- `/docs/lead-gen-crash-course/` - Framework library
- `/research/yc-b2b-growth-strategies-2023-2024.md` - Trend data
- Growth Orchestrator campaign priorities

**Output Deliverables:**
- 90-day editorial calendar (PED - Piano Editoriale Digitale)
- Topic cluster maps
- Content briefs for each piece
- Repurposing schedules

**Success Metrics:**
- Content pieces published per week: 15+
- Topics aligned with campaigns: 80%+
- Content-to-lead conversion: 5%+

**Integration Points:**
- Receives campaign priorities from Growth Orchestrator
- Sends content briefs to SEO Writer, Social Manager
- Reviews outputs through Quality Controller
- Reports engagement to Data Scientist

---

### 1.3 Revenue Optimizer (L'Esattore 2.0)

**File:** `/agents/esattore.md` (existing, to be enhanced)

**Role:** MRR accountability and monetization strategy.

**Responsibilities:**
- Track MRR progress weekly
- Identify monetization opportunities
- Challenge pricing and packaging decisions
- Hold Matteo accountable to revenue targets

**Input Sources:**
- Revenue data (Stripe, Gumroad, Supabase)
- Campaign conversion rates
- L'Esattore MRR roadmap (existing)

**Output Deliverables:**
- Weekly MRR scorecards
- Monetization opportunity assessments
- Pricing recommendations
- Fear/objection responses

**Success Metrics:**
- MRR tracking accuracy: 100%
- Revenue streams active: 3+
- Target hit rate: 90%+

**Integration Points:**
- Receives conversion data from Data Scientist
- Challenges priorities set by Growth Orchestrator
- Reviews pricing in campaign plans
- Escalates missed targets to Metis

---

## Tier 2: Execution Specialists

These agents produce tangible outputs - content, campaigns, data analysis.

### 2.1 Marketer

**File:** `/agents/marketer.md`

**Role:** Generate campaign-ready marketing materials.

**Responsibilities:**
- Write campaign copy (ads, landing pages, DMs)
- Create positioning and messaging
- Develop sales materials
- Generate launch plans

**Input Sources:**
- `/docs/lead-gen-crash-course/` - Frameworks and voice
- Growth Orchestrator campaign briefs
- ICP segment profiles

**Output Deliverables:**
- LinkedIn DM sequences
- Email copy
- Landing page copy
- Ad creative briefs
- Launch campaign documents

**Success Metrics:**
- Copy conversion rate: 10%+ click-through
- Materials produced per campaign: 5+
- Voice match score: 80%+

**Integration Points:**
- Receives briefs from Growth Orchestrator
- Sends copy to Quality Controller for review
- Provides copy to Email Sequencer
- Informs SEO Writer on messaging

---

### 2.2 SEO Content Writer

**File:** `/agents/seo-writer.md` (new)

**Role:** Create search-optimized long-form content.

**Responsibilities:**
- Write blog posts optimized for target keywords
- Create pillar pages and topic clusters
- Optimize existing content for SEO
- Develop content briefs with SEO requirements

**Input Sources:**
- Content Strategist topic clusters
- Keyword research data
- `/docs/lead-gen-crash-course/03-content.md` - Content methodology

**Output Deliverables:**
- Blog posts (1,500-3,000 words)
- Pillar pages (3,000-5,000 words)
- Meta descriptions and titles
- Internal linking recommendations

**Success Metrics:**
- Posts published per month: 4+
- Organic traffic growth: 20%+/month
- Keyword rankings: Top 10 for target terms

**Integration Points:**
- Receives topics from Content Strategist
- Aligns messaging with Marketer
- Passes content to Quality Controller
- Provides content for Social Manager to repurpose

---

### 2.3 Social Media Manager

**File:** `/agents/social-manager.md` (new)

**Role:** Manage social presence and community engagement.

**Responsibilities:**
- Repurpose content for LinkedIn, Twitter
- Schedule and publish social content
- Engage with comments and DMs
- Build thought leadership presence

**Input Sources:**
- SEO Writer blog posts (for repurposing)
- Content Strategist calendar
- `/docs/lead-gen-crash-course/03-content.md` - Social selling methodology

**Output Deliverables:**
- LinkedIn posts (5-7/week)
- Twitter threads (3-5/week)
- Carousel graphics briefs
- Engagement reports

**Success Metrics:**
- Posts per week: 10+
- Engagement rate: 5%+
- Leads from social: 10+/month

**Integration Points:**
- Receives content from SEO Writer
- Coordinates with Marketer on messaging
- Reports engagement to Data Scientist
- Surfaces leads to Growth Orchestrator

---

### 2.4 Email Sequencer

**File:** `/agents/email-sequencer.md` (new)

**Role:** Design and manage email nurture sequences.

**Responsibilities:**
- Create email sequences by segment
- Write email copy aligned with customer journey
- Design automation triggers
- Optimize based on performance

**Input Sources:**
- Marketer messaging and copy
- ICP segment definitions
- `/docs/lead-gen-crash-course/01-icp.md` - Client journey stages

**Output Deliverables:**
- Nurture sequences (5-7 emails each)
- Welcome sequences
- Re-engagement campaigns
- Trigger-based automation flows

**Success Metrics:**
- Open rate: 40%+
- Click rate: 10%+
- Sequence completion: 60%+

**Integration Points:**
- Receives copy from Marketer
- Aligned with Growth Orchestrator campaigns
- Reports performance to Data Scientist
- Integrates with Supabase for triggers

---

### 2.5 Research Analyst

**File:** `/agents/research-analyst.md` (new)

**Role:** Gather market intelligence and competitive insights.

**Responsibilities:**
- Research market trends
- Analyze competitors
- Document ICP insights
- Create research briefs

**Input Sources:**
- External sources (LinkedIn, Crunchbase, ProductHunt)
- Customer feedback
- `/research/` directory contents

**Output Deliverables:**
- Market research documents
- Competitive analysis
- ICP refinement recommendations
- Trend reports

**Success Metrics:**
- Research briefs per month: 2+
- Insights actioned: 80%+
- ICP accuracy improvement: measurable

**Integration Points:**
- Informs Content Strategist on trends
- Updates ICP scoring with Data Scientist
- Provides intelligence to Growth Orchestrator
- Documents findings for Archivista

---

### 2.6 Data Scientist

**File:** `/agents/data-scientist.md` (new)

**Role:** Analyze performance data and optimize scoring models.

**Responsibilities:**
- Run ICP scoring on connections
- Analyze campaign performance
- Update scoring weights based on results
- Generate performance dashboards

**Input Sources:**
- `/docs/ICP_SCORING_FRAMEWORK.md`
- `/docs/ICP_SCORING_V2_DESIGN.md`
- Supabase campaign tracking data
- Email and social performance data

**Output Deliverables:**
- ICP scored lists
- Segment performance reports
- Weight optimization recommendations
- Conversion funnel analysis

**Success Metrics:**
- Scoring accuracy: Top scorers convert at 10%+
- Data freshness: Weekly updates
- Attribution clarity: 90%+ tracked

**Integration Points:**
- Provides scores to Growth Orchestrator
- Updates weights based on Marketer results
- Reports to Revenue Optimizer
- Stores data via Archivista to Supabase

---

## Tier 3: Support & Quality

These agents maintain infrastructure, quality, and operational rhythm.

### 3.1 Quality Controller

**File:** `/agents/quality-controller.md` (new)

**Role:** Ensure all content matches Matteo's voice and brand standards.

**Responsibilities:**
- Review all content before publication
- Maintain voice profile document
- Flag off-brand content
- Provide feedback to execution agents

**Input Sources:**
- `/docs/lead-gen-crash-course/` - Voice examples
- All content from execution agents
- Brand guidelines

**Output Deliverables:**
- Approved/rejected content decisions
- Voice profile document
- Feedback notes
- Brand consistency reports

**Success Metrics:**
- Voice match score: 80%+
- Content approved first pass: 70%+
- Brand incidents: 0

**Integration Points:**
- Reviews all content before Archivista commits
- Provides feedback to Marketer, SEO Writer, Social Manager
- Maintains voice profile for Content Engine
- Reports quality trends to Metis

**Voice Profile Checklist:**
- Direct, no-fluff tone
- Framework-driven thinking
- Evidence-based claims (60%, 15%, etc.)
- Experiment mindset
- Avoid: motivational fluff, generic advice, buzzwords

---

### 3.2 Archivista (Existing)

**File:** `/agents/archivista.md`

**Role:** Workspace organization, Git management, memory.

**Responsibilities:**
- Maintain folder structure per CLAUDE.md
- Manage Git commits and history
- Archive completed work
- Ensure nothing gets lost

**Unchanged from existing definition.**

---

### 3.3 Session Closer (Existing)

**File:** `/agents/session-closer.md`

**Role:** End-of-day wrap and next-day setup.

**Responsibilities:**
- Capture session accomplishments
- Document decisions and blockers
- Set up tomorrow's priorities
- Create startup briefs

**Unchanged from existing definition.**

---

### 3.4 Archimede (Existing)

**File:** `/agents/archimede.md`

**Role:** Technical tutor for n8n, Supabase, SaaS development.

**Responsibilities:**
- Teach technical skills
- Build automation workflows
- Debug technical issues
- Guide toward first SaaS

**Unchanged from existing definition.**

---

### 3.5 Growth Hacker (Existing, Enhanced)

**File:** `/agents/growth-hacker.md`

**Role:** Run bi-weekly growth experiments.

**Responsibilities:**
- Design experiments with clear hypotheses
- Execute 2-week sprints
- Track results against success criteria
- Decide: Kill / Iterate / Scale

**Enhanced Integration:**
- Receives experiment priorities from Growth Orchestrator
- Reports results to Data Scientist
- Informs Content Strategist of winning content
- Contributes to Revenue Optimizer MRR tracking

---

## Coordination Protocols

### Daily Standup (Automated)

**Trigger:** Each morning, 8:00 CET

**Flow:**
1. Data Scientist surfaces key metrics
2. Growth Orchestrator confirms daily priorities
3. Content Strategist confirms publishing schedule
4. Execution agents receive assignments

**Output:** `/notes/daily-summaries/prep-DD-MM-YY.md`

---

### Weekly Review (Monday)

**Trigger:** Monday morning

**Participants:** Growth Orchestrator, Content Strategist, Revenue Optimizer, Data Scientist

**Agenda:**
1. MRR scorecard (Revenue Optimizer)
2. Campaign performance (Growth Orchestrator)
3. Content metrics (Content Strategist)
4. ICP scoring updates (Data Scientist)
5. Priority setting for week

**Output:** `/notes/weekly-reviews/WW-YYYY-review.md`

---

### Campaign Handoff Protocol

**When:** New campaign initiated

**Flow:**
```
1. Growth Orchestrator creates campaign brief
   → Includes: objective, ICP segment, channels, timeline

2. Marketer develops messaging
   → Includes: positioning, copy, CTAs

3. Quality Controller reviews voice
   → Approves or returns for revision

4. Execution splits:
   - Email Sequencer: email copy
   - Social Manager: social content
   - SEO Writer: landing page (if needed)

5. Data Scientist sets up tracking
   → Supabase tables, UTM parameters

6. Campaign launches

7. Data Scientist reports performance
   → Weekly during campaign

8. Growth Orchestrator decides: Scale / Iterate / Kill
```

---

### Content Publishing Protocol

**When:** Content ready for publication

**Flow:**
```
1. Execution agent (SEO Writer/Social Manager) submits draft

2. Quality Controller reviews
   - Voice match check
   - Brand alignment check
   - Accuracy check

3. If approved:
   - Archivista commits to repo
   - Content scheduled for publication
   - Data Scientist sets up tracking

4. If rejected:
   - Feedback returned to author
   - Revision cycle (max 2)

5. Post-publication:
   - Data Scientist tracks performance
   - Content Strategist reviews for repurposing
```

---

## Data Flow Architecture

### Supabase Schema (Core Tables)

```sql
-- Contacts & ICP Scoring
CREATE TABLE linkedin_connections (
  id UUID PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  linkedin_url TEXT UNIQUE,
  email TEXT,
  company TEXT,
  position TEXT,
  connected_on DATE,

  -- V1 Scoring
  seniority_score INTEGER,
  position_score INTEGER,
  company_score INTEGER,
  recency_score INTEGER,
  email_score INTEGER,
  total_score_v1 DECIMAL(5,2),

  -- V2 Scoring (Engagement)
  message_count INTEGER,
  connection_direction TEXT,
  last_message_date DATE,
  engagement_score INTEGER,
  total_score_v2 DECIMAL(5,2),

  -- Segmentation
  segment TEXT,
  geography TEXT,
  tier INTEGER,

  -- Campaign Tracking
  campaign_id UUID REFERENCES campaigns(id),
  dm_sent BOOLEAN DEFAULT FALSE,
  dm_sent_date DATE,
  responded BOOLEAN DEFAULT FALSE,
  response_date DATE,
  signed_up BOOLEAN DEFAULT FALSE,
  converted_paid BOOLEAN DEFAULT FALSE,

  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Campaigns
CREATE TABLE campaigns (
  id UUID PRIMARY KEY,
  name TEXT,
  status TEXT,
  start_date DATE,
  end_date DATE,
  segment TEXT,
  channel TEXT,

  -- Metrics
  contacts_targeted INTEGER,
  messages_sent INTEGER,
  responses INTEGER,
  signups INTEGER,
  conversions INTEGER,
  revenue DECIMAL(10,2),

  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Content Performance
CREATE TABLE content_pieces (
  id UUID PRIMARY KEY,
  title TEXT,
  type TEXT, -- blog, linkedin, twitter, email
  url TEXT,
  published_date DATE,

  -- Metrics
  views INTEGER,
  clicks INTEGER,
  shares INTEGER,
  leads_generated INTEGER,

  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Revenue Tracking
CREATE TABLE revenue_events (
  id UUID PRIMARY KEY,
  source TEXT, -- gumroad, stripe, direct
  product TEXT,
  amount DECIMAL(10,2),
  currency TEXT DEFAULT 'EUR',
  customer_email TEXT,
  attribution_campaign UUID REFERENCES campaigns(id),
  attribution_content UUID REFERENCES content_pieces(id),

  event_date DATE,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Experiments
CREATE TABLE experiments (
  id UUID PRIMARY KEY,
  hypothesis TEXT,
  channel TEXT,
  primary_metric TEXT,
  target_value TEXT,

  start_date DATE,
  end_date DATE,
  status TEXT, -- active, completed, killed

  -- Results
  actual_value TEXT,
  decision TEXT, -- scale, iterate, kill
  learnings TEXT,

  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

---

## Agent Activation Commands

### How to Invoke Each Agent

**Growth Orchestrator:**
```
"Growth Orchestrator: Create a campaign plan for targeting Segment A (Agency) with Stratega School pre-launch"
```

**Content Strategist:**
```
"Content Strategist: Build a 90-day editorial calendar for Q1 2026 focused on lead generation education"
```

**Marketer:**
```
"Marketer: Write a LinkedIn DM sequence for Italian founders in my top 50 ICP list"
```

**Data Scientist:**
```
"Data Scientist: Run ICP V2 scoring on my connections and segment the top 150"
```

**Quality Controller:**
```
"Quality Controller: Review this LinkedIn post for voice match before I publish"
```

---

## Success Metrics (System-Wide)

| Metric | Baseline | 30-Day | 60-Day | 90-Day |
|--------|----------|--------|--------|--------|
| **Agents Active** | 4 | 8 | 10 | 12 |
| **Content/Week** | 3 | 15 | 20 | 25 |
| **Campaigns Active** | 0 | 2 | 3 | 4 |
| **ICP Contacts Scored** | 0 | 4,715 | 4,715 | 5,000+ |
| **Top Tier Contacted** | 0 | 50 | 100 | 150 |
| **Leads Generated** | 5/mo | 20/mo | 40/mo | 60/mo |
| **MRR** | €0 | €100 | €300 | €500 |

---

## Next Steps

1. **Implement Priority Agents:**
   - `/agents/marketer.md` (Day 1-2)
   - `/agents/content-strategist.md` (Day 3-4)
   - `/agents/growth-orchestrator.md` (Day 5-7)

2. **Run Proof of Concept:**
   - Use Marketer to create Stratega School launch campaign
   - Validate voice, frameworks, output quality

3. **Deploy Data Infrastructure:**
   - Create Supabase project
   - Run ICP V2 scoring
   - Populate contacts table

4. **Launch First Campaign:**
   - Target Segment A (Agency/Growth) Italy
   - 50 personalized DMs
   - Track in Supabase

---

**Document Version:** 1.0
**Status:** Ready for implementation
**Maintainer:** Metis (Stratega Brain)

