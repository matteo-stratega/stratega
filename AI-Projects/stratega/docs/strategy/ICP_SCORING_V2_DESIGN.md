# ICP Scoring V2.0 - Engagement-Based Refinement

**Date:** 24 Nov 2024
**Status:** Design Phase (not implemented yet)
**Goal:** Fix recency bias + add real engagement signals

---

## 🔴 Problems with V1.0

### Issue #1: Recency Bias
**Problem:** Recent connections (2024-2025) scored higher, but they're OUTGOING cold campaigns.

**Example from your data:**
- **2025 Nov connections:** Almost all OUTGOING invites (sport partnerships, PickEat)
- **2023 connections:** Your active period, genuine relationships

**V1 wrongly assumed:** Recent = warmer
**Reality:** Recent = your campaigns (colder), Old = organic (warmer if engaged)

---

### Issue #2: No Engagement Signal
**Problem:** V1 only looked at static profile data (seniority, position, company).

**Missing:**
- Did you exchange messages?
- How long was the conversation?
- Who initiated the connection?
- Did they endorse you back?

**Result:** Cold VC from your campaign scored same as warm founder you talked with for months.

---

### Issue #3: No Geographic Split
**Problem:** Italia vs International requires different messaging/timing.

**Why it matters:**
- Italian connections = Italian DM (higher trust)
- International = English DM (different value prop)
- Campaigns should be split

---

## ✅ V2.0 Design - Engagement-First Model

### New Philosophy

```
Connection Value = (Profile Fit × Static Score) + (Relationship Warmth × Engagement Score)
```

**Trade-off:**
- V1: Optimize for "best fit on paper"
- V2: Optimize for "best fit + highest engagement"

**Why V2 is better:**
- Engaged low-fit > Cold high-fit (easier to convert)
- 2023 connections with 10 messages > 2025 VC you never talked to

---

## 🧮 New Scoring Model

### Total Score Formula (0-100)

```
Total Score = (Static_Score × 0.60) + (Engagement_Score × 0.40)
```

**Weights:**
- 60% Static (profile fit) - still matters
- 40% Engagement (relationship warmth) - NEW, high weight

---

### Static Score (0-100) - Adjusted from V1

**Factors:**

| Factor | Weight | V1 Weight | Change |
|--------|--------|-----------|--------|
| Seniority | 40% | 30% | +10% (more important) |
| Position Fit | 35% | 25% | +10% (more important) |
| Company Type | 25% | 20% | +5% (more important) |
| ~~Recency~~ | ~~15%~~ | 15% | **REMOVED** |
| ~~Email~~ | ~~10%~~ | 10% | **MOVED to engagement** |

