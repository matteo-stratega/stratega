# Task Parallelism Guide

**Purpose:** Quando e come usare il Task tool per massimizzare efficienza

---

## Quando usare Task tool

### ✅ USA Task per:

1. **Ricerche multiple indipendenti**
   - "Cerca info su competitor A, B, C"
   - → 3 Task in parallelo, ognuno su un competitor

2. **Analisi file multipli**
   - "Analizza questi 5 report"
   - → 5 Task in parallelo, poi sintesi

3. **Esplorazione codebase**
   - "Trova dove viene gestito X"
   - → Task con Explore agent (più veloce di grep manuale)

4. **Content generation batch**
   - "Scrivi 3 varianti di questo post"
   - → 3 Task in parallelo con prompt diversi

5. **Ricerca web**
   - "Trova pricing dei competitor"
   - → Task con WebSearch per ogni competitor

### ❌ NON usare Task per:

1. **Operazioni sequenziali dipendenti**
   - Se step 2 dipende da output step 1 → fai sequenziale

2. **File singolo/semplice**
   - Leggi direttamente con Read, non delegare

3. **Domande semplici**
   - Se puoi rispondere in 2 secondi, non creare Task

4. **Operazioni che modificano file**
   - Task agents sono per ricerca/analisi, usa Edit/Write direttamente

---

## Subagent Types

| Type | Use For |
|------|---------|
| `Explore` | Codebase exploration, file search, understanding structure |
| `general-purpose` | Complex multi-step tasks, research |
| `Plan` | Implementation planning, architecture decisions |
| `claude-code-guide` | Questions about Claude Code features |

---

## Pattern: Parallel Research

**Scenario:** Devi analizzare 3 competitor

**Sequenziale (lento):**
```
1. Task: research competitor A → wait → result
2. Task: research competitor B → wait → result
3. Task: research competitor C → wait → result
Total: 3x wait time
```

**Parallelo (veloce):**
```
1. Task A + Task B + Task C (tutti insieme)
2. Wait once
3. Synthesize results
Total: 1x wait time
```

**Come farlo:** Metti tutti i Task nella stessa function_calls block

---

## Pattern: Research → Action

**Scenario:** Devi capire come funziona X, poi modificarlo

**Corretto:**
```
1. Task (Explore): "Come funziona X?"
2. [Aspetta risultato]
3. Edit: applica modifica basata su risultato
```

**Sbagliato:**
```
1. Task: "Trova e modifica X"
   ❌ Task non può modificare file
```

---

## Pattern: Roast Cycle

**Scenario:** Scrivi contenuto e vuoi feedback

```
1. Write: crea draft
2. Task: "Valuta questo contenuto 1-10, dai feedback specifico"
3. [Se <8.5] Edit: applica feedback
4. [Repeat step 2-3 until ≥8.5]
```

---

## Quick Reference

| Situazione | Approccio |
|------------|-----------|
| 1 file da leggere | Read diretto |
| 3+ file da analizzare | Task paralleli |
| Cercare pattern nel codebase | Task Explore |
| Modificare file | Edit/Write diretto |
| Ricerca web multipla | Task paralleli con WebSearch |
| Domanda su Claude Code | Task claude-code-guide |
| Planning complesso | Task Plan |

---

## Costi & Performance

- Ogni Task consuma tokens separatamente
- Parallelo = più tokens ma meno tempo
- Per task semplici, diretto è meglio
- Per task complessi, Task è più robusto

---

*Last updated: 17 Dec 2025*
