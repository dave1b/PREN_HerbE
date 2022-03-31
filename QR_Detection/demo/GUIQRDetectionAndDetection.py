from gpiozero import LED, Button, Buzzer
import cv2
import pyzbar.pyzbar as pyzbar
import asyncio
from datetime import datetime



# Globale Variablen
contrast=20
exposure=40
focus=0
fps=90
height=480
width=720
brightness=0
detector = cv2.QRCodeDetector()


async def searchInFrameForQR(frame):
    decodedObjects = pyzbar.decode(frame)
        # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data,'\n')  
        decodedObjects = ""     



def main():
    print("program started")
    #Get camerainput and QR-Decoder
    cap = cv2.VideoCapture(0)
    
    # Kameraeinstellungen setzten
    cap.set(cv2.CAP_PROP_CONTRAST,contrast)
    cap.set(cv2.CAP_PROP_EXPOSURE, exposure)
    #cap.set(cv2.CAP_PROP_FPS, fps)
    cap.set(3,640)
    cap.set(4,480)
    
    while (True):
#         print("camera open")
        _, frame = cap.read()
        print("capture frame at " + str(datetime.now()))
        cv2.imshow("code detector", frame)
        asyncio.run(searchInFrameForQR(frame))
        if cv2.waitKey(1) == ord("q"):
            cap.read()
            cv2.destroyAllWindows()
            print("camera destoryed")
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
	main()
