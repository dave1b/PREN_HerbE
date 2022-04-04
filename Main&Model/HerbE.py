# import modules
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import sys
import threading
import time
import requests

# Add paths
sys.path.insert(0, '../Ultrasonic_Waterproof')
sys.path.insert(0, '../QR_Detection')
sys.path.insert(0, '../Plant_Detection')
sys.path.insert(0, '../Tinyk22_Communication')
sys.path.insert(0, '../Button')

# import custom modules
from DataModel import DataModel, HerbEstates
from Ultrasonic import Ultrasonic
from VideoQRCodeScanner import VideoQRCodeScanner
from PlantApiService import PlantApiService
#from Tinyk22Interface import Tinyk22Interface
from Tinyk22InterfaceFake import Tinyk22Interface
from apiKeys import plantIDkey, restAPIKeyrestAPIKey
from Button import Button
from Log import Logger

class HerbE:
    def __init__(self):
        self.dataModel = DataModel()
        self.plantIDKey = plantIDkey
        self.firstPlantScanned = False
        self.ultrasonic = Ultrasonic(self.ultrasonicObjectDetected, self.dataModel)
        self.videoQRCodeScanner = VideoQRCodeScanner(self.qrCodeDetected, self.dataModel)
        self.plantApiService = PlantApiService(self.plantIDKey, self.dataModel, 0.025)
        self.tinyk22Interface = Tinyk22Interface(self.newDistanceCallback)
        self.button = Button(self.initialStartOfHerbE,self.shutdownHerbE)
        self.lastUltrasonicAlertTimestamp = time.time()
        self.lastQRcodeDetectedAlertTimestap = time.time()
        self.minWaitingtimeBetweenAlerts = 5
        self.RESTapiURL = "https://prenh21-dbrunner.enterpriselab.ch/api/v1/updateRun"
        self.log = Logger()
        self.log.debug("HerbE - HerbE initialisiert")

    def initialStartOfHerbE(self):
        self.log.debug("HerbE - initialStartOfHerbE()")
        executor = ThreadPoolExecutor(max_workers=3)   
        executor.submit(self.ultrasonic.startSearching)
        executor.submit(self.videoQRCodeScanner.startCapturingFrames)
        executor.submit(self.startEngine)
        self.dataModel.state = HerbEstates["initial"]
        self.dataModel.dateTimeStamp = datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y, %H:%M:%S")
        self.dataModel.startTimeStamp = (time.time() * 1000) # *1000 cause of JS in Client
        self.postDataToRestAPI()
        

    def stopEngine(self):
        self.log.debug("HerbE - stopEngine()")
        self.dataModel.isDriving = False
        self.tinyk22Interface.turnEngineOff()

    def startEngine(self):
        self.log.debug("HerbE - startEngine()")
        self.dataModel.isDriving = True
        self.tinyk22Interface.turnEngineOn()

    def detectPlantInImage(self):
        self.log.debug("HerbE - detectPlantInImage()")
        self.plantApiService.detectPlant(self.firstPlantScanned)
        if not(self.firstPlantScanned):
            self.firstPlantScanned = True
        else:
            self.dataModel.amountOfPlantxScanned += 1
            self.findMatchingPlant()
        self.postDataToRestAPI()

    def newDistanceCallback(self, newDistanceDriven):
        self.log.debug("HerbE - newDistanceCallback()")
        self.dataModel.distanceDriven = newDistanceDriven
        self.postDataToRestAPI()

    def ultrasonicObjectDetected(self):
        self.log.debug("HerbE - ultrasonicObjectDetected()")
        if(self.isWaitingTimeOver(self.lastUltrasonicAlertTimestamp, self.minWaitingtimeBetweenAlerts)):
            self.stopEngine()
            self.dataModel.state = HerbEstates["ultraDetected"]
            self.postDataToRestAPI()
            threading.Timer(5, self.startEngine)
            

    def qrCodeDetected(self):
        self.log.debug("HerbE - qrCodeDetected()")       
        if(self.isWaitingTimeOver(self.lastQRcodeDetectedAlertTimestap, self.minWaitingtimeBetweenAlerts)):
            self.lastQRcodeDetectedAlertTimestap = time.time()
            self.dataModel.state = HerbEstates["qrDetected"]
            self.videoQRCodeScanner.takePhoto()
            self.detectPlantInImage()
            self.log.debug("HerbE - qrCodeDetected ende()")


    def findMatchingPlant(self):
        self.log.debug("HerbE - findMatchingPlant()")
        didFindMatch = False
        didFindMatch = self.plantApiService.findMatchingPlantInDataModel()
        if(didFindMatch):
            self.postDataToRestAPI()

    def isWaitingTimeOver(self, lastAlertTimestamp, waitingThreshold):
        self.log.debug("HerbE - isWaitingTimeOver()")
        return (((time.time()) - lastAlertTimestamp) > waitingThreshold)

    def postDataToRestAPI(self):
        self.log.debug("HerbE - postDataToRestAPI()")
        response = (requests.put(self.RESTapiURL, json= self.dataModel.toJSON(restAPIKey))).status_code
        #self.log.debug("HerbE - " + str(response))
    
    def shutdownHerbE(self):
        self.log.debug("HerbE - shutdownHerbE()")
        self.stopEngine()
        self.videoQRCodeScanner.stop()
        self.ultrasonic.stopSearching()
        self.dataModel.state = HerbEstates["finished"]
        self.dataModel.endTimeStamp = int(time.time() * 1000) # *1000 cause of JS in Client


