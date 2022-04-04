"""
--------------------------------------------------------------------------
MotorPump.py
--------------------------------------------------------------------------
License:   
Copyright 2022 <Alex Prucka>
Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------
An interface class for using a DC motor, almost identical to Motor.py but works through
the interface of a MCP23017 GPIO expander. Takes the enable and the two direction
pins as initilization values along with the bus address of the MCP
Requirements:
  - Given GPIOs for enable, in1, and in2, and I2C address of device
Uses:
  - Adafruit_I2C, MCP23017
"""


from Adafruit_I2C import Adafruit_I2C
from MCP23017 import MCP23017


#Initilize motor
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
		
	
	
	
