from mimetypes import init
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

class Button():
    def __init__(self, CallbackFunctionFirstTimePressed, CallbackFunctionXTimesPressd):
        self.CallbackFunctionFirstTimePressed = CallbackFunctionFirstTimePressed
        self.CallbackFunctionXTimesPressd = CallbackFunctionXTimesPressd
        self.pressedBefore = False

    def startButtonListener(self):
         while True: 
            if GPIO.input(12) == GPIO.HIGH:
                print("Button was pushed!")
                if not(self.pressedBefore):
                    self.CallbackFunctionFirstTimePressed()
                    self.pressedBefore = True
                else:
                    self.CallbackFunctionXTimesPressd()            