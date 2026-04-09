from serpapi import GoogleSearch
import json
import os
import sys

#OUTPUT_DIR = '../../data/json/'
OUTPUT_DIR = os.path.join(os.getcwd(), 'data/json')
OUTPUT_FILE = 'googlescholar_output.json'

params = {
  "api_key": os.getenv('SERP_API_KEY'),
  "engine": "google_scholar_author",
  "hl": "en",
  "author_id": "55_WwZ8AAAAJ",
}

search = GoogleSearch(params)
results = search.get_dict()

#print(results)

# Extract the relevant data into a new dictionary
data = {
    "citations": results['cited_by']['table'][0]['citations']['all'],
    "h_index": results['cited_by']['table'][1]['h_index']['all'],
    "i10_index": results['cited_by']['table'][2]['i10_index']['all']
}

# Ensure the directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Construct the full path to the JSON file
json_file_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)

# Write the dictionary to a JSON file
with open(json_file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
    
print(f"JSON file created at: {json_file_path}")
