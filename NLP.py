import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize

# Read in CSV file
data = pd.read_csv('datatest_nr1.csv')

# Extract text column from data
text_data = data['description']

# Convert text data to lowercase
text_data = text_data.str.lower()

# Tokenize each text into individual words
tokenized_data = [word_tokenize(text.lower()) for text in text_data]

# Tag the words in each text with their part of speech
tagged_data = [nltk.pos_tag(tokens) for tokens in tokenized_data]

# Extract the adjectives from each text
adjectives_data = [[word for word, pos in tagged_words if pos.startswith('JJ')] for tagged_words in tagged_data]

# Print the adjectives for each text
for i, adjectives in enumerate(adjectives_data):
    print(f'Text {i+1} adjectives: {adjectives}')

# # Tokenize the text data into individual words
# words = []
# for text in text_data:
#     words.extend(word_tokenize(text))

# # Remove stop words and junk words
# stop_words1 = set(stopwords.words('swedish'))
# stop_words2 = set(stopwords.words('english'))
# stop_words = stop_words1 | stop_words2
# junk_words = {'.', ',', ':', ';', '?', '!', '(', ')', '[', ']', '{', '}',"'",}
# words = [word for word in words if word not in stop_words and word not in junk_words]

# # Count the number of times each word appears
# word_counts = Counter(words)

# # Print the most common words
# print(word_counts.most_common(20))



