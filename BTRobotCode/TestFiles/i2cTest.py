import pcf8573
from machine import I2C, Pin

i2c = I2C(scl=Pin(5), sda=Pin(3))


pcf = pcf8573.PCF8574(i2c, 0x20)

print(pcf.pin(1))
