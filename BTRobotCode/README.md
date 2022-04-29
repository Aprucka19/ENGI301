## Bartending Robot Project Code

This repository holds code for the bartening robot. 
Thurough documentation on the robot itself is held here: 
https://www.hackster.io/ap83/automatic-bartending-robot-bc4bf1

Currently within the repository there is at test folder with code I used to 
test individual components of the project.

BTRobotTestStand brings up a user interface which allows individual manual
control of each of the components of the build. It uses the helper classes
Motor, MotorPump, PumpInterface, and Stepper to control the relevant components, and ramp holds a function
which allows for smoother stepper speed up and slow down. The code is further 
documented within the files themselves.

The run executable currently calls the TestStand function, and the autostart file is used to
automatically execute it, as explained in the following forum post
https://forums.raspberrypi.com/viewtopic.php?t=237218&start=25

Necesary installs: 

sudo pip3 install guizero

sudo apt-get install -y python-smbus

sudo apt-get install -y i2c-tools

sudo systemctl enable pigpiod (to enable pigpiod on boot always)
