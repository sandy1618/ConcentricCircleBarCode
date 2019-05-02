import cv2
import numpy as np 

img = cv2.imread("E:/x/CircleCode/images/circle.jpg",0)
#img=cv2.medianBlur(img,5)
#cimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# identification of a circle
#using hough circle to find the circle. 
circles=cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50)

# identifying the center of the circle


# With this center, dividing the lines by 360/n 


# Identifying the starting point.  ie. the horizontal line. 

# counting in clockwise direction from the segmenation made 
# from step 3. 

cv2.namedWindow("output",cv2.WINDOW_NORMAL)
cv2.imshow("output",img)
#cv2.imshow("output2",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()




