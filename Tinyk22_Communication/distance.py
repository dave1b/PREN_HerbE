class Distance:

    def __init__(self, ser):
        self.ser = ser

    # gets the distance from TinyK22
    def getDistance(self):
        try:
            ser = self.ser

            # sends the distance-request
            request = (bytes('distance\n', 'UTF-8'))
            ser.write(request)

            distance = ser.readline().decode('utf-8')

            print(distance)

        finally:
            ser.close()