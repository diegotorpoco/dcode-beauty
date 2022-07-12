#from google.cloud import storage
import pandas as pd
import os

### GCP configuration - - - - - - - - - - - - - - - - - - -

# /!\ you should fill these according to your account

### GCP Project - - - - - - - - - - - - - - - - - - - - - -

# not required here

### GCP Storage - - - - - - - - - - - - - - - - - - - - - -

BUCKET_NAME = 'wagon-data-840-torpoco' #anadi

##### Data  - - - - - - - - - - - - - - - - - - - - - - - -

# Path on GCS
# or if you want to use the full dataset (you need need to upload it first of course)
DESCRIPTION_PATH = 'data/description_clean.csv'
PRODUCTS_PATH = 'data/products.csv'
PAULAS_PATH = 'data/paulas_chorice.csv'

def read_file_gcs():
    products = pd.read_csv(f"gs://{BUCKET_NAME}/{PRODUCTS_PATH}")
    data = pd.read_csv(f"gs://{BUCKET_NAME}/{DESCRIPTION_PATH}")
    chori_data = pd.read_csv(f"gs://{BUCKET_NAME}/{PAULAS_PATH}")

    return products, data, chori_data


#Local Path
DESCRIPTION_PATH_LOCAL = '../data/description_clean.csv'
PRODUCTS_PATH_LOCAL= '../data/products.csv'
PAULAS_PATH_LOCAL = '../data/paulas_chorice.csv'



def read_file():
    products = pd.read_csv(PRODUCTS_PATH_LOCAL)
    data = pd.read_csv(DESCRIPTION_PATH_LOCAL)
    chori_data = pd.read_csv(PAULAS_PATH_LOCAL)

    return products, data, chori_data

##### Model - - - - - - - - - - - - - - - - - - - - - - - -

# model folder name (will contain the folders for all trained model versions)
#MODEL_NAME = 'taxifare'

# model version folder name (where the trained model.joblib file will be stored)
#MODEL_VERSION = 'v1'

### GCP AI Platform - - - - - - - - - - - - - - - - - - - -

# not required here

### - - - - - - - - - - - - - - - - - - - - - - - - - - - -
