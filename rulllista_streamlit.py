import streamlit as st
import pandas as pd

# Set Streamlit app title
st.title("Dataset Scroll List")

# File upload
file = st.file_uploader("Upload a CSV file", type=["csv"])

if file is not None:
    # Read the dataset
    data = pd.read_csv(file)

    # Display the dataset
    st.subheader("Dataset")
    st.dataframe(data)

    # Create a scrollable list
    selected_columns = st.sidebar.multiselect("Select columns", data.columns)

    # Filter the dataset based on selected columns
    filtered_data = data[selected_columns]

    # Display the filtered dataset
    st.subheader("Filtered Dataset")
    st.dataframe(filtered_data)
