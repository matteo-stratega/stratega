# FIX Workflow Content-Gen-Prod

## Problema
L'Information Extractor fallisce con errore: `Failed to parse. Text: '```json { "Headline": ...'`

**Causa:** Il modello AI ritorna JSON wrappato in markdown backticks che l'extractor non riesce a parsare.

---

## Soluzione (5 minuti)

### 1. Apri workflow
https://n8n.pickeat.cc/workflow/gQxLO22JXLBPc4Hp

### 2. Trova il nodo "Information Extractor"
Scorri il workflow fino a trovare il nodo chiamato "Information Extractor" o simile.

### 3. Identifica il nodo PRIMA dell'Information Extractor
Guarda quale nodo è collegato IN INGRESSO all'Information Extractor.
(Probabilmente si chiama "AI Agent" o qualcosa con "concatenate")

### 4. Aggiungi nodo Code
1. Click sul **+** (plus button) sulla connessione TRA quel nodo e Information Extractor
2. Nel menu, cerca "Code"
3. Seleziona **"Code"** (JavaScript)
4. Rinomina il nodo: **"Clean JSON Wrapper"**

### 5. Incolla il codice JavaScript
Apri il file `workflows/n8n-json-cleanup-node.js` e copia tutto il contenuto nel nodo Code.

Oppure copia direttamente questo:

```javascript
// Clean markdown JSON wrappers from LLM output
const items = $input.all();

return items.map(item => {
  // Get the text field (adjust field name if different)
  let text = item.json.output || item.json.text || item.json.concatenatedText || '';

  // Remove markdown code blocks
  text = text.replace(/```json\s*/g, '');
  text = text.replace(/```\s*$/g, '');
  text = text.trim();

  // Return cleaned JSON
  return {
    json: {
      ...item.json,
      output: text,
      text: text,
      concatenatedText: text
    }
  };
});
```

### 6. Verifica le connessioni
- **Input** del nuovo nodo: collegato al nodo AI precedente
- **Output** del nuovo nodo: collegato a Information Extractor

### 7. (Opzionale) Disabilita Get_job
Se c'è un nodo "Get_job" all'inizio del workflow:
- Right-click sul nodo
- Seleziona "Disable" (per ora usiamo test data dal rapid-service)

### 8. Execute Workflow
1. Click sul bottone **"Execute Workflow"** (in alto a destra)
2. Aspetta 2-3 minuti
3. Verifica l'output!

---

## Risultato Atteso

Dovresti vedere un articolo completo con:
- ✅ Headline
- ✅ Meta title e meta description
- ✅ 1500-1800 parole
- ✅ 9 sezioni strutturate
- ✅ FAQs
- ✅ People Also Ask

---

## Troubleshooting

### Se ancora fallisce al parsing:
1. Click sul nodo "Clean JSON Wrapper"
2. Guarda l'output (tab "Output")
3. Verifica che il campo `output` o `text` non abbia più i backticks
4. Se vedi ancora ```, il campo potrebbe avere un nome diverso
5. Mandami screenshot dell'output del nodo PRIMA del Clean JSON Wrapper

### Se dice "no items to process":
- Verifica che il nodo precedente abbia un output
- Click sul nodo precedente e guarda il tab "Output"
- Se è vuoto, il problema è più a monte (probabilmente modello AI)

### Se il modello AI non genera nulla:
- Verifica quota/crediti Gemini API
- Controlla l'output del nodo "rapid-service" (deve ritornare i test data)
- Verifica che i prompt siano collegati correttamente
