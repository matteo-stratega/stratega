#!/usr/bin/env python3
"""
Fix n8n workflow by adding JSON cleanup node before Information Extractor
"""
import json
import uuid

# Load workflow
with open('/Users/matteolombardi/AI-Projects/stratega/workflows/content-gen-prod.json', 'r') as f:
    workflow = json.load(f)

# Find Information Extractor node
info_extractor = None
info_extractor_idx = None
for idx, node in enumerate(workflow['nodes']):
    if 'Information' in node.get('name', '') and 'Extractor' in node.get('name', ''):
        info_extractor = node
        info_extractor_idx = idx
        print(f"✅ Found Information Extractor: {node['name']} at position {node['position']}")
        break

if not info_extractor:
    print("❌ Could not find Information Extractor node")
    exit(1)

# Find which node connects TO Information Extractor
previous_node_name = None
for conn in workflow.get('connections', {}):
    for output_type, outputs in workflow['connections'][conn].items():
        for output_list in outputs:
            for connection in output_list:
                if connection.get('node') == info_extractor['name']:
                    previous_node_name = conn
                    print(f"✅ Found previous node: {previous_node_name}")
                    break

if not previous_node_name:
    print("❌ Could not find node connecting to Information Extractor")
    exit(1)

# Create cleanup node
cleanup_node_id = str(uuid.uuid4())
cleanup_node_name = "Clean JSON Wrapper"

# Position it between the two nodes
prev_node = next(n for n in workflow['nodes'] if n['name'] == previous_node_name)
cleanup_position = [
    (prev_node['position'][0] + info_extractor['position'][0]) // 2,
    (prev_node['position'][1] + info_extractor['position'][1]) // 2
]

cleanup_node = {
    "parameters": {
        "jsCode": """// Clean markdown JSON wrappers from LLM output
const items = $input.all();

return items.map(item => {
  // Try all possible field names
  let text = item.json.output
          || item.json.text
          || item.json.concatenatedText
          || item.json.response
          || item.json.content
          || JSON.stringify(item.json);

  // If it's already an object, stringify it first
  if (typeof text === 'object') {
    text = JSON.stringify(text);
  }

  // Remove ALL markdown wrappers
  text = text.replace(/^```json\\s*/gm, '');
  text = text.replace(/^```\\s*/gm, '');
  text = text.replace(/```\\s*$/gm, '');
  text = text.trim();

  return {
    json: {
      ...item.json,
      output: text,
      text: text,
      concatenatedText: text,
      cleanedOutput: text
    }
  };
});"""
    },
    "id": cleanup_node_id,
    "name": cleanup_node_name,
    "type": "n8n-nodes-base.code",
    "typeVersion": 2,
    "position": cleanup_position
}

# Insert cleanup node
workflow['nodes'].insert(info_extractor_idx, cleanup_node)
print(f"✅ Created cleanup node at position {cleanup_position}")

# Update connections
# 1. Find connection from previous_node to info_extractor and redirect to cleanup
if previous_node_name in workflow['connections']:
    for output_type in workflow['connections'][previous_node_name]:
        for output_idx, connections_list in enumerate(workflow['connections'][previous_node_name][output_type]):
            new_connections = []
            for conn in connections_list:
                if conn.get('node') == info_extractor['name']:
                    # Redirect to cleanup node
                    new_connections.append({
                        "node": cleanup_node_name,
                        "type": conn.get('type', 'main'),
                        "index": conn.get('index', 0)
                    })
                    print(f"✅ Redirected connection: {previous_node_name} -> {cleanup_node_name}")
                else:
                    new_connections.append(conn)
            workflow['connections'][previous_node_name][output_type][output_idx] = new_connections

# 2. Create connection from cleanup to info_extractor
workflow['connections'][cleanup_node_name] = {
    "main": [[{
        "node": info_extractor['name'],
        "type": "main",
        "index": 0
    }]]
}
print(f"✅ Created connection: {cleanup_node_name} -> {info_extractor['name']}")

# Save fixed workflow
output_path = '/Users/matteolombardi/AI-Projects/stratega/workflows/content-gen-prod-FIXED.json'
with open(output_path, 'w') as f:
    json.dump(workflow, f, indent=2)

print(f"\n✅ DONE! Fixed workflow saved to:\n{output_path}")
print(f"\n📋 NEXT STEPS:")
print(f"1. Go to https://n8n.pickeat.cc")
print(f"2. Import the workflow from: {output_path}")
print(f"3. Execute and get your article!")
