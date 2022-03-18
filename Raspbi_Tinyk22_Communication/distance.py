import sys

import tinyk22_con
import time

class distance:

    def __init__(self, ser):
        self.ser = ser


    def getdistance(self):
        try:
            ser = self.ser


            writeinput = (bytes("distance" + "\n", 'UTF-8'))
            ser.write(writeinput)


            readline = ser.readline().decode('utf-8')

            print('Distanz: ' + readline)


        finally:
            ser.close()



## Main method for test reasons
#def main():
#    con = tinyk22_con.tinyk22_con()

#    ser = con.getconnection()

#    d1 = distance(ser)
#    d1.getdistance()

#    sys.exit()

#if __name__ == '__main__':
#    main()