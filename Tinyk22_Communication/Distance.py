import Tinyk22Con
import sys
sys.path.insert(0, 'Main_Model')
from Log import Logger

class Distance:

    def __init__(self, ser):
        self.ser = ser
        self.log = Logger("Distance")

    def getDistance(self):
        try:
            # sends the distance-request
            request = (bytes('distance\n', 'UTF-8'))
            self.ser.write(request)
            # gets the distance back from Tinyk22
            distance = str(self.ser.readline(),'utf-8')
            self.log.debug("getDistance() distance: " + distance)
            return distance
        except:
            self.log.error("error occured")