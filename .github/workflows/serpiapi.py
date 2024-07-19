from serpapi import GoogleSearch
import json
import os


params = {
  "api_key": "SERP_API_KEY",
  "engine": "google_scholar_author",
  "hl": "en",
  "author_id": "55_WwZ8AAAAJ"
}

search = GoogleSearch(params)
results = search.get_dict()

print(results)

# Extract the relevant data into a new dictionary
data = {
    "citations": results['cited_by']['table'][0]['citations']['all'],
    "h_index": results['cited_by']['table'][1]['h_index']['all'],
    "i10_index": results['cited_by']['table'][2]['i10_index']['all']
}

# Ensure the directory exists
output_dir = 'data'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Write the dictionary to a JSON file
json_file_path = os.path.join(output_dir, 'googlescholar_output.json')
with open(json_file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)