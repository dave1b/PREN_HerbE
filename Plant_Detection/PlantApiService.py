import base64
import requests

class PlantApiService:
    def __init__(self, plantIDkey, dataModel, minProbability = 0.025):
        self.dataModel = dataModel
        self.plantIDkey = plantIDkey
        self.minProbability = minProbability

    def detectPlant(self, firstScanInRun):
        image = [base64.b64encode(self.dataModel.plantImage).decode("ascii")]
        params = {
            "images": image,
            "modifiers": ["crops_medium"],
            "plant_language": "en",  # de not supported
            "plant_details": ["common_names"]
        }
        response = requests.post(
            "https://api.plant.id/v2/identify",
            json=params,
            headers={
                "Content-Type": "application/json",
                "Api-Key": self.plantIDkey
            }).json()
        recognisedPlantsList = []
        imgURLList = []
        for suggestion in response["suggestions"]:
            if(suggestion["probability"] >= self.minProbability):
                recognisedPlantsList.append(suggestion["plant_name"])
                imgURLList.append(suggestion["images"]["url"])
        if(firstScanInRun):
            self.dataModel.recognisedPlantsList1 = recognisedPlantsList
            self.dataModel.plant1Type = recognisedPlantsList[0]
            self.dataModel.imageURL = imgURLList[0]
        else:
            self.dataModel.recognisedPlantsListx = recognisedPlantsList
    
    def findMatchingPlantInDataModel(self):
        matchingPlantList = list(set(self.dataModel.recognisedPlantsList1)&set(self.dataModel.recognisedPlantsListx))
        if(len(matchingPlantList) > 0):
            print("There is a match: ", True)
            print("The matching plant type is: ", matchingPlantList[0])
            self.dataModel.plantMatchPosition = self.dataModel.amountOfPlantxScanned
            return True
        else:
            return False