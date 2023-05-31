import json
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

def filter_json(json_file_path):
    with open(json_file_path) as file:
        data = json.load(file)

    new_data = []
    for item in data:
        description = str(item['description'])  # Convert to string
        tokens = word_tokenize(description.lower())
        bigrams = list(ngrams(tokens, 2))

        if ('annan', 'sysselsättning') in bigrams:
            new_data.append(item)

    return new_data

# Example usage
json_file_path = 'cleaned_2022.json'

# Filter the JSON data to keep rows that contain 'annan sysselsättning' together
filtered_data = filter_json(json_file_path)

# Saving the filtered data to a JSON file
with open('filtered_data.json', 'w') as file:
    json.dump(filtered_data, file, indent=4)