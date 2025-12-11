# Technical Curriculum - Stratega OS Development

**Target:** Full Technical Autonomy in 90 Days
**Time Commitment:** 5-7 hours/week
**Learning Style:** Project-based, AI-augmented, immediately applicable

---

## Curriculum Overview

```
TRACK 1: JavaScript for n8n         [Days 1-21]   - HIGH PRIORITY
TRACK 2: Python for Automation      [Days 22-42]  - HIGH PRIORITY
TRACK 3: Infrastructure & DevOps    [Days 43-63]  - MEDIUM PRIORITY
TRACK 4: Integration & Mastery      [Days 64-90]  - CAPSTONE
```

---

# TRACK 1: JavaScript for n8n

**Duration:** 3 weeks (Days 1-21)
**Hours:** ~15-20 total
**Goal:** Write any n8n code node without AI assistance

## Why This Matters for Stratega

n8n is your automation backbone. Every workflow can benefit from custom JavaScript:
- Data transformation between nodes
- Complex logic and conditionals
- API response parsing
- Error handling
- Custom formatting

Currently you can do basic transformations. After this track, you'll build any logic needed.

---

## Module 1.1: ES6+ Fundamentals (Days 1-4)

### Learning Objectives
- [ ] Understand let, const, var differences
- [ ] Master arrow functions
- [ ] Use template literals fluently
- [ ] Apply destructuring (objects and arrays)
- [ ] Understand spread operator

### Topics

#### 1.1.1 Variables & Scope
```javascript
// OLD (avoid)
var name = "Matteo";

// NEW (use these)
const API_KEY = "xxx";  // Never changes
let counter = 0;        // Will change

// Why it matters in n8n:
// const prevents accidental overwrites
// let signals intentional mutation
```

#### 1.1.2 Arrow Functions
```javascript
// OLD
function processItem(item) {
  return item.json.name;
}

// NEW (arrow function)
const processItem = (item) => item.json.name;

// Multi-line
const processItem = (item) => {
  const name = item.json.name;
  const email = item.json.email;
  return { name, email };
};

// n8n pattern:
return items.map(item => ({
  json: { ...item.json, processed: true }
}));
```

#### 1.1.3 Template Literals
```javascript
// OLD
const message = "Hello " + name + ", your score is " + score;

// NEW
const message = `Hello ${name}, your score is ${score}`;

// Multi-line (great for prompts)
const prompt = `
You are analyzing ${company}.
Their competitors are: ${competitors.join(', ')}.
Generate a summary.
`;
```

#### 1.1.4 Destructuring
```javascript
// Object destructuring
const { name, email, company } = item.json;

// With rename
const { name: fullName, email: contactEmail } = item.json;

// With defaults
const { name, score = 0 } = item.json;

// Array destructuring
const [first, second, ...rest] = items;

// n8n pattern:
const { firstName, lastName, company } = $input.first().json;
```

#### 1.1.5 Spread Operator
```javascript
// Copy object with modifications
const updated = { ...item.json, processed: true };

// Merge objects
const merged = { ...defaults, ...userSettings };

// Copy array
const copy = [...originalArray];

// n8n pattern:
return items.map(item => ({
  json: {
    ...item.json,
    timestamp: new Date().toISOString()
  }
}));
```

### Resources

| Resource | Type | Time | Link |
|----------|------|------|------|
| JavaScript.info - Variables | Article | 15 min | https://javascript.info/variables |
| JavaScript.info - Arrow Functions | Article | 20 min | https://javascript.info/arrow-functions-basics |
| JavaScript.info - Destructuring | Article | 30 min | https://javascript.info/destructuring-assignment |
| ES6 Features Overview | Video | 30 min | Search "Fireship ES6 features" on YouTube |

### Practice Exercises

1. **Variable Swap** - Rewrite 5 var statements to const/let
2. **Arrow Conversion** - Convert 5 regular functions to arrow functions
3. **Template Builder** - Create an email template with 5+ variables
4. **Destructure This** - Extract 5 fields from a complex object
5. **Spread Practice** - Merge 3 objects with overrides

### Mini-Project: Contact Formatter

Build an n8n code node that:
- Takes raw contact data
- Extracts first_name, last_name, email, company
- Creates a formatted display name
- Adds a timestamp
- Returns cleaned structure

---

## Module 1.2: Array Methods (Days 5-9)

### Learning Objectives
- [ ] Master map() for transformation
- [ ] Use filter() for selection
- [ ] Apply reduce() for aggregation
- [ ] Chain methods effectively
- [ ] Handle edge cases (empty arrays, undefined)

### Topics

