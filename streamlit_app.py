import streamlit as st
import pandas as pd
import numpy as np
voc=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRy9rF8hUvz6P8kdm3AvK0wm1kcqkrhKhhH2apM5aLL-VTh9oHGPRdAZP0EOnCdlUNwOzCm_aJekCHm/pub?output=csv')
l=voc.shape[0] 
i=np.random.choice(range(l))
word_fr=voc['Définition'].values[i]
word_chi=voc['Hanzi'].values[i]
st.write(word_fr+"Hanzi"+word_chi)
st.button("refresh")
indices=np.random.choice(l,size=4,replace=False)
j=np.random.choice(indices)
word_fr=voc["Définition"].values[j]
st.write("Traduis:"+word_fr)
for i in range(4):
  st.button(voc["Hanzi"].values[indices[i]],on_clich=is_correct,args=[indices[i],j])
def is_correct(i,j):
  if i==j:
    st.write("Bravo")
  else:
    st.write("Raté")
