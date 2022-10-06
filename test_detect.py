import detection
import torch
import subprocess

print(f"Setup complete. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")
p = subprocess.getstatusoutput("python detect.py --weights best_6223.pt --img 640 --conf 0.75 --source ./imagezmq_images/image2.jpg") 
output = p[1]
with open('outputs/output_dummy.txt', 'w') as f:    # path to output .txt file
    f.write(output)
'''
message_dict = detection.process_output(path = "outputs/output_dummy.txt")

print(message_dict)

if detection.highest_conf(message_dict):
    message=detection.highest_conf(message_dict)[1]
else:
    message=100



message = str(message)
print("message = ", message)
'''
