from os import name
from os.path import exists
from PIL import Image

import cv2
import numpy as np
import skimage.morphology


directory = "Humboldt_cropped/"
filename = "HumboldtCA_"
final_directory = "Humboldt_mask/"

for i in range(11,21):
    file_exists = exists(directory+filename+str(i)+".png")
    if(not file_exists):
        print((directory+filename+str(i)+".png")+" does not exist")
        continue
    img = cv2.imread(directory+filename+str(i)+".png")
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (33, 23, 23), (110, 255,255))
    kernel1 = skimage.morphology.disk(0.5)
    kernel2 = skimage.morphology.disk(3)
    CloseMap = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel1)
    OpenMap = cv2.morphologyEx(CloseMap, cv2.MORPH_OPEN, kernel2)
    OpenMap_copy = img.copy()

    # cv2.imshow("werw",OpenMap_copy)
    # cv2.waitKey(0)
    cv2.imwrite(final_directory+filename+str(i)+".png", OpenMap)