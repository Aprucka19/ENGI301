from time import sleep
import pigpio

pi = pigpio.pi()


class Motor():
	EN = None
	IN1 = None
	IN2 = None
	
	def __init__(self, EN, IN1, IN2):
		self.EN = EN
		self.IN1 = IN1
		self.IN2 = IN2
		
		pi.set_mode(self.EN, pigpio.OUTPUT)
		pi.set_mode(self.IN1, pigpio.OUTPUT)
		pi.set_mode(self.IN2, pigpio.OUTPUT)
		pi.write(self.EN, 0)
		pi.write(self.IN1, 1)
		pi.write(self.IN2, 0)
	
	
	def enabletoggle(self):
		pi.write(self.EN, not pi.read(self.EN))
	
	
	def dirtoggle(self):
		pi.write(self.IN1, not pi.read(self.IN1))
		pi.write(self.IN2, not pi.read(self.IN2))
		
	def getDir(self):
		return pi.read(self.IN1)
	
	def getEn(self):
		return pi.read(self.EN)
	
	def setDir(self,direction):
		pi.write(self.IN1, direction)
		pi.write(self.IN2, not direction)
	
	def setEn(self,Enable):
		pi.write(self.EN, Enable)
		
	
	
	
