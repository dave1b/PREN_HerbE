import serial

class tinyk22_con:

	def getconnection(self):
		return serial.Serial('/dev/ttyAMA0', 57600)  #try ttyAMA0 and ttyS0 // ttyACM0

		#return "velocity: 88mph"
		#return "distance: 420m"
		#return "ENGINE ON"
		#return "ENGINE OFF"
