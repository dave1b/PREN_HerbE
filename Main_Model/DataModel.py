class DataModel:
    def __init__(self):
        self.QRcodeContent = None
        self.UltrasonicObjectDetected = False
        self.dateTimeStamp = None
        self.startTimeStamp = None
        self.endTimeStamp = 0
        self.isDriving = False
        self.state = HerbEstates["initial"]
        self.distanceDriven = 0
        self.plantImage = None
        self.recognisedPlantsList1 = None
        self.recognisedPlantsListx = None
        self.amountOfPlantxScanned = 1
        self.plant1Type = "noch undefiniert"
        self.commonName = ""
        self.plantMatchPosition = "noch undefiniert"
        self.isFinished = False
        self.imageURL = ""
        
    
    def toJSON(self, restAPIKey):
        return {
            "id": 1,
            "dateTimeStamp": self.dateTimeStamp,
            "startTimeStamp": self.startTimeStamp,
            "endTimeStamp": self.endTimeStamp,
            "distance": self.distanceDriven,
            "state": self.state,
            "plantType": self.plant1Type,
            "commonName": self.commonName,
            "plantMatchPosition": self.plantMatchPosition,
            "isFinished": self.isFinished,
            "imageURL": self.imageURL,
            "apiKey": restAPIKey
        }

# HerbE states
HerbEstates =  {
  "initial": "HerbiE ist parkiert und am ruhen",
  "driving": "HerbE ist am fahren. Der Ultraschallsensor sucht nach Objekten und die Kamera nach QR-Codes.",
  "ultraDetected": "Herbie hat mit dem Ultraschallsensor ein Objekt erkannt",
  "qrDetected":  "HerbiE schiesst ein Foto und sucht nach der Pflanzenart.",
  "stop":  "HerbiE hat angehalten.",
  "finished": "HerbE ist gestoppt :(",
  "goal": "Ziel erreicht!!!"
}