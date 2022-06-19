#importing necessary imports#
from time import sleep
import RPi.GPIO as GPIO
import os
import random
import serial
#end of importing necessary imports#

#set GPIO mode#
GPIO.setmode(GPIO.BCM)
#end of set GPIO mode# 

#start of all major variables# 

#import Micro:Bit from serial port#
z1baudrate = 115200
z1port = '/dev/ttyACM0'
z1serial = serial.Serial(port=z1port, baudrate=z1baudrate)
z1serial.timeout = 2
#end of import Micro:Bit form serial port#

# Touch Sensors, 2 to each pin # 
touch1 = 14
touch2 = 15
touch3 = 18 
# End of Touch Sensor Variables #

#motor1variables#
IN1 = 17
IN2 = 27
IN3 = 22
IN4 = 23
#end of motor 1 vairables# 

#motor 2 variables# 
motor2IN1 = 24
motor2IN2 = 16
motor2IN3 = 9
motor2IN4 = 25
#end of motor 2 vaiables# 

#motor 3 variables #
motor3IN1 = 8
motor3IN2 =7
motor3IN3 = 11
motor3IN4 = 5
#end of motor 3 variables#

#motor 4 variables# 
motor4IN1 = 12
motor4IN2 = 16
motor4IN3 = 20
motor4IN4 = 21
#end of motor 4 variables# 

#motor 5 variables# 
motor5IN1 = 6
motor5IN2 = 13
motor5IN3 = 19
motor5IN4 = 26
#end of motor 5 variables#

#end of all major variables# 

time = 0.001

#set up touch sensors # 
GPIO.setup(touch1, GPIO.IN) # Touch Switch
GPIO.setup(touch2, GPIO.IN) # Touch Swtich 2
GPIO.setup(touch3, GPIO.IN) # Touch Switch 3 
#end of set up touch sensors#

#motor 1 setup#
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)
#end of motor1 setup#

#motor 2 setup#
GPIO.setup(motor2IN1,GPIO.OUT)
GPIO.setup(motor2IN2,GPIO.OUT)
GPIO.setup(motor2IN3,GPIO.OUT)
GPIO.setup(motor2IN4,GPIO.OUT)
#end of motor2 setup#

#motor 3 setup#
GPIO.setup(motor3IN1,GPIO.OUT)
GPIO.setup(motor3IN2,GPIO.OUT)
GPIO.setup(motor3IN3,GPIO.OUT)
GPIO.setup(motor3IN4,GPIO.OUT)
#end of motor3 setup#

#motor 4 setup#
GPIO.setup(motor4IN1,GPIO.OUT)
GPIO.setup(motor4IN2,GPIO.OUT)
GPIO.setup(motor4IN3,GPIO.OUT)
GPIO.setup(motor4IN4,GPIO.OUT)
#end of motor4 setup#

#motor 5 setup#
GPIO.setup(motor5IN1,GPIO.OUT)
GPIO.setup(motor5IN2,GPIO.OUT)
GPIO.setup(motor5IN3,GPIO.OUT)
GPIO.setup(motor5IN4,GPIO.OUT)
#end of motor5 setup#

#setup false code numbers#
GPIO.setup(IN1, False)
GPIO.setup(IN2, False)
GPIO.setup(IN3, False)
GPIO.setup(IN4, False)

GPIO.setup(motor2IN1, False)
GPIO.setup(motor2IN2, False)
GPIO.setup(motor2IN3, False)
GPIO.setup(motor2IN4, False)

GPIO.setup(motor3IN1, False)
GPIO.setup(motor3IN2, False)
GPIO.setup(motor3IN3, False)
GPIO.setup(motor3IN4, False)

GPIO.setup(motor4IN1, False)
GPIO.setup(motor4IN2, False)
GPIO.setup(motor4IN3, False)
GPIO.setup(motor4IN4, False)

GPIO.setup(motor5IN1, False)
GPIO.setup(motor5IN2, False)
GPIO.setup(motor5IN3, False)
GPIO.setup(motor5IN4, False)
#end up setup false code numbers#


# main program
def main():
    while True:
        size = z1serial.inWaiting()
        data = z1serial.read(size)

        if data == b'2':
            while not GPIO.input(touch1):
                print ('touch on');
                left(10);

#end of main program#

