# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# img = cv2.imread('a.jpg')   # you can read in images with opencv
# img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# sensitivity  = 100
# hsv_color1 = np.asarray((36, 25, 25))   # white!
# hsv_color2 = np.asarray([70, 255,255])
#    # yellow! note the order

# mask = cv2.inRange(img_hsv, hsv_color1, hsv_color2)

# plt.imshow(mask)   # this colormap will display in black / white
# plt.show()

import cv2
import numpy as np
import skimage.morphology

## Read
img = cv2.imread("deron/Clarke/ClarkeAL_15.png")

## convert to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

## mask of green (36,25,25) ~ (86, 255,255)
# mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
mask = cv2.inRange(hsv, (40, 25, 25), (85, 255,255))
# mask = cv2.inRange(hsv, (45, 30, 30), (86, 255,255))

## slice the green
imask = mask>0
print(mask)
green = np.zeros_like(img, np.uint8)
print(green.shape)
# green[imask] = img[imask]
# green[mask == 255] = [0, 255, 0]
# green[mask == 0] = [0, 0, 255]

#custom denoise
kernel = skimage.morphology.disk(0.5)
CloseMap = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
OpenMap = cv2.morphologyEx(CloseMap, cv2.MORPH_OPEN, kernel)

cv2.imwrite("deron/Clarke/ClarkeAL_15_Bipin.jpg", OpenMap)