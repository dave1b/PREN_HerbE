class DataModel:
    def __init__(self):
        self.QRcodeContent = None
        self.UltrasonicObjectDetected = False
        self.dateTimeStamp = None
        self.startTimeStamp = None
        self.endTimeStamp = None
        self.isDriving = False
        self.state = None
        self.distanceDriven = 0
        self.plantImage = None
        self.recognisedPlantsList1 = None
        self.recognisedPlantsListx = None
        self.amountOfPlantxScanned = 1
        self.plant1Type = None
        self.plantMatchPosition = None
        self.isFinished = False
    
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
            "isFinished": self.isFinished
        }