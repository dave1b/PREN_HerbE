class DataModel:
    def __init__(self):
        self.QRcodeDetected = False
        self.UltrasonicObjectDetected = False
        self.DinstanceTravelled = 0
        self.dateStampID = None
        self.startTimeStamp = None
        self.endTimeStamp = None
        self.state = None
        self.distance = 0
        self.plant1Type = None
        self.plantMatchPosition = None
        self.isFinished = False
