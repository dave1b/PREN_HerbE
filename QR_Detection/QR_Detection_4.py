from gpiozero import LED, Button, Buzzer
import cv2
import re
import asyncio
import pyzbar.pyzbar as pyzbar
import numpy as np
import time

#Script for decoding QR with pyzbar

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
#Intiger indicating amount of QR-Codes scannt
global i 
i = 0
detector = cv2.QRCodeDetector()



async def decode(frame): 
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(frame)
    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data,'\n')     
    decodedObjects


def main():
    print("program started")
    #Get camerainput and QR-Decoder
    cap = cv2.VideoCapture(0)
    
    # Kameraeinstellungen setzten
    cap.set(cv2.CAP_PROP_CONTRAST,contrast)
    cap.set(cv2.CAP_PROP_EXPOSURE, exposure)
    cap.set(cv2.CAP_PROP_FPS, fps)
    cap.set(3,1280)
    cap.set(4,1024)

    
    while (True):
#         print("camera open")
        _, frame = cap.read()
        cv2.imshow("code detector", frame)
        #Our operations on the frame come here
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        asyncio.run(decodedObjects = decode(frame))
        
        if cv2.waitKey(16) == ord("q"):
            cap.read()
            cv2.destroyAllWindows()
            print("kamera destoryed")
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
	main()
