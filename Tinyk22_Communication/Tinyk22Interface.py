from Distance import Distance
from Engine import Engine
from Tinyk22Con import Tinyk22Con
from threading import Timer
import sys

sys.path.insert(0, '/home/pi/Desktop/PREN/Main_Model')
sys.path.insert(0, '../Main_Model')
from Log import Logger


class Tinyk22Interface:
    def __init__(self, newDistanceCallback):
        self.ser = Tinyk22Con.getconnection(self)
        self.engineRunning = False
        self.engine = Engine(self.ser)
        self.distance = Distance(self.ser)
        self.timerInterval = 1
        self.thread = Timer(self.timerInterval, self.func_wrapper)
        self.newDistanceCallback = newDistanceCallback
        self.log = Logger()

    def turnEngineOn(self):
        self.log.debug("Tinyk22 Interface: turnEngineOn()")
        self.engine.engineOn()
        self.engineRunning = True
        self.startIntervalTime()

    def turnEngineOff(self):
        self.log.debug("Tinyk22 Interface: engine: " + str(self.engine))
        self.engine.engineOff()
        self.engineRunning = False
        
    def shutdownEngine(self):
        self.log.debug("Tinyk22 Interface: shutdownEngine: " + str(self.engine))
        self.engine.engineShutdown()
        self.engineRunning = False

    def receiveDistanceAndCallCallback(self):
        self.log.debug("Tinyk22 Interface: receiveDistanceAndCallCallback()")
        distance = self.distance.getDistance()
        self.newDistanceCallback(distance)

    def func_wrapper(self):
        self.log.debug("Tinyk22 Interface: func_wrapper()")
        if (self.engineRunning):
            self.receiveDistanceAndCallCallback()
            self.thread = Timer(self.timerInterval, self.func_wrapper)
            if not (self.thread.is_alive()):
                self.thread.start()
        else:
            return

    def startIntervalTime(self):
        self.log.debug("Tinyk22 Interface: startIntervalTime()")
        if not (self.thread.is_alive()):
            self.thread = Timer(self.timerInterval, self.func_wrapper)
            self.thread.start()