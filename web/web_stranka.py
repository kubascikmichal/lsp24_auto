"""
webova stranka.

online editor webstranok: https://www.w3schools.com/html/tryit.asp?filename=tryhtml_editor

"""
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

vypis_textove_pole_1 = 'pouzivatel nezadal pekne meno'

def web_page() -> str:
    """
    Tato funkcia obsahuje nasu webovu stranku.

    :param request: str
    :return: str
    """
    global vypis_textove_pole_1
    html = """
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body>
            <h1>Toto je nadpis</h1>
            
            <p>toto je text</p>
            
            <p></p>
            <h4>Tu sa pracuje s tlacidlo</h4>
            <p></p>
            
            <a href='tlacidlo_1'>
                <button type='button'>Toto je tlacidlo cislo 1</button>
            </a>
            
            <p></p>
            <h4>Tu sa pracuje s textovym polom</h4>
            <p></p>
            
            <form action = 'textove_pole_1'>
                <label for='navratova_hodnota'>Zadaj text: </label>
                <input type='text' name='navratova_hodnota'>
                <p></p>
                <input type='submit' value='posli zadant text'>
            </form>
            
            <p> """ +  vypis_textove_pole_1 + """</p>

        </body>
    </html>"""

    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    # print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    # print(request)
    request = str(request, 'utf-8')
    # print('Content = %s' % str(request))
    
    tlacidlo_1 = request.find('tlacidlo_1')
    if tlacidlo_1 == 5:
        print('tlacidlo 1 bolo stlacene')
        
    textove_pole_1 = request.find('textove_pole_1')
    if textove_pole_1 == 5:
        
        zaciatok = request.find('?navratova_hodnota=')
        pom = request[zaciatok + len('?navratova_hodnota='):]
        koniec = pom.find('HTTP/')
        zadany_text = pom[:koniec-1]
        
        print('pouzivatel zadal text do textoveho pola 1: ' + zadany_text)
        if zadany_text == 'kika':
            vypis_textove_pole_1 = 'pouzivatel pozna pekne meno'
        else:
            vypis_textove_pole_1 = 'pouzivatel nezadal pekne meno'
        
    response = web_page()
    conn.send(response)
    conn.close()

sys.exit(0)
