import pandas as pd
import csv
import json
import sys
#Kör programmet genom att trycka in (python Sekvens_1.py "Filnamn".jsonl) i Terminalen.

# check if the user provided a filename
if len(sys.argv) != 2:
    print("Please provide a JSONL filename as an argument.")
    sys.exit()

# attempt to open the file
try:
    with open(sys.argv[1], encoding='utf-8') as inputfile:
        jobtech_data = pd.read_json(inputfile, lines=True)
except FileNotFoundError:
    print(f"Error: File '{sys.argv[1]}' not found.")
    sys.exit()
except ValueError:
    print(f"Error: File '{sys.argv[1]}' is not in valid JSONL format.")
    sys.exit()

# export all rows to a new CSV file
jobtech_data.to_csv('ny_csv_sq1.csv', index=False)

# open output CSV file as result
with open("ny_csv_sq1.csv", "r") as source:
    reader = csv.reader(source)
      
    with open("sq1.csv", "w") as result:
        writer = csv.writer(result)
        for r in reader:
            
            # Use CSV Index to remove a column from CSV
            writer.writerow((r[0], r[4], r[6], r[7], r[21], r[22], r[23], r[24], r[28]))

print("Conversion completed successfully!")
