# JavaScript Quick Reference for n8n

**Purpose:** Copy-paste snippets and patterns for n8n code nodes
**Usage:** Reference while building workflows

---

## n8n Code Node Basics

### Standard Structure
```javascript
// Get all input items
const items = $input.all();

// Process and return
return items.map(item => ({
  json: {
    // your transformed data
  }
}));
```

### Access Single Item
```javascript
// First item only
const first = $input.first();
const name = first.json.name;

// Last item
const last = $input.last();
```

### Access Previous Nodes
```javascript
// Get data from specific node by name
const previousData = $('NodeName').first().json;

// Get all items from previous node
const allItems = $('NodeName').all();

// Access nested field
const companyUrl = $('set_field_names').first().json['get-input'].company_url;

// Safe access with optional chaining
const email = $('HTTP Request')?.first()?.json?.email ?? 'not found';
```

---

## 20 Essential Snippets

### 1. Clean JSON from LLM Output
```javascript
const items = $input.all();

return items.map(item => {
  let text = item.json.output || item.json.text || '';

  // Remove markdown wrappers
  text = text.replace(/```json\s*/g, '');
  text = text.replace(/```\s*$/g, '');
  text = text.trim();

  // Try to parse
  try {
    return { json: JSON.parse(text) };
  } catch {
    return { json: { raw: text, parseError: true } };
  }
});
```

### 2. Remove Duplicates by Email
```javascript
const items = $input.all();
const seen = new Set();

const unique = items.filter(item => {
  const email = item.json.email?.toLowerCase()?.trim();
  if (!email || seen.has(email)) return false;
  seen.add(email);
  return true;
});

return unique;
```

### 3. Filter by Condition
```javascript
const items = $input.all();

return items.filter(item =>
  item.json.score >= 70 &&
  item.json.segment === 'founder'
);
```

### 4. Transform All Items
```javascript
const items = $input.all();

return items.map(item => ({
  json: {
    fullName: `${item.json.firstName} ${item.json.lastName}`,
    email: item.json.email?.toLowerCase(),
    score: item.json.score,
    processed: true,
    timestamp: new Date().toISOString()
  }
}));
```

### 5. Add Field to Existing Data
```javascript
const items = $input.all();

return items.map(item => ({
  json: {
    ...item.json,  // Keep all existing fields
    newField: 'value',
    processedAt: Date.now()
  }
}));
```

### 6. Group by Field
```javascript
const items = $input.all();

const grouped = items.reduce((acc, item) => {
  const key = item.json.segment;
  acc[key] = acc[key] || [];
  acc[key].push(item.json);
  return acc;
}, {});

return [{ json: grouped }];
```

### 7. Count by Category
```javascript
const items = $input.all();

const counts = items.reduce((acc, item) => {
  const key = item.json.segment;
  acc[key] = (acc[key] || 0) + 1;
  return acc;
}, {});

return [{ json: counts }];
```

### 8. Sort Items
```javascript
const items = $input.all();

return items.sort((a, b) => b.json.score - a.json.score);
```

### 9. Get Top N Items
```javascript
const items = $input.all();
const topN = 50;

return items
  .sort((a, b) => b.json.score - a.json.score)
  .slice(0, topN);
```

### 10. Split into Batches
```javascript
const items = $input.all();
const batchSize = 50;
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

### 11. Merge Data from Two Nodes
```javascript
const contacts = $('Contacts').all();
const scores = $('Scores').all();

// Create lookup from scores
const scoreMap = {};
scores.forEach(item => {
  scoreMap[item.json.email] = item.json.score;
});

// Merge into contacts
return contacts.map(item => ({
  json: {
    ...item.json,
    score: scoreMap[item.json.email] || 0
  }
}));
```

### 12. Calculate Statistics
```javascript
const items = $input.all();
const scores = items.map(item => item.json.score || 0);

const stats = {
  count: scores.length,
  sum: scores.reduce((a, b) => a + b, 0),
  min: Math.min(...scores),
  max: Math.max(...scores),
  avg: scores.reduce((a, b) => a + b, 0) / scores.length
};

return [{ json: stats }];
```

### 13. Format for Email
```javascript
const items = $input.all();

return items.map(item => ({
  json: {
    to: item.json.email,
    subject: `Hello ${item.json.firstName}`,
    body: `
Hi ${item.json.firstName},

I noticed you're working at ${item.json.company}...

Best,
Matteo
    `.trim()
  }
}));
```

### 14. Validate Data
```javascript
const items = $input.all();

const validated = items.map(item => {
  const errors = [];

  if (!item.json.email?.includes('@')) {
    errors.push('Invalid email');
  }
  if (!item.json.firstName) {
    errors.push('Missing first name');
  }

  return {
    json: {
      ...item.json,
      isValid: errors.length === 0,
      errors: errors
    }
  };
});

return validated;
```

### 15. Split Valid/Invalid (Multiple Outputs)
```javascript
const items = $input.all();

const valid = [];
const invalid = [];

items.forEach(item => {
  if (item.json.email?.includes('@')) {
    valid.push(item);
  } else {
    invalid.push(item);
  }
});

// Return array of arrays for multiple outputs
return [valid, invalid];
```

### 16. Extract Unique Values
```javascript
const items = $input.all();

const segments = [...new Set(
  items.map(item => item.json.segment)
)].filter(Boolean);

return [{ json: { segments } }];
```

### 17. Date Formatting
```javascript
const items = $input.all();

return items.map(item => {
  const date = new Date(item.json.connectedOn);
  return {
    json: {
      ...item.json,
      formattedDate: date.toLocaleDateString('en-GB'),
      isoDate: date.toISOString(),
      year: date.getFullYear()
    }
  };
});
```

### 18. Safe Field Access
```javascript
const items = $input.all();

return items.map(item => {
  // Safe access with defaults
  const name = item.json?.firstName ?? 'Unknown';
  const score = item.json?.score ?? 0;
  const tags = item.json?.tags ?? [];

  return {
    json: { name, score, tags }
  };
});
```

### 19. Flatten Nested Data
```javascript
const items = $input.all();

// If items contain arrays, flatten them
const flattened = items.flatMap(item => {
  const contacts = item.json.contacts || [item.json];
  return contacts.map(contact => ({ json: contact }));
});

return flattened;
```

### 20. Error-Safe Processing
```javascript
const items = $input.all();

return items.map(item => {
  try {
    // Your processing logic
    const result = processContact(item.json);
    return { json: { ...result, status: 'success' } };
  } catch (error) {
    return {
      json: {
        ...item.json,
        status: 'error',
        errorMessage: error.message
      }
    };
  }
});

function processContact(contact) {
  // Your logic here
  return {
    name: `${contact.firstName} ${contact.lastName}`,
    score: calculateScore(contact)
  };
}

function calculateScore(contact) {
  let score = 0;
  if (contact.position?.toLowerCase().includes('founder')) score += 40;
  if (contact.email) score += 10;
  return score;
}
```

---

## Common Patterns

### ICP Scoring Pattern
```javascript
const items = $input.all();

const SENIORITY_PATTERNS = [
  { pattern: /founder|ceo|chief/i, score: 100 },
  { pattern: /director|vp|head/i, score: 80 },
  { pattern: /manager|lead/i, score: 60 },
  { pattern: /specialist|analyst/i, score: 40 }
];

function scoreSeniority(position) {
  if (!position) return 20;
  for (const { pattern, score } of SENIORITY_PATTERNS) {
    if (pattern.test(position)) return score;
  }
  return 20;
}

return items.map(item => ({
  json: {
    ...item.json,
    seniorityScore: scoreSeniority(item.json.position)
  }
}));
```

### Geography Detection
```javascript
const items = $input.all();

const ITALIAN_PATTERNS = /srl|spa|italia|italy|milano|roma|fondatore/i;

function detectGeography(contact) {
  const text = `${contact.company || ''} ${contact.position || ''}`;
  return ITALIAN_PATTERNS.test(text) ? 'italy' : 'international';
}

return items.map(item => ({
  json: {
    ...item.json,
    geography: detectGeography(item.json)
  }
}));
```

### API Response Parsing
```javascript
// After HTTP Request node
const response = $input.first().json;

// Handle different response structures
const data = response.data || response.results || response;

// Normalize to array
const items = Array.isArray(data) ? data : [data];

return items.map(item => ({ json: item }));
```

---

## Quick Reference: Array Methods

| Method | Use For | Example |
|--------|---------|---------|
| `map()` | Transform each item | `items.map(i => i.json.name)` |
| `filter()` | Keep matching items | `items.filter(i => i.json.score > 70)` |
| `reduce()` | Aggregate to single value | `items.reduce((sum, i) => sum + i.json.score, 0)` |
| `find()` | Get first match | `items.find(i => i.json.id === targetId)` |
| `some()` | Check if any match | `items.some(i => i.json.segment === 'founder')` |
| `every()` | Check if all match | `items.every(i => i.json.email)` |
| `sort()` | Order items | `items.sort((a, b) => b.json.score - a.json.score)` |
| `slice()` | Get subset | `items.slice(0, 50)` |
| `flatMap()` | Map + flatten | `items.flatMap(i => i.json.tags)` |

---

## Quick Reference: Object Operations

```javascript
// Spread (copy + modify)
const updated = { ...original, newField: 'value' };

// Destructuring
const { name, email, score = 0 } = contact;

// Dynamic keys
const key = 'dynamicField';
const obj = { [key]: 'value' };

// Object.entries (iterate key-value)
Object.entries(obj).forEach(([key, value]) => {
  console.log(key, value);
});

// Object.keys / Object.values
const keys = Object.keys(obj);
const values = Object.values(obj);
```

---

## Debugging Tips

### Log to Console
```javascript
// These show in n8n execution log
console.log('Debug:', item.json);
console.log('Count:', items.length);
```

### Inspect Data Structure
```javascript
// Return data structure for inspection
return [{
  json: {
    itemCount: items.length,
    firstItem: items[0]?.json,
    keys: Object.keys(items[0]?.json || {})
  }
}];
```

### Check for Undefined
```javascript
// Safe check
if (item.json?.email) {
  // email exists
}

// Or with default
const email = item.json?.email ?? 'no-email';
```

---

*Quick Reference v1.0 - Keep this open while building n8n workflows*
