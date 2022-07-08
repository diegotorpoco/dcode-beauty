from fastapi import FastAPI
from dcodebeauty.utils import predict_product
import pandas as pd
import json

app = FastAPI()

@app.get("/predict")
def predict(text):

    df = predict_product(text)
    df = df.to_json(orient='records')
    return {'ingredients':df}

def json_df(response):
    res = json.loads(response.content)['ingredients']
    return pd.read_json(res)

    # ⚠️ TODO: get model from GCP

    # pipeline = get_model_from_gcp()
    #pipeline = joblib.load('model.joblib')

    # make prediction
    #results = pipeline.predict(x)

    # convert response from numpy to python type
    #pred = float(results[0])

    #return dict(fare=pred)
