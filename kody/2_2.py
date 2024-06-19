from machine import Pin
import time, sys

class Blik_led:
  def __init__(self):
    self.LED1 = Pin(17, Pin.OUT, value=0)
    self.LED2 = Pin(16, Pin.OUT, value=0)
  
  def blikaj(self, farba, frekvencia, pocet):
    self.perioda=1/frekvencia
    self.cas_on= 0.5*self.perioda
    
    for i in range(pocet):    # pocet bliknuti
      if farba == "cervena":
          self.LED1.on()
          self.LED2.off()
      else:
          self.LED2.on()
          self.LED1.off()
      time.sleep(self.cas_on)
      self.LED2.off()
      self.LED1.off()
      time.sleep(self.perioda-self.cas_on)
      
led = Blik_led()
led.blikaj("cervena", 10, 100) #farba, frekvencia, pocet
