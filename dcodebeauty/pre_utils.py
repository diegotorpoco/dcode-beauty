from dcodebeauty.datos import read_file

#Ejecutamos la función read_file que trae los textos a procesar
products, data, chori_data = read_file()

#Funcion de deteccion de descripcion de OCR
def find_description(text, data=data):
    df_descrip = {'ingredients':[],'descriptions':[]}
    for word in text:
        for i in range(len(data["names"])):
            if word.lower() == data["names"][i].lower():
                df_descrip['descriptions'].append(data["description"][i])
                df_descrip['ingredients'].append(data['names'][i])
    print(f"Found {round(len(df_descrip['descriptions'])/len(text)*100,2)}% of ingredients")
    return df_descrip
