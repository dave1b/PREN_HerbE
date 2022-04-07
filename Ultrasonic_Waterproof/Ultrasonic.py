import time
import sys
sys.path.insert(0, '../Main_Model')
from Log import Logger
from DFRobotRaspberryPiA02YYUW import DFRobotA02Distance as UltrasonicSensor

class Ultrasonic:
    def __init__(self, objectDetectedCallback, dataModel, distanceThreshold = 1000):
        self.callbackObjectDetected = objectDetectedCallback
        self.dataModel = dataModel
        self.ultrasonicSensor = UltrasonicSensor()
        self.ultrasonicSensor.set_dis_range(min=0, max=3000)
        self.distanceThreshold = distanceThreshold
        self.searchingRunning = False
        self.log = Logger()
        self.log.debug("Ultrasonic - initialisiert")
    
    def startSearching(self):
        self.startSearching = True
        self.log.debug("Ultrasonic - startSearching()")
        while self.searchingRunning:
            distance = self.ultrasonicSensor.getDistance()
            if distance <= self.distanceThreshold:
                self.objectDetectedCallback()
                self.dataModel.UltrasonicObjectDetected = True
            self.log.debug("Ultrasonic - meassured Distance: " + str(distance))
            time.sleep(0.3)    
    
    def stopSearching(self):
        self.log.debug("Ultrasonic - stopSearching")
        self.searchingRunning = False