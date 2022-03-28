from time import sleep
import pigpio
from guizero import App, Text, PushButton, Slider, TextBox
import ramp

DIR = 21
STEP = 20
SWITCH = 12
SLEEP = 16
freq = 1000

DIR2 = 1
STEP2 = 7
SLEEP2 = 8

pi = pigpio.pi()

pi.set_mode(SLEEP, pigpio.OUTPUT)
pi.set_mode(SLEEP2, pigpio.OUTPUT)
pi.set_mode(SWITCH, pigpio.INPUT)
pi.set_pull_up_down(SWITCH, pigpio.PUD_UP)

pi.set_PWM_dutycycle(STEP, 0)
pi.set_PWM_frequency(STEP, freq)

pi.set_PWM_dutycycle(STEP2, 0)
pi.set_PWM_frequency(STEP2, freq)

def sleeptoggle(motorsleep):
	pi.write(motorsleep, not pi.read(motorsleep))
	if(motorsleep == SLEEP):
		message2.value = pi.read(motorsleep)
	if(motorsleep == SLEEP2):
		message4.value = pi.read(motorsleep)
	

	
def dirtoggle():
	pi.write(DIR, not pi.read(DIR))
	message3.value = pi.read(DIR)

def stopstart(motorstep):
	
	if (pi.get_PWM_dutycycle(motorstep) == 128):
		pi.set_PWM_dutycycle(motorstep, 0)
	elif (pi.get_PWM_dutycycle(motorstep) == 0):
		pi.set_PWM_dutycycle(motorstep, 128)
	message.value = pi.get_PWM_dutycycle(motorstep)

def right():
    pi.write(DIR, 1)
    pi.set_PWM_dutycycle(STEP, 128)
    sleep(200/freq)
    pi.set_PWM_dutycycle(STEP, 0)

def left():
    pi.write(DIR, 0)
    pi.set_PWM_dutycycle(STEP, 128)
    sleep(200/freq)
    pi.set_PWM_dutycycle(STEP, 0)

def ramptest(motorstep):
	ramp.generate_ramp([
		   [1000, 400],
		   [2000, 1400],
		   [4000, 0],
	       [2000, 400],
	       [1000, 400]],motorstep,pi)


                                                                                           

message = Text(app)

text_box = TextBox(app)

right_button = PushButton(app, text="left", command=right)
left_button = PushButton(app, text="right", command=left)

stopstart_button = PushButton(app, text="stopstart1",command=stopstart, args=[STEP])
toggle_button = PushButton(app, text="toggle1",command=sleeptoggle, args=[SLEEP])
message2 = Text(app)
ramptestbutton = PushButton(app, text="ramp", command=ramptest, args=[STEP])

dirswapbutton = PushButton(app, text="change direction", command=dirtoggle)
message3 = Text(app)
toggle_button2 = PushButton(app, text="toggle2",command=sleeptoggle, args=[SLEEP2])
message4 = Text(app)
stopstart2_button = PushButton(app, text="stopstart2",command=stopstart, args=[STEP2])

app.display()
