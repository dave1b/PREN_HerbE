import time
from scan import Scan
from compareTwoScans import hasMatchingPlantInScan, findMatchingPlantInScan, findFirstMatchingPlantInScan

# Demonstration of functionality
photo1 = "./plantDetection/photos/minth1.jpg"
photo2 = "./plantDetection/photos/minth2.jpg"

firstScanReady = input("Erstes Pflanze gescannt?")
scanOnTheRoad = Scan(photo1)

secondScanReady = input("Zweite Pflanze gescannt?")
scanAtEnd1 = Scan(photo2)

for i in range(0,2):
    print("comparing both photos...")
    time.sleep(0.5)

print("Has found a match: ", hasMatchingPlantInScan(scanOnTheRoad.possiblePlantsList,scanAtEnd1.possiblePlantsList))
print("Found match: ", findFirstMatchingPlantInScan(scanOnTheRoad.possiblePlantsList, scanAtEnd1.possiblePlantsList))
#print(findMatchingPlantInScan(scanOnTheRoad.possiblePlantsList, scanAtEnd1.possiblePlantsList))