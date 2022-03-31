# compares two arrays and return the first machting item
def findFirstMatchingPlantInScan(scan1, scan2):
    matchingPlant = list(set(scan1)&set(scan2))
    return matchingPlant[0]
# compares two arrays for matches and return an array with all matches
def findMatchingPlantInScan(scan1, scan2):
    matchingPlant = list(set(scan1)&set(scan2))
    return matchingPlant
# compares two arrays for matches and returns boolean if there is at least one match
def hasMatchingPlantInScan(scan1, scan2):
    return (len(findMatchingPlantInScan(scan1,scan2)) >= 0)    