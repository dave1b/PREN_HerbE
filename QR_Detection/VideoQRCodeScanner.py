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
        #self.cap.set(cv2.CAP_PROP_FPS, fps)
        self.cap.set(3,640)
        self.cap.set(4,480)
        self.isRunning = False
        self.executorForCallback = ThreadPoolExecutor(max_workers=3) 
        self.executorForScanningFiles = ThreadPoolExecutor(max_workers=5)
        self.lastQRAlertTimestamp = 0
        self.minWaitingtimeBetweenAlerts = 12

   

        
    def startCapturingFrames(self):   
        self.isRunning = True
        while (self.isRunning):
            _, frame = self.cap.read()
            #cv2.imshow(frame)
            self.executorForScanningFiles.submit(self.searchFrameForQR(frame))

    #function for searching QR-Code in Frame
    def searchFrameForQR(self, frame):
        decodedObjects = pyzbar.decode(frame)
        # Log results
        for obj in decodedObjects:
            if(((time.time()) - self.lastQRAlertTimestamp) > self.minWaitingtimeBetweenAlerts):
                self.lastQRAlertTimestamp = time.time()
                self.executorForCallback.submit(self.qrDetectedCallback)
                #cv2.imwrite('test_frame_.png', frame)
                self.log.info('QR - Type : ', obj.type)
                self.log.info('QR - Data : ', obj.data,'\n')  
                self.log.debug("QR - QR detected: " + str(obj.data))
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