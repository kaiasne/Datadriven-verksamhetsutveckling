#load pandas, tool for data analysis in Python
import pandas as pd
import csv

# read the JSON file into a pandas DataFrame
jobtech_data = pd.read_json('2022.json')

# select 1000 random rows from the DataFrame
jobtech_sample = jobtech_data.sample(n=1000, random_state=42)

# export the selected rows to a new CSV file
jobtech_sample.to_csv('jobtech_dataset2022_sample.csv', index=False)

# open input CSV file as source
# open output CSV file as result
with open("jobtech_dataset2022_sample.csv", "r") as source:
    reader = csv.reader(source)
      
    with open("test2.csv", "w") as result:
        writer = csv.writer(result)
        for r in reader:
            
            # Use CSV Index to remove a column from CSV
            #r[3] = r['year']
            writer.writerow((r[0], r[4], r[5], r[6], r[7], r[8], r[9], r[11], r[12], r[13], r[16], r[18], r[19], r[20], r[21], r[22], r[23], r[24], r[25], r[26], r[27], r[29]))