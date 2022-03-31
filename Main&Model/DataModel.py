class DataModel:
    def __init__(self):
        self.QRcodeContent = None
        self.UltrasonicObjectDetected = False
        self.dateTimeStamp = None
        self.startTimeStamp = None
        self.endTimeStamp = None
        self.isDriving = False
        self.state = HerbEstates[0]
        self.distanceDriven = 0
        self.plantImage = None
        self.recognisedPlantsList1 = None
        self.recognisedPlantsListx = None
        self.amountOfPlantxScanned = 1
        self.plant1Type = None
        self.plantMatchPosition = None
        self.isFinished = False
        self.imageURL = None
    
    def toJSON(self):
        return {
            "id": 1,
            "dateTimeStamp": self.dateStampID,
            "startTimeStamp": self.startTimeStamp,
            "endTimeStamp": self.endTimeStamp,
            "distance": self.distanceDriven,
            "state": self.state,
            "plantType": self.plant1Type,
            "plantMatchPosition": self.plantMatchPosition,
            "isFinished": self.isFinished,
            "imageURL": self.imageURL
        }

# HerbE states
HerbEstates =  {
  "initial": "HerbiE ist parkiert und am ruhen",
  "driving": "HerbE ist am fahren. Der Ultraschallsensor sucht nach Objekten und die Kamera nach QR-Codes.",
  "ultraDetected": "Herbie hat mit dem Ultraschallsensor ein Objekt erkannt",
  "qrDetected":  "HerbiE schiesst ein Foto und sucht nach der Pflanzenart.",
  "finished": "HerbE ist gestoppt :(",
  "goal": "Ziel erreicht!!!"
}