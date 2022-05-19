import Tinyk22Con
import sys
sys.path.insert(0, '/home/pi/Desktop/PREN/Main_Model')
sys.path.insert(0, '../Main_Model')
from Log import Logger

class Distance:

    def __init__(self, ser):
        self.ser = ser
        self.log = Logger()

    def getDistance(self):
        try:
            ser = self.ser
            # sends the distance-request
            request = (bytes('distance\n', 'UTF-8'))
            ser.write(request)
            # gets the distance back from Tinyk22
            distance = str(ser.readline(),'utf-8')
            self.log.debug("Tinyk22 Distance: getDistance() distance: " + distance)
            return distance
        except:
            self.log.error("Tinyk22 Distance - error occured")