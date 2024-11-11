import streamlit as st
import pandas as pd
import numpy as np

st.title('Police Incident Reports from 2018 to 2020 in San Francisco')
df=pd.read_csv("Policev1.csv")

st.markdown('The data show below belong to incident reports in the city os San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.')
mapa=pd.DataFrame()
mapa['Date']=df ['Incident Date']
mapa['Day']=df ['Incident Day of week']
mapa['Police District']=df ['Police district']
mapa['Neighborhood']=df ['Analysis neighborhood']
mapa['Incident category']=df ['Incident Category']
mapa['Incident subcategory']=df ['Incident subcategory']
mapa['Resolution']=df ['Resolution']
mapa['lat']=df ['Latitud']
mapa['lon']=df ['Longitud']
mapa=maoa.dropna()
df
