# 90-Day Technical Learning Roadmap

**Start Date:** _____________
**Target Completion:** _____________
**Weekly Commitment:** 5-7 hours

---

## Phase Overview

| Phase | Days | Focus | Goal |
|-------|------|-------|------|
| **Phase 1** | 1-30 | JavaScript + Foundations | n8n mastery |
| **Phase 2** | 31-60 | Python + Data | Automation power |
| **Phase 3** | 61-90 | Integration + Capstone | Technical autonomy |

---

# PHASE 1: Foundation (Days 1-30)

**Theme:** JavaScript for n8n + Dev Environment
**Hours:** 20-25 total (5-6 hours/week)

---

## Week 1: JavaScript Fundamentals

**Learning Time:** 5 hours
**Focus:** ES6+ basics that unlock n8n

### Daily Breakdown

| Day | Topic                                   | Time | Resource        |
| --- | --------------------------------------- | ---- | --------------- |
| Mon | Variables (let, const), Arrow functions | 1h   | JavaScript.info |
| Tue | Template literals, Destructuring        | 1h   | JavaScript.info |
| Wed | Spread operator, Object shortcuts       | 1h   | JavaScript.info |
| Thu | Practice: Convert old code to ES6       | 1h   | Exercise        |
| Fri | Mini-project: Contact Formatter         | 1h   | Project 1 prep  |

### Exercises
1. Rewrite 5 `var` statements to `const`/`let`
2. Convert 5 functions to arrow syntax
3. Use template literals for 3 email templates
4. Destructure LinkedIn contact object

### Checkpoint
- [ ] Can explain let vs const vs var
- [ ] Write arrow functions naturally
- [ ] Use template literals for strings
- [ ] Destructure objects and arrays

---

## Week 2: Array Methods Mastery

**Learning Time:** 6 hours
**Focus:** map, filter, reduce - the n8n essentials

### Daily Breakdown

| Day | Topic | Time | Resource |
|-----|-------|------|----------|
| Mon | map() deep dive | 1h | JavaScript.info |
| Tue | filter() patterns | 1h | JavaScript.info |
| Wed | reduce() fundamentals | 1.5h | JavaScript.info |
| Thu | Method chaining | 1h | Practice |
| Fri | Project: JSON Cleaner Node | 1.5h | Project 1 |

### Exercises
1. Transform contacts array to "Name <email>" format (map)
2. Filter Italian founders with score > 70 (filter)
3. Count contacts by segment (reduce)
4. Chain 3 methods in one expression

### Checkpoint
- [ ] Use map() without thinking
- [ ] Write complex filter conditions
- [ ] Understand reduce for aggregation
- [ ] Chain methods confidently

### Project Deliverable
**Project 1: JSON Cleaner Node** - Complete and tested

---

## Week 3: Async & n8n Patterns

**Learning Time:** 6 hours
**Focus:** Async/await + n8n-specific code

### Daily Breakdown

| Day | Topic | Time | Resource |
|-----|-------|------|----------|
| Mon | Promises basics | 1h | JavaScript.info |
| Tue | async/await syntax | 1.5h | JavaScript.info |
| Wed | Error handling (try/catch) | 1h | JavaScript.info |
| Thu | n8n variables ($input, $node) | 1h | n8n docs |
| Fri | Project: Contact Deduplicator | 1.5h | Project 2 |

### Exercises
1. Write async function with await
2. Handle 3 different error types
3. Access data from multiple n8n nodes
4. Build batch processor logic

### Checkpoint
- [ ] Understand Promise concept
- [ ] Use async/await correctly
- [ ] Handle errors gracefully
- [ ] Navigate n8n code node API

### Project Deliverable
**Project 2: Contact Deduplicator** - Complete and tested

---

## Week 4: Consolidation + First Major Project

**Learning Time:** 7 hours
**Focus:** Apply everything in real project

### Daily Breakdown

| Day | Topic | Time | Resource |
|-----|-------|------|----------|
| Mon | Review weak areas | 1h | Self-assessment |
| Tue | Git workflow practice | 1h | Guide |
| Wed | Project: ICP Scorer Node (part 1) | 2h | Project 3 |
| Thu | Project: ICP Scorer Node (part 2) | 2h | Project 3 |
| Fri | Testing + documentation | 1h | - |

