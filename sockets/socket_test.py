"""socket-test."""
import sys
try:
    import usocket as socket
except:
    import socket
import network
import esp
import gc

esp.osdebug(None)
gc.collect()

# nazov_wifi_siete = 'KTK-96385247'
# heslo_wifi_siete = 'Kopera00'

nazov_wifi_siete = 'KTK'
heslo_wifi_siete = '12345678'

# # kod pre vytvorenie pristupoveho bodu (access point)
# ap = network.WLAN(network.AP_IF)
# ap.active(True)
# ap.config(essid=nazov_wifi_siete, authmode=3, password=heslo_wifi_siete)
# while ap.active() is False:
#     pass
# 
# print('Connection successful')
# print(ap.ifconfig())


# # kod pre vytvorenie klienta (client)
# station = network.WLAN(network.STA_IF)
# station.active(True)
# if not station.isconnected():
#     station.connect(nazov_wifi_siete, heslo_wifi_siete)
#     while station.isconnected() is False:
#         pass
# 
# print('Connection to access point successful')
# print(station.ifconfig())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request, 'utf-8').strip()
    print('Content = %s' % str(request))
    
    conn.send('sprava prijata - zadaj pekne meno\r\n')
    
    if request == 'kika':
        print('pekne meno')
        conn.send('pouzivatel zadal pekne meno \r\n')

    conn.close()

sys.exit(0)
