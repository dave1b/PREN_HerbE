import base64
import requests
import time
from apiKeys import plantIDkey

def scan(imagePfad):
    # encode image to base64
    with open(imagePfad, "rb") as file:
        image = [base64.b64encode(file.read()).decode("ascii")]
    params = {
        "images": image,
        "modifiers": ["crops_medium"],
        "plant_language": "en", # de not supported 
        "plant_details": ["common_names"]
    }
    response = requests.post(
        "https://api.plant.id/v2/identify",
        json=params,
        headers={
            "Content-Type": "application/json",
            "Api-Key": plantIDkey
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