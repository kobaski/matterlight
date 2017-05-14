import time

import RPi.GPIO as GPIO

import re

from mattermost_bot.bot import listen_to
from mattermost_bot.bot import respond_to
from mattermost_bot.bot import Bot


R_PIN = 13
G_PIN = 5
B_PIN = 21
RGB = [R_PIN, G_PIN, B_PIN]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(R_PIN, GPIO.OUT)
GPIO.setup(G_PIN, GPIO.OUT)
GPIO.setup(B_PIN, GPIO.OUT)

def light(rgb):
    for this_pin, this_bit in enumerate(rgb):
        if this_bit == '1':            
            GPIO.output(RGB[this_pin], GPIO.HIGH)
        else:
            GPIO.output(RGB[this_pin], GPIO.LOW)

def str2rgb(this_str):
    ret = ''
    for this_b in ''.join(format(ord(x), 'b') for x in this_str):
        if len(ret) == 3:
            yield ret
            ret = ''
        else:
            ret += this_b

@listen_to('Hey Blue')
def hey_blue(message):
    light('001')
    message.reply('Blue is on')

@listen_to('Hello Red')
def hello_red(message):
    light('100')
    message.reply('Red is on')

@listen_to('Hi Green')
def hi_green(message):
    light('010')
    message.reply('Green is on')

@respond_to('Give me (.*)')
def give_me(message, something):
    kirakira(message+something)
    message.reply('Here is %s' % something)

@listen_to('(.*)')
def kirakira(message, everything):
    light('000')
    for this_rgb in str2rgb(everything):
        print this_rgb
        light(this_rgb)
        time.sleep(0.1)
    light('000')


if __name__ == "__main__":
    Bot().run()    
