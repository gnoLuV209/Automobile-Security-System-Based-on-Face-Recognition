# Automobile-Security-System-Based-on-Face-Recognition
Design and Simulate The Automobile Security System Based On Face Recognition

This is a personal project. Now i'll guide you how to create the model and run the code

STEP 1 : You need to prepare some electronic components
+ Two Microcontroller Arduino Uno, one for receiving data from Small single-board computers Raspberry Pi or your personal computer and control motor stater, one for trasmitting signal from crankshaft position sensor 
+ One Motor 
+ One Small single-board computers Raspberry Pi with Module Camera Mini Raspberry "or" your personal computer with computer's webcam for road marking recognition
+ One Encoder V1 speed sensor circuit for steering wheel simulation

STEP 2 : Download some sofware for this project
+ Download the Arduino IDE sofware for uploading source code to the microcontroller
+ Download the Anaconda sofware for create working environment Anaconda python
+ Download the Pycharm sofware for image processing by computer vision
+ Open Command Prompt to install some package for python: type command: pip install cmake, type command: conda install-c menpo opencv, type command: pip install face_recognition, type command: pip install pyserial

STEP 3 : Design model with all components prepared at STEP 1, you can see file "Circuit Diagram with L298.png" and "DesignModel.png" for designing models

STEP 4 : Run the source code and watch the result  
+ Open Arduino IDE software and copy code in file "Control_Motor_Stater.ino" to your first Arduino IDE program, copy code in file "Control_Bobin.ino" to your second Arduino IDE program
+ Connect to your computer and select board, here you'll chose Arduino Uno and click "upload" for loading into the microcontroller
+ Put all files with .py extension in the same folder and create a folder named Owner in it 
+ First run file "collect_data.py .py" and press space button for collecting owner's data 
+ Second run file "train_model.py" for computer training 
+ Finally, run file "main.py " to see the result

