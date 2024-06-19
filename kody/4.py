from machine import Pin, PWM
import time, sys
 
LED1 = Pin(16, Pin.OUT, value=0)
LED2 = Pin(17, Pin.OUT, value=0)
Tlac = Pin(7, Pin.IN, Pin.PULL_UP)
print('START')

while(1):
    if Tlac.value()==0:
        LED1.on()
        LED2.off()
    else:
        LED1.off()
        LED2.on()
    time.sleep_ms(5)    # pre umoznenie obsluhy stop
