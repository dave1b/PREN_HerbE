import sys
sys.path.insert(0, '/home/pi/Desktop/PREN/Main_Model')
sys.path.insert(0, '../Main_Model')
from Log import Logger

class Engine:

    def __init__(self, ser):
        self.ser = ser
        self.log = Logger()

    def engineOn(self):
        self.log.debug("Tinyk22 Engine: engineOn()")
        try:
            self.updateState('start')
        except (RuntimeError):
            self.log.debug("EngineOn(): RuntimeError")
        except TypeError:
            self.log.debug("EngineOn(): TypeError")
        except NameError:
            self.log.debug("EngineOn(): NameError")

    def engineOff(self):
        self.log.debug("Tinyk22 Engine: engineOff()")
        try:
            self.updateState('stop')
        except (RuntimeError):
            self.log.debug("EngineOff(): RuntimeError")
        except TypeError:
            self.log.debug("EngineOff(): TypeError")
        except NameError:
            self.log.debug("EngineOff(): NameError")

    def updateState(self, state):
        self.log.debug("Tinyk22 Engine: updateState()")
        changeState = (bytes(state + "\n", 'UTF-8'))
        self.ser.write(changeState)