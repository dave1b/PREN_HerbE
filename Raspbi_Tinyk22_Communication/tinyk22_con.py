import serial

class tinyk22_con:

	def getconnection(self):
		return serial.Serial('COM3', 57600)  #try ttyAMA0 and ttyS0 // ttyACM0

		#return "velocity: 88mph"
		#return "distance: 420m"
		#return "ENGINE ON"
		#return "ENGINE OFF"
