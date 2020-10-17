import streamlit as st
import pandas as pd
from datetime import datetime

st.title("Tissue Biorepository")

df = pd.read_csv (r'C:\Personal Projects\Development\Tarun\Tissue_data.csv',  encoding= 'unicode_escape')

# #selecting sex
# st.sidebar.subheader("Select sex")
# S_type = df['Sex'].unique()
# Sex_SELECTED = st.sidebar.multiselect('', S_type)
# if Sex_SELECTED == []:
#     pass 
# else:
#     df = df[df['Sex'].isin(Sex_SELECTED)]

#selecting Chromosome
st.sidebar.subheader("Chromosome")
S_type = df['Sex'].unique()
Chromo_list = st.sidebar.text_input(label="", value="", key="na_upper")

if Chromo_list == []:
    pass 
else:
    df = df[df['Sex'] = str(Chromo_list)]
    


#selecting position
st.sidebar.subheader("Position")
Position_list = st.sidebar.text_input(label="", value="", key="na_lower")
# df = (df.loc[df['Type']== Type_list])

st.subheader('Total Cases: ')
st.write(len(df))
st.write(df) 
