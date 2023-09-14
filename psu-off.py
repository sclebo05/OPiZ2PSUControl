#!/usr/bin/python3

# needs the Python3 version of OPI.GPIO  https://github.com/NadavK/OPI.GPIO
# on Debian, had to install python3-dev
# Pins identified in physical order.  e.g. "5" is 5th when counting the left header.

import OPi.GPIO as GPIO
from time import sleep          # this lets us have a time delay

PIN = 3
GPIO.setboard(GPIO.H616)
GPIO.setmode(GPIO.BOARD)        # set up BOARD BCM numbering
GPIO.setup(PIN, GPIO.OUT)         # configure PIN

print ("Powering Off...")
GPIO.output(PIN, 0)       # set port/pin value to 1/HIGH/True
sleep(1)

print ("Done.")
