from curses.ascii import DEL
from time import sleep
import RPi.GPIO as GPIO
import vlc
import board
import neopixel_spi as neopixel
from random import randint
NUM_PIXELS = 167
PIXEL_ORDER = neopixel.GRB
ColorsAR = (0x0080FF, 0xFFFFFF)
ColorsAU = (0x0000FF, 0xFFFFFF, 0xFF0000)
ColorsBE = (0x5E2612, 0xFFFF00, 0xFF0000)
ColorsBR = (0x0000CC, 0xFFFF00, 0x00CC00)
ColorsCA = (0xFF0000, 0xFFFFFF)
ColorsCN = (0xFF0000, 0xFFFF00)
ColorsCO = (0xFFFF00, 0x0000CC, 0xFF0000)
ColorsCD = (0x0066CC, 0xFFFF00, 0xFF0000)
ColorsEG = (0xFF0000, 0xFFFFFF, 0x5E2612)
ColorsIN = (0xFF9933, 0xFFFFFF, 0x00FF00)
ColorsMX = (0x00FF00, 0xFFFFFF, 0xFF0000)
ColorsNZ = (0x0000FF, 0xFF0000, 0xFFFF00)
ColorsRU = (0xFFFFFF, 0x0000FF, 0xFF0000)
ColorsES = (0xFF0000, 0xFFFF00)
ColorsUS = (0x0000FF, 0xFFFFFF, 0xFF0000)
ColorsZA = (0xFFFF00, 0x00FF00, 0xFF0000, 0x0000FF)
ColorsSE = (0x0000FF, 0xFFFF00)
ColorsSPEC = (0xFF0000, 0x00FF00, 0x0000FF, 0xFFFFFF)
ColorsOFF = 0x000000
DELAY = 1
#GPIO 10 voor de datapin
spi=board.SPI()

