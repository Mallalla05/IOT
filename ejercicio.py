import streamlit as st
import pandas as pd
import numpy as np

st.title('Police Incident Reports from 2018 to 2020 in San Francisco')
df=pd.read_csv("Policev1.csv")

st.markdown('The data show below belong to incident reports in the city os San Francisco,from the year 2018 to 2020,with details from each case such as date, day of the week, police district,neighborhood in which it happened,type of incident in category and subcategory,exact location and resolution.')
df
