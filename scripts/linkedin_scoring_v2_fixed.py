"""
LinkedIn ICP Scoring V2.1 - Fixed Classification Logic

Fixes from V2.0:
1. Italian name + Italian company = Italy (simple, effective)
2. "Fondatore" = Founder segment (not agency)
3. Founder titles get proper seniority scores (100, not 20)
4. Job title relevance is primary filter
5. Output files deliver promised counts (100 = 100 rows)
"""

import csv
import re
from datetime import datetime
from typing import Dict, Optional, List
from collections import defaultdict
import os


class LinkedInScorerV2Fixed:
    """ICP Scoring Engine V2.1 - Fixed Logic"""

    # Italian detection patterns
    ITALIAN_NAME_ENDINGS = r'(a|o|i|e)$'
    ITALIAN_COMMON_NAMES = r'(matteo|luca|francesco|giovanni|andrea|marco|alessandro|davide|giuseppe|antonio|pietro|giorgio|roberto|paolo|stefano|federico|lorenzo|valentino|leonardo|michele|giulia|chiara|francesca|alessia|sara|martina|elena|valentina|giorgia|silvia|elisa|anna|federica|laura|beatrice|alice|caterina|claudia|barbara|serena|maria|nicola|simone|filippo|daniele|cristian|fabio|massimo|riccardo|tommaso|gabriele|enrico|emanuele|vincenzo|giacomo|alberto|diego|manuel|ivan|alessio|edoardo|samuel|christian|mirko|michele)'

    ITALIAN_COMPANY_KEYWORDS = r'(srl|spa|s\.r\.l\.|s\.p\.a\.|società|societa|gruppo|pallacanestro|pallavolo|calcio|serie\s?[abcd]|lega\s?pro|basket|volley|reggiana|bologna|milano|roma|torino|napoli|firenze|venezia|genova|verona|brescia|parma|modena|bergamo|vicenza|treviso|padova|rimini|forlì|prato|livorno|perugia|foggia|salerno|ravenna|pescara|trieste|lecce|siena|pisa|lucca|como|cremona|mantova|pavia|asti|cuneo|biella|vercelli|novara|alessandria|cantucci|vin santo|vino|pasta|pizza|risotto|gelato|tiramisu|parmigiano|prosciutto|chianti|barolo|brunello|prosecco|amarone|juventus|inter|milan|napoli|lazio|ferrari|lamborghini|maserati|alfa romeo|fiat|armani|versace|prada|gucci|dolce|gabbana|valentino|fendi)'

    # Seniority patterns
    SENIORITY_PATTERNS = {
        # Founders (Italian + English)
        r'(founder|co-?founder|ceo|chief executive|cxo|fondatore|cofondatore|socio fondatore|amministratore delegato|\bad\b)': 100,
        # Top executives
        r'(managing partner|general partner|chairman|president|owner|proprietario)': 95,
        # Senior management
        r'(vp|vice president|director|head of|chief|direttore|responsabile)': 80,
        # Middle management
        r'(manager|lead|coordinator|supervisor|capo)': 60,
        # Junior roles
        r'(specialist|analyst|associate|coordinator|assistant)': 40,
    }

    # Position fit patterns by segment
    POSITION_PATTERNS_AGENCY = {
        r'(growth|marketing|digital|performance|acquisition|seo|sem|ads|campaign)': 100,
        r'(sales|business development|bd|revenue|commercial)': 85,
        r'(product|strategy|consulting|consultant)': 70,
        r'(operations|project|program)': 50,
    }

    POSITION_PATTERNS_FOUNDER = {
        r'(founder|ceo|entrepreneur|chief executive|fondatore|cofondatore)': 100,
        r'(co-?founder|founding|startup)': 100,
        r'(cto|chief technology|product|chief product)': 80,
    }

    POSITION_PATTERNS_CORPORATE = {
        r'(marketing|growth|digital|performance|brand)': 100,
        r'(content|social|community|communication)': 85,
        r'(sales|partnerships|alliances|business development)': 70,
    }

    COMPANY_PATTERNS = {
        r'(saas|software|platform|app|tech|technology|ai|ml|data)': 100,
        r'(agency|consulting|services|studio|consultant)': 95,
        r'(venture|capital|vc|fund|investment|accelerator)': 90,
        r'(startup|scale.?up)': 85,
        r'(google|amazon|microsoft|meta|apple|facebook)': 70,
        r'(sme|small business)': 50,
        r'(freelance|self.?employed)': 40,
    }

    # Segment detection patterns
    FOUNDER_KEYWORDS = r'(founder|ceo|entrepreneur|co.?founder|chief executive|owner|fondatore|cofondatore|amministratore delegato|\bad\b|proprietario)'
    AGENCY_KEYWORDS = r'(marketing|growth|digital|consultant|agency|freelance|performance|seo|sem)'
    CORPORATE_KEYWORDS = r'(manager|director|head of|coordinator|lead|specialist|analyst)'

    # Out-of-scope job titles (filter these out)
    OUT_OF_SCOPE_KEYWORDS = r'(pricing|legal|lawyer|attorney|counsel|hr\s|human resources|recruiter|recruitment|finance|accounting|accountant|auditor|compliance|risk\s|admin|administrative|assistant\s|secretary|receptionist|logistics|supply chain|warehouse|procurement|purchasing|buyer|facilities|property|real estate|estate\s|insurance|claims|underwriting)'

    def __init__(self):
        self.connections = []
        self.messages_data = {}
        self.invitations_data = {}
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

        message_counts = defaultdict(list)

        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for row in reader:
                sender_url = row.get('SENDER PROFILE URL', '')
                recipient_urls = row.get('RECIPIENT PROFILE URLS', '')
                date_str = row.get('DATE', '')

                if not sender_url:
                    continue

                try:
                    msg_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S UTC")
                except:
                    msg_date = None

                if sender_url:
                    message_counts[sender_url].append((msg_date, 'sent'))

                if recipient_urls:
                    for url in recipient_urls.split(','):
                        url = url.strip()
                        if url:
                            message_counts[url].append((msg_date, 'received'))

        self.messages_data = {}
        for url, messages in message_counts.items():
            message_count = len(messages)
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

                if direction and invitee_url:
                    self.invitations_data[invitee_url] = direction

        print(f"✅ Loaded {len(self.invitations_data)} invitation records")
        return self.invitations_data

    def is_italian_name(self, first_name: str, last_name: str) -> bool:
        """Check if name is Italian"""
        name = f"{first_name} {last_name}".lower()

        # Check common Italian names
        if re.search(self.ITALIAN_COMMON_NAMES, name):
            return True

        # Check typical Italian endings
        if re.search(self.ITALIAN_NAME_ENDINGS, last_name.lower()):
            return True

        return False

    def is_italian_company(self, company: str) -> bool:
        """Check if company is Italian"""
        if not company:
            return False

        company_lower = company.lower()
        return bool(re.search(self.ITALIAN_COMPANY_KEYWORDS, company_lower))

    def detect_geography(self, connection: Dict) -> str:
        """
        Detect if contact is Italian or International
        Rule: Italian name = Italy (name is primary signal)
        """
        first_name = connection.get('First Name', '')
        last_name = connection.get('Last Name', '')

        # Primary rule: Italian name = Italy (regardless of company)
        if self.is_italian_name(first_name, last_name):
            return 'italy'

        # Secondary: Check company if name isn't Italian
        company = connection.get('Company', '')
        if self.is_italian_company(company):
            return 'italy'

        return 'international'

    def determine_segment(self, position: str) -> str:
        """
        Determine segment based on position
        Priority: Founder > Agency > Corporate
        """
        if not position:
            return 'agency'  # Default

        position_lower = position.lower()

        # Check founder first (highest priority)
        if re.search(self.FOUNDER_KEYWORDS, position_lower):
            return 'founder'

        # Then agency
        if re.search(self.AGENCY_KEYWORDS, position_lower):
            return 'agency'

        # Then corporate
        if re.search(self.CORPORATE_KEYWORDS, position_lower):
            return 'corporate'

        # Default
        return 'agency'

    def match_patterns(self, text: str, patterns: Dict[str, int], default: int = 20) -> int:
        """Match text against regex patterns and return highest score"""
        if not text:
            return default

        text = text.lower()
        scores = [score for pattern, score in patterns.items() if re.search(pattern, text)]
        return max(scores) if scores else default

    def calculate_static_score(self, connection: Dict, segment: str) -> Dict:
        """Calculate V2.1 static score"""
        position = connection.get('Position', '')
        company = connection.get('Company', '')

        # 1. Seniority Score (40%)
        seniority_score = self.match_patterns(position, self.SENIORITY_PATTERNS, default=20)

        # 2. Position Fit Score (35%)
        if segment == 'founder':
            position_patterns = self.POSITION_PATTERNS_FOUNDER
        elif segment == 'agency':
            position_patterns = self.POSITION_PATTERNS_AGENCY
        else:
            position_patterns = self.POSITION_PATTERNS_CORPORATE

        position_score = self.match_patterns(position, position_patterns, default=20)

        # 3. Company Type Score (25%)
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
        """Calculate engagement score"""
        url = connection.get('URL', '')

        msg_stats = self.messages_data.get(url, {})
        message_count = msg_stats.get('message_count', 0)
        last_message_date = msg_stats.get('last_message_date')

        direction = self.invitations_data.get(url, 'UNKNOWN')
        email = connection.get('Email Address', '')

        # 1. Message Volume (40%)
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

        # 2. Direction (30%)
        if direction == 'INCOMING':
            direction_score = 100
        elif direction == 'OUTGOING' and message_count > 0:
            direction_score = 60
        elif direction == 'OUTGOING' and message_count == 0:
            direction_score = 20
        else:
            direction_score = 50

        # 3. Conversation Recency (20%)
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
            conversation_recency_score = 10

        # 4. Email (10%)
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

    def is_out_of_scope(self, position: str) -> bool:
        """Check if position is out of scope (not marketing/growth/founder)"""
        if not position:
            return False

        position_lower = position.lower()
        return bool(re.search(self.OUT_OF_SCOPE_KEYWORDS, position_lower))

    def score_connection(self, connection: Dict) -> Dict:
        """V2.1 Complete Scoring"""

        # Check if out of scope first
        position = connection.get('Position', '')
        if self.is_out_of_scope(position):
            # Mark as out of scope with low scores
            return {
                **connection,
                'segment': 'out_of_scope',
                'geography': 'unknown',
                'engagement_level': 'low',
                'total_score_v2': 0.0,
                'static_score': 0.0,
                'engagement_score': 0.0,
                'seniority_score': 0,
                'position_score': 0,
                'company_score': 0,
                'message_count': 0,
                'direction': 'UNKNOWN',
                'last_message_date': None,
                'message_volume_score': 0,
                'direction_score': 0,
                'conversation_recency_score': 0,
                'email_score': 0,
            }

        # Determine segment first
        segment = self.determine_segment(position)

        # Calculate scores
        static_data = self.calculate_static_score(connection, segment)
        engagement_data = self.calculate_engagement_score(connection)

        # V2.1 Total Score
        total_score = (
            static_data['static_score'] * 0.60 +
            engagement_data['engagement_score'] * 0.40
        )

        # Detect geography
        geography = self.detect_geography(connection)

        # Engagement level
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
        """Score all connections with V2.1 logic"""
        print(f"\n🧮 Scoring {len(self.connections)} connections (V2.1)...")

        for connection in self.connections:
            scored = self.score_connection(connection)
            self.scored_connections.append(scored)

        print(f"✅ Scored all connections")

        # Stats
        segments = defaultdict(int)
        geographies = defaultdict(int)
        engagement_levels = defaultdict(int)

        # Filter out out-of-scope
        self.scored_connections = [c for c in self.scored_connections if c['segment'] != 'out_of_scope']

        print(f"✅ Kept {len(self.scored_connections)} in-scope connections")

        for conn in self.scored_connections:
            segments[conn['segment']] += 1
            geographies[conn['geography']] += 1
            engagement_levels[conn['engagement_level']] += 1

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

    def export_top_lists(self, output_dir: str = 'outputs'):
        """Export top 50 Italy + top 100 International"""
        os.makedirs(output_dir, exist_ok=True)

        fieldnames = [
            'First Name', 'Last Name', 'URL', 'Email Address', 'Company', 'Position', 'Connected On',
            'segment', 'geography', 'engagement_level',
            'total_score_v2', 'static_score', 'engagement_score',
            'seniority_score', 'position_score', 'company_score',
            'message_count', 'direction', 'last_message_date'
        ]

        # Group by geography
        italy_contacts = [c for c in self.scored_connections if c['geography'] == 'italy']
        international_contacts = [c for c in self.scored_connections if c['geography'] == 'international']

        print(f"\n💾 Exporting top lists...")
        print(f"   Total Italy: {len(italy_contacts)}")
        print(f"   Total International: {len(international_contacts)}")

        # Italy Top 50
        italy_sorted = sorted(italy_contacts, key=lambda x: x['total_score_v2'], reverse=True)
        italy_top_50 = italy_sorted[:50]

        filename = f"{output_dir}/italy_top_50.csv"
        print(f"   → {filename} ({len(italy_top_50)} contacts)")

        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(italy_top_50)

        # International Top 100
        intl_sorted = sorted(international_contacts, key=lambda x: x['total_score_v2'], reverse=True)
        intl_top_100 = intl_sorted[:100]

        filename = f"{output_dir}/international_top_100.csv"
        print(f"   → {filename} ({len(intl_top_100)} contacts)")

        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(intl_top_100)

        print(f"\n✅ Export complete!")

    def export_full_dataset(self, output_dir: str = 'outputs'):
        """Export complete scored dataset"""
        os.makedirs(output_dir, exist_ok=True)

        filename = f"{output_dir}/linkedin_connections_scored_v2.1_complete.csv"
        print(f"\n💾 Exporting full dataset to {filename}...")

        fieldnames = [
            'First Name', 'Last Name', 'URL', 'Email Address', 'Company', 'Position', 'Connected On',
            'segment', 'geography', 'engagement_level',
            'total_score_v2', 'static_score', 'engagement_score',
            'seniority_score', 'position_score', 'company_score',
            'message_count', 'direction', 'last_message_date',
            'message_volume_score', 'direction_score', 'conversation_recency_score', 'email_score'
        ]

        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(self.scored_connections)

        print(f"✅ Exported {len(self.scored_connections)} connections")


def main():
    """Main execution"""
    print("🚀 LinkedIn ICP Scoring Engine V2.1 - Fixed Classification\n")

    scorer = LinkedInScorerV2Fixed()

    base_path = '/Users/matteolombardi/AI-Projects/stratega/assets/LinkedIn data'
    scorer.load_connections(f'{base_path}/Connections.csv')
    scorer.load_messages(f'{base_path}/messages.csv')
    scorer.load_invitations(f'{base_path}/Invitations.csv')

    scorer.score_all_connections()

    output_dir = '/Users/matteolombardi/AI-Projects/stratega/outputs/linkedin_scoring_v2.1_final'
    scorer.export_full_dataset(output_dir)
    scorer.export_top_lists(output_dir)

    print("\n✅ V2.1 scoring complete!")
    print(f"\n📌 Key files:")
    print(f"   - italy_top_50.csv (50 best Italian contacts)")
    print(f"   - international_top_100.csv (100 best international contacts)")


if __name__ == '__main__':
    main()