#### 1.2.1 map() - Transform Every Item
```javascript
// Transform array items
const names = items.map(item => item.json.name);

// Full transformation
const processed = items.map(item => ({
  json: {
    fullName: `${item.json.firstName} ${item.json.lastName}`,
    email: item.json.email.toLowerCase(),
    score: calculateScore(item.json)
  }
}));

// With index
const numbered = items.map((item, index) => ({
  json: { ...item.json, rank: index + 1 }
}));
```

#### 1.2.2 filter() - Select Items
```javascript
// Basic filter
const founders = items.filter(item =>
  item.json.position.toLowerCase().includes('founder')
);

// Multiple conditions
const highValue = items.filter(item =>
  item.json.score > 70 &&
  item.json.hasEmail === true
);

// Remove empty/null
const valid = items.filter(item =>
  item.json.email && item.json.email.trim() !== ''
);
```

#### 1.2.3 reduce() - Aggregate Data
```javascript
// Sum scores
const totalScore = items.reduce(
  (sum, item) => sum + item.json.score,
  0  // initial value
);

// Group by segment
const bySegment = items.reduce((groups, item) => {
  const segment = item.json.segment;
  groups[segment] = groups[segment] || [];
  groups[segment].push(item);
  return groups;
}, {});

// Count occurrences
const counts = items.reduce((acc, item) => {
  const country = item.json.country;
  acc[country] = (acc[country] || 0) + 1;
  return acc;
}, {});
```

#### 1.2.4 find() & findIndex()
```javascript
// Find first match
const matteo = items.find(item =>
  item.json.firstName === 'Matteo'
);

// Find index
const index = items.findIndex(item =>
  item.json.id === targetId
);
```

#### 1.2.5 some() & every()
```javascript
// Check if any match
const hasFounders = items.some(item =>
  item.json.segment === 'founder'
);

// Check if all match
const allHaveEmail = items.every(item =>
  item.json.email && item.json.email.includes('@')
);
```

#### 1.2.6 Method Chaining
```javascript
// Power of chaining
const topItalianFounders = items
  .filter(item => item.json.segment === 'founder')
  .filter(item => item.json.geography === 'italy')
  .map(item => ({
    json: {
      name: `${item.json.firstName} ${item.json.lastName}`,
      company: item.json.company,
      score: item.json.score
    }
  }))
  .sort((a, b) => b.json.score - a.json.score)
  .slice(0, 50);  // Top 50
```

### Resources

| Resource | Type | Time | Link |
|----------|------|------|------|
| JavaScript.info - Array Methods | Article | 45 min | https://javascript.info/array-methods |
| Array Methods Explained | Video | 25 min | Search "Web Dev Simplified array methods" |
| Reduce in 100 seconds | Video | 2 min | Search "Fireship reduce" |

### Practice Exercises

1. **Map It** - Transform contacts to "Name <email>" format
2. **Filter Chain** - Find Italian founders with score > 70
3. **Reduce Counter** - Count contacts by country
4. **Group By** - Group contacts by segment
5. **Find The One** - Find specific contact by LinkedIn URL

### Mini-Project: Lead Scorer

Build an n8n code node that:
- Receives array of contacts
- Calculates ICP score based on rules
- Filters low-score contacts out
- Groups by segment
- Returns top 10 per segment

---

## Module 1.3: Async & Promises (Days 10-14)

### Learning Objectives
- [ ] Understand synchronous vs asynchronous
- [ ] Use async/await syntax
- [ ] Handle Promise.all() for parallel operations
- [ ] Implement proper error handling
- [ ] Debug async code

### Topics

#### 1.3.1 The Problem: Async Operations
```javascript
// This WON'T work (data isn't ready yet)
const response = fetch('https://api.example.com/data');
console.log(response);  // Promise, not data!

// We need to WAIT for async operations
```

#### 1.3.2 async/await Syntax
```javascript
// Basic pattern
const fetchData = async () => {
  const response = await fetch('https://api.example.com/data');
  const data = await response.json();
  return data;
};

// In n8n code node
const items = $input.all();

// If you need to make HTTP calls (rare in code node)
return items.map(item => ({
  json: { ...item.json, processed: true }
}));
```

#### 1.3.3 Promise.all() - Parallel Operations
```javascript
// Wait for multiple async operations
const [users, products, orders] = await Promise.all([
  fetchUsers(),
  fetchProducts(),
  fetchOrders()
]);

// Useful for batch processing
const enrichedItems = await Promise.all(
  items.map(async (item) => {
    const extraData = await fetchExtraData(item.json.id);
    return {
      json: { ...item.json, ...extraData }
    };
  })
);
```

