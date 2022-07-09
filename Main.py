import streamlit as st
from PIL import Image
from io import StringIO
import time
from dcodebeauty.datos import read_file
import pandas as pd
import requests
#para probarlo correr
#url = http://localhost:8501/


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


st.write("# D-Code Beauty App🌿")

st.markdown(
    """
    D-Code Beauty App is here to help decode your skincare routine.


    **👈 Please select an option from the sidebar**
    """
)
var = st.text_input('Texto')
api_url = "http://0.0.0.0:8888/predict"

if var:
    params = {'text':var}
    res = requests.post(api_url, params = params)
    res.content

# # ACA TENEMOS QUE DEFINIR QUE MOSTRAR
# sidebar = st.sidebar.radio('Please select an option', ("I want to check the product", "More info about ingredients"))

# if sidebar == 'I want to check the product':
#      st.write('Show the look-up bar')
# else:
#      st.write("Show Paulas Chorice")


# st.title('DCode-Beauty')
# st.subheader('Here to help decode your skincare routine')


# st.markdown('''
# ### 💡 We'll try and help decode the ingredients of your skincare routine
# #
# # ''')
