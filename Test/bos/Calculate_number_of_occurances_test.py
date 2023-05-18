# OBS! Kod uppdaterad så den räcknar antalet gånger Göteborg och liknande städer finns med

import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import gutenberg
import csv
from nltk.metrics.distance import edit_distance

# Define the target sentence
target_sentence = "Göteborg"

# Open the CSV file and extract the sentences
with open('Test_sys - Test_sys.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    sentences = [row['workplace_address'] for row in reader]

# Search for the target sentence and similar sentences
similar_sentences = []
threshold_distance = 3  # Maximum edit distance for a sentence to be considered similar
target_count = 0

for sentence in sentences:
    if target_sentence in sentence:
        target_count += 1
    elif edit_distance(target_sentence.lower(), sentence.lower()) <= threshold_distance:
        similar_sentences.append(sentence)

# Print the results
print(f"The sentence '{target_sentence}' appears {target_count} times in the dataset.")
print(f"There are {len(similar_sentences)} similar sentences:")
for similar_sentence in similar_sentences:
    print(similar_sentence)
