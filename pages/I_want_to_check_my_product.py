from distutils.command.upload import upload
import streamlit as st
import numpy as np
import pandas as pd
import streamlit as st
# from PIL import Image
# from io import StringIO
import time
import requests
import json

# #products, data, chori_data = read_file()
# PRODUCTS_PATH_LOCAL= './data/products.csv'
# products_full = pd.read_csv(PRODUCTS_PATH_LOCAL)
# products = products_full["name"]

# # products, data, chori_data = read_file()

st.set_page_config(
    page_title="D-Code Beauty App",
    page_icon="๐ฟ",
    layout="centered",  # wide
    initial_sidebar_state="collapsed", #collapsed
    menu_items={
#         'Get Help': 'https://www.extremelycoolapp.com/help',
#         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "### This is a header. This is an *extremely* cool app/n developed by DCodeBeauty.com!"})


st.subheader("""The app will evaluate from ๐ฟ to ๐ฟ๐ฟ๐ฟ depending on the amount of natural ingredients:""")

st.write("๐ฟ Means less than 33% of its ingredients are natural")
st.write("๐ฟ๐ฟ Means less than 66% of its ingredients are natural")
st.write("๐ฟ๐ฟ๐ฟ Means more than 67% of its ingredients are natural")

var = st.text_input('Please type the name of your product below')
api_url = "https://dcodebeauty-api-o4dbbg4ljq-uc.a.run.app/predict" #acรก hay que levantar la url de gcp

if var:
    params = {'text':var}
    res = requests.post(api_url, params = params)
    res = json.loads(res.content)['ingredients']
    res = pd.DataFrame(pd.read_json(res))
    natural = sum(res["resultado_final"] == "natural")
    quimico = sum(res["resultado_final"] == "quimico")
    indet = sum(res["resultado_final"] == "no se puede determinar")
    total = res["resultado_final"].count()
    nat_por = natural/total
    if nat_por < 0.33:
        st.markdown(''' ### ๐ฟ - Your product is not so natural''')
    elif nat_por <= 0.66:
        st.markdown(''' ### ๐ฟ๐ฟ - Your product is pretty natural!''')
    else:
        st.markdown(''' ### ๐ฟ๐ฟ๐ฟ - Good choice! this product is amazing!''')

    conds = [
    (res['resultado_final'] == "natural"),
    (res['resultado_final'] == "quimico"),
    (res['resultado_final'] == "no se puede determinar")]

    letters = ["๐ฟ The origin of this product is natural",
               '๐งช The origin of this product is synthetic',
               "๐ We don't have enough information about this product, so please head to the sidebar for more details on the product"]

    res['Result'] = np.select(conds,letters)
    res = res.drop(columns = ["quimico", "efecto", "natural", "resultado_parcial", "resultado_final"]).set_index("Ingredient")
    res #aca mejorar el tamaรฑo del dataframe

else:
    st.markdown('### No product was found, please upload a picture of the ingredients')


# SUBIR LA FOTITO DESDE LA COMPU
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    if st.button('Check me out!'):
        st.image(uploaded_file, width=200)
        params = {"img": uploaded_file.getvalue()}
        api_url = "https://dcodebeauty-api-o4dbbg4ljq-uc.a.run.app/predict_photo"  #acรก hay que levantar la url de gcp
        res = requests.post(api_url, files=params,verify=False)
        res = json.loads(res.content)['ingredients']
        res = pd.read_json(res)
        natural = sum(res["resultado_final"] == "natural")
        quimico = sum(res["resultado_final"] == "quimico")
        indet = sum(res["resultado_final"] == "no se puede determinar")
        total = res["resultado_final"].count()
        nat_por = natural/total
        if nat_por < 0.33:
            st.markdown(''' ### ๐ฟ - Your product is not so natural''')
        elif nat_por <= 0.66:
            st.markdown(''' ### ๐ฟ๐ฟ - Your product is pretty natural!''')
        else:
            st.markdown(''' ### ๐ฟ๐ฟ๐ฟ - Good choice! this product is amazing!''')

        conds = [
        (res['resultado_final'] == "natural"),
        (res['resultado_final'] == "quimico"),
        (res['resultado_final'] == "no se puede determinar")]

        letters = ["๐ฟ The origin of this product is natural",
                '๐งช The origin of this product is synthetic',
                "๐ We don't have enough information about this product, so please head to the sidebar for more details on the product"]

        res['Result'] = np.select(conds,letters)
        res = res.drop(columns = ["quimico", "efecto", "natural", "resultado_parcial", "resultado_final"]).set_index("Ingredient")
        res


# with st.spinner('Wait for it...'):
#     time.sleep(5)
# st.success('Done!')


#PARA LOS PRODUCTOS PELIGROSOS
# st.warning('This is a warning')
