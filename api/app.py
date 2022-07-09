from dcodebeauty.utils import predict_product
from dcodebeauty.ocr import detect_photo
import pandas as pd
import json
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/predict")
def predict(text):

    df = predict_product(text)
    df = df.to_json(orient='records')
    return {'ingredients':df}

#def json_df(response):
 #   res = json.loads(response.content)['ingredients']
  #  return pd.read_json(res)

@app.post("/predict_photo")
def predict_photo(img: UploadFile = File(...)):
    text = detect_photo(img)
    df = predict_product(text,search=False)
    df = df.to_json(orient='records')
    return {'ingredients':df}
