import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode (GPIO.BCM)
inputlijst =[11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
for i in range (17):
    GPIO.setup (inputlijst[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
knop = 22
try:
    while True:
        if GPIO.input(knop):
            print(knop)
            print("deze poort werkt")
            sleep(1)
except:
    GPIO.cleanup()

