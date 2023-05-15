import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Read the dataset
data = pd.read_csv('TestSys.csv')

# Streamlit app layout
st.title('Value Counts Visualization')

# Select the column to count and visualize
column = st.sidebar.selectbox('Column', list(data.columns))

# Calculate the value counts for each unique value in the column
value_counts = data[column].value_counts()

# Plot the value counts with a larger figure size
fig, ax = plt.subplots(figsize=(15, 6))  # Adjust the figsize as needed
value_counts.plot(kind='bar', ax=ax)
ax.set_xlabel(column)
ax.set_ylabel('Count')
ax.set_title(f"Value Counts of {column}")


# Display the plot
st.pyplot(fig)
