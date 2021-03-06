"""
--------------------------------------------------------------------------
BTRobotTestStand
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
Create a test stand for the bartending robot components. This uses guizero to create
a simple user interface allowing control over all of the motors/steppers/pumps in the build
at the click of a button

Makes use of the Motor.py and Stepper.py classes to control the components


Requirements:
  - None, brings up a window to be used as a test stand
Uses:
  - Motor.py and Stepper.py (in the same folder as this file)
"""


from time import sleep
import pigpio
from guizero import App, Text, PushButton, Slider, TextBox, Box, TitleBox
import Stepper, Motor, PumpInterface
import RPi.GPIO as GPIO
#import sys
#import signal


pi = pigpio.pi()
GPIO.setmode(GPIO.BCM)

#Initilize steppers with their control GPIOS
ShakeStepper = Stepper.Stepper(23, 8, 7)
SlideStepper = Stepper.Stepper(16, 21, 20)

#Increase the speed of shakeStepper from standard 500
ShakeStepper.setFreq(1200)

#Initilize the pumps
pInt = PumpInterface.PumpInterface(0x20, 0x21)


#Initilize the 2 12 volt motors
IceMotor = Motor.Motor(24, 5, 6)
ShakeMotor = Motor.Motor(26, 19, 13)

IceMotor.setDir(0)


#Set a port for the signal line of the optical endstop
Optical1 = 12

#Was testing an interrupt via the optical endstop
#GPIO.setup(Optical1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


#Helper function used to change the displayed values on the test bench interface
def changeText(msg, new):
	msg.value = new

#Function used when testing the optical endstop interrupt
def triggerPump(channel):
	Pump1.setEn(GPIO.input(Optical1))


#GPIO.add_event_detect(Optical1, GPIO.BOTH, callback=triggerPump)

#Create app and box subsections
app = App(layout = "grid")
box1 = TitleBox(app,"Pump Control", layout = "grid", grid = [0,1], align = "left")


'''
#Create buttons and display values for pumps direction and toggle on/off
PT = [PushButton(box1, text="Pump"+str(pump+1)+"Toggle", grid = [0,pump+1], command=lambda:[pInt.enabletoggle(pump+1), changeText(PTmsg[pump], pInt.getEn(pump+1))]) for pump in range(11)]
PTmsg = [Text(box1,text = str(pInt.getEn(pump+1)), grid = [1,pump+1]) for pump in range(11)]
PD = [PushButton(box1, text="Pump"+str(pump+1)+"Direction", grid = [2,pump+1], command=lambda:[pInt.dirtoggle(pump+1), changeText(PDmsg[pump], pInt.getDir(pump+1))]) for pump in range(11)]
PDmsg = [Text(box1,text = str(pInt.getDir(pump+1)), grid = [4,pump+1]) for pump in range(11)]

for i in range(11):
	pump = i+1
	PT[pump] = PushButton(box1, text="Pump"+str(pump)+"Toggle", grid = [0,pump], command=lambda:[pInt.enabletoggle(pump), changeText(PTmsg[pump], pInt.getEn(pump))])
	PTmsg[pump] = Text(box1,text = str(pInt.getEn(pump)), grid = [1,pump])
	PD[pump] = PushButton(box1, text="Pump"+str(pump)+"Direction", grid = [2,pump], command=lambda:[pInt.dirtoggle(pump), changeText(PDmsg[pump], pInt.getDir(pump))])
	PDmsg[pump] = Text(box1,text = str(pInt.getDir(pump)), grid = [4,pump])
'''


