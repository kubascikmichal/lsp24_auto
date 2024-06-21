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
from machine import Pin
from machine import I2C
import neopixel
import time
import trieda_motor
from ssd1306 import SSD1306_I2C

esp.osdebug(None)
gc.collect()

# nazov_wifi_siete = 'KTK-96385247'
# heslo_wifi_siete = 'Kopera00'

nazov_wifi_siete = 'KTK-LETNA_SKOLA_2024'
heslo_wifi_siete = 'veronika'

# # kod pre vytvorenie pristupoveho bodu (access point)
# ap = network.WLAN(network.AP_IF)
# ap.active(True)
# ap.config(essid=nazov_wifi_siete, authmode=3, password=heslo_wifi_siete)
# while ap.active() is False:
#     pass
# #
# print('Connection successful')
# print(ap.ifconfig())
# #
# ip_address = ap.ifconfig()[0]
# print(ip_address)


# kod pre vytvorenie klienta (client)
station = network.WLAN(network.STA_IF)
station.active(True)
if not station.isconnected():
    station.connect(nazov_wifi_siete, heslo_wifi_siete)
    while station.isconnected() is False:
        pass

print('Connection to access point successful')
print(station.ifconfig())

ip_address = station.ifconfig()[0]
print(ip_address)

np = neopixel.NeoPixel(Pin(14), 1)


def led_zhasni() -> None:
    """
    Tato funkcia zhasne seriovu RGB led diodu.

    :param: None
    :return: None
    """
    np[0] = (0, 0, 0)
    np.write()


def led_zasviet(R: int, G: int, B: int) -> None:
    """
    Tato funkcia zasvieti zvolenu farbu na seriovej RGB led diode.

    :param R: int
    :param G: int
    :param B: int
    :return: None

    Parametre:
    - prvy parameter je intenzita cervenej farby (0-255)
    - druhy parameter je intenzita zelenej farby (0-255)
    - treti parameter je intenzita modrej farby (0-255)
    """
    np[0] = (R, G, B)
    np.write()


WIDTH = 128
HEIGHT = 32
# I2C0 pin assignments
SCL = 9  # 22
SDA = 8  # 21
i2c = I2C(0, scl=Pin(SCL), sda=Pin(SDA), freq=400000)
# k = i2c.scan()
display = SSD1306_I2C(WIDTH, HEIGHT, i2c)
display.text("LETNA SKOLA 2024", 0, 0)
display.text(ip_address, 0,20 )
display.show()

mot = trieda_motor.Motor()
speed_r = 0
speed_l = 0
b_state = 'Stop'
shift_l = 0
shift_r = 0


def b_control() -> None:
    """
    Tato funkcia nastavi zvolene rychlosti na oba motory.

    :param: None
    :return: None
    """
    global speed_r
    global speed_l
    global shift_l
    global shift_r

    if speed_l >= 0:
        mot.lavy_motor_dopredu(speed_l + shift_l)
    else:
        mot.lavy_motor_dozadu((-speed_l) + shift_l)

    if speed_r >= 0:
        mot.pravy_motor_dopredu(speed_r + shift_r)
    else:
        mot.pravy_motor_dozadu((-speed_r) + shift_r)


background_color = 'white'
text_color = 'black'
change_color_text = 'turn on dark mode'


