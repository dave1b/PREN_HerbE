import sys

import tinyk22_con
import time


class distance:

    def setdistance(self):

        con = tinyk22_con.tinyk22_con()

        ser = con.getconnection()


        while True:
            serialdata=ser.readline()          #take comment out when testing
            #serialdata = ser                   #for test causes


            #read serial data and print it on screen
            if "distance" in serialdata:
                print(serialdata)


            #Timer, how fast the velocity is gonna be updated
            time.sleep(2)


    def getdistance(self):
        return distance;



## Main method for test reasons
#def main():
#    d1 = distance()
#    d1.setdistance()
#    print(d1.getdistance())

#    sys.exit()

#if __name__ == '__main__':
#    main()