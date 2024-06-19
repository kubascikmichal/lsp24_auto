from machine import Pin, PWM
import time, sys

pom=0
LED1 = Pin(16, Pin.OUT, value=0)
LED2 = Pin(17, Pin.OUT, value=1)
Tlac = Pin(7, Pin.IN, Pin.PULL_UP)
print('START')
'''
while(1):
    if Tlac.value()==0:
        LED1.value(not LED1.value())
        LED2.value(not LED2.value())
        time.sleep_ms(10) 
        while(Tlac.value()==0):
            time.sleep_ms(10) 
'''       
def debounce(pin):
    prev = None
    for _ in range(1000):
        current_value = pin.value()
        if prev != None and prev != current_value:
            return None
        prev = current_value
    return prev

def obsluha(Tlac):                      #Tlac
     if debounce(Tlac) != None:
        LED1.value(not LED1.value())
        LED2.value(not LED2.value())

    
Tlac.irq(trigger=Pin.IRQ_RISING, handler=obsluha)   #handler=obsluha
#button.irq(trigger=Pin.IRQ_FALLING, handler=lambda t:led.value(not led.value()))
while(1):
    time.sleep(1)
''' if(pom>0):
        pom=0
        obsluha()
    time.sleep_ms(5)
#print('KONIEC')'''




#from machine import Pin, Timer

#led = Pin(23, Pin.OUT)
#led.value(0)

#timer = Timer(0)
#timer.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:led.value(not led.value()))
