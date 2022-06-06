import sys
sys.path.insert(0, '/home/pi/Desktop/PREN/Main_Model')
sys.path.insert(0, '../Main_Model')
from Log import Logger

class Engine:

    def __init__(self, ser):
        self.ser = ser
        self.shutdown= False
        self.log = Logger("Engine")

    def engineOn(self):
        if not(self.shutdown):
            self.log.debug("engineOn()")
            try:
                self.updateState('start')
            except (RuntimeError):
                self.log.debug("RuntimeError")
            except TypeError:
                self.log.debug("TypeError")
            except NameError:
                self.log.debug("NameError")

    def engineOff(self):
        try:
            self.updateState('stop')
        except (RuntimeError):
            self.log.debug("EngineOff() - RuntimeError")
        except TypeError:
            self.log.debug("EngineOff() -TypeError")
        except NameError:
            self.log.debug("EngineOff(): NameError")
        self.log.debug("engineOff()")
            
    def engineShutdown(self):
        self.log.debug("EngineShutdown()")
        self.shutdown= True
        self.engineOff()

    def updateState(self, state):
        changeState = (bytes(state + "\n", 'UTF-8'))
        self.ser.write(changeState)
        self.log.debug("updateState(): " + state)
    
    def resetEngine(self):
        self.shutdown = False
        self.updateState('reset')