# import streamlit as st

# st.title("My Streamlit Test App")

# st.write("Welcome to my test page!")

# x = st.slider('Select a value:', 0, 100, 50)
# st.write('You selected:', x)

# if st.button('Double the value'):
#     x *= 2
#     st.write('New value:', x)

import pandas as pd

# Read the CSV file into a pandas dataframe
df = pd.read_csv('TestSys.csv')

# Group the dataframe by name and sum the numbers in the other column
counts = df.groupby('workplace_address')['number_of_vacancies'].sum()

# Print the counts for each name
print(counts)

