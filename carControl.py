#!/usr/bin/env python3
import keyboard
from servoControl import servo_control
from motorControl import motor_control
from pinControl import pin_setup, pin_clean
import time
import math


pin_setup()

#while True:  #polling; ctrl+C to stop


   # try:  # used try so that if user pressed other than the given key error will not be shown
       # if keyboard.is_pressed('w'): 
        #    motor_control(100)
      #  elif keyboard.is_pressed('s'):
       #     motor_control(-100)
      #  elif keyboard.is_pressed('a'):
        #    servo_control(-100)
       # elif keyboard.is_pressed('d'):
        #    servo_control(100)
        
    #except:

#define the front of the car and the back of the car from the image 
#use the front of the car to determine the distance from the car to the parking spot



class parkingAssistant: 
    def init(self, carFrontX, carFrontY): #initialize the front of the car
        self.carFrontX = carFrontX
        self.carFrontY = carFrontY

    def distanceToParkingSpot(self, parkingSpotX, parkingSpotY): #distance from the front of the car to the parking spot
        return math.sqrt((parkingSpotX - self.carFrontX)**2 + (parkingSpotY - self.carFrontY)**2) #distance formula / radius of path

    def turnToFace(self, parkingSpotX, parkingSpotY): #angle towards the parking spot
        angle = math.atan2(parkingSpotY - self.carFrontY, parkingSpotX - self.carFrontX) #angle in radians
        return angle


#image resolution
imageWidth = 320
imageHeight = 240

#Sample XY coordinates for the front of the car 
carFrontX = 160
carFrontY = 120

#Sample XY coordinates for the parking spot
parkingSpotX = 200
parkingSpotY = 100

#initialize the parking assistant
parkingAssistant  = parkingAssistant(carFrontX, carFrontY)

#parking spot detection boolean 
parkingSpotDetected = True

while not parkingSpotDetected:
    servo_control(0)
    motor_control(25)#move the car forward
    if parkingSpotDetected:
        motor_control(0) #stop the car

        #1st path of perpendicular parking

        #Calculate the distance and angle to the parking spot
        distance = parkingAssistant.distanceToParkingSpot(parkingSpotX, parkingSpotY)
        angle = parkingAssistant.turnToFace(parkingSpotX, parkingSpotY)
        angleDegrees = math.degrees(angle)
        servo_control(angleDegrees)#turn the car to complete first path of perpendicular parking
        motor_control(25)
        time.sleep(distance/25) #move the car forward for the duration based on the distance
        motor_control(0) 

        #2nd path of perpendicular parking (backing in)

        #sample of new car frontend coordinates
        carFrontX = 200
        carFrontY = 100

        #initialize the parking assistant with the new coordinates
        parkingAssistant = parkingAssistant(carFrontX, carFrontY)

        #calculate the distance and angle to the parking spot for the second path
        distance = parkingAssistant.distanceToParkingSpot(parkingSpotX, parkingSpotY)
        angle = parkingAssistant.turnToFace(parkingSpotX, parkingSpotY)
        angleDegrees = math.degrees(angle)
        servo_control(angleDegrees)
        motor_control(-25)
        time.sleep(distance/25)
        servo_control(0)
        motor_control(-10)
        time.sleep(5)
        motor_control(0)
        break

pin_clean()

        