P1T = PushButton(box1, text="Pump1Toggle", grid = [0,1], command=lambda:[pInt.enabletoggle(1), changeText(P1Tmsg, pInt.getEn(1))])
P1Tmsg = Text(box1,text = str(pInt.getEn(1)), grid = [1,1])
P1D = PushButton(box1, text="Pump1Direction", grid = [2,1], command=lambda:[pInt.dirtoggle(1), changeText(P1Dmsg, pInt.getDir(1))])
P1Dmsg = Text(box1,text = str(pInt.getDir(1)), grid = [4,1])
P2T = PushButton(box1, text="Pump2Toggle", grid = [0,2], command=lambda:[pInt.enabletoggle(2), changeText(P2Tmsg, pInt.getEn(2))])
P2Tmsg = Text(box1,text = str(pInt.getEn(2)), grid = [1,2])
P2D = PushButton(box1, text="Pump2Direction", grid = [2,2], command=lambda:[pInt.dirtoggle(2), changeText(P2Dmsg, pInt.getDir(2))])
P2Dmsg = Text(box1,text = str(pInt.getDir(2)), grid = [4,2])
P3T = PushButton(box1, text="Pump3Toggle", grid = [0,3], command=lambda:[pInt.enabletoggle(3), changeText(P3Tmsg, pInt.getEn(3))])
P3Tmsg = Text(box1,text = str(pInt.getEn(3)), grid = [1,3])
P3D = PushButton(box1, text="Pump3Direction", grid = [2,3], command=lambda:[pInt.dirtoggle(3), changeText(P3Dmsg, pInt.getDir(3))])
P3Dmsg = Text(box1,text = str(pInt.getDir(3)), grid = [4,3])
P4T = PushButton(box1, text="Pump4Toggle", grid = [0,4], command=lambda:[pInt.enabletoggle(4), changeText(P4Tmsg, pInt.getEn(4))])
P4Tmsg = Text(box1,text = str(pInt.getEn(4)), grid = [1,4])
P4D = PushButton(box1, text="Pump4Direction", grid = [2,4], command=lambda:[pInt.dirtoggle(4), changeText(P4Dmsg, pInt.getDir(4))])
P4Dmsg = Text(box1,text = str(pInt.getDir(4)), grid = [4,4])
P5T = PushButton(box1, text="Pump5Toggle", grid = [0,5], command=lambda:[pInt.enabletoggle(5), changeText(P5Tmsg, pInt.getEn(5))])
P5Tmsg = Text(box1,text = str(pInt.getEn(5)), grid = [1,5])
P5D = PushButton(box1, text="Pump5Direction", grid = [2,5], command=lambda:[pInt.dirtoggle(5), changeText(P5Dmsg, pInt.getDir(5))])
P5Dmsg = Text(box1,text = str(pInt.getDir(5)), grid = [4,5])
P6T = PushButton(box1, text="Pump6Toggle", grid = [0,6], command=lambda:[pInt.enabletoggle(6), changeText(P6Tmsg, pInt.getEn(6))])
P6Tmsg = Text(box1,text = str(pInt.getEn(6)), grid = [1,6])
P6D = PushButton(box1, text="Pump6Direction", grid = [2,6], command=lambda:[pInt.dirtoggle(6), changeText(P6Dmsg, pInt.getDir(6))])
P6Dmsg = Text(box1,text = str(pInt.getDir(6)), grid = [4,6])
P7T = PushButton(box1, text="Pump7Toggle", grid = [0,7], command=lambda:[pInt.enabletoggle(7), changeText(P7Tmsg, pInt.getEn(7))])
P7Tmsg = Text(box1,text = str(pInt.getEn(7)), grid = [1,7])
P7D = PushButton(box1, text="Pump7Direction", grid = [2,7], command=lambda:[pInt.dirtoggle(7), changeText(P7Dmsg, pInt.getDir(7))])
P7Dmsg = Text(box1,text = str(pInt.getDir(7)), grid = [4,7])
P8T = PushButton(box1, text="Pump8Toggle", grid = [0,8], command=lambda:[pInt.enabletoggle(8), changeText(P8Tmsg, pInt.getEn(8))])
P8Tmsg = Text(box1,text = str(pInt.getEn(8)), grid = [1,8])
P8D = PushButton(box1, text="Pump8Direction", grid = [2,8], command=lambda:[pInt.dirtoggle(8), changeText(P8Dmsg, pInt.getDir(8))])
P8Dmsg = Text(box1,text = str(pInt.getDir(8)), grid = [4,8])
P9T = PushButton(box1, text="Pump9Toggle", grid = [0,9], command=lambda:[pInt.enabletoggle(9), changeText(P9Tmsg, pInt.getEn(9))])
P9Tmsg = Text(box1,text = str(pInt.getEn(9)), grid = [1,9])
P9D = PushButton(box1, text="Pump9Direction", grid = [2,9], command=lambda:[pInt.dirtoggle(9), changeText(P9Dmsg, pInt.getDir(9))])
P9Dmsg = Text(box1,text = str(pInt.getDir(9)), grid = [4,9])
P10T = PushButton(box1, text="Pump10Toggle", grid = [0,10], command=lambda:[pInt.enabletoggle(10), changeText(P10Tmsg, pInt.getEn(10))])
P10Tmsg = Text(box1,text = str(pInt.getEn(10)), grid = [1,10])
P10D = PushButton(box1, text="Pump10Direction", grid = [2,10], command=lambda:[pInt.dirtoggle(10), changeText(P10Tmsg, pInt.getDir(10))])
P10Dmsg = Text(box1,text = str(pInt.getDir(10)), grid = [4,10])
P11T = PushButton(box1, text="Pump11Toggle", grid = [0,11], command=lambda:[pInt.enabletoggle(11), changeText(P11Tmsg, pInt.getEn(11))])
P11Tmsg = Text(box1,text = str(pInt.getEn(11)), grid = [1,11])
P11D = PushButton(box1, text="Pump11Direction", grid = [2,11], command=lambda:[pInt.dirtoggle(11), changeText(P11Dmsg, pInt.getDir(11))])
P11Dmsg = Text(box1,text = str(pInt.getDir(11)), grid = [4,11])

