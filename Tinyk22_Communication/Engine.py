import sys
sys.path.insert(0, '../Main&Model')
from Log import Logger

class Engine:

    def __init__(self, ser):
        self.ser = ser
        self.log = Logger()

    def engineOn(self):
        self.log.debug("Tinyk22 Engine: engineOn()")
        ser = self.ser
        try:
            self.updateState(ser, 'start')

        finally:
            print("")

    def engineOff(self):
        self.log.debug("Tinyk22 Engine: engineOff()")
        ser = self.ser

        try:
            self.updateState(ser, 'stop')
        finally:
            print("")

    def updateState(self, ser, state):
        self.log.debug("Tinyk22 Engine: updateState()")
        changeState = (bytes(state + "\n", 'UTF-8'))
        ser.write(changeState)

        readState = ser.readline().decode('utf-8')

        print(readState)



