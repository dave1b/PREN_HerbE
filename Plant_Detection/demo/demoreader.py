import json
from urllib import response
import time
import threading

f = open('/Users/davebrunner/Documents/GitHub/pren/Plant_Detection/demorespone.json')
print(time.time())
time.sleep(10)
print(time.time())
# returns JSON object as 
# a dictionary
response = json.load(f) 

recognisedPlantsList = []
recognisedPlantsListx = []
imgURL = (response["images"][0]["url"])
print("PlantApiSerice - detectPlant() URL: " + str(imgURL))
print("start")
for suggestion in response["suggestions"]:
        if(suggestion["probability"] >= 0):
            recognisedPlantsList.append(suggestion["plant_name"])
        if not(False):
            recognisedPlantsList1 = recognisedPlantsList
            try:
                print(type(response["suggestions"][0]["plant_details"]["common_names"][1]) == None)
                commonName = response["suggestions"][0]["plant_details"]["common_names"][0]
                plant1Type = recognisedPlantsList[0]
                imageURL = imgURL
                print("PlantApiSerice - detectPlant() plantList " + str(recognisedPlantsList1))
                print("PlantApiSerice - detectPlant() plant1Type " + str(plant1Type))
            except:
                commonName = 'keine bekannten commonName'
                print("error")
            else:
                print("der typ ist: " + type(response["suggestions"][0]["plant_details"]["common_names"][0]))
        else:
            recognisedPlantsListx = recognisedPlantsList
            print("PlantApiSerice - detectPlant() recognisedPlantsListx " + str(recognisedPlantsListx))
print("PlantApiSerice - detectPlant(): am Ende")   
print(recognisedPlantsList)   
print(commonName)   
print("PlantApiSerice - detectPlant(): am Ende")   
