from gpiozero import LED, Button, Buzzer
import cv2
import re
import asyncio


led = LED(19)
sw1 = Button(21)
buzzer = Buzzer(26)

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


async def searchInFrameForQR(frame):
    data, bbox, _ = detector.detectAndDecode(frame)
    if len(data)>1:
    #if bbox is not None:
        #buzzer.beep(0.1, 0.1, 1)
        print(str(i) + " Data found: " + data)             
        data = ""      
        #for i in range(len(bbox)):
        #cv2.line(frame, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
        #cv2.putText(frame, data, (int(bbox[0][0][0]), int(bbox[0][0][1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)                    
        #cv2.imshow("code detector", frame)

detector = cv2.QRCodeDetector()

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
        
        asyncio.run(searchInFrameForQR(frame))
        if cv2.waitKey(16) == ord("q"):
            cap.read()
            cv2.destroyAllWindows()
            print("camera destoryed")
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
	main()
