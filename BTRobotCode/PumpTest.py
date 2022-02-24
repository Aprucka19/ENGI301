from time import sleep
import pigpio

IN1 = 14
IN2 = 15
EN = 18
SWITCH = 16

pi = pigpio.pi()

pi.set_mode(SWITCH, pigpio.INPUT)
pi.set_pull_up_down(SWITCH, pigpio.PUD_UP)
pi.set_mode(IN1, pigpio.OUTPUT)
pi.set_mode(IN2, pigpio.OUTPUT)

pi.set_mode(EN, pigpio.OUTPUT)
pi.write(EN, 1)

try:
    while True:
        pi.write(IN1, not pi.read(SWITCH))
        pi.write(IN2, pi.read(SWITCH))
        sleep(.1)
except KeyboardInterrupt:
    print("\nCtrl-C pressed. Stopping PIGPIO and Exiting...")
finally:
    pi.set_PWM_dutycycle(EN,0)
    pi.stop()