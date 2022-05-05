import RPi.GPIO as GPIO
from time import sleep
import vlc
import board
import neopixel_spi as neopixel

NUM_PIXELS = 16
PIXEL_ORDER = neopixel.GRB
ColorsBE = (0x330019, 0xFFFF00, 0xFF0000)
ColorsCN = (0xFF0000, 0xFFFF00)
ColorsSE = (0x0000FF, 0xFFFF00)
ColorsOFF = 0x000000
DELAY = 0.1

spi=board.SPI()

pixels = neopixel.NeoPixel_SPI(spi, NUM_PIXELS,pixel_order=PIXEL_ORDER,auto_write = False)
GPIO.setmode (GPIO.BCM)
GPIO.setup (5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup (6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup (7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup (21, GPIO.OUT)

try:
    while True:
        GPIO.output(21, 1)
        China = vlc.MediaPlayer("China.mp3")
        Zweden = vlc.MediaPlayer("Zweden.mp3")
        Belgie = vlc.MediaPlayer("België.mp3")
        
        if GPIO.input(5):
            China.play()
            for j in range(5):
                for color in ColorsCN:
                    for i in range(NUM_PIXELS):
                        pixels[i] = color
                        pixels.show()
                        sleep(DELAY)
                        pixels.fill(0)
        elif GPIO.input(6):    
            Zweden.play()
            for j in range(5):
                for color in ColorsSE:
                    for i in range(NUM_PIXELS):
                        pixels[i] = color
                        pixels.show()
                        sleep(DELAY)
                        pixels.fill(0)
        elif GPIO.input(7):
            Belgie.play()
            for j in range(5):
                for color in ColorsBE:
                    for i in range(NUM_PIXELS):
                        pixels[i] = color
                        pixels.show()
                        sleep(DELAY)
                        pixels.fill(0)
        else:
            for i in range(NUM_PIXELS):
                pixels[i] = ColorsOFF
                pixels.show()
                      

except KeyboardInterrupt:
    for i in range(NUM_PIXELS):
        pixels[i] = ColorsOFF
        pixels.show()
    GPIO.cleanup()         