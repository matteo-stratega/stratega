# ICP Scoring Framework - Game Theory Model
*Mathematical Segmentation for LinkedIn Connections*

**Date:** 24 Nov 2024
**Total Universe:** 4,715 connections
**Goal:** Identify top 150 targets (50 per segment) with highest conversion probability

---

## 🎯 Game Theory Approach

### Core Principle: Expected Value Optimization

```
EV(contact) = P(conversion) × Value(conversion) - Cost(outreach)
```

**Where:**
- `P(conversion)` = Probability they convert (derived from scoring model)
- `Value(conversion)` = €49-99/month LTV
- `Cost(outreach)` = Time + opportunity cost (~5 min/DM)

**Goal:** Maximize EV across portfolio of 150 contacts.

---

## 📊 Scoring Model (0-100 Scale)

### Multi-Factor Weighted Scoring

**Total Score = Σ (Factor × Weight)**

```
Score = (Seniority × 0.30) +
        (Position_Fit × 0.25) +
        (Company_Type × 0.20) +
        (Recency × 0.15) +
        (Email_Available × 0.10)
```

---

## 🔢 Factor Definitions

### 1. Seniority Score (0-100) - Weight: 30%

**Logic:** Decision-makers convert faster, have budget authority.

| Pattern Match | Score | Reasoning |
|---------------|-------|-----------|
| CEO, Founder, Co-Founder | 100 | Ultimate decision maker |
| Managing Partner, General Partner | 95 | Investment/consulting authority |
| VP, Director, Head of | 80 | Budget holder, strategic decisions |
| Manager, Lead | 60 | Influencer, limited budget |
| Specialist, Analyst | 40 | Executor, no budget |
| No title / Student | 20 | Low purchase authority |

**Regex patterns:**
```regex
founder|co-founder|ceo|chief executive
managing partner|general partner|chairman
vp|vice president|director|head of
manager|lead|coordinator
specialist|analyst|associate
```

---

### 2. Position Fit Score (0-100) - Weight: 25%

**Logic:** Closer to growth/marketing = higher product-market fit.

**Segment A: Agency/Consultant (Growth Operator)**
| Pattern Match | Score | Reasoning |
|---------------|-------|-----------|
| Growth, Marketing, Digital | 100 | Direct PMF |
| Sales, Business Development | 85 | Adjacent, need lead gen |
| Product, Strategy | 70 | Strategic buyers |
| Operations, Project Manager | 50 | Support function |
| HR, Finance, Legal | 20 | Low relevance |

**Segment B: Founder/Entrepreneur**
| Pattern Match | Score | Reasoning |
|---------------|-------|-----------|
| Founder, CEO, Entrepreneur | 100 | Builder mindset |
| Product Manager | 80 | Execution-focused |
| Engineer, Developer | 60 | Technical but not primary |

**Segment C: Corporate Marketer**
| Pattern Match | Score | Reasoning |
|---------------|-------|-----------|
| Marketing, Growth, Digital | 100 | Direct PMF |
| Brand, Content, Social | 85 | Adjacent skill set |
| Sales, Partnerships | 70 | Growth-adjacent |

---

### 3. Company Type Score (0-100) - Weight: 20%

**Logic:** B2B SaaS/Agency/Startups = higher propensity to buy growth education.

| Company Indicators | Score | Reasoning |
|--------------------|-------|-----------|
| SaaS, Software, Platform | 100 | High growth need |
| Agency, Consulting, Services | 95 | Need for process |
| VC, Investment Fund | 90 | Portfolio support |
| Startup, Scale-up | 85 | Learning mode |
| Enterprise Tech (Google, Amazon, etc.) | 70 | Corporate learner |
| SMB/Traditional Industry | 50 | Lower digital maturity |
| Sports, Fashion, Hospitality | 40 | Low tech adoption |
| Student, Freelance, Unemployed | 20 | Low budget |

**Detection:**
- Company name matching (SaaS, Tech, Digital, Agency, VC, etc.)
- Position context (e.g., "Founder @ SaaS startup")
- Industry keywords

---

### 4. Recency Score (0-100) - Weight: 15%

**Logic:** Recent connections = warmer relationship, higher response rate.

| Connection Age | Score | Reasoning |
|----------------|-------|-----------|
| 0-30 days | 100 | Very fresh, top of mind |
| 31-90 days | 80 | Recent, still warm |
| 91-180 days (6 months) | 60 | Medium recency |
| 181-365 days (1 year) | 40 | Cooling down |
| 1-2 years | 25 | Cold, needs reactivation |
| 2+ years | 10 | Very cold |

**Calculation:**
```python
days_since_connection = (today - connected_on).days
if days <= 30: score = 100
elif days <= 90: score = 80
elif days <= 180: score = 60
elif days <= 365: score = 40
elif days <= 730: score = 25
else: score = 10
```

