import requests


additive_dictionary = {}
with open("la_hacks/static/additive_dictionary", 'r') as f:
    for line in f:
        key, value = line.strip().split('\t', 1)
        additive_dictionary[key] = value
    

def get_product_info(barcode_number):
    FOOD_FACTS_API_URL = f"https://world.openfoodfacts.org/api/v0/product/{barcode_number}.json"
    response = requests.get(FOOD_FACTS_API_URL)
    #toss a popup modal here if there's an error when implemented
    response.raise_for_status() 
    product_data = None
    try:
        product_data = response.json()["product"]
    except:
        return {
            "brand": "error",
            "name": "error",
            "ingredients": [],
            "additives": [],
            "eco_grade": -1,
            "co2": -1,
            "image_url" : "error"
        }

    product_name = product_data.get("product_name", "Unknown")
    product_brand = product_data.get("brands", product_name).capitalize()
    
    try:
        ingredients_list = list(map(lambda x: x.split(':')[1].replace('-', ' ').capitalize(), product_data["ingredients_hierarchy"]))
    except:
        ingredients_list = []
    additives_list = []
    image_url = product_data["image_url"]
    if(product_data.get("ecoscore_data") != None):
        grade = product_data.get("ecoscore_data").get("grade", "Unknown")
        co2 = product_data.get("ecoscore_data").get("agribalyse").get("co2_total")
        if co2 != None:
            co2 = float(co2) * 100 
            co2 = "{:.2f}".format(co2)
        else:
            co2 = "Unknown"
    for i in range(len(ingredients_list)):
        if ingredients_list[i].lower() in additive_dictionary:
            ingredients_list[i] = additive_dictionary[ingredients_list[i].lower()]
            additives_list.append(ingredients_list[i])
    return {
        "brand": product_brand,
        "name": product_name,
        "ingredients": ingredients_list,
        "additives": additives_list,
        "eco_grade": grade,
        "co2": co2,
        "image_url" : image_url
    }