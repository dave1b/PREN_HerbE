import sys

import tinyk22_con
import time


class engine:
    def getState(self):
        con = tinyk22_con.tinyk22_con()

        ser = con.getconnection()

        #serialdata = ser.readline()  # take comment out when testing
        serialdata = ser                   #for test causes

        if "ENGINE" in serialdata:
            return serialdata

        return 0


    def setState(STATE):

        con = tinyk22_con.tinyk22_con()

        ser = con.getconnection();

        serialdata = ser.writelines(STATE)


    def engineon(self):
        e1 = engine()

        if(e1.getState() == "ENGINE ON"):
            print("Engine is already on!")
        else:
            e1.setState("ENGINE ON")

    def engineoff(self):
        e1 = engine()

        if(e1.getState() == "ENGINE OFF\n"):
            print("Engine is already off")
        else:
            e1.setState("ENGINE OFF\n")

## Main method for test reasons
def main():
    e1 = engine()
   # e1.getState()
    print(e1.getState())

    sys.exit()

if __name__ == '__main__':
    main()
