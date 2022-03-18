import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInit = serial.Serial()


portList = []


for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))
val = input("select Port: COM")


print(val)


for x in range(0, len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "com" + str(val)
        print(portVar)