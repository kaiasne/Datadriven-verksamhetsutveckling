import json
from nltk.tokenize import word_tokenize, ngrams

def extract_description(json_file_path):
    with open(json_file_path) as file:
        data = json.load(file)
    
    new_data = []
    for item in data:
        description = item['description']
        tokens = word_tokenize(description.lower())
        bigrams = list(ngrams(tokens, 2))
        
        if ('annan', 'sysselsättning') in bigrams:
            new_data.append(item)
    
    return new_data

def filter_json(json_file_path):
    with open(json_file_path) as file:
        data = json.load(file)
    
    new_data = []
    for item in data:
        description = item['description']
        tokens = word_tokenize(description.lower())
        bigrams = list(ngrams(tokens, 2))
        
        if ('annan', 'sysselsättning') in bigrams:
            new_data.append(item)
    
    return new_data

# Example usage
json_file_path = 'your_json_file.json'

# Extract and save the rows that contain 'annan sysselsättning' together
extracted_data = extract_description(json_file_path)

# Remove the rows that do not contain 'annan sysselsättning' together
filtered_data = filter_json(json_file_path)

# Saving the extracted and filtered data back to a JSON file
with open('extracted_data.json', 'w') as file:
    json.dump(extracted_data, file, indent=4)

with open('filtered_data.json', 'w') as file:
    json.dump(filtered_data, file, indent=4)
