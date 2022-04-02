import time
from DFRobotRaspberryPiA02YYUW import DFRobotA02Distance as UltrasonicSensor

class Ultrasonic:
    def __init__(self, objectDetected, dataModel, distanceThreshold = 1000):
        self.callbackObjectDetected = objectDetected
        self.dataModel = dataModel
        self.ultrasonicSensor = UltrasonicSensor()
        self.ultrasonicSensor.set_dis_range(min=0, max=3000)
        self.distanceThreshold = distanceThreshold
        self.serachingRunning = False
    
    def startSearching(self):
        self.startSearching = True
        while self.serachingRunning:
            distance = self.ultrasonicSensor.getDistance()
            if distance <= self.distanceThreshold:
                self.callbackObjectDetected()
                self.dataModel.UltrasonicObjectDetected = True
            time.sleep(0.3)    
    
    def stopSearching(self):
        self.serachingRunning = False