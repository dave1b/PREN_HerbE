# import modules
from concurrent.futures import ThreadPoolExecutor
from configparser import ConfigParser
from datetime import datetime
import sys
from threading import Timer
import time
import requests

# Add paths
sys.path.insert(0, '../Ultrasonic_Waterproof')
sys.path.insert(0, '../QR_Detection')
sys.path.insert(0, '../Plant_Detection')
sys.path.insert(0, '../Tinyk22_Communication')

# import custom modules
from DataModel import DataModel, HerbEstates
from Log import Logger
from Ultrasonic import Ultrasonic
from VideoQRCodeScanner import VideoQRCodeScanner
from PlantApiService import PlantApiService
from Tinyk22Interface import Tinyk22Interface
# from Tinyk22InterfaceFake import Tinyk22Interface


class HerbE:
    def __init__(self):
        #reading variables from config
        self.config_object = ConfigParser()
        self.config_object.read("config.ini")
        self.herbEConfig = self.config_object["HERBECONFIG"]
        self.plantIDKey = self.herbEConfig["plantIDkey"]
        self.restAPIKey = self.herbEConfig["restAPIKey"]
        self.RESTapiURL = self.herbEConfig["restAPIURL"]
        self.stopQRCodeContent = self.herbEConfig["qrContentOfFinish"]
        self.startEngineAfterUltraDetectedThreshold = int(self.herbEConfig["afterUltraDetectedRestartHerbETimeInSeconds"])
        self.firstPlantScanned = False
        # instantiate components
        self.dataModel = DataModel()
        self.ultrasonic = Ultrasonic(
            self.ultrasonicObjectDetected, int(self.herbEConfig["ultrasonicDistanceThresholdInMM"]))
        self.videoQRCodeScanner = VideoQRCodeScanner(
            self.qrCodeDetected, self.dataModel)
        self.plantApiService = PlantApiService(
            self.plantIDKey, self.dataModel, float(self.herbEConfig["plantMinProbability"]))
        self.tinyk22Interface = Tinyk22Interface(self.newDistanceCallback)
        self.log = Logger("HerbE")
        self.log.debug("HerbE instantiated")

    def initialStartOfHerbE(self):
        self.dataModel.resetModel()
        self.tinyk22Interface.resetComponents()
        self.log.debug("initialStartOfHerbE()")
        self.dataModel.state = HerbEstates["initial"]
        executor = ThreadPoolExecutor(max_workers=3)
        executor.submit(self.ultrasonic.startSearching)
        executor.submit(self.videoQRCodeScanner.startCapturingFrames)
        executor.submit(self.startEngine)
        self.dataModel.dateTimeStamp = datetime.fromtimestamp(
            time.time()).strftime("%H:%M:%S, %d/%m/%Y")
        self.dataModel.startTimeStamp = (
            time.time() * 1000)  # *1000 cause of JS in Client
        self.postDataToRestAPI()

    def stopEngine(self):
        self.tinyk22Interface.turnEngineOff()
        self.dataModel.isDriving = False
        self.log.debug("stopEngine()")
        self.dataModel.state = HerbEstates["stop"]

    def startEngine(self):
        self.log.debug("startEngine()")
        self.dataModel.isDriving = True
        self.tinyk22Interface.turnEngineOn()
        self.dataModel.state = HerbEstates["driving"]

    def detectPlantInImage(self):
        self.log.debug("detectPlantInImage()")
        self.plantApiService.detectPlant(self.firstPlantScanned)
        if not (self.firstPlantScanned):
            self.firstPlantScanned = True
        else:
            self.dataModel.amountOfPlantxScanned += 1
            self.findMatchingPlant()
        self.postDataToRestAPI()
        self.startEngine()

    def newDistanceCallback(self, newDistanceDriven):
        self.log.debug("distanceCallback()")
        self.dataModel.distanceDriven = int(newDistanceDriven)
        self.postDataToRestAPI()

    def ultrasonicObjectDetected(self):
        self.dataModel.state = HerbEstates["ultraDetected"]
        self.log.debug("ultrasonicObjectDetected()")
        self.stopEngine()
        self.postDataToRestAPI()
        Timer(self.startEngineAfterUltraDetectedThreshold, self.startEngine).start()

    def qrCodeDetected(self):
        self.log.debug("qrCodeDetected()")
        self.dataModel.state = HerbEstates["qrDetected"]
        # check if finish has been reached
        if(self.dataModel.QRcodeContent == self.stopQRCodeContent):
            # if reached finish line -> shutdown in 5 seconds
            self.log.debug("finish has ben reached")
            Timer(int(self.herbEConfig["shutdownAfterFinishQRcodeTimeInSeconds"]), self.shutdownHerbE).start()
            return
        self.videoQRCodeScanner.takePhoto()
        self.detectPlantInImage()

    def findMatchingPlant(self):
        self.log.debug("findMatchingPlant()")
        didFindMatch = False
        didFindMatch = self.plantApiService.findMatchingPlantInDataModel()
        if (didFindMatch):
            self.postDataToRestAPI()

    def postDataToRestAPI(self):
        requests.put(self.RESTapiURL,
                    json=self.dataModel.toJSON(self.restAPIKey))

    def shutdownHerbE(self, stopButtonPressed=False):
        self.log.debug("shutdownHerbE()")
        self.tinyk22Interface.shutdownEngine()
        self.videoQRCodeScanner.stop()
        self.ultrasonic.stopSearching()
        if(stopButtonPressed):
            self.dataModel.state = HerbEstates["stopButtonPressed"]
        else:
            self.dataModel.state = HerbEstates["goal"]
        self.dataModel.endTimeStamp = int(
            time.time() * 1000)  # *1000 cause of JS in Client
        self.dataModel.isFinished = True
        self.postDataToRestAPI()