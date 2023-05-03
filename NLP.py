import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Read in CSV file
data = pd.read_csv('datatest_nr1.csv')

# Extract text column from data
text_data = data['description']

# Convert text data to lowercase
text_data = text_data.str.lower()

# Tokenize the text data into individual words
words = []
for text in text_data:
    words.extend(word_tokenize(text))

# Remove stop words and junk words
stop_words = set(stopwords.words('swedish'))
junk_words = {'.', ',', ':', ';', '?', '!', '(', ')', '[', ']', '{', '}',"'",}
words = [word for word in words if word not in stop_words and word not in junk_words]

# Count the number of times each word appears
word_counts = Counter(words)

# Print the most common words
print(word_counts.most_common(10))