### Project Deliverable
**Project 3: ICP Scorer Node** - Complete, tested, documented

### Phase 1 Assessment

**Self-Check Quiz:**
1. What's the difference between map() and forEach()?
2. How do you handle a failed async operation?
3. How do you access previous node data in n8n?
4. Write a function to score a contact (from memory)

**Practical Test:**
Build an n8n code node (without AI help) that:
- Takes array of contacts
- Filters by minimum score
- Transforms to display format
- Handles empty/null values

**Pass Criteria:**
- [ ] Complete in under 30 minutes
- [ ] No syntax errors
- [ ] Handles edge cases
- [ ] Clean, readable code

---

# PHASE 2: Power User (Days 31-60)

**Theme:** Python Data Automation
**Hours:** 20-25 total (5-6 hours/week)

---

## Week 5: Python Fundamentals Refresh

**Learning Time:** 5 hours
**Focus:** Ensure Python basics are solid

### Daily Breakdown

| Day | Topic | Time | Resource |
|-----|-------|------|----------|
| Mon | Data structures (lists, dicts, sets) | 1h | Python.org |
| Tue | Functions & type hints | 1h | Real Python |
| Wed | List/dict comprehensions | 1h | Python.org |
| Thu | File I/O & paths | 1h | Automate Boring Stuff |
| Fri | Project: CSV Processor CLI | 1h | Project 5 |

### Exercises
1. Build dictionary from two lists
2. Write function with type hints
3. Filter contacts with comprehension
4. Read/write CSV without pandas

### Checkpoint
- [ ] Confident with Python data structures
- [ ] Write clean functions
- [ ] Use comprehensions naturally
- [ ] Handle files correctly

### Project Deliverable
**Project 5: CSV Processor CLI** - Basic version working

---

## Week 6: Pandas Essentials

**Learning Time:** 6 hours
**Focus:** Data manipulation power

### Daily Breakdown

| Day | Topic | Time | Resource |
|-----|-------|------|----------|
| Mon | Loading data, basic inspection | 1h | Pandas docs |
| Tue | Selecting & filtering | 1.5h | Pandas docs |
| Wed | Transforming & cleaning | 1.5h | Pandas docs |
| Thu | Grouping & aggregating | 1h | Pandas docs |
| Fri | Project: LinkedIn Data Analyzer | 1h | Project 6 start |

### Exercises
1. Load LinkedIn CSV (skip header rows)
2. Filter Italian founders
3. Clean email column (lowercase, strip)
4. Count connections by segment

### Checkpoint
- [ ] Load any CSV/Excel file
- [ ] Filter with complex conditions
- [ ] Transform columns with apply()
- [ ] Group and aggregate

### Project Deliverable
**Project 6: LinkedIn Data Analyzer** - Started (50% complete)

---

## Week 7: APIs & Web Requests

**Learning Time:** 6 hours
**Focus:** Connect to any service

### Daily Breakdown

| Day | Topic | Time | Resource |
|-----|-------|------|----------|
| Mon | HTTP basics, requests library | 1h | Real Python |
| Tue | Authentication patterns | 1h | API docs |
| Wed | Error handling & retries | 1.5h | Best practices |
| Thu | Rate limiting | 1h | Best practices |
| Fri | Project: LinkedIn Data Analyzer (complete) | 1.5h | Project 6 finish |

### Exercises
1. GET request with headers
2. POST request with JSON body
3. Handle 429 (rate limit) errors
4. Build retry logic

### Checkpoint
- [ ] Call any REST API
- [ ] Handle authentication
- [ ] Manage rate limits
- [ ] Retry failed requests

### Project Deliverables
- **Project 6: LinkedIn Data Analyzer** - Complete
- **Project 7: API Enrichment Tool** - Started

---

## Week 8: Automation Scripts

**Learning Time:** 7 hours
**Focus:** Production-ready Python

### Daily Breakdown

