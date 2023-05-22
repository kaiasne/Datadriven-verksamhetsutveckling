

import streamlit as st
import pandas as pd
import altair as alt

# Load data
df = pd.read_csv('2021_2022_merged_streamlit.csv')

# Convert Headline column to string data type
df['Headline'] = df['Headline'].astype(str)

# Get list of unique workplaces
workplaces = df['Workplace'].dropna().unique()

# Sidebar for selecting workplaces
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
with st.sidebar.expander("Aktiva jobbannonser:"):
    # Display the URL code
    st.markdown('[Kundsupport SEB, Stockholm](https://arbetsformedlingen.se/platsbanken/annonser/27610844)')
    st.markdown('[Arbetare till lager, Eskilstuna](https://arbetsformedlingen.se/platsbanken/annonser/27311340)')
    st.markdown('[Extrajobb till terminal, Helsingborg ](https://arbetsformedlingen.se/platsbanken/annonser/27594109)')
    st.markdown('[Lagerarbetare DHL, Jönköping](https://arbetsformedlingen.se/platsbanken/annonser/27576294)')
# Render the chart using Streamlit
st.altair_chart(line_chart, use_container_width=True)
