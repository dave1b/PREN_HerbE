import sys

import tinyk22_con
import time


class velocity:

    def setvelocity(self):

        con = tinyk22_con.tinyk22_con()

        ser = con.getconnection()


        while True:
            #serialdata=ser.readline()          #take comment out when testing
            serialdata = ser                   #for test causes


            #read serial data and print it on screen
            if "velocity" in serialdata:
                print(serialdata)


            #Timer, how fast the velocity is gonna be updated
            time.sleep(2)


    def getvelocity(self):
        return velocity;



## Main method for test reasons
#def main():
#    v1 = velocity()
#    v1.setvelocity()
#    print(v1.getvelocity())

#    sys.exit()

#if __name__ == '__main__':
#    main()