#### 1.3.4 Error Handling with try/catch
```javascript
// Always wrap async code
const processItems = async () => {
  try {
    const items = $input.all();

    const processed = items.map(item => {
      // Processing logic
      return { json: { ...item.json, status: 'ok' } };
    });

    return processed;
  } catch (error) {
    // Log error and return safe value
    console.error('Processing failed:', error.message);
    return [{
      json: {
        error: true,
        message: error.message
      }
    }];
  }
};

return await processItems();
```

### Resources

| Resource | Type | Time | Link |
|----------|------|------|------|
| JavaScript.info - Promises | Article | 30 min | https://javascript.info/promise-basics |
| JavaScript.info - Async/await | Article | 30 min | https://javascript.info/async-await |
| Async JS Crash Course | Video | 25 min | Search "Traversy Media async await" |

### Practice Exercises

1. **Sequential Await** - Chain 3 async operations
2. **Parallel Batch** - Process 10 items simultaneously
3. **Error Recovery** - Handle failures gracefully
4. **Timeout Handler** - Add timeout to async operation
5. **Retry Logic** - Retry failed operations 3 times

### Mini-Project: API Enrichment Node

Build an n8n code node that:
- Takes array of company names
- Simulates API calls (mock data)
- Handles potential failures
- Returns enriched data with error tracking

---

## Module 1.4: n8n-Specific Patterns (Days 15-21)

### Learning Objectives
- [ ] Master n8n code node structure
- [ ] Use $input, $node, $workflow variables
- [ ] Handle binary data
- [ ] Implement conditional routing
- [ ] Build reusable code patterns

### Topics

#### 1.4.1 n8n Code Node Structure
```javascript
// Standard structure
const items = $input.all();  // Get all input items

// Process each item
const processed = items.map(item => {
  // Your logic here
  return {
    json: {
      // Output data
    }
  };
});

return processed;
```

#### 1.4.2 Accessing Data from Other Nodes
```javascript
// Get data from specific node
const inputData = $('NodeName').first().json;

// Get all items from node
const allItems = $('NodeName').all();

// Access nested fields
const companyUrl = $('set_field_names').first().json['get-input'].company_url;

// Safe access with optional chaining
const email = $('HTTP Request')?.first()?.json?.email ?? 'not found';
```

#### 1.4.3 Common Patterns for Stratega

