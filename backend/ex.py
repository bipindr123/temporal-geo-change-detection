import cv2
import numpy as np

image1 = cv2.imread('Siskiyou_mask/SiskiyouCA_12.png', 0)
image2 = np.ones((image1.shape[0],image1.shape[1]), np.uint8)
image2 = image2*255
