#clone YOLOv5 and 
'''pip install -qr requirements.txt
!git clone https://github.com/ultralytics/yolov5  # clone repo
%cd yolov5
%pip install -qr requirements.txt # install dependencies
'''

import torch
import subprocess
import json
import numpy as np
'''
print(f"Setup complete. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")

p = subprocess.getstatusoutput("python detect.py --weights best_v3.pt --img 640 --conf 0.6 --source ./imagezmq_images") 
output = p[1]

with open('outputs/output.txt', 'w') as f:    # path to output .txt file
  f.write(output)
'''

def process_output(path = None, string = None, area_limit = 3600):
  if path==None and string==None:
    print('No output specified for processing.')
    return
  elif path!=None and string!=None:
    print('Multiple outputs specified for processing.')
    return
  elif path!=None:
    f = open(path, 'r')
    # split each line into a string, all in 1 list
    raw = f.read().split('\n')
  else:
    raw = string.split('\n')
  
  #a list of only strings of image lines in output
  raw = [line for line in raw if (line[:5]=="image")]
  output = {}
  for line in raw:
    # determine image file type
    if ".jpg" in line:
      name_tail = ".jpg:"
    elif ".jpeg" in line:
      name_tail = ".jpeg:"
    elif ".png" in line:
      name_tail = ".png:"
      
    #split the line into words
    line_split = line.split()
    name = [i for i in line_split if i.endswith(name_tail)][0]
    name = name[:-1] #remove : from image name
    # no classes detected
    #last word
    if line_split[-1] == "None":
      detections = None
    # classes detected
    else:
      # from aft 640x480 to before speed
      raw_results = line_split[line_split.index("1280x1280")+1:]
      # check if everything is there
      assert(len(raw_results) % 6 == 0)
      # segment raw_results
      num = int(len(raw_results) / 6)
      classes = raw_results[:num]
      confidences = raw_results[num:int(num*2)]
      coordinates = np.array_split(raw_results[int(num*2):], num)
      '''
      #no. of classes detected in the pic
      class_num = [int(i) for i in raw_classes if not i.endswith(',')]
      #remove ',' only int
      #classes detected in 1 pic
      classes = [int(''.join(filter(str.isdigit, i))) for i in raw_classes if i.endswith(',')]
      classes_with_duplicates = []
      for i in range(len(classes)):
        for dup in range(class_num[i]):
          classes_with_duplicates.append(classes[i])
      detections = []
      assert(len(classes_with_duplicates) == len(confidences))
      for i in range(len(confidences)):
        #added
        detections.append([classes_with_duplicates[i], float(confidences[i])])
      '''
      detections = []
      for i in range(len(classes)):
        if int(classes[i]) != 10:
          # check bounding box area
          width = abs(float(coordinates[i][0]) - float(coordinates[i][2]))
          height = abs(float(coordinates[i][1]) - float(coordinates[i][3]))
          area = width * height
          if area > area_limit:
            # append [class, confidence, bounding box area]
            detections.append([int(classes[i]), float(confidences[i]), area])
      if len(detections) == 0:
        detections = None
    output[name] = detections
  # return output
  if len(output) != 0:
    return output
  else:
    return None

  # return detected_classes

# print(process_output(path = "outputs/output_test.txt"))
# print(json.dumps(process_output(path = "outputs/output_test.txt"), indent=4))    # path to output .txt file






# returns tuple (image_name, detected_class)
def highest_conf(message_dict):
  if message_dict:
    keys = message_dict.keys()
    # initialise image_name, detected_class and max_conf
    detected_class = None
    for key in keys:
      if message_dict[key]:
        max_conf = message_dict[key][0][1]
        image_name = key
        detected_class = message_dict[key][0][0]
    # no images contain a detection
    if detected_class == None:
      print("No detections found in images")
      return None

    for key in keys:
      if message_dict[key]:
        for detection in message_dict[key]:
          if detection[1] > max_conf:
            max_conf = detection[1]
            image_name = key
            detected_class = detection[0]
    
    return (image_name, detected_class)
  print("No images in detection")
  return None




# returns tuple (image_name, detected_class)
def biggest_area(message_dict):
  if message_dict:
    keys = message_dict.keys()
    # initialise image_name, detected_class and max_area
    detected_class = None
    for key in keys:
      if message_dict[key]:
        max_area = message_dict[key][0][2]
        image_name = key
        detected_class = message_dict[key][0][0]
    # no images contain a detection
    if detected_class == None:
      print("No detections found in images")
      return None

    for key in keys:
      if message_dict[key]:
        for detection in message_dict[key]:
          if detection[2] > max_area:
            max_area = detection[2]
            image_name = key
            detected_class = detection[0]
    
    return (image_name, detected_class)
  print("No images in detection")
  return None


