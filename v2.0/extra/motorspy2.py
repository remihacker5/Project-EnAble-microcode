from time import sleep
import RPi.GPIO as GPIO
import os
#from random import randint
import random
import serial
import time
z1baudrate = 115200
z1port = '/dev/ttyACM0'

GPIO.setmode(GPIO.BCM)

z1serial = serial.Serial(port=z1port, baudrate=z1baudrate)
z1serial.timeout = 2



IN1 = 6
IN2 = 13
IN3 = 19
IN4 = 26
touch = 3
touch2 = 2

time = 0.001

GPIO.setup(touch, GPIO.IN) # Touch Switch
GPIO.setup(touch2, GPIO.IN) # Touch Swtich 2
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)

GPIO.setup(IN1, False)
GPIO.setup(IN2, False)
GPIO.setup(IN3, False)
GPIO.setup(IN4, False)

# microbit serial


# main program
def main():
    while True:
        size = z1serial.inWaiting()
        data = z1serial.read(size)

        sleep(1)
        if data == b'1':
            while not GPIO.input(touch) and not GPIO.input(touch2):
                print ('touch on');
                left(10);


def Step1():
    GPIO.output(IN4, True)
    sleep (time)
    GPIO.output(IN4, False)

def Step2():
    GPIO.output(IN4, True)
    GPIO.output(IN3, True)
    sleep (time)
    GPIO.output(IN4, False)
    GPIO.output(IN3, False)

def Step3():
    GPIO.output(IN3, True)
    sleep (time)
    GPIO.output(IN3, False)

def Step4():
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    sleep (time)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)

def Step5():
    GPIO.output(IN2, True)
    sleep (time)
    GPIO.output(IN2, False)

def Step6():
    GPIO.output(IN1, True)
    GPIO.output(IN2, True)
    sleep (time)
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)

def Step7():
    GPIO.output(IN1, True)
    sleep (time)
    GPIO.output(IN1, False)

def Step8():
    GPIO.output(IN4, True)
    GPIO.output(IN1, True)
    sleep (time)
    GPIO.output(IN4, False)
    GPIO.output(IN1, False)

# Umdrehung links herum
def left(step):	
	for i in range (step):
		#os.system('clear') # verlangsamt die Bewegung des Motors zu sehr.
		Step1()
		Step2()
		Step3()
		Step4()
		Step5()
		Step6()
		Step7()
		Step8()
		print ("Step left: ",i)

# Umdrehung rechts herum		
def right(step):
	for i in range (step):
		#os.system('clear') # verlangsamt die Bewegung des Motors zu sehr.
		Step8()
		Step7()
		Step6()
		Step5()
		Step4()
		Step3()
		Step2()
		Step1()
		print ("Step right: ",i)




main()

# Copyright © 2023 Jeron Osguthorpe 
