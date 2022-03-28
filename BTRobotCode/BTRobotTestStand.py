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
import Stepper, Motor
import RPi.GPIO as GPIO
#import sys
#import signal

pi = pigpio.pi()
GPIO.setmode(GPIO.BCM)

#Initilize steppers with their control GPIOS
ShakeStepper = Stepper.Stepper(8, 23, 7)
SlideStepper = Stepper.Stepper(16, 21, 20)

#Increase the speed of shakeStepper from standard 500
ShakeStepper.setFreq(1200)

#Initilize the pumps
Pump1 = Motor.Motor(15, 14, 18)
Pump2 = Motor.Motor(2, 3, 4)
Pump3 = Motor.Motor(17, 27, 22)
Pump4 = Motor.Motor(10, 9, 11)


#Initilize the 2 12 volt motors
IceMotor = Motor.Motor(24, 5, 6)
ShakeMotor = Motor.Motor(26, 19, 13)


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
box1 = TitleBox(app,"Pump Control", layout = "grid", grid = [0,0], align = "left")



#Create buttons and display values for pumps direction and toggle on/off
P1T = PushButton(box1, text="Pump1Toggle", grid = [0,1], command=lambda:[Pump1.enabletoggle(), changeText(P1Tmsg, Pump1.getEn())])
P1Tmsg = Text(box1,text = str(Pump1.getEn()), grid = [1,1])
P1D = PushButton(box1, text="Pump1Direction", grid = [2,1], command=lambda:[Pump1.dirtoggle(), changeText(P1Dmsg, Pump1.getDir())])
P1Dmsg = Text(box1,text = str(Pump1.getDir()), grid = [4,1])
P2T = PushButton(box1, text="Pump2Toggle", grid = [0,2], command=lambda:[Pump2.enabletoggle(), changeText(P2Tmsg, Pump2.getEn())])
P2Tmsg = Text(box1,text = str(Pump2.getEn()), grid = [1,2])
P2D = PushButton(box1, text="Pump2Direction", grid = [2,2], command=lambda:[Pump2.dirtoggle(), changeText(P2Dmsg, Pump2.getDir())])
P2Dmsg = Text(box1,text = str(Pump1.getDir()), grid = [4,2])
P3T = PushButton(box1, text="Pump3Toggle", grid = [0,3], command=lambda:[Pump3.enabletoggle(), changeText(P3Tmsg, Pump3.getEn())])
P3Tmsg = Text(box1,text = str(Pump3.getEn()), grid = [1,3])
P3D = PushButton(box1, text="Pump3Direction", grid = [2,3], command=lambda:[Pump3.dirtoggle(), changeText(P3Dmsg, Pump3.getDir())])
P3Dmsg = Text(box1,text = str(Pump1.getDir()), grid = [4,3])
P4T = PushButton(box1, text="Pump4Toggle", grid = [0,4], command=lambda:[Pump4.enabletoggle(), changeText(P4Tmsg, Pump4.getEn())])
P4Tmsg = Text(box1,text = str(Pump4.getEn()), grid = [1,4])
P4D = PushButton(box1, text="Pump4Direction", grid = [2,4], command=lambda:[Pump4.dirtoggle(), changeText(P4Dmsg, Pump4.getDir())])
P4Dmsg = Text(box1,text = str(Pump1.getDir()), grid = [4,4])

box2 = TitleBox(app,"Stepper Control", layout = "grid", grid = [0,1])

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
box3 = TitleBox(app,"Motor Control", layout = "grid", grid = [0,2], align = "left")
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



