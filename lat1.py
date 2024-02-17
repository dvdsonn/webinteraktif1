import streamlit as st
import pandas as pd
st.write("Coding Club 2024")
import matplotlib.pyplot as plt

df = pd.DataFrame ({
    'No': [1, 2, 3, 4],
    'Nama' : ['Nurul','Nadia','Vino','Zahwa'],
    'Nilai' : [98, 90, 83, 92]
})

df