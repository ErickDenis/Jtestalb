import urllib.request
import json
import os

# Get data of json
url_items_shop = "https://raw.githubusercontent.com/broderickhyman/ao-bin-dumps/master/items.json"
url_items="https://raw.githubusercontent.com/broderickhyman/ao-bin-dumps/master/formatted/items.json"
response_shop = urllib.request.urlopen(url_items_shop)
data = json.loads(response_shop.read())
print("Se obtuvieron todos los datos")

# # Create principal path items
directory = os.path.abspath(os.getcwd())
new_dir = ""
if not os.path.exists("items"):
    os.makedirs("items")
directory+="/items"
print("Carpeta items Creada o encontrada con exito")

# loops of container items category and sub category
items = data["items"]
categories_rares = [
    "farmableitem",
    "simpleitem",
    "consumableitem",
    "consumablefrominventoryitem",
    "equipmentitem",
    "weapon",
    "mount",
    "furnitureitem",
    "journalitem",
    "labourercontract",
    "mountskin",
    "crystalleagueitem"
]
item_first = "hideoutitem"

if(len(items)==16):
    categories = items["shopcategories"]["shopcategory"];
    for category in categories:
        new_dir = directory
        if not os.path.exists(new_dir+"/"+category["@id"]):
            os.makedirs(new_dir+"/"+category["@id"])
        subcategories = category["shopsubcategory"]
        for subcategory in subcategories:
            if not os.path.exists(new_dir+"/"+category["@id"]+"/"+subcategory["@id"]):
                os.makedirs(new_dir+"/"+category["@id"]+"/"+subcategory["@id"])
            items_of_category_subcategory = []
            if(items[item_first]["@shopcategory"]==category["@id"] and items[item_first]["@shopsubcategory1"]==subcategory["@id"]):
                items_of_category_subcategory.append(items[item_first])
            for i, category_rare in enumerate(categories_rares):
                if(category_rare == "mountskin"):
                    if(category["@id"]=="consumables" and subcategory["@id"]=="vanity"):
                        for i, object in enumerate(items[category_rare]):
                            items_of_category_subcategory.append(object)
                else:
                    for i, object in enumerate(items[category_rare]):
                        if(object["@shopcategory"]==category["@id"] and object["@shopsubcategory1"]==subcategory["@id"]):
                            items_of_category_subcategory.append(object)
            with open(new_dir+"/"+category["@id"]+"/"+subcategory["@id"]+"/"+subcategory["@id"]+'.json', 'w+') as json_file:
                json.dump(items_of_category_subcategory, json_file)
else:
    print("Cambiaron algo chequear");
