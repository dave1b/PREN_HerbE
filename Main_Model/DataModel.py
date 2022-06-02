class DataModel:
    def __init__(self):
        self.QRcodeContent = None
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
    
    def resetModel(self):
        self.QRcodeContent = None
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

# HerbE states
HerbEstates =  {
  "initial": "Herb-E ist bereit für die Fahrt. Start-Knopf drücken um zu beginnen.",
  "driving": "Herb-E ist am fahren. Der Ultraschallsensor sucht nach Objekten und die Kamera nach QR-Codes.",
  "ultraDetected": "Herb-E hat mit dem Ultraschallsensor ein Objekt erkannt und sucht jetzt nach QR-Codes.",
  "qrDetected":  "Herb-E hat ein QR-Code erkannt, schiesst ein Foto und sucht nach der Pflanzenart.",
  "stop":  "Herb-E hat angehalten.",
  "stopButtonPressed": "Der Stop-Button wurde gedrückt. Herb-E ist bereit für einen erneuten Start.",
  "goal": "Herb-E hat seine Arbeit erledigt und das Ziel erreicht!!!"
}