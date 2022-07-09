import streamlit as st
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from io import StringIO
import time
import requests

#products, data, chori_data = read_file()
PRODUCTS_PATH_LOCAL= './data/products.csv'
products_full = pd.read_csv(PRODUCTS_PATH_LOCAL)
products = products_full["name"]

# products, data, chori_data = read_file()

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

# result_product = acá viene el % de productos naturales sobre el total
# si result_product es entre 0 y 33% una hojita, si es entre 34% y 66% poner dos hojitas y si es +66% poner 3 hojitas
# Luego imprimir el dataframe en columnas donde es Ingrediente: "Resultado Final"
# Si la columna resultado final es igual a:
#   quimico: "[Tubo de ensayo] The origin of this product is synthetic"
#   natural: "[Hojita] The origin of this product is natural"
#   otro: "[Signo de pregunta] We don't have enough information about this product, so please head to the sidebar
# for more details on the product"

var = st.text_input('Texto')
var
if var:
    api_url = "https://localhost:8000/predict"
    params = {'text':var}
    res = requests.get(api_url, params = params)
    res



# SUBIR LA FOTITO DESDE LA COMPU
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    if st.button('predecir'):
        # photo = Image.open(uploaded_file)
        st.image(uploaded_file, use_column_width=False)
        params = {"img": uploaded_file.getvalue()}
        api_url = "https://127.0.0.1:8000/predict_photo"
        res = requests.post(api_url, files=params,verify=False)


# with st.spinner('Wait for it...'):
#     time.sleep(5)
# st.success('Done!')

# result_OCR = acá viene el % de productos naturales sobre el total
# si result_product es entre 0 y 33% una hojita, si es entre 34% y 66% poner dos hojitas y si es +66% poner 3 hojitas
# Luego imprimir el dataframe en columnas donde es Ingrediente: "Resultado Final"
# Si la columna resultado final es igual a:
#   quimico: "[Tubo de ensayo] The origin of this product is synthetic"
#   natural: "[Hojita] The origin of this product is natural"
#   otro: "[Signo de pregunta] We don't have enough information about this product, so please head to the sidebar
# for more details on the product"

#PARA LOS PRODUCTOS PELIGROSOS
# st.warning('This is a warning')
