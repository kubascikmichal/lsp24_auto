from machine import Pin
import time, sys

LED1 = Pin(17, Pin.OUT, value=0)
LED2 = Pin(16, Pin.OUT, value=0)

class Sviet_led:
    
  def sviet(self, farba):
      if farba == "cervena":
          LED1.on()
          LED2.off()
      else:
          LED2.on()
          LED1.off()
  def zhasni(self):
          LED1.off()
          LED2.off()
       
led = Sviet_led()
led.sviet("cervena") #farba
time.sleep(2)
led.sviet("zelena") #farba
time.sleep(2)
led.zhasni()