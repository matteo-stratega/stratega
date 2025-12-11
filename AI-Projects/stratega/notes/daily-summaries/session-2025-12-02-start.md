# Session Start - 2 Dicembre 2025

## Contesto
Continuazione lavoro su workflow n8n `content-gen-prod` per generazione articoli blog.

---

## Stato Ereditato dalla Sessione Precedente

### Completato
- Setup MCP n8n
- Fix JSON parsing (backticks)
- Fix troncamento output (schema ridotto)
- Switch a Claude Haiku 3.5
- Aggiunto 27 colonne a tabella `blog_pages`
- Primo articolo generato (id: 1, keyword: "B2B lead generation without ads")

### Da Fare
| Priorità | Task | Tempo Stimato |
|----------|------|---------------|
| 1 | Migliorare qualità articolo (less AI, more human) | 1h |
| 2 | Ripristinare schema completo (PAA, Sources, FAQ) | 30min |
| 3 | Test su 2-3 keyword diversi | 30min |
| 4 | Deploy in produzione | 15min |

**Tempo totale stimato: ~2 ore**

---

## Risorse

### Crediti Disponibili
- Anthropic: ~$1.60 rimanenti
- Gemini: Quota reset (50 req/day)

### Link Utili
- Workflow: https://n8n.pickeat.cc/workflow/gQxLO22JXLBPc4Hp
- Supabase: https://supabase.com/dashboard → progetto content-gen-prod
- Articolo test: `blog_pages` id: 1

### Pinned Data
- `gemini-research` e `set_field_names` hanno dati pinnati per testing

---

## Obiettivo Sessione
Portare la qualità degli articoli a livello "human-made" per vendita B2B.

**Target:** Articoli che non sembrano scritti da AI.

---

## Prima Azione Suggerita
1. Leggere articolo generato (id: 1) in Supabase
2. Identificare pattern "AI-like" da eliminare
3. Modificare prompt Gemini per tono più naturale

---

*Pronto per iniziare quando vuoi.*
