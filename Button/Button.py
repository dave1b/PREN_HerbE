import sys
sys.path.insert(0, '/home/pi/Desktop/PREN/Main_Model')
sys.path.insert(0, '../Main_Model')
from HerbE import HerbE
from Log import Logger
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from concurrent.futures import ThreadPoolExecutor

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 16 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 18 to be an input pin and set initial value to be pulled low (off)


class Button():
    def __init__(self):
        self.herbE = HerbE()
        self.log = Logger()
        self.startPressedBefore = False
        self.stopPressedBefore = False
        executor = ThreadPoolExecutor(max_workers=1)
        executor.submit(self.startButtonListener)

    def startButtonListener(self):
        while True: 
            if GPIO.input(16) == GPIO.HIGH and not self.startPressedBefore:
                self.startPressedBefore = True
                self.stopPressedBefore = False
                self.log.info("Button - Starte Herb-E")
                self.herbE.initialStartOfHerbE()
            elif GPIO.input(18) == GPIO.HIGH and not self.stopPressedBefore and self.startPressedBefore:
                self.stopPressedBefore = True
                self.startPressedBefore = False
                print("Stop-Button was pressed!")
                self.herbE.shutdownHerbE(True)
                
button = Button()
button.startButtonListener()