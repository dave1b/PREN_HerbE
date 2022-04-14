class Engine:

    def __init__(self, ser):
        self.ser = ser

    def engineOn(self):

        ser = self.ser
        try:
            self.updateState(ser, 'start')

        finally:
            print("")

    def engineOff(self):

        ser = self.ser

        try:
            self.updateState(ser, 'stop')
        finally:
            print("")

    def updateState(self, state):

        ser = self.ser

        changeState = (bytes(state + "\n", 'UTF-8'))
        ser.write(changeState)

        readState = ser.readline().decode('utf-8')

        print(readState)