| Day | Topic | Time | Resource |
|-----|-------|------|----------|
| Mon | Command-line arguments (argparse) | 1h | Python docs |
| Tue | Environment variables | 1h | python-dotenv |
| Wed | Logging | 1h | Python docs |
| Thu | Project: API Enrichment Tool (complete) | 2h | Project 7 |
| Fri | Project: n8n Workflow Fixer | 2h | Project 9 |

### Exercises
1. Build CLI with 3 arguments
2. Load secrets from .env
3. Add logging to existing script
4. Create script template

### Checkpoint
- [ ] Build proper CLI tools
- [ ] Manage configuration securely
- [ ] Log operations properly
- [ ] Structure scripts for production

### Project Deliverables
- **Project 7: API Enrichment Tool** - Complete
- **Project 9: n8n Workflow Fixer** - Complete

### Phase 2 Assessment

**Self-Check Quiz:**
1. How do you load a CSV with pandas (skip rows)?
2. What's the difference between filter() and query()?
3. How do you handle rate limiting in API calls?
4. Write a script to process command-line arguments

**Practical Test:**
Build a Python script (without AI help) that:
- Loads LinkedIn CSV
- Scores contacts (seniority + position)
- Filters to top 100
- Exports to new CSV
- Uses command-line arguments

**Pass Criteria:**
- [ ] Complete in under 45 minutes
- [ ] Uses pandas effectively
- [ ] Proper error handling
- [ ] Clean code structure

---

# PHASE 3: Mastery (Days 61-90)

**Theme:** Integration + Capstone Projects
**Hours:** 25-30 total (6-7 hours/week)

---

## Week 9: Git & Docker Confidence

**Learning Time:** 5 hours
**Focus:** Infrastructure independence

### Daily Breakdown

| Day | Topic | Time | Resource |
|-----|-------|------|----------|
| Mon | Git branching workflow | 1h | Guide |
| Tue | Merge conflicts | 1h | Practice |
| Wed | Docker essentials | 1.5h | Guide |
| Thu | Debugging containers | 1h | Docker docs |
| Fri | Project: Git Backup Script | 0.5h | Project 10 |

### Exercises
1. Create feature branch, make changes, merge
2. Resolve a merge conflict
3. Debug n8n container (logs, exec)
4. Write docker-compose modification

### Checkpoint
- [ ] Branch workflow is natural
- [ ] Can resolve conflicts
- [ ] Debug Docker issues
- [ ] Read/modify docker-compose

### Project Deliverable
**Project 10: Git Backup Script** - Complete

---

## Week 10: Database & Integration

**Learning Time:** 6 hours
**Focus:** Supabase + Full Integration

### Daily Breakdown

| Day | Topic | Time | Resource |
|-----|-------|------|----------|
| Mon | SQL fundamentals | 1.5h | W3Schools |
| Tue | Supabase Python client | 1.5h | Supabase docs |
| Wed | Project: Docker Health Monitor | 1.5h | Project 11 |
| Thu | Project: Supabase Data Loader | 1.5h | Project 12 |
| Fri | Integration testing | - | - |

### Exercises
1. Write 5 SQL queries (SELECT, WHERE, GROUP BY)
2. Insert data to Supabase
3. Query data from Supabase
4. Upsert logic

### Checkpoint
- [ ] Basic SQL queries
- [ ] Supabase CRUD operations
- [ ] Monitor Docker services
- [ ] Load data to database

### Project Deliverables
- **Project 11: Docker Health Monitor** - Complete
- **Project 12: Supabase Data Loader** - Complete

---

## Week 11: Advanced Integration

**Learning Time:** 7 hours
**Focus:** Multi-component Systems

### Daily Breakdown

| Day | Topic | Time | Resource |
|-----|-------|------|----------|
| Mon | Web scraping basics | 1.5h | BeautifulSoup docs |
| Tue | Project: Web Scraper | 2h | Project 8 |
| Wed | Email templating | 1h | Jinja2 |
| Thu | Project: Email Campaign Generator | 2.5h | Project 13 |
| Fri | - | - | - |

