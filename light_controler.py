import time
import fileinput

import RPi.GPIO as GPIO

R_PIN = 13
G_PIN = 5
B_PIN = 21
RGB = [R_PIN, G_PIN, B_PIN]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(R_PIN, GPIO.OUT)
GPIO.setup(G_PIN, GPIO.OUT)
GPIO.setup(B_PIN, GPIO.OUT)

for rgb in fileinput.input():
    rgb = rgb.strip()
    
    if len(rgb) != 3:
        continue
        
    for this_pin, this_bit in enumerate(rgb):
        if this_bit == '1':            
            GPIO.output(RGB[this_pin], GPIO.HIGH)
        else:
            GPIO.output(RGB[this_pin], GPIO.LOW)
        
