from Distance import Distance
from Engine import Engine
from Tinyk22Con import Tinyk22Con
from threading import Timer
import sys
sys.path.insert(0, '../Main&Model')
from Log import Logger

class Tinyk22Interface:
    def __init__(self, newDistanceCallback):
        self.ser = Tinyk22Con.getconnection()
        self.engineRunning = False
        self.engine = Engine(self.ser)
        self.distance = Distance(self.ser)
        self.timerInterval = 1
        self.thread = Timer(self.timerInterval, self.func_wrapper)
        self.newDistanceCallback = newDistanceCallback
        self.log = Logger()

    def turnEngineOn(self):
        self.log.debug("Tinyk22 Interface: turnEngineOn()")
        self.engine.engineOn(self.ser)
        self.engineRunning = True
        self.startIntervalTime()

    def turnEngineOff(self):        
        self.log.debug("Tinyk22 Interface: turnEngineOff()")
        self.engine.engineOff(self.ser)
        self.engineRunning = True

    def receiveDistanceAndCallCallback(self):
        self.log.debug("Tinyk22 Interface: receiveDistanceAndCallCallback()")
        distance = self.distance.getDistance(self.ser)
        self.newDistanceCallback(distance)

     def func_wrapper(self):
            self.log.debug("Tinyk22 Interface: func_wrapper()")
        if(self.engineRunning):
            self.log.debug("Tinyk22 Interface: startIntervalTime() if(self.engineRunning)")
            self.receiveDistanceAndCallCallback()
            self.thread = Timer(self.timerInterval, self.func_wrapper)
            self.thread.start()
        else:
            return

    def startIntervalTime(self):
        self.log.debug("Tinyk22 Interface: startIntervalTime()")
        if not(self.thread.is_alive()):
            self.thread.start()