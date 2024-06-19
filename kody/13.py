from machine import Pin, PWM
import time, sys

INA1 = PWM(Pin(10),freq=1000, duty=0)   # INA1
INB1 = PWM(Pin(11),freq=1000, duty=0)   # INB1
INA2 = PWM(Pin(13),freq=1000, duty=0)   # INA2 
INB2 = PWM(Pin(12),freq=1000, duty=0)   # INB2

def motor1(rychlost):
    if rychlost > 1023: rychlost = 1023
    if rychlost < -1023: rychlost = -1023
    print("Dopredu")
    INA1.duty(rychlost)
    INB1.duty(0)
    time.sleep(5)

    print("Stop")
    INA1.duty(0)
    INB1.duty(0)
    time.sleep(1)

    print("Dozadu")
    INA1.duty(0)
    INB1.duty(rychlost)
    time.sleep(5)

    print("Stop")
    INA1.duty(0)
    INB1.duty(0)
    time.sleep(1)


motor1(10)

sys.exit(0)