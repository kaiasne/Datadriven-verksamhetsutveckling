import pandas as pd
data = pd.read_csv('datatest_nr1.csv')
for col in data.columns:
    print(col)