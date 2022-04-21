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
        except (RuntimeError):
            self.log.debug("EngineOn(): RuntimeError")
        except TypeError:
            self.log.debug("EngineOn(): TypeError")
        except NameError:
            self.log.debug("EngineOn(): NameError")

    def engineOff(self):
        self.log.debug("Tinyk22 Engine: engineOff()")
        ser = self.ser

        try:
            self.updateState(ser, 'stop')
        except (RuntimeError):
            self.log.debug("EngineOff(): RuntimeError")
        except TypeError:
            self.log.debug("EngineOff(): TypeError")
        except NameError:
            self.log.debug("EngineOff(): NameError")

    def updateState(self, ser, state):
        self.log.debug("Tinyk22 Engine: updateState()")
        changeState = (bytes(state + "\n", 'UTF-8'))
        ser.write(changeState)

        readState = ser.readline().decode('utf-8')

        print(readState)