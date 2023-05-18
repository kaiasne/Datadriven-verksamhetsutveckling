import pandas as pd
import nltk
import os

filename = "cleaned_sq1.csv"
df = pd.read_csv(filename)

# Convert column index 3 to lowercase
df.iloc[:, 3] = df.iloc[:, 3].str.lower()

# Tokenize column index 3 using NLTK
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
df.iloc[:, 3] = df.iloc[:, 3].apply(lambda x: tokenizer.tokenize(x))

# Find rows where "annan sysselsättning" is present
df_sys = df[df.iloc[:, 3].apply(lambda x: 'annan' in x and 'sysselsättning' in x)]

# Print the first 5 rows where "annan sysselsättning" is present
num_rows = df_sys.shape[0]
num_rows_to_print = min(num_rows, 5)
for i in range(num_rows_to_print):
    print(df_sys.iloc[i, :])


# Save the filtered dataframe to a new CSV file in the same directory as the original file
new_filename = os.path.splitext(filename)[0] + "Sq1_final.csv"
df_sys.to_csv(new_filename, index=False)
