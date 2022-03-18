class Engine:

    def __init__(self, ser):
        self.ser = ser

    def engineOn(self):

        ser = self.ser
        try:
            self.updateState(ser, 'start')

        finally:
            # ser.close()
            print("")

    def engineOff(self):

        ser = self.ser

        try:
            self.updateState(ser, 'stop')
        finally:
            # ser.close()
            print("")

    def updateState(ser, state):

        print('STATE: ' + state)

        changeState = (bytes(state + "\n", 'UTF-8'))
        ser.write(changeState)

        readState = ser.readline().decode('utf-8')
        print(readState)
