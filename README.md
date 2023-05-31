# Datadriven-verksamhetsutveckling

I mapparna som har label Test finns flera filer som har använts för att testa nya idéer och nya funktioner som sedermera inte har fungerat. Dessa innehåller allt ifrån test kring visualisering, NLP men främst olika sätt att plocka ut och hämta data. 

För att utvinna den data som behövs finns det 4 olika filer som sedan kan appliceras och köras i med Streamlit. Samtliga ligger i mappen Create dataset. De är därefter numrerade i den ordning de ska köras. Observera att man kan behöva uppdatera filnamn etc på de filer som är input. 

## Paket + installtion
För att köra det slutgiltliga programmet använder vi nedan paket.
För att installera paketen använder vi [pip](https://pip.pypa.io/en/stable/)

**Streamlit**
Streamlit används för att framställa det visuella
```bash
pip install streamlit
```

**Pandas**
Används för att visualisera och framförallt spara information i DataFrame
```bash
pip install pandas
```

**Altair**
Altair är visualiserar statistisk data i python. Det förenklar processen genom att deklrarera syntax, integrerar med Pandas och ger stöd för interaktivitet i viusaliseringen. 
```bash
pip install altair
```

**Plotly**
Plotly används för att få fram grafer och på så sätt visa på trender
```bash
pip install plotly
```
**NLTK**
Används som paket för att processa och gå igenom data, används både i när vi tar bort data från workplace_address kolumnen men främst när vi söker efter key_words i description. Denna är installerad sedan tidigare när man kör kod via Conda

## Användning

Kör filen main_STREAMLIT.py i terminalen. Du kommer därefter få en prompt om att köra streamlit applikationen. Kör denna 
```bash
streamlit run 'c:/main_STREAMLIT.py'
```
Appen kommer nu öppna sig i webbläsaren och användaren kan nu använda listan till vänster för att skriva in eller välja en eller flera kommunera att jämföra.

Linjediagrammet kommer att visa antalet lediga jobb per kvartal för den valda arbetsplatsen. Hovra över datapunkterna för att se rubriken och antalet lediga jobb i verktygstipset.

Avsnittet "Aktiva jobbannonser" i sidofältet visar aktiva jobbannonser med motsvarande webbadresser (URL:er).

Avsnittet "Unika jobbannonser för SDFF" i sidofältet visar ett exempel på de jobbannonser som en förening skulle kunna visa i sin portal. (URL:er).

## License
This project is licensed under the MIT License