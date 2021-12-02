import cv2
import numpy as np
import json
d= {}

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

# import cv2
# import numpy as np
# import json
# d= {}
# ## Read
# for i in range(14,21,2):
#     filename = "Siskiyou_deforest_final/SiskiyouCA_"+str(i-2)+".png_SiskiyouCA_"+str(i)+".png_OpenMap.jpg"
#     img = cv2.imread(filename)

#     ## convert to hsv
#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     white = 0
#     black = 0
#     white = np.sum(hsv == 255)  
#     black = np.sum(hsv == 0) 
#     d[filename] = str(white/(white+black)*100)
#     print(d)
#     f = open("change_defor.json","w+")
#     f.write(json.dumps(d))

for i in range(14,21,2):
    filename = "Humboldt_deforest_final/HumboldtCA_"+str(i-2)+"_HumboldtCA_"+str(i)+"_OpenMap.jpg"
    img = cv2.imread(filename)

    ## convert to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    white = 0
    black = 0
    white = np.sum(hsv == 255)  
    black = np.sum(hsv == 0) 
    d[filename] = str(white/(white+black)*100)
    print(d)
    f = open("changehumdef.json","w+")
    f.write(json.dumps(d))