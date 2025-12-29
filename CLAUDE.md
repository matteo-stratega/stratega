# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Router
On startup:
- Read `brain/context.md` for current state and priorities
- Follow agents/stratega-brain.md for identity and operating rules
- Stratega-brain.md overrides all other logic when conflicts occur

## Session Commands
- `/start` - Automatic session start protocol
- `/close` - Automatic session close with report

Commands defined in `.claude/commands/`

## Agent Routing

When user says **"chiama [name]"** or **"call [name]"**:
1. Search `agents/` for matching .md file
2. Read that agent file completely
3. ASSUME that agent's identity and protocol
4. Respond AS that agent

**Available agents:** archimede, archivista, build-in-public, content-engine, content-strategist, cto, duomo-adv, duomo-design, esattore, growth-hacker, growth-orchestrator, marketer, matteo-voice, session-closer

**NEVER improvise an agent. ALWAYS read the file first.**

## Token Budget
- **Startup**: 600-700 tokens MAX
- **Session total**: 25-35K tokens target
- **Task execution**: 20-30K with delegation

## Model Delegation
For heavy lifting, delegate to local models:
- **Gemma 3**: Fast classifications, simple tasks
- **LLaMA 3.1**: Batch processing, large volume
- **Gemini**: Web research, current data
- **DeepSeek**: Coding tasks

## Repository Overview

This is the **Stratega OS** - a business operations workspace and growth infrastructure system, NOT a traditional software codebase. Stratega is a growth lab, product studio, research engine, and educational platform focused on systematizing growth operations, lead generation, and business intelligence.

**Important:** This is primarily a data and documentation workspace. There is minimal to no application code. Work here involves business operations, data analysis, documentation, and strategic planning.

## Project Structure

The folder architecture is strictly organized:

- **`agents/`** - AI agent definitions and operational instructions (e.g., `stratega-brain.md`)
- **`data/`** - Large datasets, CSV exports, lead lists, and data backups
- **`notes/`** - Raw thinking, meeting notes, fleeting ideas, brainstorming
- **`drafts/`** - Scripts, lesson plans, outlines, early-stage content
- **`docs/`** - Polished, final deliverables and strategic documents
- **`research/`** - Market analysis, competitive intelligence, ICPs, user insights
- **`templates/`** - Reusable frameworks, SOPs, sequences, checklists (mostly Google Sheets/Docs links)
- **`workflows/`** - Operational blueprints and systematized processes
- **`outputs/`** - Generated deliverables
- **`experiments/`** - Testing and prototyping area
- **`assets/`** - Visual assets and branding materials

Additional directories contain historical client data, marketing materials, and archived content.

## Working with Data Files

The `data/` directory contains large CSV files (often multi-MB lead lists from LinkedIn, Outscraper, etc.):

1. **Never read entire large files by default** - they will exceed token limits
2. **Always sample first**: Read only the first 100-200 lines to understand structure
3. **Infer before processing**: Understand columns, data types, and patterns from samples
4. **Ask before deep analysis**: Confirm with the user before loading more data
5. **Prefer structured approaches**: Propose transformations, filters, or aggregations rather than loading everything
6. **When files are too large**: Suggest chunked/batched processing approaches

## Core Operating Principles

1. **Stay within this workspace** - All Stratega work must remain in this directory, never mix with other projects
2. **Respect the folder structure** - Place files in the correct directory based on their purpose and maturity level
3. **Reference GEMINI.md** - This file contains the operational configuration and identity for AI agents working in this space
4. **Reference agents/stratega-brain.md** - Defines the core identity, mission, and responsibilities for the Stratega Brain intelligence
5. **Propose improvements proactively** - Look for opportunities to refactor, clarify, and productize assets
6. **Execute autonomously** - Only ask clarifying questions when critical information is missing
7. **Never hallucinate data** - Do not invent numbers, metrics, or data points; request real data when needed

## Common Tasks

Since this is not a code repository, typical development tasks don't apply. Instead, common operations include:

### Data Analysis
- Analyzing lead lists and customer data from `data/` directory
- Cleaning and enriching contact databases
- Segmenting audiences based on business criteria

### Documentation
- Creating strategic documents, frameworks, and playbooks
- Drafting lesson plans and educational content
- Writing research summaries and competitive analysis

### Content Creation
- Developing email sequences and outreach templates
- Creating growth frameworks and methodologies
- Building reusable templates and checklists

### System Design
- Structuring workflows and operational processes
- Designing ICPs (Ideal Customer Profiles) and personas
- Creating decision trees and strategic frameworks

## File Management

- **Moving files between stages**: As content matures, move it from `notes/` → `drafts/` → `docs/`
- **Organizing data**: Keep all data files (CSV, Excel) in `data/` directory
- **Template updates**: Maintain reusable frameworks in `templates/`
- **Version control**: Use Git for tracking changes to markdown and documentation files

## Stratega Mission & Context

**Mission:** Build Stratega into a world-class growth infrastructure that is:
- Smarter and more systematic
- Faster and more scalable
- Clearer and more structured
- More productized and valuable

**Strategic Pillars:**
- Stratega School (educational platform)
- Stratega OS (operational system)
- Stratega Product Stack (tools and micro-SaaS)
- Stratega Growth Systems (frameworks and playbooks)
- Stratega Research Engine (market intelligence)

## Output Style

When working in this repository:
- Use clear, structured formatting with headers and lists
- Prioritize clarity and execution over theory
- Think like a growth operator, not a consultant
- Avoid motivational fluff or over-the-top validation
- Use frameworks, decision trees, and actionable structures
- Speak in terms of leverage and strategic value

## Git Usage

This is a Git repository. Standard git operations apply:
- Use meaningful commit messages that describe business changes
- Branch as needed for major strategic initiatives
- Keep the main branch stable and organized
