import time

from Distance import Distance
from Engine import Engine
from Tinyk22Con import Tinyk22Con
import threading



class Tinyk22Interface:
    def __init__(self, newDistanceCallback):
        self.ser = Tinyk22Con.getconnection()
        self.engineRunning = False
        self.engine = Engine(ser)
        self.distance = Distance(ser)

        self.newDistanceCallback = newDistanceCallback

        self._timer = None
        self.interval = 5


    def turnEngineOn(self):
        self.engine.engineOn(self.ser)
        self.engineRunning = True
        setIntervalTime()

    def turnEngineOff(self):
        self.engine.engineOff(self.ser)
        self.engineRunning = True
        setIntervalTime()

    def receiveDistanceAndCallCallback(self):
        distance = self.distance.getDistance(self.ser)
        self.newDistanceCallback(distance)

    def setIntervalTime(self):
        thread = threading.Timer(interval, self.receiveDistanceAndCallCallback())

        if self.engineRunning == true:
            #self._timer = Timer(self.interval, self.receiveDistanceAndCallCallback())
            #starttime = threading.Timer(interval, self.receiveDistanceAndCallCallback())
            thread.start()

        else:
            thread.stop()

