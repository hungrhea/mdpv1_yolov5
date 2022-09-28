import cv2
import os
import detect

def conversion(labelName):
    print(labelName)

    # Convert the alphabetical name into the encoded answer on the MDP Slides
    if labelName == "White Arrow Up":
        return "36"

    elif labelName == "Red Arrow Down":
        return "37"

    elif labelName == "Green Right Arrow":
        return "38"

    elif labelName == "Blue Left Arrow":
        return "39"

    elif labelName == "Yellow Circle":
        return "40"

    elif labelName == "White 1":
        return "11"

    elif labelName == "Green 2":
        return "12"

    elif labelName == "Blue 3":
        return "13"

    elif labelName == "Red 4":
        return "14"

    elif labelName == "Yellow 5":
        return "15"

    elif labelName == "White 6":
        return "16"

    elif labelName == "Green 7":
        return "17"

    elif labelName == "Blue 8":
        return "18"

    elif labelName == "Red 9":
        return "19"

    elif labelName == "Yellow A":
        return "20"

    elif labelName == "White B":
        return "21"

    elif labelName == "Green C":
        return "22"

    elif labelName == "Blue D":
        return "23"

    elif labelName == "Red E":
        return "24"

    elif labelName == "Yellow F":
        return "25"

    elif labelName == "White G":
        return "26"

    elif labelName == "Green H":
        return "27"

    elif labelName == "Blue S":
        return "28"

    elif labelName == "Red T":
        return "29"

    elif labelName == "Yellow U":
        return "30"

    elif labelName == "White V":
        return "31"

    elif labelName == "Green W":
        return "32"

    elif labelName == "Blue X":
        return "33"

    elif labelName == "Red Y":
        return "34"

    elif labelName == "Yellow Z":
        return "35"
    # pending bullseye
    elif labelName == "White Bullseye":
        return "XXX"
def get_latest_image(dirpath, valid_extensions=('jpg','jpeg','png')):
    """
    Get the latest image file in the given directory
    """
    valid_files = [os.path.join(dirpath, filename) for filename in os.listdir(dirpath)]
    # Filter out directories, no-extension, and wrong extension files
    valid_files = [f for f in valid_files if '.' in f and \
        f.rsplit('.',1)[-1] in valid_extensions and os.path.isfile(f)]

    if not valid_files:
        raise ValueError("No valid images in %s" % dirpath)

    return max(valid_files, key=os.path.getmtime)

def detect_image():
    print("Testing YOLOv5...")
    #output_dir = r'C:\Users\tengwei\Desktop\image\image.jpg'
    # results_dir = r'C:\Users\tengwei\Desktop'
    input_dir = os.path.join('image.jpg')
    picture = get_latest_image(dirpath=r'C:\Users\ASUS\Desktop\mdp\mdpv1_yolov5\images', valid_extensions=('jpg', 'jpeg', 'png'))
    cv2.imwrite(input_dir, picture)
    print("Sending to image detection...")

    # Parse the .png file into the YOLOv5 model
    results_dir = os.path.join('runs', 'results')
    return detect.run(weights='best_80.pt',
                      source=input_dir,
                      imgsz=(640,640),
                      conf_thres=0.25,
                      iou_thres=0.25,
                      max_det=1,
                      device='',
                      view_img=False,  # show results
                      save_txt=False,  # save results to *.txt
                      save_conf=False,  # save confidences in --save-txt labels
                      save_crop=False,  # save cropped prediction boxes
                      nosave=False,  # do not save images/videos
                      classes=None,  # filter by class: --class 0, or --class 0 2 3
                      agnostic_nms=False,  # class-agnostic NMS
                      augment=False,  # augmented inference
                      visualize=False,  # visualize features
                      update=False,  # update all models
                      project=results_dir,  # save results to project/name
                      exist_ok=False,  # existing project/name ok, do not increment
                      line_thickness=3,  # bounding box thickness (pixels)
                      hide_labels=False,  # hide labels
                      hide_conf=False,  # hide confidences
                      half=False,   # use FP16 half-precision inference
                      )
def main():
    #image = get_latest_image(dirpath=r'C:\Users\tengwei\Desktop\image', valid_extensions=('jpg', 'jpeg', 'png'))
    # Read the image file as a numpy array
    #picture = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    #print("")
    #print("Sending to image conversion, RGB to Grayscale...")

    #return preprocessingImg.rgbToGray(picture)
    result = detect_image()
    print("result: ", result)
    return result
    
if __name__ == "__main__":
    main()