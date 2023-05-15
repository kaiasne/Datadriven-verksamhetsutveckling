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

# import pandas as pd

# # read the CSV file into a DataFrame
# df = pd.read_csv('TestSys.csv')

# def convert_datetime(filename, date_column):


#     # convert the date column to a pandas DatetimeIndex
#     df['publication_date'] = pd.to_datetime(df['publication_date'])
#     df.set_index('publication_date', inplace=True)

#     # print the quarter for each date
#     return df.index.quarter


# def count_names(filename, name_column, number_column, convert_datetime):
#     # Read the CSV file into a pandas dataframe
#     df = pd.read_csv(filename)

#     # # Convert the date column to a pandas datetime object
#     # df[date_column] = pd.to_datetime(df[date_column])

#     # Group the dataframe by name and sum the numbers in the other column
#     counts = df.groupby(name_column)[number_column].sum()

#     # Resample the counts by quarter and sort the result
#     counts = counts.resample('Q').sum().sort_values(ascending=False)

#     # Return the counts for each name
#     return counts

# counts = count_names('TestSys.csv','workplace_address', 'number_of_vacancies', 'publication_date')
# print(counts)


