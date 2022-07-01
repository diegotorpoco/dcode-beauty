from dcodebeauty.datos import read_file

#Ejecutamos la función read_file que trae los textos a procesar
products, data, chori_data = read_file()

#Funcion de deteccion de descripcion
def find_description(text):
    description_list = []
    for word in text:
        for i in range(len(data["names"])):
            if word == data["names"][i].lower():
                description_list.append(data["description"][i])
    print(f"Found {round(len(description_list)/len(text)*100,2)}% of ingredients")
    return description_list
