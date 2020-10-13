import streamlit as st
import pandas as pd
from datetime import datetime

st.title("Tissue Biorepository")

df = pd.read_csv (r'C:\Personal Projects\Development\Tarun\Tissue_data.csv',  encoding= 'unicode_escape')

#selecting Chromosome
st.sidebar.subheader("Chromosome")
Chromo_list = st.sidebar.text_input(label="", value="", key="na_upper")
# df = (df.loc[df['Type']== Type_list])

#selecting position
st.sidebar.subheader("Position")
Position_list = st.sidebar.text_input(label="", value="", key="na_lower")
# df = (df.loc[df['Type']== Type_list])
