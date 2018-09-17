import numpy as np
import cv2

'''
Methods found in Opencv documentation:
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_features_harris/py_features_harris.html'''
#### second input
img = cv2.imread('input2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray,140,255,cv2.THRESH_BINARY_INV)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
thresh = cv2.GaussianBlur(thresh,(5,5),0)

#cv2.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance[, corners[, mask[, blockSize[, useHarrisDetector[, k]]]]]) 
corners = cv2.goodFeaturesToTrack(gray, 60, 0.01, 10)
corners = np.int0(corners)
rabbitData = []
birdData = []

for i in range(len(corners)):
    x,y = corners[i].ravel()
    if i%20 == 0:
        rabbitData.append((x,y))
        cv2.circle(img,(x,y),3,255,-1)
    elif i%15 == 0:
        birdData.append((x,y))
        cv2.circle(img,(x,y),3,255,-1)


cv2.imwrite('output/Corner2.jpg',img)