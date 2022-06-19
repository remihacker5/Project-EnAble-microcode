#import
import RPi.GPIO as GPIO
import time


# Define GPIO mapping
touch = 3
touch2 = 2


# Use BCM GPIO numbers
GPIO.setmode(GPIO.BCM) # Use BCM GPIO numbers
GPIO.setup(touch, GPIO.IN) # Touch Switch
GPIO.setup(touch2, GPIO.IN) # Touch Switch 2


# Main touch block
def main():
    while True:
        if GPIO.input(touch):
            print ('touch on');
            time.sleep(2.0) # 2.0 second delay

        if GPIO.input(touch2):
            print ('touch2 on')
            time.sleep(2.0) # 2.0 second delay



if __name__ == '__main__':
    try:
        main()
    finally:
        GPIO.cleanup()
        print ('Done')
# Copyright © 2023 Jeron Osguthorpe 
