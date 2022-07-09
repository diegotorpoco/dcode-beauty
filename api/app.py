from dcodebeauty.utils import predict_product
from dcodebeauty.ocr import detect_photo
import pandas as pd
import json
from fastapi import FastAPI, File, UploadFile


app = FastAPI()

@app.get("/predict")
def predict(text):

    df = predict_product(text)
    df = df.to_json(orient='records')
    return {'ingredients':df}

#def json_df(response):
 #   res = json.loads(response.content)['ingredients']
  #  return pd.read_json(res)

@app.get("/predict_photo")
def predict_photo(img: UploadFile = File(...)):
    text = detect_photo(img)
    df = predict_product(text,search=False)
    df = df.to_json(orient='records')
    return {'ingredients':df}
