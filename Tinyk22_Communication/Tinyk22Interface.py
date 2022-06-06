from Distance import Distance
from Engine import Engine
from Tinyk22Con import Tinyk22Con
from threading import Timer
import sys

sys.path.insert(0, 'Main_Model')
from Log import Logger


class Tinyk22Interface:
    def __init__(self, newDistanceCallback, distanceTimerInterval):
        self.ser = Tinyk22Con.getconnection(self)
        self.engineRunning = False
        self.engine = Engine(self.ser)
        self.distance = Distance(self.ser)
        self.timerInterval = distanceTimerInterval
        self.thread = Timer(self.timerInterval, self.func_wrapper)
        self.newDistanceCallback = newDistanceCallback
        self.log = Logger("Tinyk22Interface")

    def turnEngineOn(self):
        self.log.debug("turnEngineOn()")
        self.engine.engineOn()
        self.engineRunning = True
        self.startIntervalTime()

    def turnEngineOff(self):
        self.engine.engineOff()
        self.log.debug("engine: " + str(self.engine))
        self.engineRunning = False
        
    def shutdownEngine(self):
        self.log.debug("shutdownEngine: " + str(self.engine))
        self.engine.engineShutdown()
        self.engineRunning = False

    def receiveDistanceAndCallCallback(self):
        self.log.debug("receiveDistanceAndCallCallback()")
        distance = self.distance.getDistance()
        self.newDistanceCallback(distance)

    def func_wrapper(self):
        self.log.debug("func_wrapper()")
        if (self.engineRunning):
            self.receiveDistanceAndCallCallback()
            self.thread = Timer(self.timerInterval, self.func_wrapper)
            if not (self.thread.is_alive()):
                self.thread.start()
        else:
            self.thread.cancel()

    def startIntervalTime(self):
        self.log.debug("startIntervalTime()")
        if not (self.thread.is_alive()):
            self.thread = Timer(self.timerInterval, self.func_wrapper)
            self.thread.start()
    
    def resetComponents(self):
        self.engine.resetEngine()