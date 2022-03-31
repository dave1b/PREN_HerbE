from Distance import Distance
from Engine import Engine
from Tinyk22Con import Tinyk22Con
import threading

class Tinyk22Interface:
    def __init__(self, newDistanceCallback):
        self.ser = Tinyk22Con.getconnection()
        self.engineRunning = False
        self.engine = Engine(self.ser)
        self.distance = Distance(self.ser)
        self.timerInverval = 5
        self.newDistanceCallback = newDistanceCallback

    def turnEngineOn(self):
        self.engine.engineOn(self.ser)
        self.engineRunning = True
        self.startIntervalTime()

    def turnEngineOff(self):
        self.engine.engineOff(self.ser)
        self.engineRunning = True

    def receiveDistanceAndCallCallback(self):
        distance = self.distance.getDistance(self.ser)
        self.newDistanceCallback(distance)

    def startIntervalTime(self):
        def func_wrapper(self):
            if(self.engineRunning):
                self.set_interval(self.receiveDistanceAndCallCallback(), self.timerInverval)
                self.receiveDistanceAndCallCallback()
            else:
                return
        t = threading.Timer(self.timerInterval, func_wrapper)
        t.start()
