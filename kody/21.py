try:
  import usocket as socket
except:
  import socket
from machine import Pin
import network
import esp
esp.osdebug(None)
import gc
gc.collect()
import neopixel, time

np = neopixel.NeoPixel(Pin(14), 1)
def LEDzhasni():
    np[0] = (0, 0, 0, 0) 
    np.write()

def LEDzasviet(R, G, B, Y):
    np[0] = (R, G, B, Y) 
    np.write()

LEDzasviet(0, 0, 100, 128)
time.sleep(2)
LEDzhasni()

ssid = "UPC3921403"       #     'LetnaSkola-AP'  wifree
password ='Ym6uwaznRav4'        #'123456789'

"""station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())   """

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


do_connect()

led = Pin(2, Pin.OUT)

def web_page():
  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
  
  html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>Letna skola 2024</h1> 
  <p>GPIO state: <strong>""" + gpio_state + """</strong></p><p><a href="/?led=on"><button class="button">ON</button></a></p>
  <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  if led_on == 6:
    print('LED ON')
    #led.value(1)
    LEDzasviet(0, 100, 0, 128)
  if led_off == 6:
    print('LED OFF')
    #led.value(0)
    LEDzhasni()
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
