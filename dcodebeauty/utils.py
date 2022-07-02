from dcodebeauty.datos import read_file
from dcodebeauty.ocr import find_product_description,detect_text
from dcodebeauty.pre_utils import find_description
from gensim.models.ldamodel import LdaModel

ruta_modelo = '../models/model_3_topics'
model = LdaModel.load(ruta_modelo)

def predict_product(text):
    product = find_product_description(text)
    description = find_description(product)
