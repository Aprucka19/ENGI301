from time import sleep
import pigpio
from guizero import App, Text, PushButton, Slider, TextBox
#import ramp


 
pi = pigpio.pi()

pi.set_mode(EN1, pigpio.OUTPUT)
pi.set_mode(IN11, pigpio.OUTPUT)
pi.set_mode(IN12, pigpio.OUTPUT)

pi.set_mode(EN2, pigpio.OUTPUT)
pi.set_mode(IN21, pigpio.OUTPUT)
pi.set_mode(IN22, pigpio.OUTPUT)

pi.set_mode(EN3, pigpio.OUTPUT)
pi.set_mode(IN31, pigpio.OUTPUT)
pi.set_mode(IN32, pigpio.OUTPUT)

pi.set_mode(EN4, pigpio.OUTPUT)
pi.set_mode(IN41, pigpio.OUTPUT)
pi.set_mode(IN42, pigpio.OUTPUT)

pi.write(IN11, 1)
pi.write(IN12, 0)

pi.write(IN21, 1)
pi.write(IN22, 0)

pi.write(IN31, 1)
pi.write(IN32, 0)

pi.write(IN41, 1)
pi.write(IN42, 0)


def enabletoggle(motorsleep):
    pi.write(motorsleep, not pi.read(motorsleep))
    if(motorsleep == EN1):
        message2.value = pi.read(motorsleep)
    if(motorsleep == EN2):
        message4.value = pi.read(motorsleep)
    if(motorsleep == EN3):
        message6.value = pi.read(motorsleep)
   
    if(motorsleep == EN4):
        message8.value = pi.read(motorsleep)


	

	
def dirtoggle(DIR1, DIR2):
    pi.write(DIR1, not pi.read(DIR1))
    pi.write(DIR2, not pi.read(DIR2))
    if(DIR1 == IN11):
        message3.value = pi.read(DIR1)
    if(DIR1 == IN21):
        message5.value = pi.read(DIR1)
    if(DIR1 == IN31):
        message7.value = pi.read(DIR1)
    if(DIR1 == IN41):
        message9.value = pi.read(DIR1)




app = App()




toggle_button = PushButton(app, text="EnableToggle1",command=enabletoggle, args=[EN1])
message2 = Text(app)


dirswapbutton = PushButton(app, text="change direction", command=dirtoggle, args=[IN11, IN12])
message3 = Text(app)

toggle_button2 = PushButton(app, text="EnableToggle2",command=enabletoggle, args=[EN2])
message4 = Text(app)


dirswapbutton2 = PushButton(app, text="change direction", command=dirtoggle, args=[IN21, IN22])
message5 = Text(app)

toggle_button3 = PushButton(app, text="EnableToggle3",command=enabletoggle, args=[EN3])
message6 = Text(app)


dirswapbutton3 = PushButton(app, text="change direction", command=dirtoggle, args=[IN31, IN32])
message7 = Text(app)

toggle_button4 = PushButton(app, text="EnableToggle4",command=enabletoggle, args=[EN4])
message8 = Text(app)


dirswapbutton4 = PushButton(app, text="change direction", command=dirtoggle, args=[IN41, IN42])
message9 = Text(app)



app.display()
