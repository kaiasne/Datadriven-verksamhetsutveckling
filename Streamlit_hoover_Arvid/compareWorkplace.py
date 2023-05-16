

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
selected_workplaces = st.sidebar.multiselect('Välj komun', workplaces)

# Filter data by selected workplaces
df_workplaces = df[df['Workplace'].isin(selected_workplaces)]

# Group data by quarter, workplace, and headline, and sum vacancies
df_workplaces_grouped = df_workplaces.groupby(['Quarter', 'Workplace', 'Headline']).sum().reset_index()

# Create line chart with larger tooltip area
line_chart = alt.Chart(df_workplaces_grouped).mark_line().encode(
    x=alt.X('Quarter:O', title='Kvartal'),
    y=alt.Y('VacancyCount', title='Antall jobb'),
    color='Workplace',
    tooltip=[
        alt.Tooltip('Headline', title='Jobbannonsen'),
        alt.Tooltip('VacancyCount', title='Antall jobber')
    ],
    size=alt.value(2)  # Set tooltip size to 150
).properties(
    title='Antall jobb per kvartal',
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
