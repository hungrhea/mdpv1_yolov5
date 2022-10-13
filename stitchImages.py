from imutils import paths
from PIL import Image
import shutil
import os

def stitching():
  print("stitching...")
  # replace with raw captures directory (under stitchedImages)
  image_folder = r'C:\Users\ASUS\Documents\GitHub\mdpv1_yolov5\stitchedImages\rawCaptures'
  imagePaths = list(paths.list_images(image_folder))
  images = [Image.open(x) for x in imagePaths]
  widths, heights = zip(*(i.size for i in images))

  total_width = sum(widths)
  max_height = max(heights)

  new_im = Image.new('RGB', (total_width, max_height))

  x_offset = 0
  for im in images:
    new_im.paste(im, (x_offset,0))
    x_offset += im.size[0]

  new_im.save('stitchedImages/stitchedOutput.png', format='png')
  print("stitched all")

def copyCapture():
  print("copying captures...")
  # movdir should be the \runs\detect directory
  movdir = r"C:\Users\ASUS\Documents\GitHub\mdpv1_yolov5\runs\detect"
  #basedir should be the \stitchedImages\rawCaptures directory
  basedir = r"C:\Users\ASUS\Documents\GitHub\mdpv1_yolov5\stitchedImages\rawCaptures"

  # Walk through all files in the directory that contains the files to copy
  ii = 2
  for root, dirs, files in os.walk(movdir):
      for filename in files:
          # absolute path
          old_name = os.path.join( os.path.abspath(root), filename )
          #C:\Users\ASUS\Documents\GitHub\mdpv1_yolov5\runs\detect\exp\image.jpg

          # Separate base from extension
          base, extension = os.path.splitext(filename)

          # Initial new name
          new_name = os.path.join(basedir, filename)
          #C:\Users\ASUS\Documents\GitHub\mdpv1_yolov5\stitchedImages\rawCaptures\image.jpg

          # If folder basedir/base does not exist
          if not os.path.exists(basedir):
              print (basedir, "not found" )
              continue    # Next filename
          elif not os.path.exists(new_name):  # folder exists, file does not, just copy in
              shutil.copy(old_name, new_name)
              print ("Copied", old_name, "as", new_name)
          else:  # folder exists, file exists as well
              while True:
                  new_name = os.path.join(basedir, base + "_" + str(ii) + extension)
                  if not os.path.exists(new_name):
                    shutil.copy(old_name, new_name)
                    print ("Copied", old_name, "as", new_name)
                    break 
              ii += 1
  print("copied all")

def clearFolder(folder):
  for filename in os.listdir(folder):
      file_path = os.path.join(folder, filename)
      try:
          if os.path.isfile(file_path) or os.path.islink(file_path):
              os.unlink(file_path)
          elif os.path.isdir(file_path):
              shutil.rmtree(file_path)
      except Exception as e:
          print('Failed to delete %s. Reason: %s' % (file_path, e))

def start_stitch():
  copyCapture()
  stitching()

#clear runs\detect and stitchedImages\rawCaptures
def clear_runs_rawCaptures():
  clearFolder(r'C:\Users\ASUS\Documents\GitHub\mdpv1_yolov5\stitchedImages\rawCaptures')
  clearFolder(r'C:\Users\ASUS\Documents\GitHub\mdpv1_yolov5\runs\detect')

#below 2 wont rlly be used, can just use the function above to clear both folders
def clear_rawCaptures():
  clearFolder(r'C:\Users\ASUS\Documents\GitHub\mdpv1_yolov5\stitchedImages\rawCaptures')

def clear_runs():
  clearFolder(r'C:\Users\ASUS\Documents\GitHub\mdpv1_yolov5\runs\detect')

def saveImages():
  print("saving images...")
  # movdir should be the \runs\detect directory
  movdir = r"C:\Users\ASUS\Documents\GitHub\mdpv1_yolov5\runs\detect"
  #basedir should be the \stitchedImages\rawCaptures directory
  basedir = r"C:\Users\ASUS\Desktop\mdp photos\SAVED_PICS"

  # Walk through all files in the directory that contains the files to copy
  ii = 2
  for root, dirs, files in os.walk(movdir):
      for filename in files:
          # absolute path
          old_name = os.path.join( os.path.abspath(root), filename )
          #C:\Users\ASUS\Documents\GitHub\mdpv1_yolov5\runs\detect\exp\image.jpg

          # Separate base from extension
          base, extension = os.path.splitext(filename)

          # Initial new name
          new_name = os.path.join(basedir, filename)
          #C:\Users\ASUS\Documents\GitHub\mdpv1_yolov5\stitchedImages\rawCaptures\image.jpg

          # If folder basedir/base does not exist
          if not os.path.exists(basedir):
              print (basedir, "not found" )
              continue    # Next filename
          elif not os.path.exists(new_name):  # folder exists, file does not, just copy in
              shutil.copy(old_name, new_name)
              print ("Copied", old_name, "as", new_name)
          else:  # folder exists, file exists as well
              while True:
                  new_name = os.path.join(basedir, base + "_" + str(ii) + extension)
                  if not os.path.exists(new_name):
                    shutil.copy(old_name, new_name)
                    print ("Copied", old_name, "as", new_name)
                    break 
              ii += 1
  print("saved images")


# raw version of increment_path
from pathlib import Path
import os

def increment_path(
    path,             # path to increment (eg. "runs/detect/exp", "images/stitched.jpg")
    exist_ok=False,   # existing project/name ok, do not increment
    sep='',           # (eg. "runs/detect/exp{sep}2", "images/stitched{sep}2.jpg")
    mkdir=False,      # create a new directory at the new incremented path
    return_path=False # returns type filename instead of type string
):
    # Increment file or directory path, i.e. runs/exp --> runs/exp{sep}2, runs/exp{sep}3, ... etc.
    path = Path(path)  # os-agnostic
    if path.exists() and not exist_ok:
        path, suffix = (path.with_suffix(''), path.suffix) if path.is_file() else (path, '')

        for n in range(2, 9999):
            p = f'{path}{sep}{n}{suffix}'  # increment path
            if not os.path.exists(p):  #
                break
        path = Path(p)

    if mkdir:
        path.mkdir(parents=True, exist_ok=True)  # make directory
    
    if return_path:
      print("returning path directory: " , path)
      return path
    else:
      print("returning path string: " , path)
      return str(path)