#MOTOR1 steps#

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

def left(step):	
	for i in range (step):
		Step1()
		Step2()
		Step3()
		Step4()
		Step5()
		Step6()
		Step7()
		Step8()
		print ("Step left: ",i)
	
def right(step):
	for i in range (step):
		Step8()
		Step7()
		Step6()
		Step5()
		Step4()
		Step3()
		Step2()
		Step1()
		print ("Step right: ",i)

# end of motor 1 steps# 

#MOTOR2 steps#

def motor2Step1():
    GPIO.output(motor2IN4, True)
    sleep (time)
    GPIO.output(motor2IN4, False)

def motor2Step2():
    GPIO.output(motor2IN4, True)
    GPIO.output(motor2IN3, True)
    sleep (time)
    GPIO.output(motor2IN4, False)
    GPIO.output(motor2IN3, False)

def motor2Step3():
    GPIO.output(motor2IN3, True)
    sleep (time)
    GPIO.output(motor2IN3, False)

def motor2Step4():
    GPIO.output(motor2IN2, True)
    GPIO.output(motor2IN3, True)
    sleep (time)
    GPIO.output(motor2IN2, False)
    GPIO.output(motor2IN3, False)

def motor2Step5():
    GPIO.output(motor2IN2, True)
    sleep (time)
    GPIO.output(motor2IN2, False)

def motor2Step6():
    GPIO.output(motor2IN1, True)
    GPIO.output(motor2IN2, True)
    sleep (time)
    GPIO.output(motor2IN1, False)
    GPIO.output(motor2IN2, False)

def motor2Step7():
    GPIO.output(motor2IN1, True)
    sleep (time)
    GPIO.output(motor2IN1, False)

def motor2Step8():
    GPIO.output(motor2IN4, True)
    GPIO.output(motor2IN1, True)
    sleep (time)
    GPIO.output(motor2IN4, False)
    GPIO.output(motor2IN1, False)

def motor2left(step): 
    for i in range (step):
        motor2Step1()
        motor2Step2()
        motor2Step3()
        motor2Step4()
        motor2Step5()
        motor2Step6()
        motor2Step7()
        motor2Step8()
        print ("Step left: ",i)
    
def motor2right(step):
    for i in range (step):
        motor2Step8()
        motor2Step7()
        motor2Step6()
        motor2Step5()
        motor2Step4()
        motor2Step3()
        motor2Step2()
        motor2Step1()
        print ("Step right: ",i)

# end of motor 2 steps#

#MOTOR3 steps#

def motor3Step1():
    GPIO.output(motor3IN4, True)
    sleep (time)
    GPIO.output(motor3IN4, False)

def motor3Step2():
    GPIO.output(motor3IN4, True)
    GPIO.output(motor3IN3, True)
    sleep (time)
    GPIO.output(motor3IN4, False)
    GPIO.output(motor3IN3, False)

def motor3Step3():
    GPIO.output(motor3IN3, True)
    sleep (time)
    GPIO.output(motor3IN3, False)

def motor3Step4():
    GPIO.output(motor3IN2, True)
    GPIO.output(motor3IN3, True)
    sleep (time)
    GPIO.output(motor3IN2, False)
    GPIO.output(motor3IN3, False)

def motor3Step5():
    GPIO.output(motor3IN2, True)
    sleep (time)
    GPIO.output(motor3IN2, False)

def motor3Step6():
    GPIO.output(motor3IN1, True)
    GPIO.output(motor3IN2, True)
    sleep (time)
    GPIO.output(motor3IN1, False)
    GPIO.output(motor3IN2, False)

def motor3Step7():
    GPIO.output(motor3IN1, True)
    sleep (time)
    GPIO.output(motor3IN1, False)

def motor3Step8():
    GPIO.output(motor3IN4, True)
    GPIO.output(motor3IN1, True)
    sleep (time)
    GPIO.output(motor3IN4, False)
    GPIO.output(motor3IN1, False)

def motor3left(step): 
    for i in range (step):
        motor3Step1()
        motor3Step2()
        motor3Step3()
        motor3Step4()
        motor3Step5()
        motor3Step6()
        motor3Step7()
        motor3Step8()
        print ("Step left: ",i)
    
