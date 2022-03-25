import time

import Tinyk22Con
import Distance
import Engine
import sys


class Tinyk22_Interface:
    def __init__(self, ser):
        self.ser = ser

    def turnEngineOn(self, engine, ser):
        return engine.engineOn()

    def turnEngineOff(self, engine, ser):
        return engine.engineOff()

    def returnDistance(self, distance, ser):
        return distance.getDistance()

## Main method for test reasons
def main():

    t22c = Tinyk22Con.tinyk22_con()
    ser = t22c.getconnection()
    engine = Engine.Engine(ser)
    distance = Distance.Distance(ser)


    interface = Tinyk22_Interface(ser)

    interface.turnEngineOn(engine, ser)

    time.sleep(2)

    interface.turnEngineOff(engine, ser)

    interface.returnDistance(distance, ser)
    print("Test")

    sys.exit()


if __name__ == '__main__':
    main()