box2 = TitleBox(app,"Stepper Control", layout = "grid", grid = [1,1])

#Create buttons and display values for stepper direction, enable, and toggle on/off
ShakeT = PushButton(box2, text="Shake Toggle", grid = [0,1], command=lambda:[ShakeStepper.enabletoggle(), changeText(ShakeTmsg, ShakeStepper.getEn())])
ShakeTmsg = Text(box2,text = str(ShakeStepper.getEn()), grid = [1,1])
ShakeD = PushButton(box2, text="Shake Direction", grid = [2,1], command=lambda:[ShakeStepper.dirtoggle(), changeText(ShakeDmsg, ShakeStepper.getDir())])
ShakeDmsg = Text(box2,text = str(ShakeStepper.getDir()), grid = [3,1])
ShakeM = PushButton(box2, text="Shake Move", grid = [4,1], command=lambda:[ShakeStepper.movetoggle(), changeText(ShakeMmsg, ShakeStepper.getDuty())])
ShakeMmsg = Text(box2,text = str(ShakeStepper.getDuty()), grid = [5,1])

SlideT = PushButton(box2, text="Slide Toggle", grid = [0,2], command=lambda:[SlideStepper.enabletoggle(), changeText(SlideTmsg, SlideStepper.getEn())])
SlideTmsg = Text(box2,text = str(SlideStepper.getEn()), grid = [1,2])
SlideD = PushButton(box2, text="Slide Direction", grid = [2,2], command=lambda:[SlideStepper.dirtoggle(), changeText(SlideDmsg, SlideStepper.getDir())])
SlideDmsg = Text(box2,text = str(SlideStepper.getDir()), grid = [3,2])
SlideM = PushButton(box2, text="Slide Move", grid = [4,2], command=lambda:[SlideStepper.movetoggle(), changeText(SlideMmsg, SlideStepper.getDuty())])
SlideMmsg = Text(box2,text = str(SlideStepper.getDuty()), grid = [5,2])


#Create buttons and display values for 12V motors direction and toggle on/off
box3 = TitleBox(app,"Motor Control", layout = "grid", grid = [2,1], align = "left")
ShakeMotorT = PushButton(box3, text="Shake Motor Toggle", grid = [0,1], command=lambda:[ShakeMotor.enabletoggle(), changeText(ShakeMotorTmsg, ShakeMotor.getEn())])
ShakeMotorTmsg = Text(box3, text = str(ShakeMotor.getEn()), grid = [1,1])
ShakeMotorD = PushButton(box3, text="Shake Motor Direction", grid = [2,1], command=lambda:[ShakeMotor.dirtoggle(), changeText(ShakeMotorDmsg, ShakeMotor.getDir())])
ShakeMotorDmsg = Text(box3, text = str(ShakeMotor.getDir()), grid = [3,1])
IceMotorT = PushButton(box3, text="Ice Motor Toggle", grid = [0,2], command=lambda:[IceMotor.enabletoggle(), changeText(IceMotorTmsg, IceMotor.getEn())])
IceMotorTmsg = Text(box3, text = str(IceMotor.getEn()), grid = [1,2])
IceMotorD = PushButton(box3, text="Ice Motor Direction", grid = [2,2], command=lambda:[IceMotor.dirtoggle(), changeText(IceMotorDmsg, IceMotor.getDir())])
IceMotorDmsg = Text(box3, text = str(IceMotor.getDir()), grid = [3,2])

#Display the app
app.display()



