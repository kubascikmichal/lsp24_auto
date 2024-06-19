from machine import Pin, PWM
import time, sys

rychlost = 1000
class Motor: 
  def __init__(self):
    self.AIN1 = PWM(Pin(10),freq=1000, duty=0)
    self.BIN1 = PWM(Pin(11),freq=1000, duty=0)
    self.AIN2 = PWM(Pin(13),freq=1000, duty=0)
    self.BIN2 = PWM(Pin(12),freq=1000, duty=0)
  
  def motor(self, motor, rychlost):  # lavy,  pravy
    if rychlost > 1023: rychlost = 1023
    if rychlost < -1023: rychlost = -1023
    if motor == 'pravy':
      if rychlost >= 0:
        self.AIN1.duty(rychlost)
        self.BIN1.duty(0)
      else:
        self.AIN1.duty(0)
        self.BIN1.duty(-rychlost)
    if motor == 'lavy': 
      if rychlost >= 0:
        self.AIN2.duty(rychlost)
        self.BIN2.duty(0)
      else:
        self.AIN2.duty(0)
        self.BIN2.duty(-rychlost)

class Tlacidlo:
  def __init__(self):
      self.tlac = Pin(7, Pin.IN, Pin.PULL_UP)
  def daj_stav():
      return self.tlac.value()
 
mot = Motor()
mot.motor('pravy', rychlost)
time.sleep(3)
mot.motor('pravy', 0)
time.sleep(1)
mot.motor('pravy', -rychlost)
time.sleep(3)
mot.motor('pravy', 0)
sys.exit(0)