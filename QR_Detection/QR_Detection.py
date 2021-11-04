from gpiozero import LED, Button, Buzzer
import cv2
import re

led = LED(19)
sw1 = Button(21)
buzzer = Buzzer(26)

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
cap.

def sw1Pressed():
    global sw1Press
    sw1Press = True

sw1.when_pressed = sw1Pressed
sw1Press = False

print("Reading QR code using Raspberry Pi camera")
print("Press SW1 to scan.")

while True:
    if sw1Press == True:
        led.toggle()
        
        _, img = cap.read()
        data, bbox, _ = detector.detectAndDecode(img)
        
        if bbox is not None:
            for i in range(len(bbox)):
                cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255,
                         0, 0), thickness=2)
                
            cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) – 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 2)
            
            if data:
                sw1Press = False
                buzzer.beep(0.1, 0.1, 1)
                print("Data found: " + data)
                led.off()
                data = ""

        cv2.imshow("code detector", img)
    
    else:
        cap.read()
        cv2.destroyAllWindows()
    
    if cv2.waitKey(1) == ord("q"):
        break

led.off()
cap.release()
cv2.destroyAllWindows()