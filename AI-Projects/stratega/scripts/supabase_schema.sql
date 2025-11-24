-- Supabase Schema for LinkedIn ICP Scoring
-- Data Warehouse for Connection Segmentation & Campaign Tracking

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Main connections table
CREATE TABLE linkedin_connections (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),

  -- LinkedIn data
  first_name TEXT,
  last_name TEXT,
  linkedin_url TEXT UNIQUE NOT NULL,
  email TEXT,
  company TEXT,
  position TEXT,
  connected_on DATE,

  -- Scoring fields
  segment TEXT CHECK (segment IN ('agency', 'founder', 'corporate')),
  seniority_score INTEGER CHECK (seniority_score >= 0 AND seniority_score <= 100),
  position_score INTEGER CHECK (position_score >= 0 AND position_score <= 100),
  company_score INTEGER CHECK (company_score >= 0 AND company_score <= 100),
  recency_score INTEGER CHECK (recency_score >= 0 AND recency_score <= 100),
  email_score INTEGER CHECK (email_score IN (0, 100)),
  total_score DECIMAL(5,2) CHECK (total_score >= 0 AND total_score <= 100),

  -- Campaign tracking
  campaign_sent BOOLEAN DEFAULT FALSE,
  campaign_sent_date DATE,
  campaign_week INTEGER, -- Which week/sprint they were contacted
  dm_message_variant TEXT, -- A/B test variant

  -- Response tracking
  responded BOOLEAN DEFAULT FALSE,
  response_date DATE,
  response_text TEXT,

  -- Signup tracking
  signed_up BOOLEAN DEFAULT FALSE,
  signup_date DATE,
  signup_source TEXT, -- 'dm', 'linkedin_post', 'referral', etc.

  -- Engagement tracking
  module_1_complete BOOLEAN DEFAULT FALSE,
  module_1_complete_date DATE,
  engagement_score INTEGER DEFAULT 0, -- 0-100 based on activity

  -- Conversion tracking
  converted_paid BOOLEAN DEFAULT FALSE,
  conversion_date DATE,
  plan TEXT, -- '49_monthly', '99_monthly', '299_lifetime'
  ltv_eur DECIMAL(10,2), -- Lifetime value

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for fast querying
CREATE INDEX idx_total_score ON linkedin_connections(total_score DESC);
CREATE INDEX idx_segment ON linkedin_connections(segment);
CREATE INDEX idx_campaign_tracking ON linkedin_connections(campaign_sent, responded, signed_up);
CREATE INDEX idx_conversion ON linkedin_connections(converted_paid);
CREATE INDEX idx_segment_score ON linkedin_connections(segment, total_score DESC);

-- Updated_at trigger
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_linkedin_connections_updated_at BEFORE UPDATE
    ON linkedin_connections FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Segment performance tracking table
CREATE TABLE segment_performance (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  segment TEXT NOT NULL,
  week INTEGER NOT NULL,
  campaign_name TEXT,

  -- Volume metrics
  dms_sent INTEGER DEFAULT 0,
  responses INTEGER DEFAULT 0,
  signups INTEGER DEFAULT 0,
  module_1_completions INTEGER DEFAULT 0,
  conversions INTEGER DEFAULT 0,

  -- Rate metrics (auto-calculated)
  response_rate DECIMAL(5,2),
  signup_rate DECIMAL(5,2),
  completion_rate DECIMAL(5,2),
  conversion_rate DECIMAL(5,2),

  -- Revenue metrics
  mrr_generated DECIMAL(10,2),
  total_ltv DECIMAL(10,2),

  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),

  UNIQUE(segment, week)
);

-- Index
CREATE INDEX idx_segment_week ON segment_performance(segment, week);

-- Updated_at trigger for segment_performance
CREATE TRIGGER update_segment_performance_updated_at BEFORE UPDATE
    ON segment_performance FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Scoring weights table (for Bayesian updates)
