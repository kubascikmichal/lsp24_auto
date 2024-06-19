from machine import Pin, PWM
import time, sys
 
LED1 = Pin(16, Pin.OUT, value=0)
LED2 = Pin(17, Pin.OUT, value=1)
Tlac = Pin(7, Pin.IN, Pin.PULL_UP)
print('START')

while(1):
    if Tlac.value()==0:
        LED1.value(not LED1.value())
        LED2.value(not LED2.value())
        time.sleep_ms(10) 
        while(Tlac.value()==0):
            time.sleep_ms(10) 