**Pattern 1: JSON Cleanup (LLM Output)**
```javascript
// Clean markdown wrappers from AI output
const items = $input.all();

return items.map(item => {
  let text = item.json.output || item.json.text || '';

  // Remove markdown code blocks
  text = text.replace(/```json\s*/g, '');
  text = text.replace(/```\s*$/g, '');
  text = text.trim();

  // Try to parse if it's JSON
  let parsed;
  try {
    parsed = JSON.parse(text);
  } catch {
    parsed = { raw: text };
  }

  return { json: parsed };
});
```

**Pattern 2: Data Deduplication**
```javascript
const items = $input.all();

// Dedupe by email
const seen = new Set();
const unique = items.filter(item => {
  const email = item.json.email?.toLowerCase();
  if (!email || seen.has(email)) return false;
  seen.add(email);
  return true;
});

return unique;
```

**Pattern 3: ICP Scoring**
```javascript
const items = $input.all();

const scoreContact = (contact) => {
  let score = 0;

  // Seniority scoring
  const position = (contact.position || '').toLowerCase();
  if (/founder|ceo|chief/.test(position)) score += 40;
  else if (/director|head|vp/.test(position)) score += 30;
  else if (/manager|lead/.test(position)) score += 20;

  // Company scoring
  const company = (contact.company || '').toLowerCase();
  if (/saas|software|tech/.test(company)) score += 30;
  else if (/agency|consulting/.test(company)) score += 25;

  // Email bonus
  if (contact.email) score += 10;

  return score;
};

return items.map(item => ({
  json: {
    ...item.json,
    icp_score: scoreContact(item.json)
  }
}));
```

**Pattern 4: Conditional Output**
```javascript
const items = $input.all();

// Split into multiple outputs (use IF node instead usually)
const highScore = [];
const lowScore = [];

items.forEach(item => {
  if (item.json.score >= 70) {
    highScore.push(item);
  } else {
    lowScore.push(item);
  }
});

// Return array of arrays for multiple outputs
return [highScore, lowScore];
```

**Pattern 5: Batch Processing**
```javascript
const items = $input.all();
const batchSize = 50;

// Split into batches
const batches = [];
for (let i = 0; i < items.length; i += batchSize) {
  batches.push({
    json: {
      batch: Math.floor(i / batchSize) + 1,
      items: items.slice(i, i + batchSize).map(item => item.json)
    }
  });
}

return batches;
```

### Resources

| Resource | Type | Time | Link |
|----------|------|------|------|
| n8n Code Node Docs | Docs | 30 min | https://docs.n8n.io/code-examples/methods/code-node/ |
| n8n Built-in Variables | Docs | 20 min | https://docs.n8n.io/code-examples/methods/variables/ |
| n8n Expressions | Docs | 20 min | https://docs.n8n.io/code-examples/expressions/ |

### Practice Exercises

1. **Build JSON Cleaner** - Clean any LLM output
2. **Build Deduplicator** - Remove duplicates by multiple fields
3. **Build Scorer** - Score contacts with custom rules
4. **Build Splitter** - Split large datasets into batches
5. **Build Merger** - Merge data from multiple nodes

### Capstone Project: Contact Processing Pipeline

Build a complete code node that:
- Takes raw CSV data (parsed by n8n)
- Cleans and normalizes fields
- Deduplicates by email
- Scores each contact
- Tags as Italy/International
- Outputs top 100 sorted by score

---

# TRACK 2: Python for Automation

**Duration:** 3 weeks (Days 22-42)
**Hours:** ~15-20 total
**Goal:** Process any data, call any API, automate any task

## Why This Matters for Stratega

Python is your automation workhorse:
- Process large CSV/Excel files
- Call any API (LinkedIn, Clearbit, etc.)
- Web scraping for lead gen
- Data cleaning and enrichment
- Quick scripts for one-off tasks

Currently you use AI-assisted Python. After this track, you'll write scripts independently.

---

## Module 2.1: Python Fundamentals Review (Days 22-25)

### Learning Objectives
- [ ] Confident with data types and structures
- [ ] Write functions effectively
- [ ] Use comprehensions (list, dict)
- [ ] Handle files and paths
- [ ] Manage exceptions properly

### Topics

#### 2.1.1 Data Structures Deep Dive
```python
# Lists - ordered, mutable
contacts = ['Alice', 'Bob', 'Charlie']
contacts.append('Diana')
first = contacts[0]

# Dictionaries - key-value pairs
contact = {
    'name': 'Alice',
    'email': 'alice@example.com',
    'score': 85
}
name = contact['name']
name = contact.get('name', 'Unknown')  # Safe access

# Sets - unique values
seen_emails = set()
seen_emails.add('alice@example.com')
if 'alice@example.com' in seen_emails:
    print('Duplicate!')
```

#### 2.1.2 Functions
```python
# Basic function
def calculate_score(contact):
    """Calculate ICP score for a contact."""
    score = 0
    if 'founder' in contact.get('position', '').lower():
        score += 40
    if contact.get('email'):
        score += 10
    return score

# With type hints (recommended)
from typing import Dict, List, Optional

def calculate_score(contact: Dict) -> int:
    """Calculate ICP score for a contact."""
    score: int = 0
    position: str = contact.get('position', '').lower()
    if 'founder' in position:
        score += 40
    return score

# Default arguments
def score_contacts(contacts: List[Dict], min_score: int = 50) -> List[Dict]:
    """Filter contacts by minimum score."""
    return [c for c in contacts if c.get('score', 0) >= min_score]
```

#### 2.1.3 Comprehensions
```python
# List comprehension
names = [contact['name'] for contact in contacts]

# With condition
founders = [c for c in contacts if 'founder' in c.get('position', '').lower()]

# Dict comprehension
scores = {c['email']: c['score'] for c in contacts if c.get('email')}

# Nested comprehension
all_emails = [
    email
    for company in companies
    for email in company.get('contacts', [])
]
```

#### 2.1.4 File Operations
```python
from pathlib import Path

# Reading files
data_dir = Path('/Users/matteolombardi/AI-Projects/stratega/data')
connections_file = data_dir / 'connections.csv'

# Read text file
with open(connections_file, 'r', encoding='utf-8') as f:
    content = f.read()
    # or line by line:
    # lines = f.readlines()

# Write file
output_file = data_dir / 'output.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('Results:\n')
    for item in results:
        f.write(f'{item}\n')

# Check if exists
if connections_file.exists():
    print('File found!')
```

#### 2.1.5 Exception Handling
```python
# Basic try/except
try:
    score = calculate_score(contact)
except KeyError as e:
    print(f'Missing key: {e}')
    score = 0
except Exception as e:
    print(f'Unexpected error: {e}')
    score = 0

# With finally
try:
    f = open('data.csv', 'r')
    data = f.read()
finally:
    f.close()  # Always runs

# Better: context manager (with statement)
try:
    with open('data.csv', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print('File not found')
    data = []
```

### Resources

| Resource | Type | Time | Link |
|----------|------|------|------|
| Python.org Tutorial | Docs | 2 hours | https://docs.python.org/3/tutorial/ |
| Real Python - Basics | Articles | 1 hour | https://realpython.com/tutorials/basics/ |
| Automate Boring Stuff - Ch 1-4 | Book | 2 hours | https://automatetheboringstuff.com/ |

### Practice Exercises

1. **Contact Parser** - Parse raw text into dict
2. **Deduplicator** - Remove duplicates from list
3. **File Counter** - Count files in directory by type
4. **Score Calculator** - Build scoring function
5. **Error Logger** - Log errors to file

---

## Module 2.2: Pandas Essentials (Days 26-32)

### Learning Objectives
- [ ] Load and save CSV/Excel files
- [ ] Select and filter data
- [ ] Transform and clean data
- [ ] Aggregate and group data
- [ ] Merge multiple datasets

### Topics

#### 2.2.1 Loading Data
```python
import pandas as pd

# Read CSV
df = pd.read_csv('connections.csv')

# Skip rows (LinkedIn exports have 3 header rows)
df = pd.read_csv('connections.csv', skiprows=3)

# Specify encoding
df = pd.read_csv('connections.csv', encoding='utf-8')

# Read Excel
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Quick inspection
print(df.head())         # First 5 rows
print(df.info())         # Column types, null counts
print(df.describe())     # Statistics
print(df.columns)        # Column names
print(len(df))           # Row count
```

#### 2.2.2 Selecting Data
```python
# Select columns
names = df['First Name']              # Single column (Series)
contact_info = df[['First Name', 'Email']]  # Multiple columns (DataFrame)

# Select rows by index
first_10 = df.head(10)
row_5 = df.iloc[5]        # By position
rows_5_to_10 = df.iloc[5:10]

# Select rows by condition
founders = df[df['Position'].str.contains('founder', case=False, na=False)]
high_score = df[df['score'] >= 70]

# Multiple conditions
target = df[
    (df['segment'] == 'founder') &
    (df['geography'] == 'italy') &
    (df['score'] >= 60)
]
```

#### 2.2.3 Cleaning Data
```python
# Handle missing values
df['Email'].fillna('no-email', inplace=True)
df.dropna(subset=['Email'])  # Remove rows with no email

# Remove duplicates
df.drop_duplicates(subset=['Email'], keep='first', inplace=True)

# Rename columns
df.rename(columns={'First Name': 'first_name', 'Last Name': 'last_name'}, inplace=True)

# Clean strings
df['email'] = df['email'].str.lower().str.strip()
df['position'] = df['position'].str.replace('\n', ' ')

# Convert types
df['score'] = df['score'].astype(int)
df['connected_on'] = pd.to_datetime(df['connected_on'])
```

#### 2.2.4 Transforming Data
```python
# Create new columns
df['full_name'] = df['first_name'] + ' ' + df['last_name']

# Apply function to column
def score_position(position):
    if pd.isna(position):
        return 0
    position = position.lower()
    if 'founder' in position or 'ceo' in position:
        return 100
    if 'director' in position or 'vp' in position:
        return 80
    return 50

df['position_score'] = df['Position'].apply(score_position)

# Apply function to row
def calculate_total_score(row):
    return row['position_score'] * 0.6 + row['engagement_score'] * 0.4

df['total_score'] = df.apply(calculate_total_score, axis=1)
```

#### 2.2.5 Aggregating Data
```python
# Basic aggregations
total = df['score'].sum()
average = df['score'].mean()
count = df['segment'].value_counts()

# Group by
by_segment = df.groupby('segment').agg({
    'score': ['mean', 'max', 'count'],
    'email': 'count'
})

# Multiple group by
by_seg_geo = df.groupby(['segment', 'geography']).size()

# Pivot table
pivot = df.pivot_table(
    values='score',
    index='segment',
    columns='geography',
    aggfunc='mean'
)
```

#### 2.2.6 Merging Data
```python
# Merge two DataFrames (like SQL JOIN)
# Left join: keep all from left, match from right
merged = pd.merge(
    contacts_df,
    messages_df,
    left_on='url',
    right_on='sender_url',
    how='left'
)

# Concat (stack DataFrames)
combined = pd.concat([df1, df2], ignore_index=True)
```

#### 2.2.7 Saving Data
```python
# Save to CSV
df.to_csv('output.csv', index=False)

# Save to Excel
df.to_excel('output.xlsx', sheet_name='Contacts', index=False)

# Save subset
df[df['score'] >= 70].to_csv('high_score.csv', index=False)
```

### Resources

| Resource | Type | Time | Link |
|----------|------|------|------|
| Pandas Getting Started | Docs | 30 min | https://pandas.pydata.org/docs/getting_started/intro_tutorials/ |
| 10 Minutes to Pandas | Tutorial | 15 min | https://pandas.pydata.org/docs/user_guide/10min.html |
| Real Python - Pandas | Article | 1 hour | https://realpython.com/pandas-python-explore-dataset/ |
| Pandas Cheat Sheet | Reference | -- | https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf |

### Practice Exercises

1. **Load & Inspect** - Load CSV, check types and nulls
2. **Filter & Select** - Extract Italian founders with email
3. **Clean Dataset** - Remove duplicates, handle nulls
4. **Score Contacts** - Apply scoring function to dataframe
5. **Segment Analysis** - Group by segment, calculate stats

### Mini-Project: LinkedIn Data Processor

Build a Python script that:
- Loads Connections.csv (skip header rows)
- Cleans column names
- Removes duplicates by email
- Scores each contact
- Groups by segment
- Exports top 50 per segment

---

## Module 2.3: API Integration (Days 33-37)

### Learning Objectives
- [ ] Make HTTP requests with requests library
- [ ] Handle authentication (API keys, OAuth basics)
- [ ] Parse JSON responses
- [ ] Handle errors and rate limits
- [ ] Build reusable API clients

### Topics

#### 2.3.1 Basic HTTP Requests
```python
import requests

# GET request
response = requests.get('https://api.example.com/users')
print(response.status_code)  # 200, 404, etc.
print(response.json())       # Parse JSON response

# With headers
headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
}
response = requests.get('https://api.example.com/users', headers=headers)

# POST request
payload = {
    'name': 'Matteo',
    'email': 'matteo@stratega.co'
}
response = requests.post(
    'https://api.example.com/users',
    json=payload,
    headers=headers
)
```

#### 2.3.2 Query Parameters
```python
# Add query parameters
params = {
    'page': 1,
    'limit': 100,
    'segment': 'founder'
}
response = requests.get(
    'https://api.example.com/contacts',
    params=params,
    headers=headers
)
# URL becomes: https://api.example.com/contacts?page=1&limit=100&segment=founder
```

#### 2.3.3 Error Handling
```python
def fetch_data(url, headers):
    """Fetch data with proper error handling."""
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()  # Raise exception for 4xx/5xx
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
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
```

#### 2.3.4 Rate Limiting
```python
import time

def fetch_with_rate_limit(urls, requests_per_minute=60):
    """Fetch multiple URLs respecting rate limits."""
    results = []
    delay = 60 / requests_per_minute  # seconds between requests

    for url in urls:
        result = fetch_data(url)
        results.append(result)
        time.sleep(delay)

    return results

# Or use exponential backoff for retries
def fetch_with_retry(url, max_retries=3):
    """Fetch with exponential backoff."""
    for attempt in range(max_retries):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 429:  # Rate limited
            wait = 2 ** attempt  # 1, 2, 4 seconds
            print(f"Rate limited. Waiting {wait}s...")
            time.sleep(wait)
    return None
```

#### 2.3.5 Reusable API Client
```python
class APIClient:
    """Reusable API client with authentication and error handling."""

    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

    def _request(self, method, endpoint, **kwargs):
        """Make HTTP request with error handling."""
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
client = APIClient('https://api.clearbit.com', 'your_api_key')
company = client.get('companies/find', params={'domain': 'stratega.co'})
```

### Resources

| Resource | Type | Time | Link |
|----------|------|------|------|
| Requests Library Docs | Docs | 30 min | https://requests.readthedocs.io/ |
| Real Python - Requests | Article | 45 min | https://realpython.com/python-requests/ |
| API Design Best Practices | Article | 20 min | Search "REST API best practices" |

### Practice Exercises

1. **Simple GET** - Fetch data from public API
2. **With Auth** - Call API with API key
3. **POST Request** - Create resource via API
4. **Rate Limiter** - Build rate-limited fetcher
5. **API Client** - Build reusable client class

### Mini-Project: Company Enrichment Script

Build a Python script that:
- Takes list of company domains
- Calls Clearbit-like API (use mock data)
- Handles errors and rate limits
- Saves enriched data to CSV

---

## Module 2.4: Automation Scripts (Days 38-42)

### Learning Objectives
- [ ] Build command-line scripts
- [ ] Handle environment variables
- [ ] Schedule scripts (cron basics)
- [ ] Log operations properly
- [ ] Create reusable utilities

### Topics

#### 2.4.1 Command-Line Arguments
```python
import argparse

def main():
    parser = argparse.ArgumentParser(description='Process contacts')
    parser.add_argument('input', help='Input CSV file')
    parser.add_argument('--output', '-o', default='output.csv', help='Output file')
    parser.add_argument('--min-score', type=int, default=50, help='Minimum score')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')

    args = parser.parse_args()

    if args.verbose:
        print(f"Processing {args.input}")
        print(f"Min score: {args.min_score}")

    # Your processing logic here
    process_contacts(args.input, args.output, args.min_score)

if __name__ == '__main__':
    main()
```

#### 2.4.2 Environment Variables
```python
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Access variables
API_KEY = os.getenv('CLEARBIT_API_KEY')
DATABASE_URL = os.getenv('SUPABASE_URL')

# With defaults
DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'

# Required variable
REQUIRED_KEY = os.environ['REQUIRED_KEY']  # Raises KeyError if missing
```

#### 2.4.3 Logging
```python
import logging

# Basic setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='script.log'
)
logger = logging.getLogger(__name__)

# Usage
logger.info('Starting processing')
logger.warning('Missing email for contact')
logger.error(f'Failed to process: {error}')

# Also output to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
logger.addHandler(console_handler)
```

#### 2.4.4 Script Structure Template
```python
#!/usr/bin/env python3
"""
Script Name: contact_processor.py
Description: Process and score LinkedIn contacts
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
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / 'data'


def setup_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description='Process contacts')
    parser.add_argument('input', help='Input CSV file')
    parser.add_argument('--output', '-o', help='Output file')
    return parser.parse_args()


def process_contacts(input_file: Path, output_file: Path) -> int:
    """Main processing logic. Returns count of processed contacts."""
    logger.info(f"Loading {input_file}")
    df = pd.read_csv(input_file, skiprows=3)

    # Processing...
    logger.info(f"Processing {len(df)} contacts")

    # Save
    df.to_csv(output_file, index=False)
    logger.info(f"Saved to {output_file}")

    return len(df)


def main():
    """Entry point."""
    args = setup_args()

    input_file = Path(args.input)
    output_file = Path(args.output) if args.output else input_file.stem + '_processed.csv'

    if not input_file.exists():
        logger.error(f"Input file not found: {input_file}")
        sys.exit(1)

    try:
        count = process_contacts(input_file, output_file)
        logger.info(f"Done! Processed {count} contacts")
    except Exception as e:
        logger.error(f"Processing failed: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
```

### Resources

| Resource | Type | Time | Link |
|----------|------|------|------|
| Argparse Tutorial | Docs | 20 min | https://docs.python.org/3/howto/argparse.html |
| Python-dotenv | Docs | 10 min | https://github.com/theskumar/python-dotenv |
| Logging HOWTO | Docs | 30 min | https://docs.python.org/3/howto/logging.html |
| Automate Boring Stuff - Ch 12 | Book | 30 min | https://automatetheboringstuff.com/2e/chapter12/ |

### Practice Exercises

1. **CLI Script** - Build script with 3+ arguments
2. **Config Loader** - Load settings from .env
3. **Logger** - Add logging to existing script
4. **Progress Reporter** - Show progress for long operations
5. **Error Handler** - Proper error handling and exit codes

### Capstone Project: LinkedIn ICP Scorer CLI

Build a complete command-line tool that:
- Takes connections.csv as input
- Configurable via .env (API keys, thresholds)
- Scores and segments contacts
- Logs operations
- Outputs multiple CSV files (by segment, by geography)
- Has --verbose and --dry-run options

---

# TRACK 3: Infrastructure & DevOps

**Duration:** 3 weeks (Days 43-63)
**Hours:** ~15 total
**Goal:** Self-sufficient with tools, environments, and deployments

---

## Module 3.1: Git Workflow (Days 43-49)

### Learning Objectives
- [ ] Use branches effectively
- [ ] Resolve merge conflicts
- [ ] Write good commit messages
- [ ] Use git stash
- [ ] Understand gitignore

### Topics

#### 3.1.1 Branching Strategy
```bash
# Create and switch to branch
git checkout -b feature/icp-scoring-v3

# Or two commands
git branch feature/icp-scoring-v3
git checkout feature/icp-scoring-v3

# List branches
git branch -a

# Switch branches
git checkout main

# Delete branch
git branch -d feature/old-branch
```

#### 3.1.2 Typical Workflow
```bash
# 1. Start from main (updated)
git checkout main
git pull origin main

# 2. Create feature branch
git checkout -b feature/new-scoring

# 3. Make changes, commit often
git add .
git commit -m "Add position scoring logic"

git add scripts/scorer.py
git commit -m "Refactor scoring to use pandas"

# 4. Push branch to remote
git push -u origin feature/new-scoring

# 5. Create PR (on GitHub) or merge locally
git checkout main
git merge feature/new-scoring

# 6. Push merged main
git push origin main
```

#### 3.1.3 Handling Conflicts
```bash
# When merge has conflicts
git merge feature/x
# CONFLICT in file.py

# Open file, find conflict markers:
# <<<<<<< HEAD
# your changes
# =======
# their changes
# >>>>>>> feature/x

# Edit file to resolve, then:
git add file.py
git commit -m "Resolve merge conflict in file.py"
```

#### 3.1.4 Git Stash
```bash
# Save work-in-progress
git stash

# Do other work...
git checkout main
git pull

# Get work back
git stash pop

# List stashes
git stash list

# Apply specific stash
git stash apply stash@{2}
```

#### 3.1.5 Good Commit Messages
```
# Format:
# <type>: <short description>
#
# <longer description if needed>

# Types:
feat: Add ICP scoring v2
fix: Correct Italian name detection
refactor: Extract scoring to separate module
docs: Add API documentation
chore: Update dependencies
```

### Resources

See `/docs/guides/git-workflow.md` for complete reference.

---

## Module 3.2: Docker Operations (Days 50-56)

### Learning Objectives
- [ ] Understand containers vs images
- [ ] Use docker-compose effectively
- [ ] Debug container issues
- [ ] Manage volumes and data
- [ ] Basic Dockerfile understanding

### Topics

#### 3.2.1 Core Concepts
```
Image = Blueprint (like a class)
Container = Running instance (like an object)
Volume = Persistent storage
Network = Container communication
```

#### 3.2.2 Essential Commands
```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Start/stop containers
docker start n8n-production
docker stop n8n-production

# View logs
docker logs n8n-production
docker logs -f n8n-production  # Follow (live)
docker logs --tail 100 n8n-production  # Last 100 lines

# Execute command in container
docker exec -it n8n-production sh
docker exec n8n-production ls /home/node/.n8n

# Remove container
docker rm container_name
```

#### 3.2.3 Docker Compose
```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# Rebuild after changes
docker-compose up -d --build

# View logs
docker-compose logs -f

# Restart specific service
docker-compose restart n8n
```

### Resources

See `/docs/guides/docker-quick-start.md` for complete reference.

---

## Module 3.3: Environment & Database (Days 57-63)

### Learning Objectives
- [ ] Manage Python environments
- [ ] Use environment variables properly
- [ ] Basic SQL queries
- [ ] Supabase operations

### Topics

#### 3.3.1 Python Environments
```bash
# Create virtual environment
python -m venv venv

# Activate
source venv/bin/activate  # macOS/Linux
.\venv\Scripts\activate   # Windows

# Install packages
pip install pandas requests python-dotenv

# Save dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Deactivate
deactivate
```

#### 3.3.2 SQL Basics
```sql
-- Select data
SELECT first_name, last_name, score
FROM contacts
WHERE segment = 'founder'
ORDER BY score DESC
LIMIT 50;

-- Filter with multiple conditions
SELECT *
FROM contacts
WHERE geography = 'italy'
  AND score >= 70
  AND email IS NOT NULL;

-- Aggregate
SELECT segment, COUNT(*), AVG(score)
FROM contacts
GROUP BY segment;

-- Update
UPDATE contacts
SET segment = 'founder'
WHERE position ILIKE '%founder%';
```

---

# TRACK 4: Integration & Mastery

**Duration:** 4 weeks (Days 64-90)
**Goal:** Build complete systems, achieve technical autonomy

This track focuses on applying all learned skills through progressively complex projects. See `TECHNICAL_PROJECTS.md` for detailed project specifications.

---

## Success Criteria

### By Day 30 (End of Track 1)
- [ ] Write n8n code nodes without AI assistance
- [ ] Comfortable with ES6+ JavaScript
- [ ] Understand async/await

### By Day 60 (End of Track 2-3)
- [ ] Process any CSV with pandas
- [ ] Call and handle any REST API
- [ ] Navigate Git with branches
- [ ] Debug Docker issues

### By Day 90 (End of Track 4)
- [ ] Built 10+ working Stratega tools
- [ ] Can read and modify any codebase
- [ ] Technical autonomy achieved

---

## Appendix: Tool Setup Checklist

### Required Software
- [ ] VS Code (with Python and JavaScript extensions)
- [ ] Python 3.11+
- [ ] Node.js 18+
- [ ] Docker Desktop
- [ ] Git

### VS Code Extensions
- [ ] Python (Microsoft)
- [ ] Pylance
- [ ] JavaScript (ES6) code snippets
- [ ] GitLens
- [ ] Docker
- [ ] Prettier

### Python Packages
```bash
pip install pandas requests python-dotenv beautifulsoup4 openpyxl
```

---

*Curriculum Version 1.0 - November 2025*