CREATE TABLE scoring_weights (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  version INTEGER NOT NULL UNIQUE,
  segment TEXT NOT NULL,

  -- Weights (should sum to 1.0)
  seniority_weight DECIMAL(3,2) CHECK (seniority_weight >= 0 AND seniority_weight <= 1),
  position_weight DECIMAL(3,2) CHECK (position_weight >= 0 AND position_weight <= 1),
  company_weight DECIMAL(3,2) CHECK (company_weight >= 0 AND company_weight <= 1),
  recency_weight DECIMAL(3,2) CHECK (recency_weight >= 0 AND recency_weight <= 1),
  email_weight DECIMAL(3,2) CHECK (email_weight >= 0 AND email_weight <= 1),

  -- Performance data
  tested_on_count INTEGER DEFAULT 0,
  conversion_rate DECIMAL(5,2),

  -- Metadata
  notes TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Initial weights (v1.0)
INSERT INTO scoring_weights (version, segment, seniority_weight, position_weight, company_weight, recency_weight, email_weight, notes)
VALUES
  (1, 'agency', 0.30, 0.25, 0.20, 0.15, 0.10, 'Initial weights based on hypothesis'),
  (1, 'founder', 0.30, 0.25, 0.20, 0.15, 0.10, 'Initial weights based on hypothesis'),
  (1, 'corporate', 0.30, 0.25, 0.20, 0.15, 0.10, 'Initial weights based on hypothesis');

-- View: Top 50 per segment
CREATE OR REPLACE VIEW top_50_per_segment AS
WITH ranked AS (
  SELECT
    *,
    ROW_NUMBER() OVER (PARTITION BY segment ORDER BY total_score DESC) as rank
  FROM linkedin_connections
)
SELECT * FROM ranked WHERE rank <= 50;

-- View: Campaign dashboard
CREATE OR REPLACE VIEW campaign_dashboard AS
SELECT
  segment,
  COUNT(*) FILTER (WHERE campaign_sent = TRUE) as dms_sent,
  COUNT(*) FILTER (WHERE responded = TRUE) as responses,
  COUNT(*) FILTER (WHERE signed_up = TRUE) as signups,
  COUNT(*) FILTER (WHERE module_1_complete = TRUE) as completions,
  COUNT(*) FILTER (WHERE converted_paid = TRUE) as conversions,
  ROUND(COUNT(*) FILTER (WHERE responded = TRUE)::DECIMAL / NULLIF(COUNT(*) FILTER (WHERE campaign_sent = TRUE), 0) * 100, 2) as response_rate,
  ROUND(COUNT(*) FILTER (WHERE converted_paid = TRUE)::DECIMAL / NULLIF(COUNT(*) FILTER (WHERE campaign_sent = TRUE), 0) * 100, 2) as conversion_rate,
  SUM(ltv_eur) as total_ltv
FROM linkedin_connections
WHERE campaign_sent = TRUE
GROUP BY segment;

-- Function: Calculate expected value for a connection
CREATE OR REPLACE FUNCTION calculate_expected_value(
  p_total_score DECIMAL,
  p_ltv DECIMAL DEFAULT 588 -- €49/mo * 12 months
)
RETURNS DECIMAL AS $$
DECLARE
  conversion_prob DECIMAL;
BEGIN
  -- Convert score (0-100) to probability (0-1)
  -- Assumption: 90+ score = 20% conversion, linear down to 60 score = 4%
  IF p_total_score >= 90 THEN
    conversion_prob := 0.20;
  ELSIF p_total_score >= 80 THEN
    conversion_prob := 0.12;
  ELSIF p_total_score >= 70 THEN
    conversion_prob := 0.08;
  ELSIF p_total_score >= 60 THEN
    conversion_prob := 0.04;
  ELSE
    conversion_prob := 0.02;
  END IF;

  RETURN conversion_prob * p_ltv;
END;
$$ LANGUAGE plpgsql;

-- Comments for documentation
COMMENT ON TABLE linkedin_connections IS 'Main data warehouse for LinkedIn connections with scoring and campaign tracking';
COMMENT ON TABLE segment_performance IS 'Aggregated performance metrics per segment and week for A/B testing';
COMMENT ON TABLE scoring_weights IS 'Versioned scoring weights for Bayesian updates';
COMMENT ON COLUMN linkedin_connections.total_score IS 'Weighted total score (0-100) indicating conversion probability';
COMMENT ON COLUMN linkedin_connections.segment IS 'Target segment: agency (growth operators), founder (entrepreneurs), corporate (marketers)';
COMMENT ON FUNCTION calculate_expected_value IS 'Calculate expected value (EV) based on score and LTV';
