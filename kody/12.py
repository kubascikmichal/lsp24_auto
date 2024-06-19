from machine import Pin, PWM
import time, sys

INA1 = Pin(10,Pin.OUT, value=0)
INB1 = Pin(11,Pin.OUT, value=0)
INA2 = Pin(13,Pin.OUT, value=0)
INB2 = Pin(12,Pin.OUT, value=0)
  
print("Dopredu")
INA1.on()
time.sleep(5)

print("Stop")
INA1.off()
time.sleep(1)

print("Dozadu")
INB1.on()
time.sleep(5)

print("Stop")
INB1.off()
time.sleep(1)

sys.exit(0)