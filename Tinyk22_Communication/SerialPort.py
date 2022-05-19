import serial.tools.list_ports
sys.path.insert(0, '/home/pi/Desktop/PREN/Main_Model')
sys.path.insert(0, '../Main_Model')
from Log import Logger
# This file helps you to find out, which Serial port is taken by a device.

ports = serial.tools.list_ports.comports()
serialInit = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    self.log.debug("onePort: " + onePort)
val = input("select Port: COM")

for x in range(0, len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "com" + str(val)
        self.log.debug("portvar: " + portVar)
