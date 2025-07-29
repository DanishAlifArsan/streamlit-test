import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.write('Hello world!')
st.info('This is a machine learning app')

with st.expander('Data'):
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df
