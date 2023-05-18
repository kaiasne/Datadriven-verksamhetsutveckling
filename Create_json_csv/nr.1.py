import json

# Specify the input JSON file path
input_json_file = '2022.json'

# Specify the output JSON file path to save the extracted data
output_json_file = 'cleaned_2022_no_workplace.json'

# Define the columns to keep
columns_to_keep = ['id', 'headline', 'number_of_vacancies', 'description', 'workplace_address', 'publication_date']  # Replace with your desired column names

# Define the key to extract from the workplace_address
key_to_extract = 'municipality'

# Load the JSON file
with open(input_json_file) as file:
    data = json.load(file)

# Extract the desired columns and key from each row
cleaned_data = []
for row in data:
    cleaned_row = {column: row[column] for column in columns_to_keep}
    cleaned_row[key_to_extract] = row['workplace_address'][key_to_extract]
    del row['workplace_address']
    cleaned_data.append(cleaned_row)

# Save the extracted data to the output JSON file
with open(output_json_file, 'w') as file:
    json.dump(cleaned_data, file, indent=4)