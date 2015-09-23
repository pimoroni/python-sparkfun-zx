#!/usr/bin/env python

import RPi.GPIO as GPIO
import zx
import time

LED_RED    = 22
LED_YELLOW = 23
LED_GREEN  = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)

print("""
This example will recognise left/right swipes
and toggle GPIO pin 22 on and off.

You should also see the gesture names printed
as they are recognised.
""")

while True:
    if  zx.gesture_available():
        gesture = zx.get_gesture()
        gesture_name = zx.gesture_name(gesture)
        speed = zx.get_speed()
        print("Gesture: {} {}: {}".format(gesture, speed, gesture_name))
        if gesture == zx.SWIPE_LEFT:
            GPIO.output(LED_RED, GPIO.HIGH)
        if gesture == zx.SWIPE_RIGHT:
            GPIO.output(LED_RED, GPIO.LOW)

    time.sleep(0.01)
