### Modello di Lavoro per la Generazione del Report "Chi Ricontattare" (Versione Avanzata)

**Obiettivo:** Identificare e prioritizzare i lead da ricontattare, fornendo un contesto operativo conciso e actionable per l'advisor, con maggiore flessibilità nell'acquisizione e ricerca dei dati.

---

**Fase 0: Inizializzazione e Selezione Fonte Dati**

1.  **Selezione Fonte:** Decidere il punto di partenza per l'identificazione dei lead:
    *   **A) Lista Esterna:** Un file (CSV, Google Sheet, etc.) contenente i lead.
    *   **B) Query CRM Diretta:** Una ricerca diretta nel CRM (es. "tutte le aziende in Svizzera con X proprietà").
2.  **Parametri di Ricerca (se B):** Se si parte dal CRM, definire i criteri specifici per la query (es. paese, settore, data ultima attività, stato del lead).

---

**Fase 1: Raccolta e Preparazione Dati Iniziali**

1.  **Input (se A):** Per ogni lead dalla lista esterna, estrarre:
    *   Nome del lead/azienda.
    *   Link/ID al record CRM (es. HubSpot).
    *   Note o status testuali sull'ultima interazione (es. colonne "Where we are", "Notes").
2.  **Input (se B):** Per ogni lead dalla query CRM, estrarre:
    *   Nome del lead/azienda.
    *   ID del record CRM.
    *   Proprietà rilevanti per la categorizzazione.
3.  **Parsing:** Estrarre e normalizzare le informazioni chiave da ogni record.

---

**Fase 2: Normalizzazione e Arricchimento Dati (Ricerca Robustata nel CRM)**

1.  **Ricerca Primaria CRM:** Per ogni lead, tentare di trovare il record corrispondente nel CRM (es. HubSpot) usando l'ID fornito (se disponibile) o il nome esatto.
2.  **Strategia di Routing (se ricerca primaria fallisce o non è sufficiente):** Se il record non viene trovato, l'ID è obsoleto/errato, o si necessitano più dati:
    *   **Ricerca Alternativa 1 (Nome Flessibile):** Tentare la ricerca per nome con operatori più flessibili (es. "contiene" invece di "uguale a").
    *   **Ricerca Alternativa 2 (Identificativi Secondari):** Se disponibili, usare altri identificativi (es. dominio del sito web, numero di telefono, email) per la ricerca.
    *   **Ricerca Alternativa 3 (Proprietà Custom):** Considerare la ricerca per proprietà custom o tag specifici del CRM.
    *   **Gestione Fallimento:** Se tutte le ricerche falliscono, marcare il lead come "Non Trovato nel CRM" e procedere con le sole informazioni disponibili dalla fonte iniziale.
3.  **Arricchimento Dati:** Recuperare proprietà aggiuntive dal CRM che potrebbero essere utili per la categorizzazione o il brief (es. `hs_last_sales_activity_date`, `notes_last_contacted`, `hs_associated_company_id` per i contatti).

---

**Fase 3: Categorizzazione dei Lead (Hot/Cold)**

1.  **Criteri di Classificazione:** Analizzare le note testuali (dalla fonte iniziale e/o dal CRM) e le proprietà arricchite per identificare parole chiave di interesse o disinteresse.
    *   **Hot List:** Lead con segnali positivi (es. "interessato", "risposto", "parlato con", "call", "meeting", "deck inviato", "follow up richiesto").
    *   **Cold List:** Lead con segnali negativi o assenza di interazione (es. "nessuna risposta", "mai risposto", "non interessato", "non contattare", "tempismo sbagliato", "mai contattato").
2.  **Output:** Due liste distinte di lead.

---

**Fase 4: Approfondimento CRM e Analisi della "Catena Rotta" (per Hot List)**

1.  **Recupero Attività Associate:** Utilizzare le API del CRM per recuperare tutte le attività associate al record (note, email, chiamate, meeting).
2.  **Analisi Cronologica:** Ordinare le attività per data (dalla più recente alla più vecchia).
3.  **Identificazione "Catena Rotta":** Analizzare il contenuto delle ultime attività per determinare:
    *   Qual è stata l'ultima interazione significativa.
    *   Qual era il passo successivo atteso.
    *   Perché la conversazione si è interrotta (es. in attesa di feedback dal lead, problema interno del lead, mancanza di follow-up).
4.  **Generazione Brief Operativo:** Creare un riassunto conciso (2-3 righe) che includa:
    *   Data dell'ultima interazione.
    *   Contenuto chiave dell'ultima interazione.
    *   Motivo dell'interruzione.
    *   Azione suggerita per riprendere.

---

**Fase 5: Compilazione del Report Finale**

1.  **Struttura:** Organizzare il report in due sezioni chiare: "Priorità 1 (Hot List)" e "Priorità 2 (Cold List)".
2.  **Dettagli per Hot List:** Per ogni lead, includere:
    *   Nome Squadra
    *   Priorità
    *   Contesto (dal dato iniziale)
    *   Brief (generato dalla Fase 4)
    *   Azione Consigliata (derivata dal Brief)
    *   Link al CRM
3.  **Dettagli per Cold List:** Per ogni lead, includere:
    *   Nome Squadra
    *   Priorità
    *   Contesto (dal dato iniziale)
    *   Link al CRM (se disponibile)
4.  **Formato:** Presentare il report in un formato leggibile e condivisibile (es. Markdown).
