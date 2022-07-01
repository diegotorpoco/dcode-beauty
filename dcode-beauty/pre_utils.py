from data import products,data,data_chori

#Función de detección de descripción
def find_product_description(product_name):
    product_description_list = []
    for i in range(len(products["name"])):
        if product_name == (products["name"][i].lower()):
            product_description_list.append(products["ingredient_list"][i])
    return product_description_list[0]
