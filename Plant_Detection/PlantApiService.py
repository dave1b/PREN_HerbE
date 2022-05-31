import base64
import requests
import sys
sys.path.insert(0, '/home/pi/Desktop/PREN/Main_Model')
sys.path.insert(0, '/home/pi/Desktop/PREN/Button')
sys.path.insert(0, '../Main_Model')
sys.path.insert(0, '../Button')
from Log import Logger

class PlantApiService:
    def __init__(self, plantIDkey, dataModel, minProbability = 0.025):
        self.dataModel = dataModel
        self.plantIDkey = plantIDkey
        self.minProbability = minProbability
        self.log = Logger()
    def encode_file(self, file_name):
        self.log.info("PlantApiSerice - encode_file()")
        with open(file_name, "rb") as file:
            return base64.b64encode(file.read()).decode("ascii")
    def detectPlant(self, firstPlantScanned):
        self.log.info("PlantApiSerice - detectPlant()")
        image_path = '/home/pi/Desktop/PREN/Button/plantImage.png'
        self.log.info("PlantApiSerice - detectPlant() 1")
        image = self.encode_file(image_path)
        self.log.info("PlantApiSerice - detectPlant() 2")
        self.log.info("PlantApiSerice - detectPlant(): after encoding")

        params = {
             "api_key": self.plantIDkey,
            "images": [image],
            "modifiers": ["crops_medium"],
            "plant_language": "de",  # de not supported
            "plant_details": ["common_names"]
        }
        headers = {
            "Content-Type": "application/json"
        }
        self.log.info("PlantApiSerice - detectPlant(): before post")
        response = requests.post("https://api.plant.id/v2/identify",
                                 json=params,
                                 headers=headers)
        self.log.info("PlantApiSerice - detectPlant(): after post")
        self.log.info("PlantApiSerice - detectPlant(): RESPONSE: " + str(response))
        response = response.json()
        recognisedPlantsList = []
        self.log.info(response)
        imgURL = (response["images"][0]["url"])
        self.log.info("PlantApiSerice - detectPlant() URL: " + str(imgURL))
        for suggestion in response["suggestions"]:
            if(suggestion["probability"] >= self.minProbability):
                recognisedPlantsList.append(suggestion["plant_name"])
        if not(firstPlantScanned):
            self.dataModel.recognisedPlantsList1 = recognisedPlantsList
            try:
                self.dataModel.commonName = response["suggestions"][0]["plant_details"]["common_names"][0]
            except:
                self.log.warning("Die Pflanze hat keinen common Name")
                self.dataModel.commonName = 'gemeiner Name nicht bekannt'
            self.dataModel.plant1Type = recognisedPlantsList[0]
            self.dataModel.imageURL = imgURL
            self.log.info("PlantApiSerice - detectPlant() plantList " + str(self.dataModel.recognisedPlantsList1))
            self.log.info("PlantApiSerice - detectPlant() plant1Type " + str(self.dataModel.plant1Type))
        else:
            self.dataModel.recognisedPlantsListx = recognisedPlantsList
            self.log.info("PlantApiSerice - detectPlant() recognisedPlantsListx " + str(self.dataModel.recognisedPlantsListx))
        self.log.info("PlantApiSerice - detectPlant(): am Ende")   

    def findMatchingPlantInDataModel(self):
        matchingPlantList = list(set(self.dataModel.recognisedPlantsList1) & set(self.dataModel.recognisedPlantsListx))
        if(len(matchingPlantList) > 0):
            self.log.info("There is a match: ", True)
            self.log.info("The matching plant type is: ", matchingPlantList[0])
            self.dataModel.plantMatchPosition = self.dataModel.amountOfPlantxScanned
            return True
        else:
            return False