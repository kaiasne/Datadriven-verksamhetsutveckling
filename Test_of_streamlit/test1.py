import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
data = pd.read_csv('TestSys.csv')

# Streamlit app layout
st.title('Count and Visualization')

# Select the column to count occurrences
column = st.sidebar.selectbox('Column', list(data.columns))

# Select the value to count
value = st.sidebar.text_input('Value')

# Count occurrences of the value in the column
count = data[data[column] == value].shape[0]

# Display the count
st.write(f"Occurrences of {value} in {column}: {count}")

# Visualize the dataset based on the counts
fig, ax = plt.subplots()
data[column].value_counts().plot(kind='line')
ax.set_xlabel(column)
ax.set_ylabel('Count')
ax.set_title(f"Value Counts of {column}")

# Display the plot
st.pyplot(fig)
