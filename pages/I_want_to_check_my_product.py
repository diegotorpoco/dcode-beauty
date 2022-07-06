import streamlit as st
import numpy as np
import pandas as pd
from dcodebeauty.datos import read_file
import streamlit as st
from PIL import Image
from io import StringIO
import time


#products, data, chori_data = read_file()
PRODUCTS_PATH_LOCAL= './data/products.csv'
products_full = pd.read_csv(PRODUCTS_PATH_LOCAL)
products = products_full["name"]

st.set_page_config(
    page_title="D-Code Beauty App",
    page_icon="🌿",
    layout="centered",  # wide
    initial_sidebar_state="collapsed", #collapsed
    menu_items={
#         'Get Help': 'https://www.extremelycoolapp.com/help',
#         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "### This is a header. This is an *extremely* cool app/n developed by DCodeBeauty.com!"})


st.markdown("# Checking your product")
st.sidebar.header("Checking your product")
st.markdown(
    """### Please type the name of your product, so we can help you decode its ingredients"""
)

# INGRESAR EL DATO DEL PRODUCTO
option = st.selectbox('Product Name', (products), format_func=lambda x: 'None' if x == '' else x)

if option:
    st.success('Yay! 🎉')
else:
    st.markdown('### No product was found, please upload a picture of the ingredients')


# SUBIR LA FOTITO DESDE LA COMPU
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     photo = Image.open(uploaded_file)
     st.image(photo, use_column_width=False)

with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')


#PARA LOS PRODUCTOS PELIGROSOS
st.warning('This is a warning')
