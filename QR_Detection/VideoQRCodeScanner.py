import sys
import cv2
import pyzbar.pyzbar as pyzbar
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, 'Main_Model')
from Log import Logger

class VideoQRCodeScanner:
    def __init__(self, qrDetectedCallback, dataModel, contrast = 20, exposure = 40):
        self.dataModel = dataModel
        self.qrDetectedCallback = qrDetectedCallback
        self.cap = cv2.VideoCapture(0)
        self.log = Logger("VideoQRCodeScanner")
        
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
        self.log.debug("startCapturingFrames()")
        self.isRunning = True
        while (self.isRunning):
            _, frame = self.cap.read()
            self.executorForScanningFiles.submit(self.searchFrameForQR, frame)

    #function for searching QR-Code in Frame
    def searchFrameForQR(self, frame):
        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            # if QR-Code data is different last
            if(self.dataModel.QRcodeContent != obj.data):
                self.dataModel.QRcodeContent = obj.data
                self.executorForCallback.submit(self.qrDetectedCallback)
                self.log.debug('QR-Type : ' + obj.type)
                self.log.debug('QR-Data : ' + str(obj.data))  
        decodedObjects = ""
    
    def stop(self):
        self.isRunning = False

    def takePhoto(self):
        self.log.debug("takePhoto()")
        _, frame = self.cap.read()
        cv2.imwrite('plantImage.png',frame)
        self.dataModel.plantImage = frame