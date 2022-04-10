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
        self.ultrasonicSensor.set_dis_range(0, 4500)
        self.distanceThreshold = distanceThreshold
        self.searchingRunning = False
        self.log = Logger()
        self.log.debug("Ultrasonic - initialisiert")
    
    def startSearching(self):
        self.searchingRunning = True
        self.log.debug("Ultrasonic - startSearching()")
        while self.searchingRunning:
            distance = self.ultrasonicSensor.getDistance()
            if distance <= self.distanceThreshold:
                self.log.debug("Ultrasonic - under threashold, meassured Distance:1 " + str(distance))
                self.callbackObjectDetected()
                self.dataModel.UltrasonicObjectDetected = True
    
    def stopSearching(self):
        self.log.debug("Ultrasonic - stopSearching")
        self.searchingRunning = False
