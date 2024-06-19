from machine import Pin
import time, sys

LED1 = Pin(17, Pin.OUT, value=0)
LED2 = Pin(16, Pin.OUT, value=0)

def blikaj(farba,frekvencia,strieda): # cervena/zelena fekvencia v Hz strieda 0 az  1
  perioda=1/frekvencia
  cas_on= perioda*strieda
    #while(1):
  for i in range(frekvencia):    # 1 sekunda
      if farba == "cervena":
          LED1.on()
          LED2.off()
      else:
          LED2.on()
          LED1.off()
      time.sleep(cas_on)
      LED2.off()
      LED1.off()
      time.sleep(perioda-cas_on)
    
for i in range(10):
    blikaj("cervena", 100, i/10)
    
    