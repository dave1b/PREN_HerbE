import numpy as np
from queue import Queue
import cv2
import pyzbar.pyzbar as pyzbar
import re
import asyncio
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

 

class VideoStreamScanner:
    def __init__(self, contrast, exposure):
        self.MAX_QUEUE_SIZE = 128
        self.detector = cv2.QRCodeDetector()
        self.cap = cv2.VideoCapture(0)
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
            print("capture frame at " + str(datetime.now()))
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
        decodedObjects = ""
    
    def stop(self):
        self.stopped = True

def main():
    vsc = VideoStreamScanner(contrast = 20,exposure = 40)
    print("program started")
    vsc.startCapturingFrames()



if __name__ == "__main__":
	main()
