import streamlit as st
import pandas as pd
import plotly.express as px

# Set Streamlit app title
st.title("Line Plot with Hover Details")

# File upload
file = st.file_uploader("Upload a CSV file", type=["csv"])

if file is not None:
    # Read the dataset
    data = pd.read_csv(file)

    # Display the dataset
    st.subheader("Dataset")
    st.dataframe(data)

    # Graph options
    x_column = st.selectbox("Select X-axis column", data.columns)
    y_column = st.selectbox("Select Y-axis column", data.columns)

    # Create a line plot with hover details
    fig = px.line(data, x=x_column, y=y_column, hover_data=data.columns)
    st.plotly_chart(fig)
