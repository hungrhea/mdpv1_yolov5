# from curses import keyname
import cv2
import imagezmq
import socket
import detection
import sys

import torch
import subprocess

from stitchImages import increment_path, start_stitch, clear_runs_rawCaptures, saveImages

# reset image folders
#saveImages()
clear_runs_rawCaptures()

image_hub = imagezmq.ImageHub()
print("Image server started")

while True:
    rpi_name, image = image_hub.recv_image()
    print("received")

    # change path to wherever imagezmq_images is + \image.jpg
    output_dir = r'C:\Users\ASUS\Documents\GitHub\mdpv1_yolov5\imagezmq_images\image.jpg' 
    #output_dir = increment_path(path=r'C:\Users\ASUS\Documents\GitHub\mdpv1_yolov5\imagezmq_images\image.jpg')

    cv2.imwrite(output_dir, image)
    print("Receiving image, sending to image processing...")
    
    print(f"Setup complete. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")
    p = subprocess.getstatusoutput("python detect.py --weights best_task2_v2.pt --img 416 --conf 0.72 --source ./imagezmq_images") 
    output = p[1]
    with open('outputs/output.txt', 'w') as f:    # path to output .txt file
     f.write(output)
    message_dict = detection.process_output(path = "outputs/output.txt")
        
    if detection.biggest_area(message_dict):
        message=detection.biggest_area(message_dict)[1]
    else:
        message=100

    message = str(message)
    print("message = ", message)
    message = message.encode('utf-8')
    image_hub.send_reply(message)
    print(rpi_name)
    if rpi_name == "end":
        print("end")
        break

print("start stitch")
start_stitch()

     



