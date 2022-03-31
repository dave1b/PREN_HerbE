import time
import Tinyk22Con
import Distance
import Engine
import sys


class Tinyk22_Interface:
    def __init__(self, ser):
        self.ser = ser


    #turns the engine on
    def turnEngineOn(self, engine, ser):
        return engine.engineOn()

    #turns the engine off
    def turnEngineOff(self, engine, ser):
        return engine.engineOff()

    #returns the distance
    def returnDistance(self, distance, ser):
        return distance.getDistance()

        #newdistancecallback methode                        <##########################################################
        ##def newDistanceCallback(self, newDistanceDriven):
        ##self.dataModel.distanceDriven = newDistanceDriven

