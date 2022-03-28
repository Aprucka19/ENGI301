"""
--------------------------------------------------------------------------
Stepper.py
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

An interface class for using a stepper motor with a DRV8825 driver. 
Takes the enable, step, and direction pins as inputs

Requirements:
  - Given GPIOs for enable, dir, step
Uses:
  - pigpio (must use sudo pigpiod in the cmd line to allow PWM control on all pins)
  - ramp (a function that allows smooth ramping of speeds on steppers)
"""


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
		
	
