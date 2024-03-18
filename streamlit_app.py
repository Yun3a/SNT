import streamlit as st
import pandas as pd
voc=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRy9rF8hUvz6P8kdm3AvK0wm1kcqkrhKhhH2apM5aLL-VTh9oHGPRdAZP0EOnCdlUNwOzCm_aJekCHm/pubhtml')
st.dataframe(voc)
