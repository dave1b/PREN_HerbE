# import modules
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import sys
from threading import Timer
import time
import requests

# Add paths
sys.path.insert(0, '/home/pi/Desktop/PREN/Main_Model')
sys.path.insert(0, '/home/pi/Desktop/PREN/Ultrasonic_Waterproof')
sys.path.insert(0, '/home/pi/Desktop/PREN/QR_Detection')
sys.path.insert(0, '/home/pi/Desktop/PREN/Plant_Detection')
sys.path.insert(0, '/home/pi/Desktop/PREN/Tinyk22_Communication')

sys.path.insert(0, '../Ultrasonic_Waterproof')
sys.path.insert(0, '../QR_Detection')
sys.path.insert(0, '../Plant_Detection')
sys.path.insert(0, '../Tinyk22_Communication')

# import custom modules
from DataModel import DataModel, HerbEstates
from Ultrasonic import Ultrasonic
from VideoQRCodeScanner import VideoQRCodeScanner
from PlantApiService import PlantApiService
from Tinyk22Interface import Tinyk22Interface
# from Tinyk22InterfaceFake import Tinyk22Interface
from apiKeys import plantIDkey, restAPIKey
from Log import Logger


class HerbE:
    def __init__(self):
        self.dataModel = DataModel()
        self.plantIDKey = plantIDkey
        self.firstPlantScanned = False
        self.ultrasonic = Ultrasonic(self.ultrasonicObjectDetected, 1000)
        self.videoQRCodeScanner = VideoQRCodeScanner(self.qrCodeDetected, self.dataModel)
        self.plantApiService = PlantApiService(self.plantIDKey, self.dataModel, 0.025)
        self.tinyk22Interface = Tinyk22Interface(self.newDistanceCallback)
        self.RESTapiURL = "https://prenh21-dbrunner.enterpriselab.ch/api/v1/updateRun"
        self.stopQRCodeContent = "Ziel"
        self.log = Logger()
        self.log.debug("HerbE - HerbE instantiated")

    def initialStartOfHerbE(self):
        self.dataModel.resetModel()
        self.tinyk22Interface.resetComponents()
        self.log.debug("HerbE - initialStartOfHerbE()")
        self.dataModel.state = HerbEstates["initial"]
        executor = ThreadPoolExecutor(max_workers=3)
        executor.submit(self.ultrasonic.startSearching)
        executor.submit(self.videoQRCodeScanner.startCapturingFrames)
        executor.submit(self.startEngine)
        self.dataModel.dateTimeStamp = datetime.fromtimestamp(time.time()).strftime("%H:%M:%S, %d/%m/%Y")
        self.dataModel.startTimeStamp = (time.time() * 1000)  # *1000 cause of JS in Client
        self.postDataToRestAPI()

    def stopEngine(self):
        self.tinyk22Interface.turnEngineOff()
        self.dataModel.isDriving = False
        self.log.debug("HerbE - stopEngine()")
        self.dataModel.state = HerbEstates["stop"]

    def startEngine(self):
        self.log.debug("HerbE - startEngine()")
        self.dataModel.isDriving = True
        self.tinyk22Interface.turnEngineOn()
        self.dataModel.state = HerbEstates["driving"]

    def detectPlantInImage(self):
        self.log.debug("HerbE - detectPlantInImage()")
        self.plantApiService.detectPlant(self.firstPlantScanned)
        if not (self.firstPlantScanned):
            self.firstPlantScanned = True
        else:
            self.dataModel.amountOfPlantxScanned += 1
            self.findMatchingPlant()
        self.postDataToRestAPI()
        self.startEngine()

    def newDistanceCallback(self, newDistanceDriven):
        self.log.debug("HerbE - distanceCallback()")
        self.dataModel.distanceDriven = int(newDistanceDriven)
        self.postDataToRestAPI()

    def ultrasonicObjectDetected(self):
        self.dataModel.state = HerbEstates["ultraDetected"]
        self.log.debug("HerbE - ultrasonicObjectDetected()")
        self.stopEngine()
        self.postDataToRestAPI()
        Timer(1.5, self.startEngine).start()

    def qrCodeDetected(self):
        self.log.debug("HerbE - qrCodeDetected()")
        self.dataModel.state = HerbEstates["qrDetected"]
        # check if finish has been reached
        if(self.dataModel.QRcodeContent == self.stopQRCodeContent):
            # if reached finish line -> shutdown in 5 seconds
            self.log.debug("HerbE - finish has ben reached")
            Timer(5, self.shutdownHerbE).start()
            return
        self.videoQRCodeScanner.takePhoto()
        self.detectPlantInImage()

    def findMatchingPlant(self):
        self.log.debug("HerbE - findMatchingPlant()")
        didFindMatch = False
        didFindMatch = self.plantApiService.findMatchingPlantInDataModel()
        if (didFindMatch):
            self.postDataToRestAPI()

    def postDataToRestAPI(self):
        #self.log.debug("HerbE - postDataToRestAPI()")
        response = (requests.put(self.RESTapiURL, json=self.dataModel.toJSON(restAPIKey))).status_code

    def shutdownHerbE(self, stopButtonPressed = False):
        self.log.debug("HerbE - shutdownHerbE()")
        self.tinyk22Interface.shutdownEngine()
        self.videoQRCodeScanner.stop()
        self.ultrasonic.stopSearching()
        if(stopButtonPressed):
            self.dataModel.state = HerbEstates["stopButtonPressed"]
        else:
            self.dataModel.state = HerbEstates["goal"]
        self.dataModel.endTimeStamp = int(time.time() * 1000)  # *1000 cause of JS in Client
        self.dataModel.isFinished = True
        self.postDataToRestAPI()