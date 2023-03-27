import cv2
import matplotlib.pyplot as plt

config_file = 'C:\xampp\htdocs\practice\Python\python100dayscode\projects\object_detection\ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'

frozen_model = 'C:\xampp\htdocs\practice\Python\python100dayscode\projects\object_detection\frozen_inference_graph.pb'

model = cv2.dnn_DetectionModel(frozen_model, config_file)

class_Labels = []
file_name = 'C:\xampp\htdocs\practice\Python\python100dayscode\projects\object_detection\labels.txt'

with open(file_name,'rt') as fpt:
     class_Labels = fpt.read().rstrip('\n').split('\n')
    
print(class_Labels)
print(len(class_Labels))

model.setInputSize(320,320)
model.setInputScale(1.0/127.5)
model.setInputMean(127.5,127.5,127.5)
model.setInputSwapRB(True)
