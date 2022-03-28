"""
--------------------------------------------------------------------------
Motor.py
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

An interface class for using a DC motor. Takes the enable and the two direction
pins as initilization values

Requirements:
  - Given GPIOs for enable, in1, and in2
Uses:
  - pigpio
"""


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
		
		#set as outputs
		pi.set_mode(self.EN, pigpio.OUTPUT)
		pi.set_mode(self.IN1, pigpio.OUTPUT)
		pi.set_mode(self.IN2, pigpio.OUTPUT)
		#Set initial values
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
		
	
	
	
