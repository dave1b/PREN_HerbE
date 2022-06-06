from threading import Timer
import sys
sys.path.insert(0, 'Main_Model')
from Log import Logger

class Tinyk22Interface:
    def __init__(self, newDistanceCallback):
        self.log = Logger("Tinyk22InterfaceFake")
        #self.ser = Tinyk22Con.getconnection()
        self.engineRunning = False
        #self.engine = Engine(self.ser)
        self.distance = 0
        self.timerInterval = 10
        self.thread = Timer(self.timerInterval, self.func_wrapper)
        self.newDistanceCallback = newDistanceCallback

    def turnEngineOn(self):
        self.log.debug("turnEngineOn()")
        #self.engine.engineOn(self.ser)
        self.engineRunning = True
        self.startIntervalTime()

    def turnEngineOff(self):
        self.log.debug("turnEngineOff()")
        #self.engine.engineOff(self.ser)
        self.engineRunning = True

    def receiveDistanceAndCallCallback(self):
        #distance = self.distance.getDistance(self.ser)
        self.distance = self.distance + 3
        self.newDistanceCallback(self.distance)

    def func_wrapper(self):
        self.log.debug("func_wrapper()")
        if(self.engineRunning):
            self.log.debug("startIntervalTime() if(self.engineRunning)")
            self.receiveDistanceAndCallCallback()
            self.thread = Timer(self.timerInterval, self.func_wrapper)
            self.thread.start()
        else:
            return

    def startIntervalTime(self):
        self.log.debug("startIntervalTime()")
        if not(self.thread.is_alive()):
            self.thread.start()
        
    def shutdownEngine(self):
        self.log.debug("shutdownEngine: ")
        self.engineRunning = False
    
    def resetComponents(self):
        self.engineRunning = False
