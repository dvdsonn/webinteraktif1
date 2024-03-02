import streamlit as st
# import pandas as pd
# st.write(" Infinity Coding Club 2024")
# #import matplotlib.pyplot as plt

# df = pd.DataFrame ({
#     'No': [1, 2, 3, 4],
#     'Nama' : ['Nurul','Nadia','Vino','Zahwa'],
#     'Nilai' : [98, 90, 100, 92]
# })

# df

def page_1():
    st.title("Halaman 1")
    st.write('Halaman ini digunakan untuk Intro')
def page_2():
    st.title("Hlaman 2")
    st.write('Halaman ini digunakan untuk Menampilkan youtube')
def page_3():
    st.title("Hlaman 3")
    st.write('Halaman ini digunakan untuk Menampilkan rumus Matematika')
        
PAGES = {
     "Pages 1" : page_1,
     "Pages 2" : page_2,
     "Pages 3" : page_3
 }   

page = st.sidebar.radio("Halaman", list(PAGES.keys()))
PAGES[page]()