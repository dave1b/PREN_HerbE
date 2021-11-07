from gpiozero import LED, Button, Buzzer
import numpy as np
from queue import Queue
import cv2
import re
import asyncio




#Camera Settings:
contrast=20
exposure=-8
focus=0
fps=90
height=480
width=720
brightness=0


# cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


def getAndIncrementQRcounter(i):
    i += 1
    return i

#function for capturing Frame
async def captureFrame(i, queue):
    #checking if queue is not full
    if not queue.full():
        _, frame = cap.read()
        asyncio.run(searchFrameForQR(frame,i,queue))


#function for searching QR-Code in Frame
async def searchFrameForQR(frame,i, queue):
    if queue.qsize() > 0:
        data, bbox, _ = detector.detectAndDecode(frame)
        if len(data)>1:
        #if bbox is not None:
            #buzzer.beep(0.1, 0.1, 1)
            print(str(getAndIncrementQRcounter()) + " Data found: " + data)             
            data = ""     
            #for i in range(len(bbox)):
            #cv2.line(frame, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
            #cv2.putText(frame, data, (int(bbox[0][0][0]), int(bbox[0][0][1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)                    
            #cv2.imshow("code detector", frame)
    

class VideoStreamScanner:
    def __init__(self):
        self.detector = cv2.QRCodeDetector()
        self.cap = cv2.VideoCapture(0)
        # Kameraeinstellungen setzten
        self.cap.set(cv2.CAP_PROP_CONTRAST,contrast)
        self.cap.set(cv2.CAP_PROP_EXPOSURE, exposure)
        self.cap.set(cv2.CAP_PROP_FPS, fps)
        self.cap.set(3,1280)
        sel.fcap.set(4,1024)


def main():
    MAX_QUEUE_SIZE = 128

    print("program started")
    #Get camerainput and QR-Decoder
    global i
    i = 0
    queue = Queue(maxsize=MAX_QUEUE_SIZE)
    

    
    
    while (True):
        captureFrame(i, queue)
#       print("camera open")
        
        #cv2.imshow("code detector", frame)
        if ord("q"):
            cap.read()
            cv2.destroyAllWindows()
            print("camera destoryed")
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
	main()
