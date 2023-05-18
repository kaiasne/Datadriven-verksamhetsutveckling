import pandas as pd

# Read the first CSV file
df1 = pd.read_csv('output.csv')

# Read the second CSV file
df2 = pd.read_csv('headline_dataset.csv')

merged_df = pd.concat([df1, df2], ignore_index=True)

# Write the merged dataframe to a new CSV file
merged_df.to_csv('merged.csv', index=False)
