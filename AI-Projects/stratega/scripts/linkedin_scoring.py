"""
LinkedIn ICP Scoring & Segmentation
Game Theory Model Implementation

Scores 4,715 LinkedIn connections and populates Supabase data warehouse.
"""

import csv
import re
from datetime import datetime
from typing import Dict, Optional
import os

# Supabase client (install: pip install supabase)
try:
    from supabase import create_client, Client
    SUPABASE_AVAILABLE = True
except ImportError:
    print("⚠️  Supabase not installed. Run: pip install supabase")
    SUPABASE_AVAILABLE = False


class LinkedInScorer:
    """ICP Scoring Engine"""

    # Scoring patterns (regex)
    SENIORITY_PATTERNS = {
        r'(founder|co-founder|ceo|chief executive|cxo)': 100,
        r'(managing partner|general partner|chairman|board member)': 95,
        r'(vp|vice president|director|head of|chief)': 80,
        r'(manager|lead|coordinator|supervisor)': 60,
        r'(specialist|analyst|associate|coordinator)': 40,
    }

    # Position fit patterns (varies by segment)
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

    def __init__(self):
        self.connections = []
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

    def match_patterns(self, text: str, patterns: Dict[str, int], default: int = 20) -> int:
        """Match text against regex patterns and return highest score"""
        if not text:
            return default

        text = text.lower()
        scores = [score for pattern, score in patterns.items() if re.search(pattern, text)]
        return max(scores) if scores else default

    def calculate_recency_score(self, connected_on: str) -> int:
        """Calculate recency score based on connection date"""
        try:
            # Parse date (format: "DD Mon YYYY")
            date = datetime.strptime(connected_on, "%d %b %Y")
            days_since = (datetime.now() - date).days

            if days_since <= 30:
                return 100
            elif days_since <= 90:
                return 80
            elif days_since <= 180:
                return 60
            elif days_since <= 365:
                return 40
            elif days_since <= 730:
                return 25
            else:
                return 10
        except:
            # If parsing fails, assume old connection
            return 20

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

    def score_connection(self, connection: Dict, segment: str = 'agency') -> Dict:
        """Score a single connection"""

        position = connection.get('Position', '')
        company = connection.get('Company', '')
        connected_on = connection.get('Connected On', '')
        email = connection.get('Email Address', '')

        # 1. Seniority Score (30%)
        seniority_score = self.match_patterns(position, self.SENIORITY_PATTERNS, default=20)

        # 2. Position Fit Score (25%) - segment-specific
        if segment == 'agency':
            position_patterns = self.POSITION_PATTERNS_AGENCY
        elif segment == 'founder':
            position_patterns = self.POSITION_PATTERNS_FOUNDER
        else:
            position_patterns = self.POSITION_PATTERNS_CORPORATE

        position_score = self.match_patterns(position, position_patterns, default=20)

        # 3. Company Type Score (20%)
        company_score = self.match_patterns(company, self.COMPANY_PATTERNS, default=40)

        # 4. Recency Score (15%)
        recency_score = self.calculate_recency_score(connected_on)

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
            **connection,
            'segment': segment,
            'seniority_score': seniority_score,
            'position_score': position_score,
            'company_score': company_score,
            'recency_score': recency_score,
            'email_score': email_score,
            'total_score': round(total_score, 2),
            'breakdown': {
                'seniority': round(seniority_score * 0.30, 2),
                'position': round(position_score * 0.25, 2),
                'company': round(company_score * 0.20, 2),
                'recency': round(recency_score * 0.15, 2),
                'email': round(email_score * 0.10, 2),
            }
        }

    def score_all_connections(self):
        """Score all connections and assign segments"""
        print(f"\n🧮 Scoring {len(self.connections)} connections...")

        for connection in self.connections:
            # Determine segment
            segment = self.determine_segment(connection.get('Position', ''))

            if not segment:
                # Default to agency if no match
                segment = 'agency'

            # Score with segment-specific logic
            scored = self.score_connection(connection, segment)
            self.scored_connections.append(scored)

        print(f"✅ Scored all connections")

        # Stats
        segments = {}
        for conn in self.scored_connections:
            seg = conn['segment']
            segments[seg] = segments.get(seg, 0) + 1

        print(f"\n📊 Segment Distribution:")
        for seg, count in sorted(segments.items(), key=lambda x: x[1], reverse=True):
            print(f"   {seg}: {count} ({count/len(self.scored_connections)*100:.1f}%)")

        return self.scored_connections

    def get_top_n_per_segment(self, n: int = 50):
        """Get top N scored connections per segment"""
        print(f"\n🎯 Extracting top {n} per segment...")

        segments = {}
        for conn in self.scored_connections:
            seg = conn['segment']
            if seg not in segments:
                segments[seg] = []
            segments[seg].append(conn)

        top_per_segment = {}
        for seg, conns in segments.items():
            # Sort by total_score DESC
            sorted_conns = sorted(conns, key=lambda x: x['total_score'], reverse=True)
            top_per_segment[seg] = sorted_conns[:n]
            print(f"   {seg}: {len(top_per_segment[seg])} (top score: {top_per_segment[seg][0]['total_score']})")

        return top_per_segment

    def export_to_csv(self, output_dir: str = 'outputs'):
        """Export scored connections to CSV"""
        os.makedirs(output_dir, exist_ok=True)

        # All scored connections
        all_output = f"{output_dir}/linkedin_connections_scored.csv"
        print(f"\n💾 Exporting all scored connections to {all_output}...")

        fieldnames = [
            'First Name', 'Last Name', 'URL', 'Email Address', 'Company', 'Position', 'Connected On',
            'segment', 'total_score', 'seniority_score', 'position_score', 'company_score', 'recency_score', 'email_score'
        ]

        with open(all_output, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for conn in self.scored_connections:
                writer.writerow({
                    'First Name': conn.get('First Name'),
                    'Last Name': conn.get('Last Name'),
                    'URL': conn.get('URL'),
                    'Email Address': conn.get('Email Address'),
                    'Company': conn.get('Company'),
                    'Position': conn.get('Position'),
                    'Connected On': conn.get('Connected On'),
                    'segment': conn.get('segment'),
                    'total_score': conn.get('total_score'),
                    'seniority_score': conn.get('seniority_score'),
                    'position_score': conn.get('position_score'),
                    'company_score': conn.get('company_score'),
                    'recency_score': conn.get('recency_score'),
                    'email_score': conn.get('email_score'),
                })

        print(f"✅ Exported {len(self.scored_connections)} connections")

        # Top 50 per segment
        top_per_segment = self.get_top_n_per_segment(50)
        for seg, conns in top_per_segment.items():
            seg_output = f"{output_dir}/top_50_{seg}.csv"
            print(f"💾 Exporting top 50 {seg} to {seg_output}...")

            with open(seg_output, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for conn in conns:
                    writer.writerow({
                        'First Name': conn.get('First Name'),
                        'Last Name': conn.get('Last Name'),
                        'URL': conn.get('URL'),
                        'Email Address': conn.get('Email Address'),
                        'Company': conn.get('Company'),
                        'Position': conn.get('Position'),
                        'Connected On': conn.get('Connected On'),
                        'segment': conn.get('segment'),
                        'total_score': conn.get('total_score'),
                        'seniority_score': conn.get('seniority_score'),
                        'position_score': conn.get('position_score'),
                        'company_score': conn.get('company_score'),
                        'recency_score': conn.get('recency_score'),
                        'email_score': conn.get('email_score'),
                    })

        print(f"\n✅ Export complete! Check {output_dir}/ for files.")

    def upload_to_supabase(self, supabase_url: str, supabase_key: str):
        """Upload scored connections to Supabase"""
        if not SUPABASE_AVAILABLE:
            print("❌ Supabase client not available. Install: pip install supabase")
            return

        print(f"\n☁️  Uploading to Supabase...")

        supabase: Client = create_client(supabase_url, supabase_key)

        # Prepare data for Supabase
        records = []
        for conn in self.scored_connections:
            # Parse date
            try:
                connected_date = datetime.strptime(conn.get('Connected On', ''), "%d %b %Y").date()
            except:
                connected_date = None

            records.append({
                'first_name': conn.get('First Name'),
                'last_name': conn.get('Last Name'),
                'linkedin_url': conn.get('URL'),
                'email': conn.get('Email Address'),
                'company': conn.get('Company'),
                'position': conn.get('Position'),
                'connected_on': connected_date.isoformat() if connected_date else None,
                'segment': conn.get('segment'),
                'seniority_score': conn.get('seniority_score'),
                'position_score': conn.get('position_score'),
                'company_score': conn.get('company_score'),
                'recency_score': conn.get('recency_score'),
                'email_score': conn.get('email_score'),
                'total_score': conn.get('total_score'),
            })

        # Batch insert (Supabase has 1000 record limit per insert)
        batch_size = 1000
        for i in range(0, len(records), batch_size):
            batch = records[i:i+batch_size]
            try:
                response = supabase.table('linkedin_connections').insert(batch).execute()
                print(f"   ✅ Uploaded batch {i//batch_size + 1} ({len(batch)} records)")
            except Exception as e:
                print(f"   ❌ Error uploading batch {i//batch_size + 1}: {e}")

        print(f"✅ Upload complete!")


def main():
    """Main execution"""
    print("🚀 LinkedIn ICP Scoring Engine\n")

    # Initialize scorer
    scorer = LinkedInScorer()

    # Load connections
    csv_path = '/Users/matteolombardi/AI-Projects/stratega/assets/LinkedIn data/Connections.csv'
    scorer.load_connections(csv_path)

    # Score all
    scorer.score_all_connections()

    # Export to CSV
    output_dir = '/Users/matteolombardi/AI-Projects/stratega/outputs/linkedin_scoring'
    scorer.export_to_csv(output_dir)

    # Optional: Upload to Supabase (uncomment when ready)
    # supabase_url = os.getenv('SUPABASE_URL')
    # supabase_key = os.getenv('SUPABASE_KEY')
    # if supabase_url and supabase_key:
    #     scorer.upload_to_supabase(supabase_url, supabase_key)
    # else:
    #     print("\n⚠️  Supabase credentials not found. Set SUPABASE_URL and SUPABASE_KEY env vars to upload.")

    print("\n✅ Done! Check outputs/linkedin_scoring/ for results.")


if __name__ == '__main__':
    main()
