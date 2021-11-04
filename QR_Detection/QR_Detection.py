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
    if (True):
    
#         led.toggle()
        
        _, img = vid.read()
        data, bbox, _ = detector.detectAndDecode(img)
        
        if bbox is not None:
            for i in range(len(bbox)):
                cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255,
                         0, 0), thickness=2)
                
#             cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1])), cv2.FONT_HERSHEY_SIMPLEX,
#                         0.5, (0, 255, 0), 2)
            
            if data:
#                 buzzer.beep(0.1, 0.1, 1)
                print("Data found: " + data)             
                data = ""
#         cv2.imshow("code detector", img)
    
    else:
        vid.read()
        cv2.destroyAllWindows()
    
    if cv2.waitKey(1) == ord("q"):
        break

# led.off()
vid.release()
cv2.destroyAllWindows()