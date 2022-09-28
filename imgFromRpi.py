import time
import cv2
import imagezmq
import socket
# import receivingImgFromRpi
import sys
import io
# from imutils.video import VideoStream
from picamera import PiCamera

print('Server connection establishing with Image Server')
global sender
global rpi_name
sender = imagezmq.ImageSender(connect_to='tcp://192.168.1.11:5555')
rpi_name = socket.gethostname()
print('Connection established with Image Server')

# picam = VideoStream().start()
# time.sleep(2)

# TESTING WITH PICAMERA CAPTURE INSTEAD OF VideoStream()
picam = PiCamera()
# picam.start_preview()
# time.sleep(10)
# picam.stop_preview()
picam.resolution = (640, 480)
# output = PiRGBArray(picam)
picam.capture('/home/pi/Desktop/image.jpg')
image = io.open("image.jpg",'rb')
# image = io.open("images/sierra.jpg",'rb')

image = picam.read()
print("image read")
sender.send_image(rpi_name, image)
print("image sent")
picam.stop()