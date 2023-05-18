# # Nedan kod är till för att skapa en csv av antalet rader som är bestämt (som ett testdataset)

# import json
# import csv

# # Load the JSON file
# with open('filtered_data.json') as file:
#     data = json.load(file)

# # Get the first 200 rows
# rows = data[-200:]

# # Extract column names
# column_names = list(rows[0].keys())

# # Specify the output CSV file path
# output_csv_file = 'filtered_data_2022.csv'

# # Write data to CSV file
# with open(output_csv_file, 'w', newline='', encoding='utf-8') as file:
#     writer = csv.DictWriter(file, fieldnames=column_names)
#     writer.writeheader()
#     writer.writerows(rows)

import json
import csv

def json_to_csv(json_file_path, csv_file_path):
    # Open the JSON file for reading
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        # Load JSON data
        data = json.load(json_file)
        
        # Extract headers from the first item in JSON
        headers = list(data[0].keys())

        # Open CSV file for writing
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            
            # Write headers to the CSV file
            writer.writeheader()

            # Write each JSON item as a row in the CSV file
            for item in data:
                writer.writerow(item)

    print(f"CSV file '{csv_file_path}' has been created successfully.")

# Example usage:
json_file_path = 'filtered_data.json'
csv_file_path = 'filtered_data_2022.csv'
json_to_csv(json_file_path, csv_file_path)
