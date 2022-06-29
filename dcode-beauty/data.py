from google.cloud import storage
import pandas as pd


### GCP configuration - - - - - - - - - - - - - - - - - - -

# /!\ you should fill these according to your account

### GCP Project - - - - - - - - - - - - - - - - - - - - - -

# not required here

### GCP Storage - - - - - - - - - - - - - - - - - - - - - -

BUCKET_NAME = 'dcode-beauty'

##### Data  - - - - - - - - - - - - - - - - - - - - - - - -

# train data file location
# or if you want to use the full dataset (you need need to upload it first of course)
DESCRIPTION_PATH = 'description_clean.csv'
PAULAS_PATH = 'products.csv'
PRODUCTS_PATH = 'paulas_chorice.csv'

##### Training  - - - - - - - - - - - - - - - - - - - - - -

# not required here

##### Model - - - - - - - - - - - - - - - - - - - - - - - -

# model folder name (will contain the folders for all trained model versions)
#MODEL_NAME = 'taxifare'

# model version folder name (where the trained model.joblib file will be stored)
#MODEL_VERSION = 'v1'

### GCP AI Platform - - - - - - - - - - - - - - - - - - - -

# not required here

### - - - - - - - - - - - - - - - - - - - - - - - - - - - -

products = pd.read_csv('DESCRIPTION_PATH')
data = pd.read_csv('DESCRIPTION_PATH')
chori_data = pd.read_csv('PAULAS_PATH')
