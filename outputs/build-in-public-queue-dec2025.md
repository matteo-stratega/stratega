# Build in Public - Content Queue
**Periodo:** 14 Nov - 5 Dic 2025
**Posts pronti:** 17

---

## WEEK 1 (Post subito)

### Post 1: MCP + Docker (FATTO 5/12)
"What if you could give your AI superpowers?"
- Status: Pubblicato

### Post 2: ICP Scoring Algorithm
**Hook:** "Ho costruito un algoritmo che ha analizzato 4,716 connessioni LinkedIn in 30 secondi."

**Body:**
- Game theory + weighted scoring
- Risultato: 27 "hidden gems" (0.6%)
- 99.4% del mio network? Freddo.
- La metrica chiave: numero messaggi > recency

**Visual:** Screenshot dello scoring o tabella top 10

**CTA:** "Vuoi lo scoring del tuo network? DM"

---

### Post 3: Token Optimization (Technical)
**Hook:** "Ho bruciato 110K token in una sessione Claude. Poi ho fatto un fix."

**Body:**
- Problema: Claude caricava 33K token all'avvio
- Fix: SESSION_START.md - max 600 token
- Risultato: Da 110K a 48K per sessione (-56%)
- Il trick: caricare documenti SOLO quando servono

**CTA:** "Quanto spendi in token? Commenta"

---

## WEEK 2

### Post 4: n8n + Claude Content Pipeline
**Hook:** "Ho automatizzato la scrittura di articoli SEO. Tempo: 5 minuti per articolo."

**Body:**
- Stack: n8n + Claude Haiku + Supabase
- Input: keyword
- Output: headline, 9 sezioni, FAQ, meta
- Costo: ~$0.15 per articolo
- Il percorso: 8 nodi Gemini → Claude (quota esaurita Gemini, pivot forzato)

**Visual:** Screenshot workflow n8n

**CTA:** "Template workflow in DM"

---

### Post 5: Agent Architecture
**Hook:** "Ho 8 agenti AI che lavorano per me. Si parlano tra loro."

**Body:**
- Mike (L'Esattore): Head of Sales - segue come mia madre
- Archimede: CTO
- Content Engine: 20+ post/settimana
- Growth Hacker: Esperimenti
- Archivista: Organizza tutto
- Build in Public: Documenta il journey

**Visual:** Diagram degli agenti

**CTA:** "Quale agente vorresti? Commenta"

---

### Post 6: Drive Cleanup (Relatable)
**Hook:** "Avevo 303 file nella root. Ora ne ho 97."

**Body:**
- Il mio Google Drive era un disastro
- Ho delegato a un agente AI (Archivista)
- 2 round di pulizia automatica
- 66% reduction nei CSV (169→58)
- Symlink Obsidian + GitHub = source of truth

**CTA:** "Il tuo Drive com'è messo? 1-10"

---

## WEEK 3

### Post 7: MCP Debugging Saga (Fail Story)
**Hook:** "Ho passato 2 ore a debuggare Docker MCP. Poi ho scoperto che il disco era corrotto."

**Body:**
- Volevo collegare Claude a LinkedIn e HackerNews
- Errori ovunque. Log incomprensibili.
- La causa: blob Docker corrotto
- Il fix: rm -rf + reset

**Lesson:** A volte il problema non è il codice, è l'infrastruttura

**CTA:** "Qual è stato il tuo debug più frustrante?"

---

### Post 8: DM Campaign Results (Social Proof)
**Hook:** "Ho mandato 30 DM a founder. 14 hanno risposto. Ecco cosa ho imparato."

**Body:**
- Reply rate: 47%
- Top converter: Ultra-warm (50+ messaggi storici)
- Worst: Cold outreach
- Il template che ha funzionato: [snippet]
- L'errore: Non ho incluso Alex Roggero (bug nell'algoritmo → fix)

**CTA:** "Qual è il tuo reply rate sui DM?"

---

### Post 9: Financial Reality Check
**Hook:** "MRR attuale: €849. Gap mensile: -€251. Ecco il piano."

**Body:**
- Duomo Design = unico cliente ricorrente
- 3 low hanging fruits identificati
- Crono Expert: €400-800
- n8n Templates: €290-500
- School Paid: €490-735
- Target: €1,299-1,599 entro fine anno

**CTA:** "Come monetizzi le tue skills?"

---

## WEEK 4

### Post 10: Gemini → Claude Pivot
**Hook:** "Avevo un workflow perfetto con Gemini. Poi ho finito la quota gratuita."

**Body:**
- 50 request/day free = niente
- 8 nodi da convertire
- 3 ore di tentativi falliti
- Fix finale: Task agent + conversione programmatica
- Lesson: Diversifica i provider AI

**CTA:** "Quale AI usi di più?"

---

### Post 11: Obsidian as Source of Truth
**Hook:** "Ho smesso di usare Notion per lavoro. Ecco perché."

**Body:**
- Obsidian = locale, veloce, markdown puro
- Sync con GitHub
- Symlink con Google Drive
- Claude Code legge direttamente i file
- MCP integration

**CTA:** "Notion o Obsidian? (Fight)"

