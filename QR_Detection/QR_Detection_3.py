from gpiozero import LED, Button, Buzzer
import cv2
import re

led = LED(19)
sw1 = Button(21)
buzzer = Buzzer(26)
contrast=20
exposure=-8
focus=0
fps=90
height=480
width=720
#Example -130 (dark) +130(bright)
brightness=0

vid = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()


# Kameraeinstellungen setzten
vid.set(cv2.CAP_PROP_CONTRAST,contrast)
vid.set(cv2.CAP_PROP_EXPOSURE, exposure)
vid.set(cv2.CAP_PROP_FPS, fps)
vid.set(3,1280)
vid.set(4,1024)
# vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

def sw1Pressed():
    global sw1Press
    sw1Press = True

print("Reading QR code using Raspberry Pi camera")
print("Press SW1 to scan.")

while True:

   
    cv2.imshow("code detector", img)
    
    
    if cv2.waitKey(1) == ord("q"):
        break



# led.off()
vid.release()
cv2.destroyAllWindows()
