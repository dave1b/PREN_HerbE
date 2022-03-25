import Tinyk22Con
import sys
class Distance:

    def __init__(self, ser):
        self.ser = ser

    # gets the distance from TinyK22
    def getDistance(self):
        try:
            ser = self.ser

            # sends the distance-request
            request = (bytes('distance\n', 'UTF-8'))
            ser.write(request)
            distance = str(ser.readline(),'utf-8')
            print(distance)

        finally:
            #ser.close()
            print("")

def main():

    con = Tinyk22Con.tinyk22_con()
    ser = con.getconnection()

    distance = Distance(ser)

    distance.getDistance()


if __name__ == '__main__':
    main()
