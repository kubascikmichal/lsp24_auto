import time, sys
try:
  import usocket as socket
except:
  import socket
import network  
import esp
esp.osdebug(None)

import gc
gc.collect()

station = network.WLAN(network.AP_IF)
station.active(True)
station.config(essid='ESP_AUTO2')
station.config(authmode=3,password='12345678')
while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

def web_page(request):
  html = """<html><head> <title>Nas prvy Web Server</title> 
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>
  html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}
  .button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; text-decoration: none; font-size: 30px; width:100%}
  .button2{background-color: #4286f4; width:49%}
  </style></head>
  <body> <h1>Nas prvy web server</h1> 
  </body></html>"""
  
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 80))       #s.bind(addr)
s.listen(5)            #5

while True:
  try:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('The Content = %s' % request)
    response = web_page(request)
    conn.send(response)
    conn.close()
  except:
    pass
  time.sleep(0.1)
