import requestAPIplantID
from time import gmtime, strftime

class Scan():
    def __init__(self, imagePfad):
        self.imagePfad = imagePfad
        self.possiblePlantsList = requestAPIplantID.scan(imagePfad)
        self.timeStamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())