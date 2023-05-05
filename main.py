import pandas as pd
data = pd.read_csv('datatest_nr1.csv')
for col in data.columns:
    print(col)

import spacy
import csv

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Open the CSV file and read its contents
with open('data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        # Extract the text from the relevant column(s)
        text = row[0]  # Replace with the column index containing the text you want to analyze
        
        # Process the text with spaCy
        doc = nlp(text)
        
        # Print the entities found in the text
        for ent in doc.ents:
            print(ent.text, ent.label_)
