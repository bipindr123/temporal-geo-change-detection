from os import name
from os.path import exists
import cv2 
import sklearn
from sklearn.cluster import KMeans
from collections import Counter
from sklearn.decomposition import PCA
import skimage.morphology
import numpy as np
import time

directory = "Humboldt_mask/"
filename = "HumboldtCA_"
final_directory1 = "Humboldt_deforest_final/"
filenames = []

def detect_change(im1,im2):
    image1_path = directory+im1
    image2_path = directory+im2
    final_directory2 = final_directory1+im1.split(".")[0]+"_"+im2.split(".")[0]+"_"
    print(image1_path, image2_path)

    print('[INFO] Start Change Detection ...')
    print('[INFO] Importing Librairies ...')


    def find_vector_set(diff_image, new_size):
    
        i = 0
        j = 0
        vector_set = np.zeros((int(new_size[0] * new_size[1] / 25),25))
        while i < vector_set.shape[0]:
            while j < new_size[1]:
                k = 0
                while k < new_size[0]:
                    block   = diff_image[j:j+5, k:k+5]
                    feature = block.ravel()
                    vector_set[i, :] = feature
                    k = k + 5
                j = j + 5
            i = i + 1
    
        mean_vec   = np.mean(vector_set, axis = 0)
        # Mean normalization
        vector_set = vector_set - mean_vec   
        return vector_set, mean_vec

    def find_FVS(EVS, diff_image, mean_vec, new):
    
        i = 2
        feature_vector_set = []
    
        while i < new[1] - 2:
            j = 2
            while j < new[0] - 2:
                block = diff_image[i-2:i+3, j-2:j+3]
                feature = block.flatten()
                feature_vector_set.append(feature)
                j = j+1
            i = i+1
    
        FVS = np.dot(feature_vector_set, EVS)
        FVS = FVS - mean_vec
        print ("[INFO] Feature vector space size", FVS.shape)
        return FVS

    def clustering(FVS, components, new):
        kmeans = KMeans(components, verbose = 0)
        kmeans.fit(FVS)
        output = kmeans.predict(FVS)
        count  = Counter(output)
    
        least_index = min(count, key = count.get)
        change_map  = np.reshape(output,(new[1] - 4, new[0] - 4))
        return least_index, change_map
        

    # Read Images
    print('[INFO] Reading Images ...')
    start = time.time()
    image1 = cv2.imread(image1_path,0)
    image2 = cv2.imread(image2_path,0)
    # ret1, image1 = cv2.threshold(image1,160,255,0)
    # ret2, image2 = cv2.threshold(image2,160,255,0)
    end = time.time()
    print('[INFO] Reading Images took {} seconds'.format(end-start))


    # Resize Images
    print('[INFO] Resizing Images ...')
    start = time.time()
    new_size = np.asarray(image1.shape) /5
    new_size = new_size.astype(int) *5
    image1 = cv2.resize(image1, (new_size[0],new_size[1])).astype(int)
    image2 = cv2.resize(image2, (new_size[0],new_size[1])).astype(int)
    end = time.time()
    print('[INFO] Resizing Images took {} seconds'.format(end-start))

    # Difference Image
    print('[INFO] Computing Difference Image ...')
    start = time.time()
    # print(image1)
    # cv2.imshow("I1",image1)
    # cv2.waitKey(0)

    # diff_imageX = abs(image1 - image2)
    bitwiseAnd = cv2.bitwise_and(image1, image2)
    diff_imageX = image1 - bitwiseAnd

    cv2.imwrite(final_directory2+'difference.jpg', diff_imageX)
    end = time.time()
    print('[INFO] Computing Difference Image took {} seconds'.format(end-start))
    # diff_imageX=diff_imageX[:,:,1]

    print('[INFO] Performing PCA ...')
    start = time.time()
    pca = PCA()
    vector_setX, mean_vecX=find_vector_set(diff_imageX, new_size)

    pca.fit(vector_setX)
    EVS = pca.components_
    end = time.time()
    print('[INFO] Performing PCA took {} seconds'.format(end-start))

    print('[INFO] Building Feature Vector Space ...')
    start = time.time()
    FVS = find_FVS(EVS, diff_imageX, mean_vecX, new_size)
    components = 2
    end = time.time()
    print('[INFO] Building Feature Vector Space took {} seconds'.format(end-start))

    print('[INFO] Clustering ...')
    start = time.time()
    least_index, change_map = clustering(FVS, components, new_size)
    end = time.time()
    print('[INFO] Clustering took {} seconds'.format(end-start))

    change_map[change_map == least_index] = 255
    change_map[change_map != 255] = 0
    change_map = change_map.astype(np.uint8)

    print('[INFO] Save Change Map ...')
    cv2.imwrite(final_directory2+'ChangeMap.jpg', change_map)

    print('[INFO] Performing Closing ...')
    print('[WARNING] Kernel is fixed depending on image topology')
    print('[WARNING] Closing with disk-shaped structuring element with radius equal to 6')
    kernel = skimage.morphology.disk(2)
    CloseMap = cv2.morphologyEx(change_map, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite(final_directory2+'CloseMap.jpg', CloseMap)

    print('[INFO] Performing Opening ...')
    OpenMap = cv2.morphologyEx(CloseMap, cv2.MORPH_OPEN, kernel)
    cv2.imwrite(final_directory2+'OpenMap.jpg', OpenMap)

    print('[INFO] End Change Detection')

for i in range(10,21):
    file_exists = exists(directory+filename+str(i)+".png")
    if(file_exists):
        filenames.append(filename+str(i)+".png")

for i in range(len(filenames)-1):
    print(filenames[i],filenames[i+1])
    detect_change(filenames[i],filenames[i+1])
