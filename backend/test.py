from os import name
from os.path import exists
import cv2 
import numpy as np

directory = "Siskiyou_mask/"
filename = "SiskiyouCA_"
final_directory1 = "Siskiyou_deforest_final/"
filenames = []

def detect_change(im1,im2):
    image1_path = directory+im1
    image2_path = directory+im2
    final_directory2 = final_directory1+im1+"_"+im2+"_"
    image1 = cv2.imread(image1_path,0)
    new_size = np.asarray(image1.shape) /5
    new_size = new_size.astype(int) *5
    image1 = cv2.resize(image1, (new_size[0],new_size[1])).astype(int)
    cv2.imshow("qwe",image1)
    cv2.waitKey(0)

for i in range(10,21):
    file_exists = exists(directory+filename+str(i)+".png")
    if(file_exists):
        filenames.append(filename+str(i)+".png")

for i in range(len(filenames)-1):
    detect_change(filenames[i],filenames[i+1])