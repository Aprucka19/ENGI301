from time import sleep
import pigpio

DIR = 21
STEP = 20
SWITCH = 12
SLEEP = 16

pi = pigpio.pi()

pi.set_mode(SLEEP, pigpio.OUTPUT)
pi.set_mode(SWITCH, pigpio.INPUT)
pi.set_pull_up_down(SWITCH, pigpio.PUD_UP)

pi.set_PWM_dutycycle(STEP, 128)
pi.set_PWM_frequency(STEP, 1000)

try:
    while True:
        pi.write(SLEEP, pi.read(SWITCH))
        sleep(.1)
except KeyboardInterrupt:
    print("\nCtrl-C pressed. Stopping PIGPIO and Exiting...")
finally:
    pi.set_PWM_dutycycle(STEP,0)
    pi.stop()
