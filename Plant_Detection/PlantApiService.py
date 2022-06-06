import base64
import requests
import sys
sys.path.insert(0, '../Main_Model')
sys.path.insert(0, '../Button')
from Log import Logger

class PlantApiService:
    def __init__(self, plantIDkey, dataModel, minProbability = 0.025):
        self.dataModel = dataModel
        self.plantIDkey = plantIDkey
        self.minProbability = minProbability
        self.image_path = '../Button/plantImage.png'
        self.log = Logger("PlantApiService")
        
    def detectPlant(self, firstPlantScanned):
        self.log.debug("detectPlant()")
        
        # Base64 encode image
        image = self.encode_file(self.image_path)

        # plantID request  
        response = self.sendRequestToPlantid(self, self.plantIDkey, image)
        self.log.debug("detectPlant(): RESPONSE: " + str(response))
        response = response.json()

        #read imgURL from respose
        imgURL = (response["images"][0]["url"])
        
        # iterate over all suggestions in response and append to recognisedPlantsList
        recognisedPlantsList = []
        for suggestion in response["suggestions"]:
            if(suggestion["probability"] >= self.minProbability):
                recognisedPlantsList.append(suggestion["plant_name"])
        
        # if first plant -> write plantName, commonName and imageURL to DataModel        
        if not(firstPlantScanned):
            self.dataModel.recognisedPlantsList1 = recognisedPlantsList
            try:
                self.dataModel.commonName = response["suggestions"][0]["plant_details"]["common_names"][0]
            except:
                self.log.warning("Die Pflanze hat keinen common Name")
                self.dataModel.commonName = 'gemeiner Name nicht bekannt'
            self.dataModel.plant1Type = recognisedPlantsList[0]
            self.dataModel.imageURL = imgURL
            self.log.debug("detectPlant() plantList " + str(self.dataModel.recognisedPlantsList1))
            self.log.debug("detectPlant() plant1Type " + str(self.dataModel.plant1Type))
        # if not first plant -> write recognisedPlantsList to DataModel
        else:
            self.dataModel.recognisedPlantsListx = recognisedPlantsList
            self.log.debug("detectPlant() recognisedPlantsListx " + str(self.dataModel.recognisedPlantsListx))
        self.log.debug("detectPlant(): am Ende")   
        
    def encode_file(self, file_name):
        self.log.debug("encode_file()")
        with open(file_name, "rb") as file:
            return base64.b64encode(file.read()).decode("ascii")

    def sendRequestToPlantid(self, apiKey, image):
        params = {
             "api_key": apiKey,
            "images": [image],
            "modifiers": ["crops_medium"],
            "plant_language": "de",
            "plant_details": ["common_names"]
        }
        headers = {
            "Content-Type": "application/json"
        }
        self.log.debug("detectPlant(): before post")
        return requests.post("https://api.plant.id/v2/identify",
                                 json=params,
                                 headers=headers)
        
    
    def findMatchingPlantInDataModel(self):
        self.log.debug("findMatchingPlantInDataModel()")
        
        # check if matching plants in lists
        matchingPlantList = list(set(self.dataModel.recognisedPlantsList1) & set(self.dataModel.recognisedPlantsListx))
        
        if(len(matchingPlantList) > 0):
        # if there is a match write to DataModel
            self.log.debug("There is a match: ", True)
            self.log.debug("The matching plant type is: ", matchingPlantList[0])
            self.dataModel.plantMatchPosition = self.dataModel.amountOfPlantxScanned
            return True
        else:
            return False