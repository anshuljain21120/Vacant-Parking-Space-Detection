import cv2
import numpy as np
import os
import sys
import time
import matplotlib.pyplot as plt

markerLst = []
#System function to accept mouseclick position
def on_mouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(str(x) + ', ' + str(y)+ "  (" +str(img[y,x,0])+" , "+str(img[y,x,1])+" , "+str(img[y,x,2])+" )")
        markerLst.append((x,y))

#Applied colour filtering for identifying space and separate out cars
def filter(img):
    outimg = np.zeros((img.shape[0],img.shape[1]),np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j][0] >= 73 and img[i][j][0] <= 230:
                if img[i][j][1] >= 96 and img[i][j][1] <= 230:
                    if img[i][j][2] >= 146 and img[i][j][2] <= 233:
                        outimg[i][j] = 255
                    else:
                        outimg[i][j] = 0
                else:
                    outimg[i][j] = 0
            else:
                outimg[i][j] = 0

    return outimg

#User defined window size is stored
def windowSize():
    while len(markerLst)!=4:
        time.sleep(1)
    print(markerLst)
    wnWid = abs(markerLst[0][0]-markerLst[1][0])
    wnLen = abs(markerLst[2][1]-markerLst[3][1])
    return (wnWid,wnLen)

#calculates no of car parking spaces available
def carCalculator(img,colorimg,windowWidth,windowLength):
    count = 0
#    windowLength = 90
#    windowWidth = 60
    windowLength = windowLength - int(0.08*windowLength)
    windowWidth = windowWidth - int(0.08*windowWidth)
    window = np.full((windowLength,windowWidth),255,np.uint8)
    userImg = colorimg.copy()
    ws = windowWidth*windowLength*255
    newImage = img.copy()
    for i in range(0,img.shape[0]-windowLength+1,int(windowLength/2)+1):
        for j in range(100,img.shape[1]-windowWidth+1,int(windowWidth/2)+1):
            os = np.sum(newImage[i:i+windowLength,j:j+windowWidth])
            #if Intensity is more than minimum allowed than it is parking space
            #increase the count and replace that section by green box
            if os/ws > 0.92:
                count = count+1
                for n in range(i,i+windowLength+1):
                    for m in range(j,j+windowWidth+1):
                        newImage[n][m] = 0
                        userImg[n][m] = [0,255,0]
            cv2.imshow('output',userImg)
    return count

#Image opened and resized
img = cv2.imread('Pictures/Parking(post warp).jpg')
resizedImg = cv2.resize(img,None,fx=0.2, fy=0.2, interpolation = cv2.INTER_CUBIC)

#Converting coloured image into black and white image using thresholding and showing it
threshImg = filter(resizedImg)

#Circle shaped structuring element is used for applying opening and closing and then it is showed
kernel = np.array([[0,1,0],[1,1,1],[0,1,0]],np.uint8)
opnImg = cv2.morphologyEx(threshImg, cv2.MORPH_OPEN, kernel)
clsImg = cv2.morphologyEx(opnImg, cv2.MORPH_CLOSE, kernel)

#User will mark first structuring element's width folowed by its length on original image
print("\n========================================================================")
print('****Mark on input image for maximum dimensions(width * length) of car****')
cv2.namedWindow('Input')
cv2.setMouseCallback('Input', on_mouse, 0 )
cv2.imshow('Input',resizedImg)
cv2.imshow('after opening & closing',clsImg)
print('Press key to continue:')
cv2.waitKey()
tuples = windowSize()
wWid = tuples[0]
wLen = tuples[1]
print(str(wWid)+'\t'+str(wLen))
count = carCalculator(clsImg,resizedImg,wWid,wLen)
print(str(count)+" Cars can be parked.")
print("========================================================================\n")
cv2.waitKey()
cv2.destroyAllWindows()
