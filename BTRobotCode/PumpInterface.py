"""
--------------------------------------------------------------------------
PumpInterface.py
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
An interface for the bartending robots 11 pumps. Allows them to all be initilized
simultaneously and allows each of the enable, direction, set, and get functions for
all 11 pumps. Pump 11 uses the standard Motor.py class because of limitations on 
gpio count on the two MCP23017 chips
Requirements:
  - Addresses of the first and second MCP23017 chips
Uses:
  - MCP23017
"""

from Adafruit_I2C import Adafruit_I2C
from MCP23017 import MCP23017
import time
import pigpio
import MotorPump, Motor

pi = pigpio.pi()





class PumpInterface():
	#the two MCPs and the 11 pumps
	mcp1 = None
	mcp2 = None
	p1 = None
	p2 = None
	p3 = None
	p4 = None
	p5 = None
	p6 = None
	p7 = None
	p8 = None
	p9 = None
	p10 = None
	p11 = None
	
	def __init__(self, ADD1, ADD2):
		#Init everything to the relevant GPIO/port
		self.mcp1 = MCP23017(ADD1, 16)
		self.mcp2 = MCP23017(ADD2, 16)
		self.p1 = MotorPump.MotorPump(0, 1, 2, self.mcp1)
		self.p2 = MotorPump.MotorPump(3, 4, 5, self.mcp1)
		self.p3 = MotorPump.MotorPump(6, 7, 8, self.mcp1)
		self.p4 = MotorPump.MotorPump(9, 10, 11, self.mcp1)
		self.p5 = MotorPump.MotorPump(12, 13, 14, self.mcp1)
		self.p6 = MotorPump.MotorPump(0, 1, 2, self.mcp2)
		self.p7 = MotorPump.MotorPump(3, 4, 5, self.mcp2)
		self.p8 = MotorPump.MotorPump(4, 7, 8, self.mcp2)
		self.p9 = MotorPump.MotorPump(9, 10, 11, self.mcp2)
		self.p10 = MotorPump.MotorPump(12, 13, 14, self.mcp2)
		self.p11 = Motor.Motor(17, 27, 22)
		

	#No case statements available. Could potentially be done better with list
	def enabletoggle(self, pump):
		if(pump == 1):
			self.p1.enabletoggle()
		elif(pump == 2):
			self.p2.enabletoggle()
		elif(pump == 3):
			self.p3.enabletoggle()
		elif(pump == 4):
			self.p4.enabletoggle()
		elif(pump == 5):
			self.p5.enabletoggle()
		elif(pump == 6):
			self.p6.enabletoggle()
		elif(pump == 7):
			self.p7.enabletoggle()
		elif(pump == 8):
			self.p8.enabletoggle()
		elif(pump == 9):
			self.p9.enabletoggle()
		elif(pump == 10):
			self.p10.enabletoggle()
		elif(pump == 11):
			self.p11.enabletoggle()

	
	def dirtoggle(self, pump):
		if(pump == 1):
			self.p1.dirtoggle()
		elif(pump == 2):
			self.p2.dirtoggle()
		elif(pump == 3):
			self.p3.dirtoggle()
		elif(pump == 4):
			self.p4.dirtoggle()
		elif(pump == 5):
			self.p5.dirtoggle()
		elif(pump == 6):
			self.p6.dirtoggle()
		elif(pump == 7):
			self.p7.dirtoggle()
		elif(pump == 8):
			self.p8.dirtoggle()
		elif(pump == 9):
			self.p9.dirtoggle()
		elif(pump == 10):
			self.p10.dirtoggle()
		elif(pump == 11):
			self.p11.dirtoggle()
	
	def getDir(self, pump):
		if(pump == 1):
			return self.p1.getDir()
		elif(pump == 2):
			return self.p2.getDir()
		elif(pump == 3):
			return self.p3.getDir()
		elif(pump == 4):
			return self.p4.getDir()
		elif(pump == 5):
			return self.p5.getDir()
		elif(pump == 6):
			return self.p6.getDir()
		elif(pump == 7):
			return self.p7.getDir()
		elif(pump == 8):
			return self.p8.getDir()
		elif(pump == 9):
			return self.p9.getDir()
		elif(pump == 10):
			return self.p10.getDir()
		elif(pump == 11):
			return self.p11.getDir()
		
	def getEn(self, pump):
		if(pump == 1):
			return self.p1.getEn()
		elif(pump == 2):
			return self.p2.getEn()
		elif(pump == 3):
			return self.p3.getEn()
		elif(pump == 4):
			return self.p4.getEn()
		elif(pump == 5):
			return self.p5.getEn()
		elif(pump == 6):
			return self.p6.getEn()
		elif(pump == 7):
			return self.p7.getEn()
		elif(pump == 8):
			return self.p8.getEn()
		elif(pump == 9):
			return self.p9.getEn()
		elif(pump == 10):
			return self.p10.getEn()
		elif(pump == 11):
			return self.p11.getEn()

	def setDir(self, pump, direction):
		if(pump == 1):
			self.p1.setDir(direction)
		elif(pump == 2):
			self.p2.setDir(direction)
		elif(pump == 3):
			self.p3.setDir(direction)
		elif(pump == 4):
			self.p4.setDir(direction)
		elif(pump == 5):
			self.p5.setDir(direction)
		elif(pump == 6):
			self.p6.setDir(direction)
		elif(pump == 7):
			self.p7.setDir(direction)
		elif(pump == 8):
			self.p8.setDir(direction)
		elif(pump == 9):
			self.p9.setDir(direction)
		elif(pump == 10):
			self.p10.setDir(direction)
		elif(pump == 11):
			self.p11.setDir(direction)
			
	def setEn(self, pump, enable):
		if(pump == 1):
			self.p1.setEn(enable)
		elif(pump == 2):
			self.p2.setEn(enable)
		elif(pump == 3):
			self.p3.setEn(enable)
		elif(pump == 4):
			self.p4.setEn(enable)
		elif(pump == 5):
			self.p5.setEn(enable)
		elif(pump == 6):
			self.p6.setEn(enable)
		elif(pump == 7):
			self.p7.setEn(enable)
		elif(pump == 8):
			self.p8.setEn(enable)
		elif(pump == 9):
			self.p9.setEn(enable)
		elif(pump == 10):
			self.p10.setEn(enable)
		elif(pump == 11):
			self.p11.setEn(enable)
			
			

