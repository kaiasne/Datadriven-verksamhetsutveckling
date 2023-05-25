import streamlit as st
import subprocess

def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
            st.empty()
            
            # Call the function to render the other page
            main_app()

# def redirect_to_another_app():
#     # Run another Streamlit application using subprocess
#     subprocess.run(["streamlit", "run", "main_STREAMLIT.py"])

import streamlit as st
import pandas as pd
import altair as alt

# Load data
df = pd.read_csv('MAIN_2021_2022.csv')

# Convert Headline column to string data type
df['Headline'] = df['Headline'].astype(str)

# Define the desired height and calculate the corresponding width
desired_height = 100
width_to_height_ratio = 2  # Adjust this ratio according to your needs
desired_width = int(desired_height * width_to_height_ratio)

# # Class for session state management
# class SessionState:
#     def __init__(self):
#         self.is_logged_in = False

# # Function to display the login page
# def login():
#     st.title("Login Page")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if username == "your_username" and password == "your_password":
#             st.success("Logged in as {}".format(username))
#             # Set the login state to True
#             session_state.is_logged_in = True
#         else:
#             st.error("Invalid username or password")

# Function to display the main application content
def main_app():
    # Sidebar for selecting workplaces
    workplaces = df['Workplace'].dropna().unique()
    selected_workplaces = st.sidebar.multiselect('Välj komun', workplaces)

    # Filter data by selected workplaces
    df_workplaces = df[df['Workplace'].isin(selected_workplaces)]

    # Group data by quarter, workplace, and headline, and sum vacancies
    df_workplaces_grouped = df_workplaces.groupby(['MergedColumn', 'Workplace', 'Headline']).sum().reset_index()

    # Create line chart with larger tooltip area
    line_chart = alt.Chart(df_workplaces_grouped).mark_line().encode(
        x=alt.X('MergedColumn:O', title='Kvartal'),
        y=alt.Y('VacancyCount', title='Antal jobb'),
        color='Workplace',
        tooltip=[
            alt.Tooltip('Headline', title='Jobbannonsen'),
            alt.Tooltip('VacancyCount', title='Antal jobb')
        ],
        size=alt.value(2)  # Set tooltip size to 150
    ).properties(
        title='Antal jobb per kvartal',
        width=600,
        height=400
    ).configure_mark(
        opacity=0.7,  # Set line opacity
        strokeWidth=2  # Set line width
    ).configure_axis(
        labelFontSize=12,  # Set axis label font size
        titleFontSize=14  # Set axis title font size
    ).configure_title(
        fontSize=16  # Set chart title font size
    ).configure_view(
        strokeWidth=0  # Remove border around chart
    ).configure_legend(
        title=None  # Remove legend title
    )

    # Render the chart using Streamlit
    st.altair_chart(line_chart, use_container_width=True)

main_app()

# # Initialize the session state
# session_state = SessionState()

# # Check if the user is logged in
# if not session_state.is_logged_in:
#     login()

# # Display the main application content if logged in
# if session_state.is_logged_in:
#     main_app()