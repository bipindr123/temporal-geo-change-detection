import cv2
import numpy as np

base = cv2.imread('Humboldt_cropped/HumboldtCA_18.png')
afforest = cv2.imread('Humboldt_afforest_final/HumboldtCA_18_HumboldtCA_20_OpenMap.jpg', 0)
deforest = cv2.imread('Humboldt_deforest_final/HumboldtCA_18_HumboldtCA_20_OpenMap.jpg', 0)

base = base[1:base.shape[0]-1,1:base.shape[1]-1]
afforest = cv2.copyMakeBorder(afforest, 1, 1, 1, 1, cv2.BORDER_CONSTANT, (0,0,0))
deforest = cv2.copyMakeBorder(deforest, 1, 1, 1, 1, cv2.BORDER_CONSTANT, (0,0,0))

blue = np.zeros((afforest.shape[0], afforest.shape[1], 3), afforest.dtype)
blue[:,:] = (255, 0, 0)
blueMask = cv2.bitwise_and(blue, blue, mask=afforest)

red = np.zeros((deforest.shape[0], deforest.shape[1], 3), deforest.dtype)
red[:,:] = (0, 0, 255)
redMask = cv2.bitwise_and(red, red, mask=deforest)

base = cv2.addWeighted(blueMask, 1, base, 1, 1)
base = cv2.addWeighted(redMask, 1, base, 1, 1)

# cv2.imshow('Overlay',base)
# cv2.waitKey(0)

cv2.imwrite('Humboldt_overlay/Humboldt_18_20.jpg',base)