---

### 5. Email Available Score (0 or 100) - Weight: 10%

**Logic:** Email = higher conversion channel, bypasses LinkedIn DM limits.

| Email Status | Score | Reasoning |
|--------------|-------|-----------|
| Email present | 100 | Direct contact possible |
| No email | 0 | LinkedIn DM only |

---

## 🧮 Scoring Algorithm (Python-style)

```python
def calculate_icp_score(connection):
    """
    Calculate total ICP score (0-100) for a LinkedIn connection
    """

    # Extract fields
    position = connection.get('Position', '').lower()
    company = connection.get('Company', '').lower()
    connected_on = parse_date(connection.get('Connected On'))
    email = connection.get('Email Address')

    # 1. Seniority Score (30%)
    seniority_patterns = {
        r'(founder|co-founder|ceo|chief executive)': 100,
        r'(managing partner|general partner|chairman)': 95,
        r'(vp|vice president|director|head of)': 80,
        r'(manager|lead|coordinator)': 60,
        r'(specialist|analyst|associate)': 40,
    }
    seniority_score = match_patterns(position, seniority_patterns, default=20)

    # 2. Position Fit Score (25%) - segment-specific
    # This varies by segment, example for Agency/Growth:
    position_patterns = {
        r'(growth|marketing|digital)': 100,
        r'(sales|business development|bd)': 85,
        r'(product|strategy)': 70,
        r'(operations|project)': 50,
    }
    position_score = match_patterns(position, position_patterns, default=20)

    # 3. Company Type Score (20%)
    company_patterns = {
        r'(saas|software|platform|app)': 100,
        r'(agency|consulting|services)': 95,
        r'(venture|capital|vc|fund)': 90,
        r'(startup|scale)': 85,
        r'(google|amazon|microsoft|meta)': 70,
    }
    company_score = match_patterns(company, company_patterns, default=40)

    # 4. Recency Score (15%)
    days_since = (datetime.now() - connected_on).days
    if days_since <= 30: recency_score = 100
    elif days_since <= 90: recency_score = 80
    elif days_since <= 180: recency_score = 60
    elif days_since <= 365: recency_score = 40
    elif days_since <= 730: recency_score = 25
    else: recency_score = 10

    # 5. Email Available (10%)
    email_score = 100 if email and '@' in email else 0

    # Weighted total
    total_score = (
        seniority_score * 0.30 +
        position_score * 0.25 +
        company_score * 0.20 +
        recency_score * 0.15 +
        email_score * 0.10
    )

    return {
        'total_score': round(total_score, 2),
        'seniority_score': seniority_score,
        'position_score': position_score,
        'company_score': company_score,
        'recency_score': recency_score,
        'email_score': email_score,
        'breakdown': {
            'seniority': seniority_score * 0.30,
            'position': position_score * 0.25,
            'company': company_score * 0.20,
            'recency': recency_score * 0.15,
            'email': email_score * 0.10,
        }
    }
```

---

## 🎯 Segmentation Strategy

### Step 1: Score All 4,715 Connections

Run scoring algorithm on entire dataset → produce scored list.

### Step 2: Segment by Position Pattern

**Segment A: Agency/Growth Operators**
- Pattern: `marketing|growth|digital|agency|consultant`
- Expected: ~800-1,000 matches

**Segment B: Founders/Entrepreneurs**
- Pattern: `founder|ceo|entrepreneur|co-founder`
- Expected: ~600-800 matches

**Segment C: Corporate Marketers**
- Pattern: `marketing|brand|content` + company NOT agency
- Expected: ~400-600 matches

### Step 3: Rank Within Segment

- Sort each segment by `total_score` DESC
- Take top 50 from each segment
- **Output: 150 high-probability targets**

---

## 📊 Expected Value Analysis

### Conversion Probability Model

Based on scoring tiers:

| Score Range | P(conversion) | Expected # (from 50) | Value Generated |
|-------------|---------------|----------------------|-----------------|
| 90-100 | 20% | 10 | 10 × €49 = €490 MRR |
| 80-89 | 12% | 6 | 6 × €49 = €294 MRR |
| 70-79 | 8% | 4 | 4 × €49 = €196 MRR |
| 60-69 | 4% | 2 | 2 × €49 = €98 MRR |
| **Total** | **avg 11%** | **22 / 150** | **€1,078 MRR** |

**Conservative:** 10 conversions from 150 = €490 MRR ✅ **Target hit**

---

## 🧪 Testing Framework (Bayesian Update)

### Hypothesis Testing

**Null Hypothesis (H0):** All segments convert at same rate
**Alternative (H1):** Segment A (Agency) converts better than B or C

