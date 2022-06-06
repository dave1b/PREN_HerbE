from concurrent.futures import ThreadPoolExecutor
import time
import sys
from datetime import datetime
sys.path.insert(0, '../Main_Model')
sys.path.insert(0, '/home/pi/Desktop/PREN/Main_Model')
from Log import Logger
from DFRobotRaspberryPiA02YYUW import DFRobotA02Distance as UltrasonicSensor

class Ultrasonic:
    def __init__(self, objectDetectedCallback, distanceThreshold = 1000):
        self.callbackObjectDetected = objectDetectedCallback
        self.ultrasonicSensor = UltrasonicSensor()
        self.ultrasonicSensor.set_dis_range(0, 4500)
        self.distanceThreshold = distanceThreshold
        self.searchingRunning = False
        self.log = Logger("Ultrasonic")
        self.log.debug("initialisiert")
        self.executor = ThreadPoolExecutor(max_workers=3)
    
    def startSearching(self):
        self.lastUltrasonicAlertTimestamp = time.time()
        self.minWaitingtimeBetweenAlerts = 12
        self.searchingRunning = True
        self.log.debug("startSearching()")
        while self.searchingRunning:
            distance = self.ultrasonicSensor.getDistance()
            if distance < self.distanceThreshold and distance != 0:
                # distance lower than Threshold -> check if in time
                if(((time.time()) - self.lastUltrasonicAlertTimestamp) > self.minWaitingtimeBetweenAlerts):
                    self.lastUltrasonicAlertTimestamp = time.time()
                    # if in time -> reset time and start Callback
                    self.log.debug("under threashold, meassured Distance: " + str(distance))
                    self.executor.submit(self.callbackObjectDetected)
    
    def stopSearching(self):
        self.log.debug("stopSearching")
        self.searchingRunning = False