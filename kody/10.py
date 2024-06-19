from machine import Pin, I2C, Timer
from ssd1306 import SSD1306_I2C
import framebuf
import utime
import time, sys

# OLED pixel definition (WxH)
WIDTH  = 128 
HEIGHT = 32
# I2C0 pin assignments
SCL = 9  
SDA = 8  

# Initialize I2C0, Scan and Debug print of SSD1306 I2C device address
i2c = I2C(0, scl=Pin(SCL), sda=Pin(SDA), freq=400000)
k = i2c.scan()
print("Device Address      : ")
print(k)
# Initialize OLED
display = SSD1306_I2C(WIDTH, HEIGHT, i2c)
# Display image and text on OLED 
# Clear the display
display.fill(0)
# Write text in two lines
display.text("ESP32",10,8)
display.text("OLED Displej",10,22)
display.show()
time.sleep(5)

sys.exit(0)