import sys
import time
import cv2
import pyzbar.pyzbar as pyzbar
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, '/home/pi/Desktop/PREN/Main_Model')
sys.path.insert(0, '../Main_Model')
from Log import Logger

class VideoQRCodeScanner:
    def __init__(self, qrDetectedCallback, dataModel, contrast = 20,exposure = 40):
        self.dataModel = dataModel
        self.detector = cv2.QRCodeDetector()
        self.qrDetectedCallback = qrDetectedCallback
        self.cap = cv2.VideoCapture(0)
        self.log = Logger()
        
        # Kameraeinstellungen setzten
        self.cap.set(cv2.CAP_PROP_CONTRAST,contrast)
        self.cap.set(cv2.CAP_PROP_EXPOSURE, exposure)
        self.cap.set(3,640)
        self.cap.set(4,480)
        
        self.isRunning = False
        self.lastQRContent = ""
        self.executorForCallback = ThreadPoolExecutor(max_workers=3) 
        self.executorForScanningFiles = ThreadPoolExecutor(max_workers=5)

    def startCapturingFrames(self):   
        self.isRunning = True
        while (self.isRunning):
            _, frame = self.cap.read()
            self.executorForScanningFiles.submit(self.searchFrameForQR, frame)

    #function for searching QR-Code in Frame
    def searchFrameForQR(self, frame):
        decodedObjects = pyzbar.decode(frame)
        # log frame here
        self.log.info('QR -  : searchFramForQR()')
        for obj in decodedObjects:
            # if QR-Code data is different last
            self.log.info('11111111 QR - Type : ', self.lastQRContent)
            self.log.info('QR - Type : ', self.lastQRContent)
            if(self.lastQRContent != obj.data):
                self.lastQRContent = obj.data
                #self.executorForCallback.submit(self.qrDetectedCallback)
                self.log.info('QR - Type : ', obj.type)
                self.log.info('QR - Data : ', obj.data,'\n')  
                self.log.info("QR - QR detected: " + str(obj.data))
                self.dataModel.QRcodeContent = obj.data
        decodedObjects = ""
    
    def stop(self):
        self.isRunning = False

    def takePhoto(self):
        self.log.debug("QR - takePhoto()")
        _, frame = self.cap.read()
        cv2.imwrite('plantImage.png',frame)
        self.log.debug("QR - takePhoto()")
        self.dataModel.plantImage = frame