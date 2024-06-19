from machine import Pin, PWM
import time, sys
 
LED1 = PWM(Pin(16), freq=20, duty=512)  # freq je int
LED2 = Pin(17, Pin.OUT, value=0)
time.sleep(5)
LED1.deinit()           # off PWM na pine 16
LED1 = Pin(16, Pin.OUT, value=0)
while(1):
    LED1.on()
    LED2.off()
    time.sleep_ms(5)
    LED1.off()
    LED2.on()
    time.sleep_ms(1)