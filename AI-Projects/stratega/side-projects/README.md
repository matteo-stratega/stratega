# Stratega Side Projects

This folder contains standalone side projects, each with its own mini Stratega structure.

---

## Active Projects

### Off the Curious Path
**Type:** Barcelona city guide CMS
**Status:** MVP development (70% complete)
**Client:** Solo content curator
**Stack:** React + Supabase + Mapbox

**Location:** `off-the-path/`

---

## Folder Structure (Per Project)

Each side project follows this pattern:

```
project-name/
├── codebase/          # Source code
├── docs/              # Strategic documents, reports, specs
├── notes/             # Session summaries, daily notes
├── CLAUDE.md          # AI operating instructions
├── README.md          # Project overview
└── .claude-startup    # Quick startup guide
```

---

## Working on a Side Project

**From main Stratega workspace:**
```bash
cd side-projects/[project-name]/
```

**Tell Claude:**
```
Lavoriamo su [Project Name].
Carica [project-name]/README.md e latest notes.
```

---

## Session Summaries

- Main Stratega sessions → `notes/daily-summaries/`
- Side project sessions → `side-projects/[name]/notes/`

Don't duplicate — keep summaries local to each workspace.

---

*Last updated: 25 Nov 2025*
