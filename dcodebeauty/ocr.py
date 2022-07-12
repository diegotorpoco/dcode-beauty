#Imports
from google.cloud import vision
import io
import pandas as pd
from dcodebeauty.datos import read_file_gcs

#Funcion de deteccion de productos con un input del usuario - devuelve lista de ingredientes

#En primer lugar el usuario debe tipear el nombre del producto
#def user_input():
#    product_name = input("Insert product name ")

#Ejecutamos la función read_file que trae los textos a procesar
products, data, chori_data = read_file_gcs()

#Luego el modelo detecta los ingredientes del producto y los convierte en una lista
def find_product_description(product_name):
    product_description_list = []
    for i in range(len(products["name"])):
        if product_name.lower() == (products["name"][i].lower()):
            product_description_list.append(products["ingredient_list"][i])
    if product_description_list == []:
        print("Product not found, please take a photo of the ingredients")
    else:
        texts = product_description_list[0]
        return texts.split(',')


#Funcion OCR - Transforma foto desde un path en lista de ingredientes
def detect_photo(img):
    """Detects text in the file."""
    # from google.cloud import vision
    # import io
    client = vision.ImageAnnotatorClient()
    # image = vision.Image(content=img)

    response = client.text_detection(image=img.file)
    text = str((response.text_annotations[0]).description)
    return text.split(',')

def detect_text(path):
    """Detects text in the file."""
    # from google.cloud import vision
    # import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    text = str((response.text_annotations[0]).description)
    return text.split(',')


#Funcion de limpieza de texto
def cleaning(detect_text):
    text = [''.join(filter(lambda i: i not in "#$%&'()*+,.:<=>?@[\\]^_`{|}~\n",item.lower().strip().replace("/" , " ").replace('\"', " ").replace("aqua water", "water").replace("aqua", "water").replace("ingredients", "").replace("INGREDIENTS", "").replace("Ingredients", "").replace("Ingredientes", "").replace("ingredientes" , "").replace("Ingredientes ", "").replace("ingredientes ", ""))) for item in detect_text]
    text = [t.strip() for t in text]
    return text
