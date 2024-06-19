import machine
from machine import Pin, Timer
import neopixel
import time, sys

poc = 0
np = neopixel.NeoPixel(Pin(14), 1)
def LEDzhasni():
    np[0] = (0, 0, 0, 0) 
    np.write()

def LEDzasviet(R, G, B, Y):
    np[0] = (R, G, B, Y) 
    np.write()

def obsluha(tim1):
    global poc
    poc = poc+1

tim1 = Timer(1)
tim1.init(period=10000, mode=Timer.PERIODIC, callback=obsluha)
    
while (poc < 7):
    if (poc == 0):
        LEDzasviet(255, 0, 0, 0)
    if (poc == 1):
        LEDzasviet(0, 255, 0, 0)
    if (poc == 2):
        LEDzasviet(0, 0, 255, 0)
    if (poc == 3):
        LEDzasviet(255, 255, 0, 0)
    if (poc == 4):
        LEDzasviet(255, 0, 255, 0)
    if (poc == 5):
        LEDzasviet(255, 255, 255, 0)
    if (poc == 6):
        LEDzasviet(255, 0, 0, 0)
    time.sleep_ms(20)

tim1.deinit()
LEDzhasni()
sys.exit(0)