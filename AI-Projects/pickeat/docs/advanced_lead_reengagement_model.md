### Advanced Lead Re-engagement Report Generation Model

**Objective:** To identify and prioritize target entities for re-engagement, providing concise and actionable context for the advisor, with enhanced flexibility in data acquisition and CRM lookup.

---

**Phase 0: Initialization & Data Source Selection**

1.  **Source Selection:** Determine the starting point for identifying target entities (e.g., teams, fairs, food trucks, exhibition centers, partners):
    *   **A) External List:** A file (CSV, Google Sheet, etc.) containing the target entities.
    *   **B) Direct CRM Query:** A direct search within the CRM (e.g., "all companies in Switzerland with X properties").
2.  **Query Parameters (if B):** If starting from the CRM, define specific criteria for the query (e.g., country, industry, last activity date, lead status).

---

**Phase 1: Initial Data Collection & Preparation**

1.  **Input (if A):** For each target entity from the external list, extract:
    *   Entity Name.
    *   CRM Record Link/ID (e.g., HubSpot).
    *   Textual notes or status on the last interaction.
2.  **Input (if B):** For each target entity from the CRM query, extract:
    *   Entity Name.
    *   CRM Record ID.
    *   Relevant properties for categorization.
3.  **Parsing:** Extract and normalize key information for each entity.

---

**Phase 2: Data Normalization & Enrichment (Robust CRM Lookup)**

1.  **Primary CRM Lookup:** For each entity, attempt to find the corresponding record in the CRM (e.g., HubSpot) using the provided ID (if available) or the exact name.
2.  **Routing Strategy (if primary lookup fails or is insufficient):** If the record is not found, the ID is outdated/incorrect, or more data is needed:
    *   **Alternative Lookup 1 (Flexible Name Search):** Attempt to search by name using more flexible operators (e.g., "contains" instead of "equals").
    *   **Alternative Lookup 2 (Secondary Identifiers):** If available, use other identifiers (e.g., website domain, phone number, email) for the search.
    *   **Alternative Lookup 3 (Custom Properties):** Consider searching by custom CRM properties or specific tags.
    *   **Failure Handling:** If all lookups fail, mark the entity as "Not Found in CRM" and proceed with only the information available from the initial source.
3.  **Data Enrichment:** Retrieve additional properties from the CRM that could be useful for categorization or the brief (e.g., `hs_last_sales_activity_date`, `notes_last_contacted`, `hs_associated_company_id` for contacts).

---

**Phase 3: Entity Categorization (Hot/Cold)**

1.  **Classification Criteria:** Analyze textual notes (from the initial source and/or CRM) and enriched properties to identify keywords indicating interest or disinterest.
    *   **Hot List:** Entities with positive signals (e.g., "interested", "replied", "spoke with", "call", "meeting", "deck sent", "follow-up requested").
    *   **Cold List:** Entities with negative signals or lack of interaction (es. "no response", "never replied", "not interested", "do not contact", "bad timing", "never contacted").
2.  **Output:** Two distinct lists of entities.

---

**Phase 4: CRM Deep Dive & "Broken Chain" Analysis (for Hot List)**

1.  **Retrieve Associated Activities:** Use CRM APIs to retrieve all activities associated with the record (notes, emails, calls, meetings).
2.  **Chronological Analysis:** Order activities by date (most recent to oldest).
3.  **Identify "Broken Chain":** Analyze the content of the latest activities to determine:
    *   What was the last significant interaction.
    *   What was the expected next step.
    *   Why the conversation stalled (e.g., awaiting feedback from the entity, internal issue at the entity, lack of follow-up from our side).
4.  **Generate Operational Brief:** Create a concise summary (2-3 lines) that includes:
    *   Date of last interaction.
    *   Key content of the last interaction.
    *   Reason for the stall.
    *   Suggested action to resume.

---

**Phase 5: Final Report Compilation**

1.  **Structure:** Organize the report into two clear sections: "Priority 1 (Hot List)" and "Priority 2 (Cold List)".
2.  **Details for Hot List:** For each entity, include:
    *   Entity Name
    *   Priority
    *   Context (from initial data)
    *   Brief (generated from Phase 4)
    *   Recommended Action (derived from the Brief)
    *   Link to CRM
3.  **Details for Cold List:** For each entity, include:
    *   Entity Name
    *   Priority
    *   Context (from initial data)
    *   Link to CRM (if available)
4.  **Format:** Present the report in a readable and shareable format (e.g., Markdown).
