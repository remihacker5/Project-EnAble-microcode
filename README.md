# 2021-2022-Science-Fair-Project
This is my 2021-2022 Science Fair Project  made by Jeron O (codered) and Remington A (remihacker5)

This project is for both the SUU SUCCESS Academy Cedar City Utah Science Fair and for the SUU Sience and Engeneering Fair 
This project is only be used by seletive people from written permission from Jeron O (jeronosg@outlook.com). This project
is made by Jeron O (CodeRed) and Remington A (RemiHacker5). 

All changes made by people with permission place them in the change logs below so we can keep track of them for the Science Fair
Please keep track of all materials in the materials list 

-- MATERIALS -- 
Raspberry Pi 3B+
Raspbbery Pi Pico
Micro:bit 
10x - TTP223 Touch Sensor Module 
5x - Stepper Motors (serial number soon) (with driver boards) 
Full Size Breadboard
Tiny Breadboard 
Male to Male Wires,Male to Female Wires, Female to Female Wires
5+x 9V Batteries and Voltimeter
32gb ONN MircoSD Card
Raspbian (Raspberry Pi Os) Linux Operating System
16 GB ONN Flash Drive
Dell Laptop (search up purposes) Latitude E745
Basic Computer Accessories (mouse, keyboard, monitor, ect) 


--- CHANGE LOGS --- 
8.30.21 -- 
index.py is created to test the touch sensors. The touch sensors were purchased off of Amazon for 10 of them for about $8. The serial number for the sensors is TTP223 Sensor Module. The sensor module successfully works with the Raspbery Pi 3B+ 

8.31.21 - Part A: 
motors.py, microbit.py, motorspy2.py files were all crated to test certain funciton (look in directory). Remington came over to help program the sensors and the motors. Before he came over, I got all the sensors working and got it so that if the sensor goes off the motors move. We changed it with the help of Rem to make it so that it is now when the sensor is pressed the motor stops. All of this  is contained in motorspy2.py. We are trying to make it so that and "or" statement inside a while statement works. 

9.1.21
motorspy2.py alteration. Fixed the problem with getting both the sensors to stop the motor. Did this by changing it form an "or" statement to an "and" statement. For some reason, this works.

9.2.21 
Today we had science research because it is a Thurday. I realized in class that I only have 26 avaiable pins for the sensors and the motors at the same time. So I decided to put two sensors into one pin becasue as long as it can send an imput to the raspberry pi, it should work. I have decided that I am just going to stick with the Raspberry Pi an the Micro:bit because I really don't want to have to convert everything from Python into Micro:Python becasue honestly that is just a pain. Everthing has been assigned its new pins and they are all contained inside of the new file that I made. 
