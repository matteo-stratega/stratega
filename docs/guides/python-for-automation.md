# Python Quick Reference for Automation

**Purpose:** Copy-paste snippets for data processing and automation scripts
**Usage:** Reference while building Python tools

---

## Script Template

```python
#!/usr/bin/env python3
"""
Script Name: script_name.py
Description: What this script does
Author: Matteo
"""

import argparse
import logging
import os
import sys
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv

# Setup
load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / 'data'


def setup_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description='Script description')
    parser.add_argument('input', help='Input file')
    parser.add_argument('--output', '-o', help='Output file')
    parser.add_argument('--verbose', '-v', action='store_true')
    return parser.parse_args()


def main():
    """Entry point."""
    args = setup_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    logger.info(f"Processing {args.input}")

    try:
        # Your logic here
        process_file(args.input, args.output)
        logger.info("Done!")
    except Exception as e:
        logger.error(f"Failed: {e}")
        sys.exit(1)


def process_file(input_path, output_path):
    """Main processing logic."""
    # Your implementation
    pass


if __name__ == '__main__':
    main()
```

---

## 20 Essential Snippets

### 1. Load CSV with Pandas
```python
import pandas as pd

# Basic load
df = pd.read_csv('contacts.csv')

# Skip header rows (LinkedIn export has 3)
df = pd.read_csv('connections.csv', skiprows=3)

# With encoding
df = pd.read_csv('data.csv', encoding='utf-8')

# Preview
print(df.head())
print(df.info())
print(len(df))
```

### 2. Filter DataFrame
```python
# Single condition
founders = df[df['segment'] == 'founder']

# Multiple conditions
target = df[
    (df['segment'] == 'founder') &
    (df['geography'] == 'italy') &
    (df['score'] >= 70)
]

# String contains
growth = df[df['position'].str.contains('growth', case=False, na=False)]

# Not null
with_email = df[df['email'].notna()]
```

### 3. Select Columns
```python
# Single column (Series)
names = df['first_name']

# Multiple columns (DataFrame)
contact_info = df[['first_name', 'last_name', 'email']]

# Rename columns
df.rename(columns={
    'First Name': 'first_name',
    'Last Name': 'last_name'
}, inplace=True)
```

### 4. Clean Data
```python
# Remove duplicates
df.drop_duplicates(subset=['email'], keep='first', inplace=True)

# Handle missing values
df['email'].fillna('no-email', inplace=True)
df.dropna(subset=['email'], inplace=True)

# Clean strings
df['email'] = df['email'].str.lower().str.strip()
df['position'] = df['position'].str.replace('\n', ' ')
```

### 5. Create New Column
```python
# Simple concatenation
df['full_name'] = df['first_name'] + ' ' + df['last_name']

# With function
def score_position(position):
    if pd.isna(position):
        return 0
    position = position.lower()
    if 'founder' in position:
        return 100
    if 'director' in position:
        return 80
    return 50

df['position_score'] = df['position'].apply(score_position)

# With lambda
df['has_email'] = df['email'].apply(lambda x: bool(x and '@' in str(x)))
```

### 6. Group and Aggregate
```python
# Count by category
segment_counts = df['segment'].value_counts()

# Group with multiple aggregations
summary = df.groupby('segment').agg({
    'score': ['mean', 'max', 'count'],
    'email': 'count'
})

# Multiple group by
by_seg_geo = df.groupby(['segment', 'geography']).size()
```

### 7. Sort Data
```python
# Sort by column
df_sorted = df.sort_values('score', ascending=False)

# Multiple columns
df_sorted = df.sort_values(
    ['segment', 'score'],
    ascending=[True, False]
)

# Top N
top_50 = df.nlargest(50, 'score')
```

### 8. Save to CSV
```python
# Basic save
df.to_csv('output.csv', index=False)

# Save subset
df[df['score'] >= 70].to_csv('high_score.csv', index=False)

# Select columns
df[['first_name', 'email', 'score']].to_csv('export.csv', index=False)
```

### 9. HTTP GET Request
```python
import requests

# Basic GET
response = requests.get('https://api.example.com/users')
data = response.json()

# With headers
headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
}
response = requests.get(
    'https://api.example.com/users',
    headers=headers
)

# With query parameters
params = {'page': 1, 'limit': 100}
response = requests.get(
    'https://api.example.com/users',
    params=params,
    headers=headers
)
```

