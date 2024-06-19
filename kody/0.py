from machine import Pin
import time, sys

LED1 = Pin(17, Pin.OUT, value=0)
LED2 = Pin(16, Pin.OUT, value=0)

while True:
  LED1.on()
  LED2.off()
  time.sleep(0.5)
  LED2.on()
  LED1.off()
  time.sleep(0.5)

sys.exit(0)