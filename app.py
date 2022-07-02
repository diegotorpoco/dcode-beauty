import streamlit as st
from PIL import Image
from io import StringIO
import time
from dcodebeauty.datos import read_file
import pandas as pd

#para probarlo correr
#url = http://localhost:8501/

#products, data, chori_data = read_file()
PRODUCTS_PATH_LOCAL= './data/products.csv'
products_full = pd.read_csv(PRODUCTS_PATH_LOCAL)
products = products_full["name"]

# page conf
st.set_page_config(
    page_title="D-Code Beauty App",
    page_icon="🌿",
    layout="centered",  # wide
    initial_sidebar_state="collapsed", #collapsed
    menu_items={
#         'Get Help': 'https://www.extremelycoolapp.com/help',
#         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "### This is a header. This is an *extremely* cool app/n developed by DCodeBeauty.com!"})


st.title('DCode-Beauty')
st.subheader('Here to help decode your skincare routine')

# ACA TENEMOS QUE DEFINIR QUE MOSTRAR
sidebar = st.sidebar.radio('Please select an option', ("I want to check the product", "More info about ingredients"))

if sidebar == 'I want to check the product':
     st.write('Show the look-up bar')
else:
     st.write("Show Paulas Chorice")

# INGRESAR EL DATO DEL PRODUCTO
option = st.selectbox('Please type the name of the product', (products))
#st.write('You selected:', option)
st.success('This is a success message!')


# SUBIR LA FOTITO DESDE LA COMPU
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     photo = Image.open(uploaded_file)
     st.image(photo, use_column_width=False)

# SACAR FOTO DESDE CELU
picture = st.camera_input("Take a picture")
if picture:
     st.image(picture)

with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')

#PARA LOS PRODUCTOS PELIGROSOS
st.warning('This is a warning')



CSS = """
h1 {
    color: green;
}
.stApp {
    background-image: back_image;
    background-size: cover;
}
"""
st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

# st.markdown('''
# ### 💡 We'll try and help decode the ingredients of your skincare routine
# #
# # ''')
