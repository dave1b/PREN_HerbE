import base64
import requests
import time
from apiKeys import plantIDkey

def scan(imagePfad):
    # encode image to base64
    with open(imagePfad, "rb") as file:
        images = [base64.b64encode(file.read()).decode("ascii")]
    your_api_key = plantIDkey
    json_data = {
        "images": images,
        "modifiers": ["similar_images"],
        "plant_details": ["common_names", "url", "wiki_description", "taxonomy"]
    }
    response = requests.post(
        "https://api.plant.id/v2/identify",
        json=json_data,
        headers={
            "Content-Type": "application/json",
            "Api-Key": your_api_key
        }).json()
    recognisedPlantsList = []  
    for suggestion in response["suggestions"]:
        recognisedPlantsList.append(suggestion["plant_name"])  
    return recognisedPlantsList

    #print(suggestion["plant_name"])    # Taraxacum officinale
    #print(suggestion["plant_details"]["common_names"])    # ["Dandelion"]
    #print(suggestion["plant_details"]["url"])    # https://en.wikipedia.org/wiki/Taraxacum_officinale


    #print(response)
    #for suggestion in response["suggestions"]:
    #print(suggestion["plant_name"])    # Taraxacum officinale
    #print(suggestion["plant_details"]["common_names"])    # ["Dandelion"]
    #print(suggestion["plant_details"]["url"])    # https://en.wikipedia.org/wiki/Taraxacum_officinale