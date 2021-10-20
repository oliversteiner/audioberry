#!/usr/bin/python3

"""
https://gpiozero.readthedocs.io/en/v1.5.1/
http://abyz.me.uk/rpi/pigpio/download.html

PIGPIO_ADDR=10.0.1.99 python3 audioberry .

HiFiBerry:
GPIO 2
GPIO 3
GPIO 18
GPIO 19
GPIO 20
GPIO 21

Neopixel:
PIN 19 - GPIO 10
PIN 02 - 5V
PIN 06 - GND

Rotary Encoder:
PIN 33 - CLK   GPIO 13
PIN 31 - DT    GPIO 6
PIN 29 - SW    GPIO 5
PIN 02 - 5V
PIN 06 - GND

OLED:
PIN 03 - SDA GPIO 2
PIN 05 - SCL GPIO 3
PIN 02 - 5V
PIN 06 - GND

Button 1:
PIN 12 - GPIO 12
GND

Button 2:
PIN 16 - GPIO 16
GND

Button 3: (Push on Rotary Encoder)
PIN 26 - GPIO 7
GND


"""
from gpiozero import Button, LED, Device
from signal import pause
from gpiozero.pins.mock import MockFactory

# from audioberry.audioPlayer import radio_action
from subprocess import check_call

# Set the default pin factory to a mock factory
Device.pin_factory = MockFactory()

# PIN Layout

button_list = [
    {'pin': 12, 'led': 17, 'id': 'button-1', 'active': False},
    {'pin': 16, 'led': 27, 'id': 'button-2', 'active': False},
    {'pin': 26, 'led': 22, 'id': 'button-3', 'active': False},
]

# LED
# -------------
led1 = LED(17)
led2 = LED(27)
led3 = LED(22)

# leds = [led1, led2, led3, led4]

# BUTTON
# -------------
button1 = Button(12)
button2 = Button(16)
button3 = Button(26)


def action(button_nr):
    print('-- push button')
    button = button_list[button_nr]
    status = button['active']
    # led_pin = button['led']
    # led = LED(led_pin)

    if not status:
        print('-- button - on')
       # led.on()
        button['active'] = True
    #  radio_action(button)
    else:
        button['active'] = False
        print('-- button - off')
        #  radio_action(button)
       # led.off()


# Button Action
def button_action1():
    action(1)


def button_action2():
    action(2)


def button_action3():
    action(3)


def shutdown():
    check_call(['sudo', 'poweroff'])


# Listen for interaction
def run():
    print('start listening for buttons')

   # led1.off()
   # led2.off()
   # led3.off()

    button1.when_pressed = button_action1
    button2.when_pressed = button_action2
    button3.when_pressed = button_action3

    # Keep Script going
    # pause()


# if __name__ == '__main__':
    run()
    pause()
