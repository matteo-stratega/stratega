// Clean markdown JSON wrappers from LLM output
// Add this as a Code node BEFORE Information Extractor

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
