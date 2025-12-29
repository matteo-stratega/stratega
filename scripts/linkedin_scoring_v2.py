"""
LinkedIn ICP Scoring V2.0 - Engagement-Based Refinement
Fixes recency bias + adds real engagement signals + geographic split

Key improvements over V1.0:
- Parses message history to calculate engagement score
- Uses INCOMING/OUTGOING direction from invitations
- Penalizes cold campaigns (recent + no engagement)
- Splits Italy vs International for targeted messaging
"""

import csv
import re
from datetime import datetime
from typing import Dict, Optional, List
from collections import defaultdict
import os


class LinkedInScorerV2:
    """ICP Scoring Engine V2.0 with Engagement Data"""

    # Scoring patterns (regex) - inherited from V1.0
    SENIORITY_PATTERNS = {
        r'(founder|co-founder|ceo|chief executive|cxo)': 100,
        r'(managing partner|general partner|chairman|board member)': 95,
        r'(vp|vice president|director|head of|chief)': 80,
        r'(manager|lead|coordinator|supervisor)': 60,
        r'(specialist|analyst|associate|coordinator)': 40,
    }

    POSITION_PATTERNS_AGENCY = {
        r'(growth|marketing|digital|performance|acquisition)': 100,
        r'(sales|business development|bd|revenue)': 85,
        r'(product|strategy|consulting)': 70,
        r'(operations|project|program)': 50,
    }

    POSITION_PATTERNS_FOUNDER = {
        r'(founder|ceo|entrepreneur|chief executive)': 100,
        r'(co-founder|founding|startup)': 100,
        r'(product|cto|chief technology)': 80,
    }

    POSITION_PATTERNS_CORPORATE = {
        r'(marketing|growth|digital|performance)': 100,
        r'(brand|content|social|community)': 85,
        r'(sales|partnerships|alliances)': 70,
    }

    COMPANY_PATTERNS = {
        r'(saas|software|platform|app|tech|technology)': 100,
        r'(agency|consulting|services|studio)': 95,
        r'(venture|capital|vc|fund|investment)': 90,
        r'(startup|scale.?up)': 85,
        r'(google|amazon|microsoft|meta|apple)': 70,
        r'(sme|small business)': 50,
        r'(freelance|self.?employed|consultant)': 40,
    }

    SEGMENT_PATTERNS = {
        'agency': r'(marketing|growth|digital|agency|consultant|freelance)',
        'founder': r'(founder|ceo|entrepreneur|co.?founder|chief executive)',
        'corporate': r'(marketing|brand|content|manager|director)',
    }

    # Italian language indicators for geography detection
    ITALIAN_POSITION_KEYWORDS = r'(amministratore|direttore|responsabile|capo|fondatore|socio|srl|spa)'
    ITALIAN_COMPANY_KEYWORDS = r'(\.it|srl|spa|società|s\.r\.l\.|s\.p\.a\.)'

    def __init__(self):
        self.connections = []
        self.messages_data = {}  # Profile URL -> message stats
        self.invitations_data = {}  # Profile URL -> direction
        self.scored_connections = []

    def load_connections(self, filepath: str):
        """Load LinkedIn connections CSV"""
        print(f"📂 Loading connections from {filepath}...")

        with open(filepath, 'r', encoding='utf-8') as f:
            # Skip notes header (first 3 lines)
            for _ in range(3):
                next(f)

            reader = csv.DictReader(f)
            self.connections = list(reader)

        print(f"✅ Loaded {len(self.connections)} connections")
        return self.connections

    def load_messages(self, filepath: str):
        """Parse messages.csv to extract engagement metrics per person"""
        print(f"📨 Loading messages from {filepath}...")

        message_counts = defaultdict(list)  # URL -> list of (date, sender)

        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for row in reader:
                sender_url = row.get('SENDER PROFILE URL', '')
                recipient_urls = row.get('RECIPIENT PROFILE URLS', '')
                date_str = row.get('DATE', '')

                if not sender_url:
                    continue

                # Parse date
                try:
                    msg_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S UTC")
                except:
                    msg_date = None

                # Track sender
                if sender_url:
                    message_counts[sender_url].append((msg_date, 'sent'))

                # Track recipients
                if recipient_urls:
                    # LinkedIn sometimes has multiple recipient URLs
                    for url in recipient_urls.split(','):
                        url = url.strip()
                        if url:
                            message_counts[url].append((msg_date, 'received'))

        # Calculate stats per person
        self.messages_data = {}
        for url, messages in message_counts.items():
            # Count total messages
            message_count = len(messages)

            # Find last message date
            dates = [m[0] for m in messages if m[0]]
            last_message_date = max(dates) if dates else None

            self.messages_data[url] = {
                'message_count': message_count,
                'last_message_date': last_message_date,
            }

        print(f"✅ Processed {len(self.messages_data)} contacts with message history")
        return self.messages_data

    def load_invitations(self, filepath: str):
        """Parse Invitations.csv to get connection direction"""
        print(f"📬 Loading invitations from {filepath}...")

        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for row in reader:
                direction = row.get('Direction', '')
                invitee_url = row.get('inviteeProfileUrl', '')
                inviter_url = row.get('inviterProfileUrl', '')

                # Map invitee URL to direction
                if direction and invitee_url:
                    self.invitations_data[invitee_url] = direction

        print(f"✅ Loaded {len(self.invitations_data)} invitation records")
        return self.invitations_data

    def match_patterns(self, text: str, patterns: Dict[str, int], default: int = 20) -> int:
        """Match text against regex patterns and return highest score"""
        if not text:
            return default

        text = text.lower()
        scores = [score for pattern, score in patterns.items() if re.search(pattern, text)]
        return max(scores) if scores else default

    def determine_segment(self, position: str) -> Optional[str]:
        """Determine which segment this connection belongs to"""
        if not position:
            return None

        position_lower = position.lower()

        # Check each segment pattern
        for segment, pattern in self.SEGMENT_PATTERNS.items():
            if re.search(pattern, position_lower):
                return segment

        return None

    def detect_geography(self, connection: Dict) -> str:
        """Detect if contact is Italian or International"""
        position = connection.get('Position', '').lower()
        company = connection.get('Company', '').lower()
        name = f"{connection.get('First Name', '')} {connection.get('Last Name', '')}".lower()

        # Check Italian indicators
        italian_indicators = 0

        # 1. Italian position keywords
        if re.search(self.ITALIAN_POSITION_KEYWORDS, position):
            italian_indicators += 2

        # 2. Italian company keywords
        if re.search(self.ITALIAN_COMPANY_KEYWORDS, company):
            italian_indicators += 2

        # 3. Italian name heuristic (ends with vowel + common patterns)
        italian_name_pattern = r'(francesco|matteo|giovanni|luca|andrea|marco|alessandro|davide|giuseppe|antonio|pietro|giorgio|roberto|paolo|stefano|federico|lorenzo|valentino|leonardo|michele|giulia|chiara|francesca|alessia|sara|martina|elena|valentina|giorgia|silvia|elisa|anna|federica|laura|beatrice|alice|caterina|claudia|barbara|serena|maria)'
        if re.search(italian_name_pattern, name):
            italian_indicators += 1

        # Threshold: 2+ indicators = Italy
        return 'italy' if italian_indicators >= 2 else 'international'

    def calculate_static_score(self, connection: Dict, segment: str) -> Dict:
        """Calculate V2.0 static score (profile fit only, no recency/email)"""
        position = connection.get('Position', '')
        company = connection.get('Company', '')

        # 1. Seniority Score (40% of static)
        seniority_score = self.match_patterns(position, self.SENIORITY_PATTERNS, default=20)

        # 2. Position Fit Score (35% of static)
        if segment == 'agency':
            position_patterns = self.POSITION_PATTERNS_AGENCY
        elif segment == 'founder':
            position_patterns = self.POSITION_PATTERNS_FOUNDER
        else:
            position_patterns = self.POSITION_PATTERNS_CORPORATE

        position_score = self.match_patterns(position, position_patterns, default=20)

        # 3. Company Type Score (25% of static)
        company_score = self.match_patterns(company, self.COMPANY_PATTERNS, default=40)

        # Weighted static score
        static_score = (
            seniority_score * 0.40 +
            position_score * 0.35 +
            company_score * 0.25
        )

        return {
            'static_score': round(static_score, 2),
            'seniority_score': seniority_score,
            'position_score': position_score,
            'company_score': company_score,
        }

    def calculate_engagement_score(self, connection: Dict) -> Dict:
        """Calculate V2.0 engagement score (NEW)"""
        url = connection.get('URL', '')

        # Get message stats
        msg_stats = self.messages_data.get(url, {})
        message_count = msg_stats.get('message_count', 0)
        last_message_date = msg_stats.get('last_message_date')

        # Get invitation direction
        direction = self.invitations_data.get(url, 'UNKNOWN')

        # Get email
        email = connection.get('Email Address', '')

        # 1. Message Volume Score (40% of engagement)
        if message_count == 0:
            message_volume_score = 0
        elif message_count <= 2:
            message_volume_score = 20
        elif message_count <= 5:
            message_volume_score = 40
        elif message_count <= 10:
            message_volume_score = 60
        elif message_count <= 20:
            message_volume_score = 80
        else:
            message_volume_score = 100

        # 2. Connection Direction Score (30% of engagement)
        if direction == 'INCOMING':
            direction_score = 100  # They reached out
        elif direction == 'OUTGOING' and message_count > 0:
            direction_score = 60  # You reached out, they replied
        elif direction == 'OUTGOING' and message_count == 0:
            direction_score = 20  # Cold campaign, no reply
        else:
            direction_score = 50  # Unknown

        # 3. Conversation Recency Score (20% of engagement)
        if last_message_date:
            days_since = (datetime.now() - last_message_date).days

            if days_since <= 30:
                conversation_recency_score = 100
            elif days_since <= 90:
                conversation_recency_score = 80
            elif days_since <= 180:
                conversation_recency_score = 60
            elif days_since <= 365:
                conversation_recency_score = 40
            elif days_since <= 730:
                conversation_recency_score = 20
            else:
                conversation_recency_score = 10
        else:
            # Never messaged
            conversation_recency_score = 10

        # 4. Email Availability Score (10% of engagement)
        email_score = 100 if email and '@' in email else 0

        # Weighted engagement score
        engagement_score = (
            message_volume_score * 0.40 +
            direction_score * 0.30 +
            conversation_recency_score * 0.20 +
            email_score * 0.10
        )

        return {
            'engagement_score': round(engagement_score, 2),
            'message_count': message_count,
            'direction': direction,
            'last_message_date': last_message_date.strftime('%Y-%m-%d') if last_message_date else None,
            'message_volume_score': message_volume_score,
            'direction_score': direction_score,
            'conversation_recency_score': conversation_recency_score,
            'email_score': email_score,
        }

    def score_connection_v2(self, connection: Dict, segment: str) -> Dict:
        """V2.0 Complete Scoring: Static + Engagement"""

        # Calculate static score (profile fit)
        static_data = self.calculate_static_score(connection, segment)

        # Calculate engagement score (relationship warmth)
        engagement_data = self.calculate_engagement_score(connection)

        # V2.0 Total Score
        total_score = (
            static_data['static_score'] * 0.60 +
            engagement_data['engagement_score'] * 0.40
        )

        # Detect geography
        geography = self.detect_geography(connection)

        # Determine engagement level (for segmentation)
        engagement_level = 'high' if engagement_data['engagement_score'] >= 60 else 'low'

        return {
            **connection,
            'segment': segment,
            'geography': geography,
            'engagement_level': engagement_level,
            'total_score_v2': round(total_score, 2),
            **static_data,
            **engagement_data,
        }

    def score_all_connections(self):
        """Score all connections with V2.0 logic"""
        print(f"\n🧮 Scoring {len(self.connections)} connections (V2.0)...")

        for connection in self.connections:
            # Determine segment
            segment = self.determine_segment(connection.get('Position', ''))

            if not segment:
                # Default to agency if no match
                segment = 'agency'

            # Score with V2.0 logic
            scored = self.score_connection_v2(connection, segment)
            self.scored_connections.append(scored)

        print(f"✅ Scored all connections")

        # Stats
        segments = {}
        geographies = {}
        engagement_levels = {}

        for conn in self.scored_connections:
            seg = conn['segment']
            geo = conn['geography']
            eng = conn['engagement_level']

            segments[seg] = segments.get(seg, 0) + 1
            geographies[geo] = geographies.get(geo, 0) + 1
            engagement_levels[eng] = engagement_levels.get(eng, 0) + 1

        print(f"\n📊 Distribution:")
        print(f"   Segments:")
        for seg, count in sorted(segments.items(), key=lambda x: x[1], reverse=True):
            print(f"      {seg}: {count} ({count/len(self.scored_connections)*100:.1f}%)")

        print(f"   Geography:")
        for geo, count in sorted(geographies.items(), key=lambda x: x[1], reverse=True):
            print(f"      {geo}: {count} ({count/len(self.scored_connections)*100:.1f}%)")

        print(f"   Engagement:")
        for eng, count in sorted(engagement_levels.items(), key=lambda x: x[1], reverse=True):
            print(f"      {eng}: {count} ({count/len(self.scored_connections)*100:.1f}%)")

        return self.scored_connections

    def get_top_n_per_tier(self, n: int = 50):
        """Get top N scored connections per tier (geography × engagement × segment)"""
        print(f"\n🎯 Extracting top {n} per tier...")

        # Group by tier
        tiers = defaultdict(list)

        for conn in self.scored_connections:
            geography = conn['geography']
            engagement = conn['engagement_level']
            segment = conn['segment']

            tier_key = f"{geography}_{engagement}_{segment}"
            tiers[tier_key].append(conn)

        # Sort and extract top N per tier
        top_per_tier = {}
        for tier_key, conns in tiers.items():
            sorted_conns = sorted(conns, key=lambda x: x['total_score_v2'], reverse=True)
            top_per_tier[tier_key] = sorted_conns[:n]

            if sorted_conns:
                print(f"   {tier_key}: {len(sorted_conns)} total, top score: {sorted_conns[0]['total_score_v2']}")

        return top_per_tier

    def export_to_csv(self, output_dir: str = 'outputs'):
        """Export V2.0 scored connections to CSV"""
        os.makedirs(output_dir, exist_ok=True)

        # All scored connections
        all_output = f"{output_dir}/linkedin_connections_scored_v2.csv"
        print(f"\n💾 Exporting all scored connections (V2.0) to {all_output}...")

        fieldnames = [
            'First Name', 'Last Name', 'URL', 'Email Address', 'Company', 'Position', 'Connected On',
            'segment', 'geography', 'engagement_level',
            'total_score_v2', 'static_score', 'engagement_score',
            'seniority_score', 'position_score', 'company_score',
            'message_count', 'direction', 'last_message_date',
            'message_volume_score', 'direction_score', 'conversation_recency_score', 'email_score'
        ]

        with open(all_output, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(self.scored_connections)

        print(f"✅ Exported {len(self.scored_connections)} connections")

        # Top 50 per tier
        print(f"\n💾 Exporting top 50 per tier...")
        top_per_tier = self.get_top_n_per_tier(50)

        for tier_key, conns in top_per_tier.items():
            tier_output = f"{output_dir}/top_50_{tier_key}.csv"
            print(f"   → {tier_output}")

            with open(tier_output, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
                writer.writeheader()
                writer.writerows(conns)

        # Priority segments (Italy high engagement)
        print(f"\n💾 Exporting priority segments...")

        # Tier 1: Italy - High Engagement (all segments combined)
        italy_high = [c for c in self.scored_connections
                      if c['geography'] == 'italy' and c['engagement_level'] == 'high']
        italy_high_sorted = sorted(italy_high, key=lambda x: x['total_score_v2'], reverse=True)[:100]

        tier1_output = f"{output_dir}/TIER1_italy_high_engagement_top100.csv"
        with open(tier1_output, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(italy_high_sorted)
        print(f"   → TIER 1: {len(italy_high_sorted)} Italy high-engagement contacts")

        # Tier 2: International - High Engagement
        intl_high = [c for c in self.scored_connections
                     if c['geography'] == 'international' and c['engagement_level'] == 'high']
        intl_high_sorted = sorted(intl_high, key=lambda x: x['total_score_v2'], reverse=True)[:100]

        tier2_output = f"{output_dir}/TIER2_international_high_engagement_top100.csv"
        with open(tier2_output, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(intl_high_sorted)
        print(f"   → TIER 2: {len(intl_high_sorted)} International high-engagement contacts")

        print(f"\n✅ Export complete! Check {output_dir}/ for files.")


def main():
    """Main execution"""
    print("🚀 LinkedIn ICP Scoring Engine V2.0 - Engagement-Based\n")

    # Initialize scorer
    scorer = LinkedInScorerV2()

    # Load connections
    base_path = '/Users/matteolombardi/AI-Projects/stratega/assets/LinkedIn data'
    scorer.load_connections(f'{base_path}/Connections.csv')

    # Load engagement data
    scorer.load_messages(f'{base_path}/messages.csv')
    scorer.load_invitations(f'{base_path}/Invitations.csv')

    # Score all with V2.0 logic
    scorer.score_all_connections()

    # Export to CSV
    output_dir = '/Users/matteolombardi/AI-Projects/stratega/outputs/linkedin_scoring_v2'
    scorer.export_to_csv(output_dir)

    print("\n✅ V2.0 scoring complete! Check outputs/linkedin_scoring_v2/ for results.")
    print("\n📌 Priority files:")
    print("   - TIER1_italy_high_engagement_top100.csv (WARMEST - start here)")
    print("   - TIER2_international_high_engagement_top100.csv")


if __name__ == '__main__':
    main()
