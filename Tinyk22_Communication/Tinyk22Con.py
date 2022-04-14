import serial

class Tinyk22Con:

	def getconnection(self):
		return serial.Serial('/dev/ttyACM0', 57600)# try ttyAMA0 and ttyS0 // ttyACM0
		#return serial.Serial('COM3', 57600)  #for notebook tests
