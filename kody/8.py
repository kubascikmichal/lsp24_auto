import machine
import time, sys
LED1 = machine.Pin(16, machine.Pin.OUT, value=0)
LED2 = machine.Pin(17, machine.Pin.OUT, value=1)
Tlac = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_UP)
poc_prer = 0
celkovy_pocet = 0
 
casovac = machine.Timer(3)  


start = time.ticks_ms() # get millisecond counter

time.sleep(1)

delta = time.ticks_diff(time.ticks_ms(), start) # compute time difference
 
print("Cas: " + str(delta))


def obsluha(timer):
  global poc_prer
  poc_prer = poc_prer+1
 
casovac.init(period=1000, mode=machine.Timer.PERIODIC, callback=obsluha)
 
while True:
  if poc_prer>0:
    state = machine.disable_irq()
    poc_prer = poc_prer-1
    machine.enable_irq(state)
    LED1.value(not LED1.value())
    LED2.value(not LED2.value())
    if celkovy_pocet == 10: casovac.deinit()
    celkovy_pocet = celkovy_pocet+1
    print("Pocet preruseni: " + str(celkovy_pocet))
   