**Why changes:**
- Removed recency (it was wrong)
- Removed email (now part of engagement)
- Increased profile factors (they're reliable)

**Calculation:**
```
Static_Score = (Seniority × 0.40) + (Position_Fit × 0.35) + (Company_Type × 0.25)
```

---

### Engagement Score (0-100) - NEW

**This is the game changer.**

#### Factor 1: Message Volume (40% of engagement score)

**Logic:** More messages = stronger relationship.

**Calculation:**
```
messages_exchanged = count messages in conversation
if messages == 0: score = 0
elif messages == 1-2: score = 20   (minimal)
elif messages == 3-5: score = 40   (some interaction)
elif messages == 6-10: score = 60  (engaged)
elif messages == 11-20: score = 80 (very engaged)
elif messages > 20: score = 100    (hot relationship)
```

**From your data:**
- Giacomo Perazzo: 26+ messages (score = 100)
- Matteo Milone: 2 messages (score = 20)
- Most 2025 connections: 0-1 messages (score = 0-20)

---

#### Factor 2: Connection Direction (30% of engagement score)

**Logic:** INCOMING = they wanted to connect with you (warmer).

**Calculation:**
```
if direction == INCOMING: score = 100
elif direction == OUTGOING and messages > 0: score = 60  (you reached out, they replied)
elif direction == OUTGOING and messages == 0: score = 20 (cold campaign, no reply)
else: score = 50  (unknown)
```

**Key insight:**
- INCOMING + messages = highest warmth
- OUTGOING + no messages = lowest warmth

---

#### Factor 3: Conversation Recency (20% of engagement score)

**Logic:** Recent conversation = relationship still active.

**Calculation:**
```
last_message_date = most recent message in conversation
days_since = (today - last_message_date).days

if days_since <= 30: score = 100       (very recent)
elif days_since <= 90: score = 80      (recent)
elif days_since <= 180: score = 60     (medium)
elif days_since <= 365: score = 40     (cooling)
elif days_since <= 730: score = 20     (cold)
else: score = 10                       (very cold)
```

**Important:** This is conversation recency, NOT connection recency.

**Example:**
- Connected 2020, last message Nov 2025 = score 100 (still talking!)
- Connected Nov 2025, never messaged = score 10 (cold campaign)

---

#### Factor 4: Email Availability (10% of engagement score)

**Logic:** Email = direct channel (moved from V1).

```
if email_present: score = 100
else: score = 0
```

---

### Engagement Score Calculation

```python
engagement_score = (
    message_volume_score * 0.40 +
    connection_direction_score * 0.30 +
    conversation_recency_score * 0.20 +
    email_score * 0.10
)
```

---

## 🌍 Geographic Segmentation

### Detection Logic

**Italy Indicators:**
- Position contains Italian keywords: `amministratore|direttore|responsabile|capo`
- Company contains `.it` or Italian brand names
- Name is Italian (heuristic: ends in vowel + common Italian surnames)
- Messages in Italian language

**International:**
- Everything else

**Output:** `geography` field = `'italy'` or `'international'`

---

## 📊 New Segmentation Matrix

### 4 Primary Segments

| Geography | Engagement | Profile Fit | Priority |
|-----------|-----------|-------------|----------|
| Italy | High | High | **Tier 1** (warmest) |
| Italy | High | Medium | **Tier 2** |
| International | High | High | **Tier 3** |
| Italy | Low | High | **Tier 4** |
| International | High | Medium | **Tier 5** |
| International | Low | High | **Tier 6** |
| Italy | Low | Medium | **Tier 7** |
| International | Low | Medium | **Tier 8** |

### Campaign Priority

**Week 1:** Italy - High Engagement (warm Italian connections)
**Week 2:** International - High Engagement (warm global connections)
**Week 3:** Italy - Low Engagement (cold Italian, but good fit)
**Week 4+:** International - Low Engagement (cold global)

---

## 🧪 Expected Results Changes

### V1.0 Top 5 (What We Had)

| Rank | Name | Score | Why High |
|------|------|-------|----------|
| 1 | Salomon Aiach (VC) | 92.0 | Founder + email + recent (Jul 2025) |
| 2 | Viktoriya Tigipko (VC) | 88.0 | Founder + very recent (Nov 2025) |
| 3 | Matteo Milone | 88.0 | Founder + recent + email |
| 4 | Giorgio Ghisalberti | 85.5 | CEO + email (but Sep 2022) |
| 5 | Artem Smirnov | 85.5 | CEO + email (but Jul 2020) |

**Issues:**
- Salomon, Viktoriya = your VC campaigns (probably 0 messages)
- Matteo Milone = 2 messages only (minimal engagement)
- Giorgio, Artem = old but unknown engagement

---

### V2.0 Expected Top 5 (After Refinement)

**Hypothesis (needs validation with data):**

| Rank | Name | Static | Engagement | Total | Why High |
|------|------|--------|------------|-------|----------|
| 1 | [Person with 20+ messages] | 75 | 95 | 82.0 | Hot relationship > perfect profile |
| 2 | [Italy founder, 10 msgs] | 85 | 75 | 81.0 | Good fit + engaged + Italian |
| 3 | Matteo Milone | 85 | 45 | 69.0 | Good fit but low engagement (2 msgs) |
| 4 | Giacomo Perazzo (if found in connections) | 70 | 90 | 78.0 | Very engaged (26 msgs) |
| 5 | [INCOMING + messages] | 70 | 80 | 74.0 | They reached out + talked |

**Key changes:**
- Highly engaged connections rise to top (even if not perfect fit)
- Cold 2025 VCs drop (despite good fit on paper)
- 2023 engaged connections rise (if still relevant)

---

## 📈 Scoring Examples (Detailed)

### Example 1: Matteo Milone (Your Top 3 in V1)

**V1.0 Score: 88.0**
- Seniority: 100 (founder)
- Position: 100 (founder)
- Company: 40 (Advera - not SaaS/VC)
- Recency: 100 (Nov 2025)
- Email: 100 (available)

**V2.0 Analysis:**

**Static Score:**
- Seniority: 100 × 0.40 = 40.0
- Position: 100 × 0.35 = 35.0
- Company: 40 × 0.25 = 10.0
- **Static Total: 85.0**

**Engagement Score:**
- Message Volume: 2 messages → 20 × 0.40 = 8.0
- Direction: OUTGOING + replied → 60 × 0.30 = 18.0
- Conversation Recency: Nov 2025 → 100 × 0.20 = 20.0
- Email: Yes → 100 × 0.10 = 10.0
- **Engagement Total: 56.0**

**V2.0 Total:**
```
(85.0 × 0.60) + (56.0 × 0.40) = 51.0 + 22.4 = 73.4
```

**Result:** Drops from 88.0 → 73.4 (still good, but not top tier due to low engagement)

---

### Example 2: Giacomo Perazzo (High Engagement)

**From messages.csv:** 26+ messages exchanged, ongoing conversation

**V2.0 Analysis:**

**Static Score:**
- Seniority: 60 (assume manager/specialist level)
- Position: 70 (assume relevant role)
- Company: 60 (assume medium fit)
- **Static Total: 63.0**

**Engagement Score:**
- Message Volume: 26+ messages → 100 × 0.40 = 40.0
- Direction: INCOMING (hypothesis) → 100 × 0.30 = 30.0
- Conversation Recency: Last message Oct 2025 → 80 × 0.20 = 16.0
- Email: Unknown, assume no → 0 × 0.10 = 0
- **Engagement Total: 86.0**

**V2.0 Total:**
```
(63.0 × 0.60) + (86.0 × 0.40) = 37.8 + 34.4 = 72.2
```

**Result:** Despite lower static fit, high engagement pushes score to 72.2 (solid tier 2)

---

### Example 3: Cold 2025 VC (No Messages)

**V1.0 Score: 82.0** (top 10 founder segment)
- Seniority: 100 (VC partner)
- Position: 100 (VC)
- Company: 90 (VC fund)
- Recency: 60 (Jun 2025)
- Email: 0 (no email)

**V2.0 Analysis:**

**Static Score:**
- Seniority: 100 × 0.40 = 40.0
- Position: 100 × 0.35 = 35.0
- Company: 90 × 0.25 = 22.5
- **Static Total: 97.5** (excellent!)

**Engagement Score:**
- Message Volume: 0 messages → 0 × 0.40 = 0
- Direction: OUTGOING + no reply → 20 × 0.30 = 6.0
- Conversation Recency: Never messaged → 10 × 0.20 = 2.0
- Email: No → 0 × 0.10 = 0
- **Engagement Total: 8.0** (very cold!)

**V2.0 Total:**
```
(97.5 × 0.60) + (8.0 × 0.40) = 58.5 + 3.2 = 61.7
```

**Result:** Drops from 82.0 → 61.7 (perfect on paper, but zero relationship = lower priority)

---

## 🎯 Campaign Strategy with V2.0

### Tier 1: Italy - High Engagement (Priority 1)

**Characteristics:**
- Italian connections
- 6+ messages exchanged
- Recent conversation (<180 days)
- Good profile fit (60+ static score)

**Approach:**
- DM in Italian
- Reference past conversation
- "Ciao [Name], è un po' che non ci sentiamo..."
- High conversion probability (already warm)

**Expected:** Top 30-50 connections
**Conversion rate:** 15-20% (very warm)
**MRR potential:** €220-490

---

### Tier 2: International - High Engagement

**Characteristics:**
- International connections
- 6+ messages exchanged
- English communication
- Good profile fit

**Approach:**
- DM in English
- Reference past interaction
- "Hey [Name], been a while since we talked..."

**Expected:** Top 20-30 connections
**Conversion rate:** 10-15%
**MRR potential:** €98-220

---

### Tier 3: Italy - Low Engagement (Good Fit)

**Characteristics:**
- Italian connections
- 0-2 messages
- Good profile fit (70+ static score)
- Old connections (2023) or recent OUTGOING

**Approach:**
- Cold-ish DM in Italian
- Lead with value
- "Ciao [Name], sto costruendo..."

**Expected:** Top 50-70 connections
**Conversion rate:** 5-8%
**MRR potential:** €122-274

---

### Tier 4: International - Low Engagement

**Only if Tier 1-3 don't hit target.**

---

## 📊 Expected Distribution (Hypothesis)

Based on your activity pattern:

| Segment | Estimated Count | Avg Score V2 | Top 50 Avg |
|---------|----------------|--------------|------------|
| Italy - High Engagement | ~200 | 68.0 | 75.0 |
| Italy - Low Engagement | ~800 | 52.0 | 64.0 |
| International - High Engagement | ~150 | 72.0 | 78.0 |
| International - Low Engagement | ~3,500 | 48.0 | 58.0 |

**Key insight:** International connections might have higher engagement (your active 2023 period was global).

---

## 🔧 Implementation Plan

### Step 1: Data Processing (Python)

**Parse messages.csv:**
```python
# Count messages per LinkedIn URL
# Extract last message date per person
# Detect language (Italian vs English)
```

**Parse invitations.csv:**
```python
# Map URL to INCOMING vs OUTGOING
# Join with connections
```

**Parse endorsements.csv:**
```python
# Count endorsements received per person
# (Optional: boost engagement if endorsed)
```

### Step 2: Geographic Detection

```python
# Italy indicators:
italian_positions = r'(amministratore|direttore|responsabile|capo|CEO|fondatore|socio)'
italian_companies = r'(\.it|srl|spa|società)'
italian_names_pattern = ... # heuristic

# Label each connection
```

### Step 3: Recalculate Scores

```python
for connection in connections:
    static_score = calculate_static_score(connection)
    engagement_score = calculate_engagement_score(
        connection, messages_data, invitations_data
    )
    total_score = (static_score * 0.60) + (engagement_score * 0.40)
    connection['score_v2'] = total_score
    connection['geography'] = detect_geography(connection)
```

### Step 4: Segment + Export

```python
# Group by (geography, engagement_level, segment)
# Extract top 50 per tier
# Export CSVs
```

---

## ✅ V2.0 vs V1.0 Summary

| Aspect | V1.0 | V2.0 |
|--------|------|------|
| **Recency logic** | Recent = better | Conversation recency = better |
| **Engagement** | Not considered | 40% of score |
| **Cold campaigns** | Scored high (wrong) | Penalized (correct) |
| **Warm relationships** | Undervalued | Prioritized |
| **Geography** | Not split | Italy vs International |
| **Campaign strategy** | One-size-fits-all | Tiered by warmth |
| **Expected conversion** | 8-12% | 12-18% (warmer targets) |

---

## 🚀 Next Steps

1. **Review this design** - Does logic make sense?
2. **Adjust weights if needed** - 60/40 static/engagement ok?
3. **Implement V2 script** - ~20 min to code
4. **Run on your data** - See actual results
5. **Compare V1 vs V2 top 50** - Validate changes make sense
6. **Launch Tier 1 campaign** - Italy high engagement first

---

**Your call:** Proceed with implementation or adjust design first?

---

**Version:** 2.0 (Design Phase)
**Status:** Awaiting approval
**Author:** Metis (Stratega Brain)