### Checkpoint
- [ ] Scrape structured data
- [ ] Generate templated content
- [ ] Build multi-component tools

### Project Deliverables
- **Project 8: Web Scraper** - Complete
- **Project 13: Email Campaign Generator** - Complete

---

## Week 12: Capstone Projects

**Learning Time:** 8 hours
**Focus:** Prove Technical Autonomy

### Daily Breakdown

| Day | Topic | Time | Resource |
|-----|-------|------|----------|
| Mon | Project 14: Lead Scoring Pipeline (part 1) | 2h | Capstone |
| Tue | Project 14: Lead Scoring Pipeline (part 2) | 2h | Capstone |
| Wed | Project 15: Stratega CLI (part 1) | 2h | Capstone |
| Thu | Project 15: Stratega CLI (part 2) | 2h | Capstone |
| Fri | Final review + documentation | - | - |

### Project Deliverables
- **Project 14: Lead Scoring Pipeline** - Complete end-to-end system
- **Project 15: Stratega CLI Tool** - Working unified interface

---

## Final Assessment

### Technical Autonomy Test

**Can you do these without AI assistance?**

1. **JavaScript** (30 min limit)
   - [ ] Build n8n code node that scores and filters contacts
   - [ ] Handle all edge cases
   - [ ] Clean, readable code

2. **Python** (45 min limit)
   - [ ] Write script to process CSV via command line
   - [ ] Call API and handle errors
   - [ ] Export results

3. **Infrastructure** (20 min limit)
   - [ ] Create Git branch, make changes, merge
   - [ ] Debug Docker container
   - [ ] Query Supabase

4. **Integration** (60 min limit)
   - [ ] Design system connecting 3+ components
   - [ ] Implement one component fully
   - [ ] Document architecture

### Success Criteria

**You've achieved technical autonomy when:**
- [ ] Can read any code in Stratega codebase
- [ ] Can modify existing code confidently
- [ ] Can build new tools independently
- [ ] AI is a helper, not a requirement
- [ ] Debug issues without panic
- [ ] Others can use your tools

---

## Progress Tracker

### Phase 1 Progress
| Week | Status | Projects Done | Notes |
|------|--------|---------------|-------|
| 1 | [ ] | | |
| 2 | [ ] | | |
| 3 | [ ] | | |
| 4 | [ ] | | |

### Phase 2 Progress
| Week | Status | Projects Done | Notes |
|------|--------|---------------|-------|
| 5 | [ ] | | |
| 6 | [ ] | | |
| 7 | [ ] | | |
| 8 | [ ] | | |

### Phase 3 Progress
| Week | Status | Projects Done | Notes |
|------|--------|---------------|-------|
| 9 | [ ] | | |
| 10 | [ ] | | |
| 11 | [ ] | | |
| 12 | [ ] | | |

---

## Quick Reference: Best Learning Resources

### JavaScript
- **Primary:** JavaScript.info (comprehensive, free)
- **Video:** Traversy Media YouTube
- **Reference:** MDN Web Docs

### Python
- **Primary:** Real Python (articles)
- **Book:** Automate the Boring Stuff
- **Data:** Pandas documentation
- **Reference:** Python.org

### n8n
- **Primary:** n8n Documentation
- **Examples:** n8n Community Templates

### Git
- **Primary:** Atlassian Git Tutorial
- **Interactive:** Learn Git Branching (game)

### Docker
- **Primary:** Docker Documentation
- **Practical:** Docker in 100 seconds (Fireship)

---

## Tips for Success

### Do This
- Learn in 30-60 minute focused blocks
- Apply immediately to Stratega work
- Build the projects, don't skip them
- Commit code daily (even if incomplete)
- Ask Claude when stuck (but try first)

### Avoid This
- Tutorial hell (watching without doing)
- Perfect code paralysis (ship, then improve)
- Skipping fundamentals (they compound)
- Learning in isolation (apply to real work)

### When Stuck
1. Read the error message carefully
2. Search the specific error
3. Check documentation
4. Ask Claude with context
5. If still stuck after 20 min, move on and return later

---

*90-Day Roadmap v1.0 - November 2025*
