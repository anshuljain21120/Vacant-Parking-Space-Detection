import cv2
import numpy as np
import matplotlib.pyplot as plt

clicks = []
#load image and resize it
image = cv2.imread('Pictures/IMG_3980.jpg')
image = cv2.resize(image,(1023,1023))

#set perspective parameters which have border points
pts1 = np.float32([[260,330],[738,370],[0,808],[1003,808]])
pts2 = np.float32([[0,0],[200,0],[0,200],[200,200]])

#Perform perspective transform
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(image,M,(200,200))

#plotting both the images in a window
plt.subplot(121),plt.imshow(image),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