def motor3right(step):
    for i in range (step):
        motor3Step8()
        motor3Step7()
        motor3Step6()
        motor3Step5()
        motor3Step4()
        motor3Step3()
        motor3Step2()
        motor3Step1()
        print ("Step right: ",i)

# end of motor 3 steps#

#MOTOR4 steps#

def motor4Step1():
    GPIO.output(motor4IN4, True)
    sleep (time)
    GPIO.output(motor4IN4, False)

def motor4Step2():
    GPIO.output(motor4IN4, True)
    GPIO.output(motor4IN3, True)
    sleep (time)
    GPIO.output(motor4IN4, False)
    GPIO.output(motor4IN3, False)

def motor4Step3():
    GPIO.output(motor4IN3, True)
    sleep (time)
    GPIO.output(motor4IN3, False)

def motor4Step4():
    GPIO.output(motor4IN2, True)
    GPIO.output(motor4IN3, True)
    sleep (time)
    GPIO.output(motor4IN2, False)
    GPIO.output(motor4IN3, False)

def motor4Step5():
    GPIO.output(motor4IN2, True)
    sleep (time)
    GPIO.output(motor4IN2, False)

def motor4Step6():
    GPIO.output(motor4IN1, True)
    GPIO.output(motor4IN2, True)
    sleep (time)
    GPIO.output(motor4IN1, False)
    GPIO.output(motor4IN2, False)

def motor4Step7():
    GPIO.output(motor4IN1, True)
    sleep (time)
    GPIO.output(motor4IN1, False)

def motor4Step8():
    GPIO.output(motor4IN4, True)
    GPIO.output(motor4IN1, True)
    sleep (time)
    GPIO.output(motor4IN4, False)
    GPIO.output(motor4IN1, False)

def motor4left(step): 
    for i in range (step):
        motor4Step1()
        motor4Step2()
        motor4Step3()
        motor4Step4()
        motor4Step5()
        motor4Step6()
        motor4Step7()
        motor4Step8()
        print ("Step left: ",i)
    
def motor4right(step):
    for i in range (step):
        motor4Step8()
        motor4Step7()
        motor4Step6()
        motor4Step5()
        motor4Step4()
        motor4Step3()
        motor4Step2()
        motor4Step1()
        print ("Step right: ",i)

# end of motor 4 steps# 

#MOTOR5 steps#

def motor5Step1():
    GPIO.output(motor5IN4, True)
    sleep (time)
    GPIO.output(motor5IN4, False)

def motor5Step2():
    GPIO.output(motor5IN4, True)
    GPIO.output(motor5IN3, True)
    sleep (time)
    GPIO.output(motor5IN4, False)
    GPIO.output(motor5IN3, False)

def motor5Step3():
    GPIO.output(motor5IN3, True)
    sleep (time)
    GPIO.output(motor5IN3, False)

def motor5Step4():
    GPIO.output(motor5IN2, True)
    GPIO.output(motor5IN3, True)
    sleep (time)
    GPIO.output(motor5IN2, False)
    GPIO.output(motor5IN3, False)

def motor5Step5():
    GPIO.output(motor5IN2, True)
    sleep (time)
    GPIO.output(motor5IN2, False)

def motor5Step6():
    GPIO.output(motor5IN1, True)
    GPIO.output(motor5IN2, True)
    sleep (time)
    GPIO.output(motor5IN1, False)
    GPIO.output(motor5IN2, False)

def motor5Step7():
    GPIO.output(motor5IN1, True)
    sleep (time)
    GPIO.output(motor5IN1, False)

def motor5Step8():
    GPIO.output(motor5IN4, True)
    GPIO.output(motor5IN1, True)
    sleep (time)
    GPIO.output(motor5IN4, False)
    GPIO.output(motor5IN1, False)

def motor5left(step): 
    for i in range (step):
        motor5Step1()
        motor5Step2()
        motor5Step3()
        motor5Step4()
        motor5Step5()
        motor5Step6()
        motor5Step7()
        motor5Step8()
        print ("Step left: ",i)
    
def motor5right(step):
    for i in range (step):
        motor5Step8()
        motor5Step7()
        motor5Step6()
        motor5Step5()
        motor5Step4()
        motor5Step3()
        motor5Step2()
        motor5Step1()
        print ("Step right: ",i)

# end of motor 5 steps# 



main()

# Copyright © 2023 Jeron Osguthorpe 
