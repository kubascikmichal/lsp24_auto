# MicroPython boot.py - Access Point and boat/car Web Controls

try:
  import usocket as socket
except:
  import socket
  
from ssd1306 import SSD1306_I2C
from machine import Pin, PWM, I2C
import framebuf
import utime
import neopixel
import time, sys
from motor_lod import Motor


import network

np = neopixel.NeoPixel(Pin(14), 1)
def LEDzhasni():
    np[0] = (0, 0, 0, 0) 
    np.write()

def LEDzasviet(R, G, B, Y):
    np[0] = (R, G, B, Y) 
    np.write()
LEDzasviet(0, 0, 40, 128)


WIDTH  = 128 
HEIGHT = 32
# I2C0 pin assignments
SCL = 9  #22
SDA = 8  #21
i2c = I2C(0, scl=Pin(SCL), sda=Pin(SDA), freq=400000)
k = i2c.scan()
display = SSD1306_I2C(WIDTH, HEIGHT, i2c)
display.text("ESP32_AUTO-LOD",12,10)
display.text("LETNA SKOLA 2024",2,22)
display.show()
mot = Motor()
rychlost_P=0
rychlost_L=0
stav = 0
station = network.WLAN(network.AP_IF)
station.active(True)
station.config(essid='ESP_AUTO2')
station.config(authmode=3,password='12345678')

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
display.fill(0)
display.text("CONNECTION OK",4,8)
display.show()

def Bcontrol():
  global rychlost_P
  global rychlost_L
  mot.motor('lavy', rychlost_L)
  mot.motor('pravy', rychlost_P)
   
def web_page(request):
  global rychlost_P
  global rychlost_L
  B_state = "Stop"
  if request.find('/?start') > 0:
    B_state="Going"
    LEDzhasni()
    LEDzasviet(0, 100, 0, 128)
    #Bcontrol()
  if request.find('/?leftp') > 0:
    rychlost_L=rychlost_L+50
    B_state="Going"
    Bcontrol()
  if request.find('/?leftm') > 0:
    rychlost_L=rychlost_L-50
    B_state="Going"
    Bcontrol()
  if request.find('/?rightp') > 0:
    rychlost_P=rychlost_P+50
    B_state="Going" 
    Bcontrol()
  if request.find('/?rightm') > 0:
    rychlost_P=rychlost_P-50
    B_state="Going" 
    Bcontrol()
  if request.find('/?stop') > 0:
    B_state="Stop"
    rychlost_P=0
    rychlost_L=0
    LEDzhasni()
    LEDzasviet(100, 0, 0, 128)
    Bcontrol()
  S_rych_P=str(rychlost_P)
  S_rych_L=str(rychlost_L)
  #print(rychlost_P)
  html = """<html><head> <title>ESP_LOD Web Server</title> 
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>
  html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}
  .button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; text-decoration: none; font-size: 30px; width:100%}
  .button2{background-color: #4286f4; width:49%}
  </style></head>
  <body> <h1>ESP_LOD Web Server</h1> 
  <p>MOTOR_P: <strong>""" + S_rych_P + """</strong></p>
  <p>MOTOR_L: <strong>""" + S_rych_L + """</strong></p>
  <p>MOTOR_L: <strong>""" + B_state + """</strong></p>
  <p><a href='/?start'><button class="button">START</button></a></p>
  <p><a href='/?leftp'><button class="button button2">MotorL+</button></a>
  <a href='/?rightp'><button class="button button2" >MotorP+</button></a></p>
  <p><a href='/?leftm'><button class="button button2">MotorL-</button></a>
  <a href='/?rightm'><button class="button button2" >MotorP-</button></a></p>
  
  
  <p><a href='/?stop'><button class="button button">STOP</button></a></p>
  
  </body></html>"""
  
  return html
                                    #addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.setblocking(0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 80))                           #s.bind(addr)
s.listen(5)            #5

while True:
  try:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    #display.fill(0)
    #display.text(addr,4,8)
    #display.show()
    request = conn.recv(1024)
    request = str(request)
    print('The Content = %s' % request)
    response = web_page(request)
    conn.send(response)
    conn.close()
  except:
    pass
  time.sleep(0.1)