---

### Post 12: Return to Building in Public
**Hook:** "Sono sparito da LinkedIn per 6 mesi. Ecco cosa ho costruito in silenzio."

**Body:**
- Stratega OS: sistema operativo per growth
- 8 agenti AI
- ICP scoring algorithm
- Content automation pipeline
- €849 MRR (da zero)

**CTA:** "Torno a buildare in public. Follow along."

---

## NEW - Week of 12 Dec

### Post 13: Tool Friday Obsidian + AI Brain (PUBBLICATO 12/12)
**Hook:** "This is where my AI works."

**Angle:** Obsidian non come "second brain" ma come **AI brain** - shared workspace tra te e Claude Code

**Status:** Video registrato e pubblicato su LinkedIn

---

### Post 14: Content Distribution Problem (PIPELINE)
**Hook:** "Ho pubblicato un video su LinkedIn. Poi ho aperto YouTube, Twitter, Instagram... e ho capito che sono fottuto."

**Body:**
- Il problema: ogni piattaforma vuole formato diverso
- LinkedIn: post nativo + descrizione
- YouTube: description + tags + capitoli
- Twitter/X: thread o clip + caption
- Newsletter: embed + CTA + context
- Instagram: vertical + hashtags + caption
- TikTok: hook diverso, ritmo diverso

**La mia soluzione (in costruzione):**
- Master content → n8n workflow → versioni ottimizzate per ogni piattaforma
- Input: 1 video + script
- Output: 6 formati pronti

**Status:** Building this now

**CTA:** "Chi l'ha già automatizzato? Come?"

**Source:** `notes/PIPELINE_IDEAS.md`

---

### Post 15: Tool Friday Production System (Behind the Scenes)
**Hook:** "Ho scritto uno script, l'ho fatto roastare da un AI, poi l'ho riscritto. In 1 giorno."

**Body:**
- Tool Friday #4: Obsidian
- Step 1: Script v1 (generico "second brain")
- Step 2: AI roast verdict: 4/10 (ouch)
- Step 3: Rewrite con angle diverso → 8.5/10
- Il pivot: da "note-taking app" a "where my AI actually works"
- Demo vault creato: 17 note interconnesse come esempio
- Registrato + pubblicato stesso giorno

**Key insight:** "Your brain works like this. Now your workspace does too."

**Visual:** Before/after script comparison, graph view screenshot

**CTA:** "Fai roastare i tuoi contenuti da AI? Che tool usi?"

**Source:** `outputs/content-engine/tool-friday-obsidian-script.md`

---

### Post 16: Academy Beta Results
**Hook:** "Ho mandato 23 DM a founder. 20 hanno detto sì. 87% reply rate."

**Body:**
- Non ho venduto niente
- Ho chiesto feedback su un corso gratuito
- Template: "validate, don't sell"
- Il segreto: suona come parleresti al bar
- Risultato: 20 beta tester in 10 giorni

**Visual:** Screenshot tracking table

**CTA:** "Qual è il tuo reply rate sui DM? (onesto)"

---

### Post 15: Matteo Voice Agent (System Build)
**Hook:** "Ho costruito un agente AI che scrive come me."

**Body:**
- Problema: copy delle email troppo generico
- Soluzione: agente che conosce il mio stile dai video
- Input: transcript delle mie lezioni
- Output: checklist + riscrittura automatica
- Regola #1: "What would you say at a bar?"

**Key insight:** "Validate, don't sell" - mai vendere, sempre validare

**CTA:** "Hai mai provato a clonare il tuo stile di scrittura?"

---

### Post 16: Email Segmentation (Behind the Scenes)
**Hook:** "Avevo 39 studenti da ricontattare. Ho fatto 4 campagne diverse."

**Body:**
- Errore comune: stessa email a tutti
- Il mio approccio:
  - Chi ha iniziato ITA (7) → chiedo feedback specifico
  - Chi ha iniziato ENG (10) → chiedo feedback specifico
  - Chi non ha iniziato ITA (16) → chiedo perché
  - Chi non ha iniziato ENG (6) → chiedo perché
- Ogni email ha un obiettivo diverso
- "Che cazzo di mail è? Non dice niente" - me stesso, 2 ore fa

**CTA:** "Quante versioni fai delle tue email?"

---

### Post 17: Ethical Pact (NEW - 13 Dec)
**Hook:** "My AI has a contract with me. Here are the 6 rules it must follow."

**Body:**
1. Trasparenza - ammette quando non sa
2. Autonomia utente - propone, non decide
3. Privacy - minimizza i dati richiesti
4. Responsabilità reciproche - chi fa cosa
5. Limiti chiari - no decisioni finanziarie/legali
6. Correzione errori - ammette e impara

**Key insight:** "The meta-story: an AI helped me write rules for AIs"

**Visual:** Screenshot dell'Ethical Pact section

**CTA:** "Hai mai pensato a regole per il tuo AI?"

**Source:** `docs/PERSONAL_AGENT_SETUP_TEMPLATE.md` → Section 4

**Status:** Ready to publish

---

