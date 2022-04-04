## Bartending Robot Project Code

This repository holds code for the bartening robot. 

Currently within the repository there is at test folder with code I used to 
test individual components of the project.

BTRobotTestStand brings up a user interface which allows individual manual
control of each of the components of the build. It uses the helper classes
Motor and Stepper to control the relevant components, and ramp holds a function
which allows for smoother stepper speed up and slow down. The code is further 
documented within the files themselves.

Lots of automation will be added in additional code blocks, taking advantage of the
optical sensors on the bot as well as the GPIO expanders to make the useable pump
count go from 4 to 11. 
