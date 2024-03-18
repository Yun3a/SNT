import streamlit as st
import pandas as pd
voc=pd.nead_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRy9rF8hUvz6P8kdm3AvK0wm1kcqkrhKhhH2apM5aLL-VTh9oHGPRdAZP0EOnCdlUNwOzCm_aJekCHm/pubhtml')
st.dataframe(voc)
l=voc.shape[o] 
i=np.random.choice(range(l))
word_fr=voc['Définition'].values[i]
word_chi=voc['hanzi'].values[i]
st.write(word_fr+"hanzi"+word_chi)
