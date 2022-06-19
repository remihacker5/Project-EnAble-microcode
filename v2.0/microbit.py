import serial
import time
z1baudrate = 115200
z1port = '/dev/ttyACM0'

z1serial = serial.Serial(port=z1port, baudrate=z1baudrate)
z1serial.timeout = 2

print (z1serial.is_open)
if z1serial.is_open == True:
    while True:
        size = z1serial.inWaiting()
        if size:
            data = z1serial.read(size)
            print (data)
        else:
            print ("no data")
        time.sleep(1)
else:
    print("z1serial not open")

# Copyright © 2023 Jeron Osguthorpe 
