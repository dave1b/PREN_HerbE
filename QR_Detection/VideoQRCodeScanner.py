import sys
import cv2
import pyzbar.pyzbar as pyzbar
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
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
        
    def startCapturingFrames(self):   
        self.isRunning = True
        executor = ThreadPoolExecutor(max_workers=5)    
        while (self.isRunning):
            #print("capture frame at " + str(datetime.now()))
            _, frame = self.cap.read()
            #cv2.imshow(frame)
            executor.submit(self.searchFrameForQR(frame))

    #function for searching QR-Code in Frame
    def searchFrameForQR(self, frame):
        decodedObjects = pyzbar.decode(frame)
        # Print results
        for obj in decodedObjects:
            print('Type : ', obj.type)
            print('Data : ', obj.data,'\n')  
            self.log.debug("QR - QR detected: " + str(obj.data))
            self.dataModel.QRcodeContent = obj.data
            self.qrDetectedCallback()
            #cv2.imwrite('test_frame_.png', frame)
        decodedObjects = ""
    
    def stop(self):
        self.isRunning = False

    def takePhoto(self):
        self.log.debug("QR - takePhoto()")
        _, frame = self.cap.read()
        cv2.imwrite('plantImage.png',frame)
        self.log.debug("QR - takePhoto()")
        self.dataModel.plantImage = frame


def main():
    vsc = VideoQRCodeScanner(contrast = 20,exposure = 40)
    print("program started")
    vsc.startCapturingFrames()

if __name__ == "__main__":
	pass
    #main()