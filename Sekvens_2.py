import pandas as pd
import ast
import nltk

filename = "sq1.csv"
df = pd.read_csv(filename)

# Convert column index 3 to lowercase
df.iloc[:, 3] = df.iloc[:, 3].str.lower()

# Tokenize column index 3 using NLTK
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
df.iloc[:, 3] = df.iloc[:, 3].apply(lambda x: tokenizer.tokenize(x))

# Extract municipality values from column 7, handling errors for improperly formatted values
def extract_municipality(val):
    try:
        return ast.literal_eval(val)['municipality']
    except (ValueError, SyntaxError):
        return ''

df.iloc[:, 7] = df.iloc[:, 7].apply(extract_municipality)

# Write the cleaned data to a new CSV file
new_filename = "cleaned_" + filename
df.to_csv(new_filename, index=False)