### Post 18: Session Start Protocol (NEW - 13 Dec)
**Hook:** "Ho bruciato 110K token in una sessione. Poi ho scritto 10 righe che hanno cambiato tutto."

**Body:**
- Problema: Claude caricava 33K token all'avvio "just in case"
- Fix: SESSION_START.md - budget 600 token MAX
- Le 4 regole:
  1. Read weekly tasks (50 lines)
  2. Read daily prep (30 lines)
  3. Propose priorities
  4. STOP. Wait for answer.
- Risultato: -56% token usage

**Visual:** Before/after token comparison

**CTA:** "Quanto spendi in token per sessione?"

**Source:** `docs/PERSONAL_AGENT_SETUP_TEMPLATE.md` → Section 1

**Status:** Ready to publish

---

### Post 19: AI Memory Layer (NEW - 13 Dec)
**Hook:** "Il tuo AI dimentica tutto tra una sessione e l'altra. Il mio no."

**Body:**
- 4 file che cambiano tutto:
  - context.md - chi sei, progetti attivi
  - preferences.md - come lavori
  - learnings.md - errori passati
  - relationships.md - persone chiave
- L'AI li aggiorna, tu li revisioni
- Risultato: zero "ricordami chi sei" ogni sessione

**Visual:** Screenshot folder structure

**CTA:** "Come dai memoria al tuo AI?"

**Source:** `docs/PERSONAL_AGENT_SETUP_TEMPLATE.md` → Section 2 (Memory Layer)

**Status:** Ready to publish

---

### Post 20: Multi-Model Delegation (NEW - 13 Dec)
**Hook:** "Non uso un AI. Ne uso 4. Ognuno fa quello che sa fare meglio."

**Body:**
- Claude: orchestrazione, decisioni, editing finale
- Gemini: web research, large context
- Local (Ollama): batch tasks, ripetitivi
- DeepSeek: coding

**Delegation triggers:**
- Task > 5 min processing → Gemini
- Batch > 50 items → Local
- Codice complesso → DeepSeek
- Mai delegare: decisioni finali

**Visual:** Tabella ruoli

**CTA:** "Quanti AI usi? Come li dividi?"

**Source:** `docs/PERSONAL_AGENT_SETUP_TEMPLATE.md` → Section 3

**Status:** Ready to publish

---

### Post 21: The AI Operating System (Series Wrap-up)
**Hook:** "In 2 mesi saremo una bomba. Ecco il sistema che stiamo costruendo."

**Body:**
- Non è prompt engineering
- È un vero OS per lavorare con AI:
  - Startup protocol (token efficiency)
  - Memory layer (persistent context)
  - Delegation rules (multi-model)
  - Ethical pact (guardrails)
- Manca tanto, ma le fondamenta ci sono
- Build in public: vi mostro tutto

**CTA:** "Vuoi il template completo? Link in comments"

**Source:** `docs/PERSONAL_AGENT_SETUP_TEMPLATE.md` → Full doc

**Status:** Series finale - da pubblicare dopo i 4 precedenti

---

### Post 22: Crono Data Enrichment (NEW - 16 Dec)
**Hook:** "Avevo 39 contatti da importare su Crono. Ne ho importati 20. Ecco perché."

**Body:**
- Errore #1: Non ho checkato le sovrapposizioni con i DM (16 duplicati)
- Errore #2: Ho messo italiani nelle liste inglesi (Lorenzo Rea, Alessandro Vestito)
- Errore #3: Avrei dovuto chiedere prima di includere
- La lezione: cross-check SEMPRE prima di creare liste
- Il fix: enrichment automatico da LinkedIn connections + company lookup

**Key insight:** "L'automazione senza validazione è solo errori più veloci"

**CTA:** "Qual è l'errore più stupido che hai fatto con le liste contatti?"

**Status:** Ready to publish

---

### Post 23: LinkedIn Connections as CRM (NEW - 16 Dec)
**Hook:** "Ho 4,716 connessioni LinkedIn. Le ho trasformate in un CRM."

**Body:**
- Export connessioni → CSV scored
- Algoritmo: engagement + seniority + company + recency
- Risultato: company, position, LinkedIn URL per ogni contatto
- Uso: enrichment automatico per qualsiasi lista
- Il trucco: grep nel CSV invece di web search

**Visual:** Screenshot del CSV scored

**CTA:** "Come usi le tue connessioni LinkedIn?"

**Status:** Ready to publish

---

## NEXT ACTIONS

**Per me (Build in Public Agent):**
- [ ] Ricevere stile di scrittura + vecchi post da Matteo
- [ ] Adattare tone of voice
- [ ] Aggiungere visual suggestions

**Per Matteo:**
- [ ] Fornire 5-10 vecchi post LinkedIn come reference
- [ ] Scegliere 3 post da pubblicare questa settimana
- [ ] Feedback su quale stile preferisce

---

## FREQUENZA SUGGERITA

| Giorno | Post |
|--------|------|
| Lunedì | Tool/Tech discovery |
| Mercoledì | Behind the scenes / Fail |
| Venerdì | Win / Results |

**Target: 3 post/settimana**

---

*Build in Public Agent - Stratega*
*Queue generata: 5 Dicembre 2025*
