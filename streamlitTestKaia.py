import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set Streamlit app title
st.title("Dataset Graph")

# File upload
file = st.file_uploader("Upload a CSV file", type=["csv"])

if file is not None:
    # Read the dataset
    data = pd.read_csv(file)

    # Display the dataset
    st.subheader("Dataset")
    st.dataframe(data)

    # Graph options
    graph_options = st.sidebar.selectbox("Select Graph Type", ["Line Plot", "Bar Plot"])

    if graph_options == "Line Plot":
        # Line plot
        st.subheader("Line Plot")
        x_column = st.selectbox("Select X-axis column", data.columns)
        y_column = st.selectbox("Select Y-axis column", data.columns)

        # Create a line plot
        fig, ax = plt.subplots()
        ax.plot(data[x_column], data[y_column])
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        st.pyplot(fig)

    elif graph_options == "Bar Plot":
        # Bar plot
        st.subheader("Bar Plot")
        x_column = st.selectbox("Select X-axis column", data.columns)
        y_column = st.selectbox("Select Y-axis column", data.columns)

        # Create a bar plot
        fig, ax = plt.subplots()
        ax.bar(data[x_column], data[y_column])
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        st.pyplot(fig)




