# YOLO-v3-Object-Detection App
Name: Rishav Kumar
College: IIT Delhi 
Department: Engineering and computational mechanics


This repository has the code for YOLO v3 Object detection web app, and is capable of fast object detection. Input can be given through images.

Install python if you have not installed in your computer
next you need to install flask and open-cv, go to terminal and run the following command
$ pip install flask
$ pip install opencv-python

Now clone the repository

Now you need to download YOLOv3 weights file, which you can download from YOLO official website(https://pjreddie.com/darknet/yolo/)
you need to copy the weights file in same directory


next, go to yolo_detection_images.py and add the absolute path of the cgf and weight files in the function detectObjects
Example: modelConfiguration = r'C:\Users\Lenovo\Desktop\myapp\YOLOv3Object-Detection\cfg\yolov3.cfg'
         modelWeights = r'C:\Users\Lenovo\Desktop\myapp\YOLOv3Object-Detection\yolov3 .weights'

then run ap.py file in cmd
$ python ap.py






