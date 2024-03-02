import streamlit as st
from page1 import page_1
from page2 import page_2
from page3 import page_3
# import pandas as pd
# st.write(" Infinity Coding Club 2024")
# #import matplotlib.pyplot as plt

# df = pd.DataFrame ({
#     'No': [1, 2, 3, 4],
#     'Nama' : ['Nurul','Nadia','Vino','Zahwa'],
#     'Nilai' : [98, 90, 100, 92]
# })

# df


        
PAGES = {
     "Pages 1" : page_1,
     "Pages 2" : page_2,
     "Pages 3" : page_3
 }   
st.sidebar.image("pubg.webp", width = 200)
page = st.sidebar.radio("Halaman", list(PAGES.keys()))
PAGES[page]()