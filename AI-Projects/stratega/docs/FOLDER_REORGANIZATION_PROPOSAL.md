# Stratega Folder Reorganization Proposal

**Data:** 9 Dicembre 2025
**Status:** Pending Approval

---

## Problemi Identificati

### 1. Cartelle Duplicate / Confuse

| Problema | Path | Azione |
|----------|------|--------|
| `stratega/stratega/` | Nested folder con solo `notes/` | DELETE |
| `Users/matteolombardi/` | Errore di path, contiene altro `AI-Projects` | DELETE |
| `workflows/` vs `n8n-workflows/` | Due cartelle workflow | MERGE → `workflows/` |
| `task/` vs `notes/daily-summaries/` | Due posti per daily summaries | MERGE → `notes/daily-summaries/` |

### 2. File Duplicati

| File | Posizione 1 | Posizione 2 | Azione |
|------|-------------|-------------|--------|
| `AI-Code-Tools-Analysis-Dec2025.md` | `/` (root) | `/notes/` | KEEP notes/, DELETE root |

### 3. File nella Root che Non Dovrebbero Essere Lì

| File | Dove Dovrebbe Andare |
|------|---------------------|
| `AI-Code-Tools-Analysis-Dec2025.md` | `notes/` (già presente) |
| `SESSION_START.md` | `notes/daily-summaries/` o DELETE |
| `START_HERE.md` | `docs/` o DELETE (obsoleto?) |

### 4. Struttura `docs/` Troppo Frammentata

**Attuale (11 sottocartelle):**
```
docs/
├── cleanup-reports/     # 10 file - report di cleanup passati
├── financial/           # 5 file
├── guides/              # 9 file - guide tecniche
├── lead-gen-crash-course/  # 8 file - contenuto Academy
├── planning/            # 5 file
├── reference/           # 4 file
├── sessions/            # 11 file - report sessioni
├── strategy/            # 7 file
├── technical/           # 8 file
├── workflows/           # 4 file
└── 12 file .md in root docs/
```

**Problema:** Troppe sottocartelle, file sparsi, overlap con altre cartelle

### 5. Confusione Academy

| Cartella | Contenuto | Problema |
|----------|-----------|----------|
| `stratega-academy/` | Moduli, transcript, docs | OK ma ha file sparsi nella root |
| `docs/lead-gen-crash-course/` | Contenuto corso | Dovrebbe essere in `stratega-academy/` |

### 6. Daily Summaries in Due Posti

- `notes/daily-summaries/` → 24 file (ATTIVO)
- `task/daily-summaries/` → 1 file (OBSOLETO)

---

## Proposta di Riorganizzazione

### Struttura Target

```
stratega/
│
├── .claude/                    # Config Claude (keep)
├── .obsidian/                  # Config Obsidian (keep)
├── CLAUDE.md                   # Router (keep)
├── GEMINI.md                   # Config (keep)
│
├── agents/                     # AI agents definitions (keep as is)
│
├── academy/                    # RENAME da stratega-academy/
│   ├── modules/                # Moduli corso
│   ├── transcripts/            # Transcript
│   └── docs/                   # Docs specifici academy
│
├── archive/                    # Keep as is (già organizzato)
│
├── assets/                     # Keep as is
│
├── data/                       # Keep as is (lead lists, CSV)
│
├── docs/                       # SIMPLIFY
│   ├── guides/                 # How-to guides
│   ├── reports/                # Cleanup, sessions, financial reports
│   └── strategy/               # Strategic docs, ICP, planning
│
├── notes/                      # SIMPLIFY
│   ├── daily/                  # RENAME da daily-summaries
│   └── ideas/                  # Raw thinking, fleeting notes
│
├── outputs/                    # Keep as is (deliverables)
│
├── projects/                   # Keep as is (client work)
│
├── research/                   # Keep as is
│
├── scripts/                    # Keep as is
│
├── templates/                  # Keep as is
│
└── workflows/                  # MERGE n8n-workflows + workflows
    ├── n8n/                    # JSON workflow files
    └── docs/                   # Workflow documentation
```

### Cartelle da ELIMINARE

1. `stratega/stratega/` - nested error
2. `Users/` - path error
3. `task/` - merge in notes/daily
4. `n8n-workflows/` - merge in workflows/
5. `drafts/` - quasi vuota, merge in notes/
6. `tmp/` - temporanea, svuotare
7. `side-projects/` - spostare in `projects/side/`

### File da Spostare/Eliminare

| File | Da | A |
|------|-----|-----|
| `AI-Code-Tools-Analysis-Dec2025.md` | root | DELETE (duplicato) |
| `SESSION_START.md` | root | DELETE (obsoleto) |
| `START_HERE.md` | root | `docs/` o DELETE |

---

## Azioni Concrete (Se Approvi)

### Fase 1: Cleanup Immediato (5 min)
```bash
# Delete nested errors
rm -rf stratega/stratega/
rm -rf Users/

# Delete root duplicates
rm AI-Code-Tools-Analysis-Dec2025.md
rm SESSION_START.md
rm START_HERE.md
```

### Fase 2: Merge Cartelle (10 min)
```bash
# Merge task/daily-summaries → notes/daily-summaries
mv task/daily-summaries/* notes/daily-summaries/
rm -rf task/

# Merge n8n-workflows → workflows
mv n8n-workflows/* workflows/
rm -rf n8n-workflows/
```

### Fase 3: Rename Academy (5 min)
```bash
mv stratega-academy academy
```

### Fase 4: Simplify Docs (15 min)
```bash
# Merge cleanup-reports + sessions + financial → reports/
mkdir -p docs/reports
mv docs/cleanup-reports/* docs/reports/
mv docs/sessions/* docs/reports/
mv docs/financial/* docs/reports/
# ... etc
```

---

## Decisione Richiesta

**Opzioni:**

| Opzione | Scope | Tempo | Rischio |
|---------|-------|-------|---------|
| **A) Quick Clean** | Solo Fase 1-2 (delete errori + merge) | 15 min | Basso |
| **B) Full Reorg** | Tutte le fasi | 45 min | Medio |
| **C) Review First** | Tu guardi i file prima di delete | 30 min | Nullo |

**Raccomandazione Metis:** Opzione A (Quick Clean) - risolve i problemi più evidenti senza toccare troppo

---

## Note

- Questo non tocca `archive/` (già sistemato)
- Non tocca `data/` (lead lists separate)
- Non tocca `templates/` (Google links)
- Backup automatico via Git se serve rollback

---

**Attendo tua decisione.**
