from Adafruit_I2C import Adafruit_I2C
from MCP23017 import MCP23017
import MotorPump

import time


mcp1 = MCP23017(0x20, 16)
mcp2 = MCP23017(0x21, 16)

Pump1 = MotorPump.MotorPump(0, 1, 2, mcp1)

#Pump1.dirtoggle()
Pump1.setEn(0)
