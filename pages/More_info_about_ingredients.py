import streamlit as st
from PIL import Image
from io import StringIO
import time
from dcodebeauty.datos import read_file
import pandas as pd

st.set_page_config(page_title="Info about ingredients", page_icon="🔍")

st.markdown("# Info about ingredients")
st.sidebar.header("Info about ingredients")
st.write(
    """In this section you can check available information about many ingredients"""
)

#products, data, chori_data = read_file()
PRODUCTS_PATH_LOCAL= './data/paulas_chorice.csv'
chori = pd.read_csv(PRODUCTS_PATH_LOCAL)

st.dataframe(data=chori, width=None, height=None)
