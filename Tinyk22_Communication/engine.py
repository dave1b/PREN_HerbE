import sys

import tinyk22_con
import time


class engine:

    def __init__(self, ser):
        self.ser = ser





    def setState(self,ser, STATE):


        print('STATE: ' + STATE)

        #serialdata = ser.write(str.encode(STATE))
        writeinput = (bytes(STATE + "\n", 'UTF-8'))
        ser.write(writeinput)

        readline = ser.readline().decode('utf-8')
        print(readline)



    def engineon(self):

        ser = self.ser
        try:

            #if(self.getState() == "ENG"):
            #print("Engine is already on!")
            #else:
            self.setState(ser,'start')


        finally:
            #ser.close()
            print("")

    def engineoff(self):

        ser = self.ser

        try:
            #if(self.getState() == "ENGINE OFF\n"):
            #print("Engine is already off")
            #else:
            self.setState(ser,'stop')
        finally:
            #ser.close()
            print("")


## Main method for test reasons
#def main():
#    con = tinyk22_con.tinyk22_con()
#    ser = con.getconnection()

#    e1 = engine(ser)

#    e1.engineon()
#    time.sleep(5)
#    e1.engineoff()

#    ser.close()
#    sys.exit()

#if __name__ == '__main__':
#    main()
