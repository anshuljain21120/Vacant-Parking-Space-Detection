# Vacant-Parking-Space-Detection
In this project, we purpose a solution for effective use of the main parking space of [LNMIIT](https://www.lnmiit.ac.in/). Using the region growing technique we are segmenting area available and the cars present on a given image. Also, the perspective of the image was changed in order to apply the algorithm on it. 
## Requirements
- [Python3](https://www.python.org/download/releases/3.0/)
- [OpenCV](https://opencv.org/)
## Introduction
The main parking space near the mechanical department in LNMIIT, faces of a problem of effective use of the parking area. We, therefore, intend to provide a solution by creating an image processing algorithm which will utilize photographs in order to predict the number of vacant spaces available in the parking area. 
## Understanding the approach
To start the project, we first of all manually took the pictures of the site from above by fixing the camera at the roof in one position. The images we obtained were not as desired in perspective as well as size so we changed the perspective by perspective transformation and resized the image to the desired one. 
After changing the perspective and size, we performed thresholding on the image in order to obtain a binary image. The thresholding was performed using a piecewise linear transformation where the pixels that were between the range (73,96,146) and (230,230,233) were transformed to 255 while all the other pixels were transformed to 0. 
The thresholding changed the image from BGR to binary. The obtained binary image helped us in differentiating between the area which can be used for parking and car parked along with the area which can’t be used for parking. After performing threshold, we observed some salt and pepper noise in the obtained image. This noise was handled by first doing opening followed closing with same structing element. The structuring element that was used for performing the opening and closing is shown below – 
We chose the above structure keeping in mind that the curves of car are to be maintained as if we increase the edges, the number of cars that can be accommodated increases. 
After performing the above steps, we clearly got the empty region denoted by 255 and all the occupied region with 0. We asked the user to input the length of the car he wants. As the actual length differs from that of pixels in the image, he can simply click on the car edges already present in the image. Post that we created a window of the specified dimensions. We calculated ```length*breadth *255(ws)``` for the whole image. We kept on putting the window at each pixel of the image and calculated the sum of the intensity values in that window(os). We calculated the error that is there in the image and if it is greater than 8%, we ignored the error and made that region complete black and marked that region with green in the original image. Also, with help of counter we counted the number of cars. 
## Results
By performing all the above-mentioned techniques, we reached to a very good model which gave desired results. There are few issues that can be worked upon in future- 
- We couldn’t incorporate the space occupied by the grass and trees. It can be done by specifying multiple ranges and tuning them such that they can differ between grass and trees. 
- We couldn’t incorporate the orientation of the window that we used for calculating the number of available spaces for the car parking. 
## Discussion 
We could have got a better result if we have taken images from a better angle. We could have also resolved the issues mentioned in the results.  
