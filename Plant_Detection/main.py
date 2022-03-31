import time
from scan import Scan
from compareTwoScans import hasMatchingPlantInScan, findMatchingPlantInScan, findFirstMatchingPlantInScan
# With camera
import cv2

def scanPlantsInPictureFromFiles():
    # Demonstration of functionality
    photo1 = "./photos/minth1.jpg"
    photo2 = "./photos/minth2.jpg"

    photo1_1 = "./photos/rose1.jpg"
    photo1_2 = "./photos/rose2.jpg"

    firstScanReady = input("Erstes Pflanze gescannt?")
    ScanOfFirstPhoto = Scan(photo1_1)

    secondScanReady = input("Zweite Pflanze gescannt?")
    ScanOfSecondPhoto = Scan(photo1_2)

    for i in range(0, 3):
        print("comparing both photos...")
        time.sleep(0.5)

    print("Has found a match: ", hasMatchingPlantInScan(
        ScanOfFirstPhoto.possiblePlantsList, ScanOfSecondPhoto.possiblePlantsList))
    print("Found match: ", findFirstMatchingPlantInScan(
        ScanOfFirstPhoto.possiblePlantsList, ScanOfSecondPhoto.possiblePlantsList))
    #print(findMatchingPlantInScan(scanOnTheRoad.possiblePlantsList, scanAtEnd1.possiblePlantsList))

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
    def takeOneImage(self):
        _, frame = self.cap.read()
        return frame

def scanOnePlant():
    vsc = VideoStreamScanner(contrast = 20,exposure = 40)
    input("Bereit Photo zu schiessen?")
    scan = Scan(vsc.takeOneImage())
    print("Possible Plants: " + scan.possiblePlantsList)

def main():
    scanOnePlant()

if __name__ == '__main__':
    main()