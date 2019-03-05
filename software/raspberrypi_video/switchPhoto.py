# Lepton by switch control
# Author: Tianyi Liu
# Site Referenced: http://razzpisampler.oreilly.com/ch07.html & https://www.hackster.io/hardikrathod/push-button-with-raspberry-pi-6b6928 -- GPIO


import RPI.GPIO as GPIO
import time
import os
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Pin 14 connect to switch and set to pull up to 3.3V, when switch pressed, grounded
GPIO.setup(15, GPIO.OUT) # Pin 15 connect to a LED. LED illuminates when image is done saving.

while True:
    input_state = GPIO.input(14)
    if input_state == False:
        print('Start image capturing\n')
        proc = subprocess.Popen(["sudo", "./raspberrypi_video"])
        GPIO.output(15, True)
        time.sleep(3)
        GPIO.output(15, False)
