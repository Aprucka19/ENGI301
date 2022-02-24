from time import sleep
import pigpio
import ramp


pi = pigpio.pi()

class Stepper():
	EN = None
	DIR = None
	STEP = None
	freq = 500
	#pi = None
	
	def __init__(self, EN, DIR, STEP):
		self.EN = EN
		self.DIR = DIR
		self.STEP = STEP
		#self.pi = pigpio.pi()
		
		pi.set_mode(self.EN, pigpio.OUTPUT)
		pi.set_mode(self.DIR, pigpio.OUTPUT)
		pi.set_PWM_dutycycle(self.STEP, 0)
		pi.set_PWM_frequency(self.STEP, self.freq)
	
	def enabletoggle(self):
		pi.write(self.EN, not pi.read(self.EN))
		
	def dirtoggle(self):
		pi.write(self.DIR, not pi.read(self.DIR))
		
	def movetoggle(self):
		if (pi.get_PWM_dutycycle(self.STEP) == 128):
			pi.set_PWM_dutycycle(self.STEP, 0)
		elif (pi.get_PWM_dutycycle(self.STEP) == 0):
			pi.set_PWM_dutycycle(self.STEP, 128)
	
	def getDir(self):
		return pi.read(self.DIR)
	
	def getEn(self):
		return pi.read(self.EN)

	def getDuty(self):
		return pi.get_PWM_dutycycle(self.STEP)
		
	def setDir(self,direction):
		pi.write(self.DIR, direction)
	
	def setEn(self,enable):
		pi.write(self.EN, enable)
		
	def getFreq(self):
		return self.freq
		
	def setFreq(self,frequency):
		self.freq = frequency
		pi.set_PWM_frequency(self.STEP, self.freq)
		
	def runramp(self,ramplist):
		ramp.generate_ramp(ramplist,self.STEP,pi)
		
	
