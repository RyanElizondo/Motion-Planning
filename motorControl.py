#!/usr/bin/env python3
import Jetson.GPIO as GPIO
import time
from pinControl import motorPin, map_range

# Definitions
frequency = 50 #in hertz (1k to 16k?)
pulseMin = 725 #in microseconds
pulseMax = 2125 #in microseconds
speedMin = -100 #in degrees
speedMax = 100 #in degrees
period = 1.0/frequency
MAX_ITERATIONS = 1 #depends on hardware
ITERATION_DELAY = 0

def motor_control(speed):
    
    if(speed < speedMin): #keep input in range
        speed = speedMin
    elif (speed > speedMax):
        speed = speedMax
        
    print("speed: " + str(speed))
    pulse = map_range(speed, speedMin, speedMax, pulseMin, pulseMax) / 1000000.0 #convert to seconds
    
    for i in range(0, MAX_ITERATIONS): #setting it, may take multiple pulses, with delays in between, need to test on hardware
        GPIO.output(motorPin, GPIO.HIGH)
        time.sleep(pulse)
        GPIO.output(motorPin, GPIO.LOW)
        time.sleep(period - pulse)
        time.sleep(ITERATION_DELAY)
