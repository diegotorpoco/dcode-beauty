#Imports
from google.cloud import vision
import io
import pandas as pd


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
