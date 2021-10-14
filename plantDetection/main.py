import time
from scan import Scan
from compareTwoScans import hasMatchingPlantInScan, findMatchingPlantInScan, findFirstMatchingPlantInScan


firstScanReady = input("Erstes Pflanze gescannt?")
scanOnTheRoad = Scan("./plantDetection/minth1.jpg")


secondScanReady = input("Zweite Pflanze gescannt?")
scanAtEnd1 = Scan("./plantDetection/minth2.jpg")


for i in range(0,2):
    print("comparing both photos...")
    time.sleep(0.5)

print("Has found a match: ", hasMatchingPlantInScan(scanOnTheRoad.possiblePlantsList,scanAtEnd1.possiblePlantsList))
print("Found match: ", findFirstMatchingPlantInScan(scanOnTheRoad.possiblePlantsList, scanAtEnd1.possiblePlantsList))
#print(findMatchingPlantInScan(scanOnTheRoad.possiblePlantsList, scanAtEnd1.possiblePlantsList))


