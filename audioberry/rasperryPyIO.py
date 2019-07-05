#!/usr/bin/python3

"""
https://gpiozero.readthedocs.io/en/v1.5.1/
http://abyz.me.uk/rpi/pigpio/download.html
"""
from gpiozero import Button, LED, Device
from signal import pause
# from gpiozero.pins.mock import MockFactory


from audioberry.audioPlayer import radio_action
from subprocess import check_call

# Set the default pin factory to a mock factory
# Device.pin_factory = MockFactory()

# PIN Layout

button_list = [
    {'pin': 15, 'led': 17, 'id': 'button-1', 'active': False},
    {'pin': 23, 'led': 27, 'id': 'button-2', 'active': False},
    {'pin': 24, 'led': 22, 'id': 'button-3', 'active': False},
    {'pin': 25, 'led': 10, 'id': 'button-4', 'active': False}
]

# LED
# -------------
led1 = LED(17)
led2 = LED(27)
led3 = LED(22)
led4 = LED(10)  # BLE

# leds = [led1, led2, led3, led4]

# BUTTON
# -------------
button1 = Button(15)
button2 = Button(23)
button3 = Button(24)
button4 = Button(25)


# ROTARY ENCODER
# --------------
# CLK - GPIO 13
# DT  - GPIO O6
#  +  - 3v3
# GND - GND

def action(button_nr):
    button = button_list[button_nr]
    status = button['active']
    led_pin = button['led']
    led = LED(led_pin)

    if not status:
        led.on()
        button['active'] = True
        radio_action(button)
    else:
        button['active'] = False
        radio_action(button)
        led.off()


# Button Action
def button_action1():
    action(1)


def button_action2():
    action(2)


def button_action3():
    action(3)


def button_action4():
    action(4)


def shutdown():
    check_call(['sudo', 'poweroff'])


# Listen for interaction
def run():
    print('start listening for buttons')
    button1.when_pressed = button_action1
    button2.when_pressed = button_action2
    button3.when_pressed = button_action3
    button4.when_pressed = button_action4

    # Keep Script going
   # pause()
