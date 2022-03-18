import serial

class tinyk22_con:

	def getconnection(self):

		return serial.Serial('ttyAMA0', 57600)# try ttyAMA0 and ttyS0 // ttyACM0
		#return serial.Serial('COM3', 57600)  #for notebook tests
