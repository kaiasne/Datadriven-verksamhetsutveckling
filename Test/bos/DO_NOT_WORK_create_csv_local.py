# #load pandas, tool for data analysis in Python
# import pandas as pd
# import csv

# # read the JSON file into a pandas DataFrame
# jobtech_data = pd.read_json('2022.json')

# # select 1000 random rows from the DataFrame
# jobtech_sample = jobtech_data.sample(n=10000, random_state=10)

# # export the selected rows to a new CSV file
# jobtech_sample.to_csv('jobtech_10000_sample_dataset.csv', index=False)

# # open input CSV file as source
# # open output CSV file as result
# with open("jobtech_10000_sample_dataset.csv", "r") as source:
#     reader = csv.reader(source)
      
#     with open("test2.csv", "w") as result:
#         writer = csv.writer(result)
#         for r in reader:
            
#             # Use CSV Index to remove a column from CSV
#             #r[3] = r['year']
#             writer.writerow((r[0], r[4], r[6], r[7], r[21], r[22], r[23], r[24],r[28]))


# import json
# import pandas as pd
# import random

# # Path to the JSON file
# jobtech_data_json = pd.read_json('2022.json')

# # List of indexes to keep
# indexes_to_keep = [0, 4, 6, 7, 21, 22, 23, 24, 28]

# # Load the JSON file into a list of dictionaries
# with open(jobtech_data_json, "r") as f:
#     jobtech_data = json.load(f)

# # Select 10,000 random rows from the list
# jobtech_sample = random.sample(jobtech_data, k=5000)

# # Create a list of indexes to remove from the original dataset
# indexes_to_remove = [jobtech_data.index(d) for d in jobtech_sample if jobtech_data.index(d) not in indexes_to_keep]

# # Remove selected rows from the original dataset
# for i in sorted(indexes_to_remove, reverse=True):
#     del jobtech_data[i]

# # Create a DataFrame from the modified dataset
# jobtech_df = pd.DataFrame(jobtech_data)

# # Output the DataFrame to a CSV file
# jobtech_df.to_csv("jobtech_data_clean.csv", index=False)

import ijson
import json

# Open the JSON file for reading
with open('2022.json', 'r') as file:

    # Create an ijson parser object
    parser = ijson.parse(file)

    # Create an empty list to store the cleaned JSON data
    cleaned_data = []

    # Loop through each object in the JSON file
    for prefix, event, value in parser:

        # Check if the current object is a dictionary
        if isinstance(value, dict):

            # Create a new dictionary for the cleaned data
            cleaned_dict = {}

            # Loop through each key-value pair in the dictionary
            for key, val in value.items():

                # Check if the key is one of the columns to keep
                if key in ['column1', 'column2', 'column3']:
                    cleaned_dict[key] = val

            # Append the cleaned dictionary to the cleaned data list
            cleaned_data.append(cleaned_dict)

# Save the cleaned data to a new JSON file
with open('path/to/cleaned_file.json', 'w') as outfile:
    json.dump(cleaned_data, outfile)