### 10. HTTP POST Request
```python
import requests

payload = {
    'name': 'Matteo',
    'email': 'matteo@stratega.co'
}

response = requests.post(
    'https://api.example.com/users',
    json=payload,
    headers={'Authorization': 'Bearer KEY'}
)

if response.status_code == 200:
    result = response.json()
else:
    print(f"Error: {response.status_code}")
```

### 11. Error Handling for APIs
```python
import requests

def fetch_data(url, headers=None):
    """Fetch data with error handling."""
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        return None
    except requests.exceptions.ConnectionError:
        print("Connection failed")
        return None
    except requests.exceptions.Timeout:
        print("Request timed out")
        return None
```

### 12. Rate Limiting
```python
import time
import requests

def fetch_with_rate_limit(urls, requests_per_minute=60):
    """Fetch URLs respecting rate limits."""
    delay = 60 / requests_per_minute
    results = []

    for url in urls:
        result = requests.get(url)
        results.append(result.json())
        time.sleep(delay)

    return results
```

### 13. Retry with Backoff
```python
import time
import requests

def fetch_with_retry(url, max_retries=3):
    """Fetch with exponential backoff."""
    for attempt in range(max_retries):
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        if response.status_code == 429:  # Rate limited
            wait = 2 ** attempt
            print(f"Rate limited. Waiting {wait}s...")
            time.sleep(wait)

    return None
```

### 14. Read/Write JSON
```python
import json
from pathlib import Path

# Read JSON
with open('config.json', 'r') as f:
    config = json.load(f)

# Write JSON
data = {'name': 'Matteo', 'score': 85}
with open('output.json', 'w') as f:
    json.dump(data, f, indent=2)

# Pretty print
print(json.dumps(data, indent=2))
```

### 15. Environment Variables
```python
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Access variables
API_KEY = os.getenv('API_KEY')
DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'

# Required variable (raises if missing)
REQUIRED = os.environ['REQUIRED_KEY']
```

### 16. Command Line Arguments
```python
import argparse

parser = argparse.ArgumentParser(description='Process contacts')
parser.add_argument('input', help='Input CSV file')
parser.add_argument('--output', '-o', default='output.csv')
parser.add_argument('--min-score', type=int, default=50)
parser.add_argument('--verbose', '-v', action='store_true')
parser.add_argument('--segments', nargs='+', default=['founder'])

args = parser.parse_args()

print(f"Input: {args.input}")
print(f"Min score: {args.min_score}")
print(f"Segments: {args.segments}")
```

### 17. Logging
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='script.log'
)
logger = logging.getLogger(__name__)

# Usage
logger.debug('Detailed info')
logger.info('General info')
logger.warning('Warning message')
logger.error('Error occurred')
```

### 18. File Path Handling
```python
from pathlib import Path

# Current directory
cwd = Path.cwd()

# Script directory
script_dir = Path(__file__).parent

# Build paths
data_file = script_dir / 'data' / 'contacts.csv'

# Check exists
if data_file.exists():
    print(f"Found: {data_file}")

# List files
csv_files = list(script_dir.glob('*.csv'))
all_csvs = list(script_dir.rglob('**/*.csv'))  # Recursive
```

### 19. Regex Patterns
```python
import re

text = "CEO & Co-Founder at TechStartup"

# Search
if re.search(r'founder|ceo', text, re.IGNORECASE):
    print("Found executive")

# Find all
matches = re.findall(r'\b[A-Z][a-z]+\b', text)

# Replace
cleaned = re.sub(r'\s+', ' ', text)

# Pattern matching
patterns = {
    r'founder|ceo|chief': 100,
    r'director|vp|head': 80,
    r'manager|lead': 60
}

def match_score(text, patterns):
    text = text.lower()
    for pattern, score in patterns.items():
        if re.search(pattern, text):
            return score
    return 0
```

### 20. List/Dict Comprehensions
```python
# List comprehension
names = [c['name'] for c in contacts]
emails = [c['email'] for c in contacts if c.get('email')]

# Dict comprehension
scores = {c['email']: c['score'] for c in contacts}
by_segment = {s: [] for s in ['founder', 'agency', 'corporate']}

