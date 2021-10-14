



def findFirstMatchingPlantInScan(scan1, scan2):
    matchingPlant = list(set(scan1)&set(scan2))
    return matchingPlant[0]

def findMatchingPlantInScan(scan1, scan2):
    matchingPlant = list(set(scan1)&set(scan2))
    return matchingPlant

def hasMatchingPlantInScan(scan1, scan2):
    return (len(findMatchingPlantInScan(scan1,scan2)) >= 0)
        