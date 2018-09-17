import numpy as np
import cv2
import random
'''
Methods found in Opencv documentation:
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_features_harris/py_features_harris.html'''
#### first input
img = cv2.imread('input.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray,140,255,cv2.THRESH_BINARY_INV)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
thresh = cv2.GaussianBlur(thresh,(5,5),0)

#cv2.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance[, corners[, mask[, blockSize[, useHarrisDetector[, k]]]]]) 
corners = cv2.goodFeaturesToTrack(gray, 60, 0.01, 10)
corners = np.int0(corners)
cornerData = []
for i in range(len(corners)):
    corner = corners[i]
    x,y = corner.ravel()
    cornerData.append((x,y))
    if i % 5 == 0:
        leftOffset = random.randint (-800,0)
        rightOffset = random.randint(0,800)
        cornerData.append((x+leftOffset,y))
        cornerData.append((x+rightOffset,y))

# cv2.imwrite('output/Corner.jpg',img)

mediumTreeData = []
bushData = []
largeTreeData=[]

_,contours,_ = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,255,0))
contours = np.vstack(contours).squeeze()
for i in range(len(contours)):
    if i%200 == 0:
        x,y = contours[i].ravel()
        mediumTreeData.append((x,y))
    elif i%879 == 0:
        a,b = contours[i].ravel()
        bushData.append((a,b))
    elif i%678 == 0:
        c,d = contours[i].ravel()
        largeTreeData.append((c,d))
