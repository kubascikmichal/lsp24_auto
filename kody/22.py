from machine import Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C
import framebuf
import utime
import neopixel
import time, sys

intenzita = 64
onpower = Pin(38,Pin.OUT)
onpower.on()

np = neopixel.NeoPixel(Pin(14), 1)
def LEDzhasni():
    np[0] = (0, 0, 0, 0) 
    np.write()

def LEDzasviet(R, G, B, Y):
    np[0] = (R, G, B, Y) 
    np.write()

LEDzasviet(0, 0, 60, 128)
WIDTH  = 128 
HEIGHT = 32
# Initialize I2C0, Scan and Debug print of SSD1306 I2C device address
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)
k = i2c.scan()
print("Device Address      : ")
print(k)
# Initialize OLED
display = SSD1306_I2C(WIDTH, HEIGHT, i2c)
display.text("LetnaSkola-AP",10,8)
display.text("123456789",10,22)
display.show()

try:
  import usocket as socket
except:
  import socket

import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'LetnaSkola-AP'
password = '123456789'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

display.fill(0)
display.text("Pripojene",10,8)
#display.text(ap.ifconfig(),10,22)
display.show()

def web_page():
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
  <body><h1>Ahoj!</h1></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  print('Content = %s' % str(request))
  response = web_page()
  conn.send(response)
  conn.close()            