def web_page() -> str:
    """
    Tato funkcia nam vrati webovu stranku.

    :param: None
    :return: str

    Return:
    - funkcia nam navrati webovu stranku ako string.
    """
    global speed_l
    global speed_r
    global b_state
    global background_color
    global text_color
    global change_color_text
    global shift_l
    global shift_r
    html = """
    <html>
        <head>
            <title>ESP32-S2  - SHIP/CAR  -  Web Server</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="icon" href="data:,">

            <style>

                body{
                    background-color: """ + background_color + """;
                }

                html{
                    font-family: Helvetica;
                    display:inline-block;
                    margin: 0px auto;
                    text-align: center;
                }

                h1{
                    color: #0F3376;
                    padding: 2vh;
                }

                p{
                    font-size: 1.5rem;
                    color: """ + text_color + """;
                }

                .button{
                    display: inline-block;
                    background-color: #e7bd3b;
                    border: none;
                    border-radius: 4px;
                    color: white;
                    text-decoration: none;
                    font-size: 30px;
                    width:100%
                }

                .button2{
                    background-color: #4286f4;
                    width:49%;
                }
                
                input[type=text] {
                  background-color: #4286f4;
                  color: white;
                  font-size: 25px;
                }

                input[type=button], input[type=submit], input[type=reset] {
                    background-color: #e7bd3b;
                    border: none;
                    color: white;
                    padding: 16px 32px;
                    text-decoration: none;
                    margin: 4px 2px;
                    cursor: pointer;
                    font-size: 25px;
                }
                
                label{
                    font-size: 25px;
                    color: """ + text_color + """;
                }

            </style>

        </head>
        <body>
            <h1>ESP32-S2  - SHIP/CAR  -  Web Server</h1>

            <p><a href='/?change_color_mode'>
                <button class="button"> """ + change_color_text + """ </button>
            </a></p>

            <p>MOTOR_R: <strong>""" + str(speed_r) + """</strong></p>
            <p>MOTOR_L: <strong>""" + str(speed_l) + """</strong></p>
            <p>MOTOR_STATE: <strong>""" + b_state + """</strong></p>

            <p></p>

            <a href='/?start'>
                <button class="button">START</button>
            </a>

            <p></p>

            <a href='/?leftp'>
                <button class="button button2">MotorL+</button>
            </a>

            <a href='/?rightp'>
                <button class="button button2" >MotorR+</button>
            </a>

            <p></p>

            <a href='/?leftm'>
                <button class="button button2">MotorL-</button>
            </a>

            <a href='/?rightm'>
                <button class="button button2" >MotorR-</button>
            </a>

            <p></p>

            <a href='/?stop'>
                <button class="button button">STOP</button>
            </a>

            <p></p>
            
            <p>MOTOR_R_ADJUSTMENT: <strong>""" + str(shift_r) + """</strong></p>
            <p>MOTOR_L_ADJUSTMENT: <strong>""" + str(shift_l) + """</strong></p>

            <form action = '/?adjusting_speed'>
                <label for='right_adjustment'>Right wheel speed adjustment: </label>
                <input type='text' name='right_adjustment', name='left_adjustment'>
                <p></p>
                <label for='left_adjustment'>Left wheel speed adjustment: </label>
                <input type='text' name='left_adjustment', name='left_adjustment'>
                <p></p>
                <input type='submit' value='SET'>
            </form>

            <p>Author: prof. Ing. Juraj Micek PhD.</p>
            <p>University: University of Zilina</p>
            <p>Faculty: Faculty of Management, Science and Informatics</p>
            <p>Department: Department of Technical Cybernetics</p>

        </body>
    </html>"""

    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 80))
s.listen(5)

while True:
    try:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        conn.settimeout(5)
        request = conn.recv(1024)
        # print(request)
        request = str(request, 'utf-8')
        # print('The Content = %s' % request)

        change_color = request.find('/?change_color_mode')
        if change_color == 4:
            if background_color == 'white':
                background_color = 'black'
                text_color = 'white'
                change_color_text = 'turn on light mode'
            elif background_color == 'black':
                background_color = 'white'
                text_color = 'black'
                change_color_text = 'turn on dark mode'

        start = request.find('/?start')
        if start == 4:
            b_state = "Going"
            led_zhasni()
            led_zasviet(0, 100, 0)

        leftp = request.find('/?leftp')
        if leftp == 4:
            if speed_l < 1000:
                speed_l = speed_l + 50
            b_state = "Going"
            b_control()

        leftm = request.find('/?leftm')
        if leftm == 4:
            if speed_l > -1000:
                speed_l = speed_l - 50
            b_state = "Going"
            b_control()

        rightp = request.find('/?rightp')
        if rightp == 4:
            if speed_r < 1000:
                speed_r = speed_r + 50
            b_state = "Going"
            b_control()

        rightm = request.find('/?rightm')
        if rightm == 4:
            if speed_r > -1000:
                speed_r = speed_r - 50
            b_state = "Going"
            b_control()

        stop = request.find('/?stop')
        if stop == 4:
            b_state = "Stop"
            speed_l = 0
            speed_r = 0
            led_zhasni()
            led_zasviet(100, 0, 0)
            b_control()

        adjusting_speed = request.find('/?right_adjustment')
        if adjusting_speed == 4:
            zaciatok = request.find('/?right_adjustment')
            pom = request[zaciatok + len('/?right_adjustment='):]
            koniec = pom.find('HTTP/')
            zadany_text = pom[:koniec-1]
            zaciatok_2 = zadany_text.find('&')
            shift_r_pom = zadany_text[:zaciatok_2]
            shift_l_pom = zadany_text[zaciatok_2 + len('left_adjustment=') + 1:]
            try:
                shift_l = int(shift_l_pom)
            except ValueError:
                pass
            
            try:
                shift_r = int(shift_r_pom)
            except ValueError:
                pass

        print('speed_l = ' + str(speed_l))
        print('speed_r = ' + str(speed_r))
        print('shift_l = ' + str(shift_l))
        print('shift_r = ' + str(shift_r))
        print()
        response = web_page()
        conn.send(response)
        conn.close()

    except OSError as e:
        print(e)
        pass

    time.sleep(0.1)

sys.exit(0)
