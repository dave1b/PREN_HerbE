import Tinyk22Con
import sys
class Distance:

    def __init__(self, ser):
        self.ser = ser

    def getDistance(self):
        try:
            ser = self.ser

            # sends the distance-request
            request = (bytes('distance\n', 'UTF-8'))
            ser.write(request)

            # gets the distance back from Tinyk22
            distance = str(ser.readline(),'utf-8')

            print(distance)

        finally:
            print("")
