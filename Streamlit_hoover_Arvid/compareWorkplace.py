import streamlit as st
import pandas as pd
import altair as alt

# Load data
df = pd.read_csv('output.csv')

# Convert Headline column to string data type
df['Headline'] = df['Headline'].astype(str)

# Get list of unique workplaces
workplaces = df['Workplace'].dropna().unique()

# Sidebar for selecting workplaces
selected_workplaces = st.sidebar.multiselect('Select Workplaces', workplaces)

# Filter data by selected workplaces
df_workplaces = df[df['Workplace'].isin(selected_workplaces)]

# Group data by quarter, workplace, and headline, and sum vacancies
df_workplaces_grouped = df_workplaces.groupby(['Quarter', 'Workplace', 'Headline']).sum().reset_index()

# Create line chart with larger tooltip area
line_chart = alt.Chart(df_workplaces_grouped).mark_line().encode(
    x=alt.X('Quarter:O', title='Quarter'),
    y='VacancyCount',
    color='Workplace',
    tooltip=[
        'Quarter', 
        'Workplace', 
        'Headline', 
        'VacancyCount'
    ],
    size=alt.value(10)  # Set tooltip size to 150
).properties(
    title='Vacancies by Quarter',
    width=600,
    height=400
)

# Render the chart using Streamlit
st.altair_chart(line_chart, use_container_width=True)
