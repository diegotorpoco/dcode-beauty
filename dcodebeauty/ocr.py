#Imports
from google.cloud import vision
import io
import pandas as pd
from dcodebeauty.datos import read_file

#Funcion de deteccion de productos con un input del usuario - devuelve lista de ingredientes

#En primer lugar el usuario debe tipear el nombre del producto
#def user_input():
#    product_name = input("Insert product name ")

#Ejecutamos la función read_file que trae los textos a procesar
products, data, chori_data = read_file()

#Luego el modelo detecta los ingredientes del producto y los convierte en una lista
def find_product_description(product_name):
    product_description_list = []
    for i in range(len(products["name"])):
        if product_name == (products["name"][i].lower()):
            product_description_list.append(products["ingredient_list"][i])
    return product_description_list[0]

#Funcion OCR - Transforma foto desde un path en lista de ingredientes
def detect_text(path):
    """Detects text in the file."""
    # from google.cloud import vision
    # import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = str((response.text_annotations[0]).description)
    return texts.split(',')


#Funcion de limpieza de texto
def cleaning(detect_text):
    return [''.join(filter(lambda i: i not in "#$%&\'()*+,./:;<=>?@[\\]^_`{|}~\n", item.lower().strip())) for item in detect_text]