# Nested
all_tags = [tag for contact in contacts for tag in contact.get('tags', [])]

# With condition
high_scorers = {
    c['email']: c['score']
    for c in contacts
    if c.get('score', 0) >= 70
}
```

---

## Common Patterns

### ICP Scoring with Pandas
```python
import pandas as pd
import re

def score_contact(row):
    """Calculate ICP score for a contact."""
    score = 0
    position = str(row.get('position', '')).lower()
    company = str(row.get('company', '')).lower()

    # Seniority
    if re.search(r'founder|ceo|chief', position):
        score += 40
    elif re.search(r'director|vp|head', position):
        score += 30
    elif re.search(r'manager|lead', position):
        score += 20

    # Company type
    if re.search(r'saas|software|tech', company):
        score += 30
    elif re.search(r'agency|consulting', company):
        score += 25

    # Email bonus
    if pd.notna(row.get('email')):
        score += 10

    return score

# Apply to dataframe
df['icp_score'] = df.apply(score_contact, axis=1)
```

### Batch Processing Large Files
```python
import pandas as pd

def process_large_csv(filepath, chunk_size=10000):
    """Process large CSV in chunks."""
    results = []

    for chunk in pd.read_csv(filepath, chunksize=chunk_size):
        # Process each chunk
        processed = process_chunk(chunk)
        results.append(processed)

    return pd.concat(results)

def process_chunk(df):
    """Process a single chunk."""
    # Your processing logic
    return df
```

### Reusable API Client
```python
import requests

class APIClient:
    """Reusable API client."""

    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.request(
                method, url,
                headers=self.headers,
                timeout=30,
                **kwargs
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API Error: {e}")
            return None

    def get(self, endpoint, params=None):
        return self._request('GET', endpoint, params=params)

    def post(self, endpoint, data):
        return self._request('POST', endpoint, json=data)

# Usage
client = APIClient('https://api.example.com', 'your_key')
data = client.get('users', params={'page': 1})
```

### Progress Indicator
```python
from tqdm import tqdm

# For loops
for item in tqdm(items, desc='Processing'):
    process(item)

# With pandas
tqdm.pandas(desc='Scoring')
df['score'] = df.progress_apply(score_contact, axis=1)
```

---

## Quick Reference: Pandas

| Operation | Code |
|-----------|------|
| Load CSV | `pd.read_csv('file.csv')` |
| Save CSV | `df.to_csv('file.csv', index=False)` |
| Filter rows | `df[df['col'] > value]` |
| Select columns | `df[['col1', 'col2']]` |
| Sort | `df.sort_values('col', ascending=False)` |
| Group by | `df.groupby('col').agg({'col2': 'sum'})` |
| Remove duplicates | `df.drop_duplicates(subset=['col'])` |
| Fill NA | `df['col'].fillna(value)` |
| Drop NA | `df.dropna(subset=['col'])` |
| Apply function | `df['col'].apply(func)` |
| Apply to row | `df.apply(func, axis=1)` |
| Top N | `df.nlargest(N, 'col')` |
| Value counts | `df['col'].value_counts()` |

---

## Quick Reference: Files

```python
from pathlib import Path

# Paths
p = Path('/Users/matteo/data')
file = p / 'contacts.csv'

# Check
file.exists()
file.is_file()
file.is_dir()

# List files
list(p.glob('*.csv'))
list(p.rglob('**/*.csv'))

# Read/write
file.read_text()
file.write_text('content')

# File info
file.name       # 'contacts.csv'
file.stem       # 'contacts'
file.suffix     # '.csv'
file.parent     # Path('/Users/matteo/data')
```

---

## Debugging Tips

### Print DataFrame Info
```python
print(df.head())       # First 5 rows
print(df.info())       # Types, null counts
print(df.describe())   # Statistics
print(df.columns)      # Column names
print(len(df))         # Row count
print(df['col'].unique())  # Unique values
```

### Inspect API Response
```python
response = requests.get(url)
print(f"Status: {response.status_code}")
print(f"Headers: {response.headers}")
print(f"JSON: {response.json()}")
```

### Debug with Breakpoint
```python
# Insert this where you want to pause
breakpoint()
# Then use: n (next), c (continue), p variable (print)
```

---

*Quick Reference v1.0 - Keep this open while building Python scripts*
