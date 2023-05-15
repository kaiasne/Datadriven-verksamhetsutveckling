import streamlit as st
import pandas as pd

# Read the dataset
data = pd.read_csv('TestSys.csv')

# Function to count occurrences of the same name in a column
def count_same_name(column_name):
    name = st.sidebar.text_input('Enter a name')
    count = data[data[column_name] == name].shape[0]
    return count

# Streamlit app layout
st.title('Counting Occurrences of Same Name')

# Select the column to count occurrences
column = st.sidebar.selectbox('Column', list(data.columns))

# Call the function to count occurrences
occurrences_count = count_same_name(column)

# Display the count
st.write(f"Occurrences of the same name: {occurrences_count}")
