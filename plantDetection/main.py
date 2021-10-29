import time
from scan import Scan
from compareTwoScans import hasMatchingPlantInScan, findMatchingPlantInScan, findFirstMatchingPlantInScan

def main():

    # Demonstration of functionality
    photo1 = "./photos/minth1.jpg"
    photo2 = "./photos/minth2.jpg"

    photo1_1 = "./plantDetection/photos/rose1.jpg"
    photo1_2 = "./plantDetection/photos/rose2.jpg"

    firstScanReady = input("Erstes Pflanze gescannt?")
    ScanOfFirstPhoto = Scan(photo1_1)

    secondScanReady = input("Zweite Pflanze gescannt?")
    ScanOfSecondPhoto = Scan(photo1_2)

    for i in range(0,3):
        print("comparing both photos...")
        time.sleep(0.5)

    print("Has found a match: ", hasMatchingPlantInScan(ScanOfFirstPhoto.possiblePlantsList,ScanOfSecondPhoto.possiblePlantsList))
    print("Found match: ", findFirstMatchingPlantInScan(ScanOfFirstPhoto.possiblePlantsList, ScanOfSecondPhoto.possiblePlantsList))
    #print(findMatchingPlantInScan(scanOnTheRoad.possiblePlantsList, scanAtEnd1.possiblePlantsList))

if __name__ == '__main__':
    main()