### A/B/C Test Design

**Week 1-2:** 50 DMs per segment (150 total)

**Track:**
- Response rate (%)
- Signup rate (%)
- Module 1 completion rate (%)
- Conversion to paid (%)

**Metrics:**
```
Segment A: 50 DMs → 12 responses → 6 signups → 2 paid
Segment B: 50 DMs → 8 responses → 4 signups → 1 paid
Segment C: 50 DMs → 5 responses → 2 signups → 0 paid
```

**Bayesian Update:**
If Segment A outperforms → allocate more resources (100 more DMs to A)
If all equal → diversify

---

## 🔄 Feedback Loop

### Iteration 1: Initial Scoring (Week 1)
- Run algorithm on all connections
- Segment top 150
- Launch DM campaigns

### Iteration 2: Update Weights (Week 3)
- Analyze which factors predicted conversion best
- Adjust weights:
  - If founders converted better → increase seniority weight
  - If recent connections responded more → increase recency weight

**Example adjustment:**
```python
# Original weights
weights = {'seniority': 0.30, 'position': 0.25, 'company': 0.20, 'recency': 0.15, 'email': 0.10}

# After data: recency matters more than expected
weights_v2 = {'seniority': 0.30, 'position': 0.20, 'company': 0.15, 'recency': 0.25, 'email': 0.10}
```

### Iteration 3: Rescore + Expand (Week 5)
- Rescore with updated weights
- Identify new top 100
- Scale winning segment

---

## 🏗️ Data Warehouse Schema (Supabase)

```sql
-- connections table
CREATE TABLE linkedin_connections (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  first_name TEXT,
  last_name TEXT,
  linkedin_url TEXT UNIQUE,
  email TEXT,
  company TEXT,
  position TEXT,
  connected_on DATE,

  -- Scoring fields
  seniority_score INTEGER,
  position_score INTEGER,
  company_score INTEGER,
  recency_score INTEGER,
  email_score INTEGER,
  total_score DECIMAL(5,2),

  -- Segmentation
  segment TEXT, -- 'agency', 'founder', 'corporate'

  -- Campaign tracking
  campaign_sent BOOLEAN DEFAULT FALSE,
  campaign_sent_date DATE,
  responded BOOLEAN DEFAULT FALSE,
  response_date DATE,
  signed_up BOOLEAN DEFAULT FALSE,
  signup_date DATE,
  converted_paid BOOLEAN DEFAULT FALSE,
  conversion_date DATE,

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Index for fast querying
CREATE INDEX idx_total_score ON linkedin_connections(total_score DESC);
CREATE INDEX idx_segment ON linkedin_connections(segment);
CREATE INDEX idx_campaign_tracking ON linkedin_connections(campaign_sent, responded, signed_up);

-- segment_performance table (for A/B testing)
CREATE TABLE segment_performance (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  segment TEXT,
  week INTEGER,
  dms_sent INTEGER,
  responses INTEGER,
  signups INTEGER,
  conversions INTEGER,
  response_rate DECIMAL(5,2),
  conversion_rate DECIMAL(5,2),
  created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 🎯 Implementation Steps

### Phase 1: Data Warehouse Setup (Day 1)
1. Create Supabase project
2. Run SQL schema
3. Import Connections.csv with scoring

### Phase 2: Scoring Execution (Day 1-2)
1. Write Python script for scoring
2. Score all 4,715 connections
3. Insert into Supabase

### Phase 3: Segmentation (Day 2)
1. Query top 50 per segment (SQL)
2. Export to campaign CSV
3. Validate manual (sanity check top 10 per segment)

### Phase 4: Campaign Launch (Day 3-7)
1. Send 50 DMs per segment
2. Track responses in Supabase
3. Update conversion funnel

### Phase 5: Analysis + Iteration (Day 8-14)
1. Calculate segment performance
2. Bayesian weight update
3. Rescore + launch round 2

---

## 📈 Success Metrics

**Primary:**
- Total Score accuracy: Do high-scorers convert at >10%?

**Secondary:**
- Segment winner: Which segment has highest conversion?
- Factor importance: Which factor best predicts conversion?

**Optimization:**
- Cost per conversion: Total time / conversions
- Portfolio EV: Total MRR generated / 150 contacts

---

## 🚀 Next Steps

1. **Build scoring script** (Python + Supabase client)
2. **Create Supabase project** + run schema
3. **Score 4,715 connections** + populate warehouse
4. **Extract top 150** (50 per segment)
5. **Launch Week 1 campaign** with tracking

---

**This is your replicable, scalable, game-theory ICP model.**

Every future campaign uses this framework. Update weights based on data. Scale what wins.

---

**Version:** 1.0
**Author:** Metis (Stratega Brain)
**Status:** Ready for implementation