pixels = neopixel.NeoPixel_SPI(spi, NUM_PIXELS,pixel_order=PIXEL_ORDER,auto_write = False)
GPIO.setmode (GPIO.BCM)
inputlijst =[5,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
for i in range (18):
    GPIO.setup (inputlijst[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup (8, GPIO.OUT)
for color in ColorsBE:
    for i in range(16,28):
        pixels[i] = color
        pixels.show()
    sleep(DELAY)
    pixels.fill(0)

try:
    while True:
        GPIO.output(8, 1)
        if GPIO.input(11):
            AR = vlc.MediaPlayer("ArgentiniĆ«.mp3")
            AR.play()            
            for j in range(9):
                for color in ColorsAR:
                    for i in range(139,145):
                        pixels[i] = color
                        pixels.show()
                    sleep(DELAY)
            AR = 0
        elif GPIO.input(12): 
            AU = vlc.MediaPlayer("AustraliĆ«.mp3")   
            AU.play()
            for j in range(6):
                for color in ColorsAU:
                    for i in range(16):
                        pixels[i] = color
                        pixels.show()
                    sleep(DELAY)
                    pixels.fill(0)
            AU = 0
        elif GPIO.input(13):
            BE = vlc.MediaPlayer("BelgiĆ«.mp3")
            BE.play()
            for j in range(7):
                for color in ColorsBE:
                    for i in range(16,28):
                        pixels[i] = color
                        pixels.show()
                    sleep(DELAY)
                    pixels.fill(0)
            BE = 0
        elif GPIO.input(14):
            BR = vlc.MediaPlayer("BraziliĆ«.mp3")
            BR.play()
            for j in range(6):
                for color in ColorsBR:
                    for i in range(28,44):
                        pixels[i] = color
                        pixels.show()
                    sleep(DELAY)
                    pixels.fill(0)
            BR = 0
        elif GPIO.input(15):
            CA = vlc.MediaPlayer("Canada.mp3")
            CA.play()            
            for j in range(9):
                for color in ColorsCA:
                    for i in range(44,56):
                        pixels[i] = color
                        pixels.show()
                    sleep(DELAY)
                    pixels.fill(0)
            CA = 0
        elif GPIO.input(16): 
            CN = vlc.MediaPlayer("China.mp3")   
            CN.play()
            for j in range(9):
                for color in ColorsCN:
                    for i in range(56,72):
                        pixels[i] = color
                        pixels.show()
                    sleep(DELAY)
                    pixels.fill(0)
            CN = 0
        elif GPIO.input(17):
            CO = vlc.MediaPlayer("Colombia.mp3")
            CO.play()
            for j in range(7):
                for color in ColorsCO:
                    pixels[138] = color
                    pixels.show()
                    sleep(DELAY)
                pixels.fill(0)
            CO = 0
        elif GPIO.input(18):
            CD = vlc.MediaPlayer("Congo.mp3")
            CD.play()
            for j in range(7):
                for color in ColorsCD:
                    for i in range(72,84):
                        pixels[i] = color
                        pixels.show()
                    sleep(DELAY)
                    pixels.fill(0)
            CD = 0
        elif GPIO.input(19):
            EG = vlc.MediaPlayer("Egypte.mp3")
            EG.play()            
            for j in range(8):
                for color in ColorsEG:
                    pixels[147] = color
                    pixels.show()
                    sleep(DELAY)
                pixels.fill(0)
            EG = 0
        elif GPIO.input(20): 
            IN= vlc.MediaPlayer("India.mp3")   
            IN.play()
            for j in range(7):
                for color in ColorsIN:
                    for i in range(84,96):
                        pixels[i] = color
                        pixels.show()
                    sleep(DELAY)
                    pixels.fill(0)
            IN = 0
        elif GPIO.input(21):
            MX = vlc.MediaPlayer("Mexico.mp3")
            MX.play()
            for j in range(8):
                for color in ColorsMX:
                    for i in range(136,138):
                        pixels[i] = color
                        pixels.show()
                    sleep(DELAY)
                    pixels.fill(0)
            MX = 0
        elif GPIO.input(22):
            NZ = vlc.MediaPlayer("Nieuw Zeeland.mp3")
            NZ.play()
            for j in range(6):
                for color in ColorsNZ:
                    for i in range(96,108):
                        pixels[i] = color
                        pixels.show()
                    sleep(DELAY)
                    pixels.fill(0)
            NZ = 0
        elif GPIO.input(23):
            RU = vlc.MediaPlayer("Rusland.mp3")
            RU.play()            
            for j in range(7):
                for color in ColorsRU:
                    for i in range(151,167):
                        pixels[i] = color
                        pixels.show()
                    sleep(DELAY)
                    pixels.fill(0)
            RU = 0
        elif GPIO.input(24): 
            ES = vlc.MediaPlayer("Spanje.mp3")   
            ES.play()
            for j in range(12):
                for color in ColorsES:
                    pixels[148] = color
                    pixels.show()
                    sleep(DELAY)
                    pixels.fill(0)
            ES = 0
        elif GPIO.input(25):
            US = vlc.MediaPlayer("Verenigde Staten.mp3")
            US.play()
            for j in range(6):
                for color in ColorsUS:
                    for i in range(108,136):
                        pixels[i] = color
                        pixels.show()
                    sleep(DELAY)
                    pixels.fill(0)
            US = 0
        elif GPIO.input(26):
            ZA = vlc.MediaPlayer("Zuid-Afrika.mp3")
            ZA.play()
            for j in range(5):
                for color in ColorsZA:
                    for i in range(145,147):
                        pixels[i] = color
                        pixels.show()
                    sleep(DELAY)
                    pixels.fill(0)
            ZA = 0
        elif GPIO.input(27):
            SE = vlc.MediaPlayer("Zweden.mp3")
            SE.play()
            for j in range(10):
                for color in ColorsSE:
                    for i in range(149,151):
                        pixels[i] = color
                        pixels.show()
                    sleep(DELAY)
                    pixels.fill(0)
            SE = 0
        elif GPIO.input(5):
            i = randint(0,3)   
            j = randint(0,160) 
            pixels[j] = ColorsSPEC[i]
            pixels[j+1] = ColorsSPEC[i]
            pixels[j+2] = ColorsSPEC[i]
            pixels[j+3] = ColorsSPEC[i]
            pixels[j+4] = ColorsSPEC[i]
            pixels.show()
            sleep(0.3)
            pixels[j] = ColorsOFF
            pixels[j+1] = ColorsOFF
            pixels[j+2] = ColorsOFF
            pixels[j+3] = ColorsOFF
            pixels[j+4] = ColorsOFF       
        else:
            for i in range(NUM_PIXELS):
                pixels[i] = ColorsOFF
                pixels.show()
                      
except KeyboardInterrupt:
    for i in range(NUM_PIXELS):
        pixels[i] = ColorsOFF
        pixels.show()
    GPIO.cleanup()         