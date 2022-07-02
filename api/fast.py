from fastapi import FastAPI
import pandas as pd
from dcodebeauty.datos import read_file
from dcodebeauty.ocr import find_product_description,detect_text
from dcodebeauty.pre_utils import find_description

app = FastAPI()

@app.get("/predict")
def predict(description_list):

    description_list = description_list






    # ⚠️ TODO: get model from GCP

    # pipeline = get_model_from_gcp()
    #pipeline = joblib.load('model.joblib')

    # make prediction
    #results = pipeline.predict(x)

    # convert response from numpy to python type
    #pred = float(results[0])

    #return dict(fare=pred)
