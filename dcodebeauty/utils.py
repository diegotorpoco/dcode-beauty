from dcodebeauty.datos import read_file
from dcodebeauty.pre_utils import find_description
from dcodebeauty.ocr import find_product_description,detect_text,cleaning
from gensim.models.ldamodel import LdaModel
from dcodebeauty.gensim_func import id2word,corpus
import pandas as pd
import numpy as np

def predict_product(text,search=True):
    ruta_modelo = '../models/model_3_topics'
    model = LdaModel.load(ruta_modelo)
    if search:
        product = find_product_description(text)
        clean_product = cleaning(product)
        #description = find_description(clean_product)
    else:
        clean_product = cleaning(text)
    description = find_description(clean_product)
    values = [model[id2word.doc2bow(description['descriptions'][i].split())] for i in range(len(description['descriptions']))]
    df_topic = pd.DataFrame(values)
    df_topic['Ingredient'] = description['ingredients']
    df_topic = df_topic.rename(columns={0:'quimico',1:"efecto",2:"natural"})
    df_topic = df_topic.applymap(lambda x: (0,0) if x is None else x)
    df_topic['quimico'] = df_topic['quimico'].apply(lambda x: x[1])
    df_topic['efecto'] = df_topic['efecto'].apply(lambda x: x[1])
    df_topic['natural'] = df_topic['natural'].apply(lambda x: x[1])
    df_topic = df_topic.set_index('Ingredient')

    conds = [
    (df_topic['quimico'] > df_topic['efecto']) & (df_topic['quimico'] > df_topic['natural']),
    (df_topic['natural'] > df_topic['efecto']) & (df_topic['natural'] > df_topic['quimico']),
    (df_topic['efecto'] > df_topic['quimico']) & (df_topic['efecto'] > df_topic['natural'])]
    leters = ['quimico','natural','efecto']
    df_topic['resultado_parcial'] = np.select(conds,leters)

    conds2 = [
    (df_topic['quimico'] > df_topic['natural'])& (df_topic['quimico']-(df_topic['natural'])>0.1),
    (df_topic['natural'] > df_topic['quimico'])& (df_topic['natural']-(df_topic['quimico'])>0.1),
    (df_topic['quimico'] > df_topic['natural']),
    (df_topic['natural'] > df_topic['quimico'])]
    leters2 = ['quimico','natural','no se puede determinar','no se puede determinar']
    df_topic['resultado_final'] = np.select(conds2,leters2)

    return df_topic
