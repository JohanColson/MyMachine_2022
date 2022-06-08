
import RPi.GPIO as GPIO
from time import sleep
import vlc
import board
import neopixel_spi as neopixel

NUM_PIXELS = 180
PIXEL_ORDER = neopixel.GRB
ColorsAR = (0x0080FF, 0xFFFFFF)
ColorsAU = (0x0000FF, 0xFFFFFF, 0xFF0000)
ColorsBE = (0xFFFFFF, 0xFFFF00, 0xFF0000)
ColorsBR = (0x0000CC, 0xFFFF00, 0x00CC00)
ColorsCA = (0xFF0000, 0xFFFFFF)
ColorsCN = (0xFF0000, 0xFFFF00)
ColorsCO = (0xFFFF00, 0x0000CC, 0xFF0000)
ColorsCD = (0x0066CC, 0xFFFF00, 0xFF0000)
ColorsEG = (0xFF0000, 0xFFFFFF, 0xFFFFFF)
ColorsIN = (0xFF9933, 0xFFFFFF, 0x00FF00)
ColorsMX = (0x00FF00, 0xFFFFFF, 0xFF0000)
ColorsNZ = (0x0000FF, 0xFF0000, 0xFFFF00)
ColorsRU = (0xFFFFFF, 0x0000FF, 0xFF0000)
ColorsES = (0xFF0000, 0xFFFF00)
ColorsUS = (0x0000FF, 0xFFFFFF, 0xFF0000)
ColorsZA = (0xFFFF00, 0x00FF00, 0xFF0000, 0x0000FF)
ColorsSE = (0x0000FF, 0xFFFF00)
ColorsOFF = 0x000000
DELAY = 1
#GPIO 10 voor de datapin
spi=board.SPI()

pixels = neopixel.NeoPixel_SPI(spi, NUM_PIXELS,pixel_order=PIXEL_ORDER,auto_write = False)
GPIO.setmode (GPIO.BCM)
inputlijst =[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
for i in range (16):
    GPIO.setup (inputlijst[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup (8, GPIO.OUT)

try:
    while True:
          
        for j in range(4):
            for color in ColorsRU:
                for i in range(151,167):
                    pixels[i] = color
                    pixels.show()   
                sleep(1)
        
                    #pixels.fill(0)
        


                      
except KeyboardInterrupt:
    for i in range(NUM_PIXELS):
        pixels[i] = ColorsOFF
        pixels.show()
    GPIO.cleanup() 