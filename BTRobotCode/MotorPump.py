from Adafruit_I2C import Adafruit_I2C
from MCP23017 import MCP23017



class MotorPump():
	EN = None
	IN1 = None
	IN2 = None
	mcp = None
	
	def __init__(self, EN, IN1, IN2, mcp):
		self.EN = EN
		self.IN1 = IN1
		self.IN2 = IN2
		self.mcp = mcp
		#set as outputs
		self.mcp.pinMode(EN, self.mcp.OUTPUT)
		self.mcp.pinMode(IN1, self.mcp.OUTPUT)
		self.mcp.pinMode(IN2, self.mcp.OUTPUT)
		#Set initial values
		self.mcp.output(EN, self.mcp.LOW)
		self.mcp.output(IN1, self.mcp.HIGH)
		self.mcp.output(IN2, self.mcp.LOW)
	
	
	def enabletoggle(self):
		if(self.mcp.currentVal(self.EN) == 1):
			self.mcp.output(self.EN, self.mcp.LOW)
		else:
			self.mcp.output(self.EN, self.mcp.HIGH)
		
	
	
	def dirtoggle(self):
		if(self.mcp.currentVal(self.IN1) == 1):
			self.mcp.output(self.IN1, self.mcp.LOW)
			self.mcp.output(self.IN2, self.mcp.HIGH)
		else:
			self.mcp.output(self.IN1, self.mcp.HIGH)
			self.mcp.output(self.IN2, self.mcp.LOW)

		
	def getDir(self):
		return self.mcp.currentVal(self.IN1)
	
	def getEn(self):
		return self.mcp.currentVal(self.EN)
	
	def setDir(self,direction):
		if(direction == 1):
			self.mcp.output(self.IN1, self.mcp.HIGH)
			self.mcp.output(self.IN2, self.mcp.LOW)
		else:
			self.mcp.output(self.IN1, self.mcp.LOW)
			self.mcp.output(self.IN2, self.mcp.HIGH)
	def setEn(self,Enable):
		if(Enable == 1):
			self.mcp.output(self.EN, self.mcp.HIGH)
		else:
			self.mcp.output(self.EN, self.mcp.LOW)
		
	
	
	
