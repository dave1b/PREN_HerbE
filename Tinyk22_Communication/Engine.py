import sys

sys.path.insert(0, '../Main_Model')
from Log import Logger


class Engine:

    def __init__(self, ser):
        self.log = Logger()
        self.ser = ser

    def engineOn(self):
        self.log.debug("Tinyk22 Engine: engineOn()")
        try:
            self.updateState('start')

        finally:
            print("")

    def engineOff(self):
        self.log.debug("Tinyk22 Engine: engineOff()")
        try:
            self.updateState('stop')
        finally:
            print("")

    def updateState(self, state):
        self.log.debug("Tinyk22 Engine: updateState()")

        changeState = (bytes(state + "\n", 'UTF-8'))
        self.ser.write(changeState)
        print(readState)
