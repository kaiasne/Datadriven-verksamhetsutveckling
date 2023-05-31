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

# Get list of unique workplaces
workplaces = df['Workplace'].dropna().unique()

st.sidebar.image("sdff.png", caption="Sundsvalls Damfotbollsförening ", width=desired_width,)

# Sidebar for selecting workplaces
selected_workplaces = st.sidebar.multiselect('Välj komun', workplaces)

# Filter data by selected workplaces
df_workplaces = df[df['Workplace'].isin(selected_workplaces)]

# Group data by quarter, workplace, and headline, and sum vacancies
df_workplaces_grouped = df_workplaces.groupby(['MergedColumn', 'Workplace', 'Headline']).sum().reset_index()

# Create line chart with larger tooltip area
line_chart = alt.Chart(df_workplaces_grouped).mark_line().encode(
    x=alt.X('MergedColumn:O', title='Kvartal'),
    y=alt.Y('VacancyCount:Q', title='Antal jobb'),
    color='Workplace',
).properties(
    title='Antal jobb per kvartal',
    width=600,
    height=400
) + alt.Chart(df_workplaces_grouped).mark_circle(size=150).encode(
    x=alt.X('MergedColumn:O', title='Kvartal'),
    y=alt.Y('VacancyCount:Q', title='Antal jobb'),
    color='Workplace',
    tooltip=[
        alt.Tooltip('Headline:N', title='Jobbannonser'),
        alt.Tooltip('VacancyCount:Q', title='Antal jobb')
    ]
)

with st.sidebar.expander("Aktiva jobbannonser:"):
    # Display the URL code
    st.markdown('[Butiksmedarbetare Sportringen, Sundsvall](https://arbetsformedlingen.se/platsbanken/annonser/27620458)')
    st.markdown('[Kundtjänstrådgivare SEB, Sundsvall](https://arbetsformedlingen.se/platsbanken/annonser/27638437)')
    st.markdown('[Kassamedarbetare Elgiganten, Östersund ](https://arbetsformedlingen.se/platsbanken/annonser/27621622)')
    st.markdown('[Kundtjänstmedarbetare Telenor, Östersund](https://arbetsformedlingen.se/platsbanken/annonser/27533949)')

with st.sidebar.expander("Unika jobbannonser för SDFF:"):
    # Display the URL code
    st.markdown('[Receptionist för Länsförsäkringar, Sundsvall](https://arbetsformedlingen.se/platsbanken/annonser/27610844)')
    st.markdown('[Löneadministatör HSB, Sundsvall ](https://arbetsformedlingen.se/platsbanken/annonser/27311340)')
    st.markdown('[Fastighetsskötare, NP3 Sundsvall ](https://arbetsformedlingen.se/platsbanken/annonser/27594109)')

# Render the chart using Streamlit
st.altair_chart(line_chart, use_container_width=True)
