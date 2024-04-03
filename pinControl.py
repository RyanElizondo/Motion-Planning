#!/usr/bin/env python3
import Jetson.GPIO as GPIO

servoPin = 26 #pin 7
motorPin = 6 #pin 8

def pin_setup():
    GPIO.setmode(GPIO.BCM)  #using BCM, find values in src lib numbering
    GPIO.setup(servoPin, GPIO.OUT) #set pin to output
    GPIO.setup(motorPin, GPIO.OUT)
    
    
def pin_clean():
    GPIO.cleanup()
    
    
def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
