import cv2
import numpy as np

img = cv2.imread("E:/x/CircleCode/images/4.jpg", 0)
img = cv2.medianBlur(img, 11)
# cimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ret,tresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# identification of a circle
# using hough circle to find the circle.

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,90,param1=140,param2=60)
                           
print(circles)

#circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(img, (i[0], i[1]), 50, (0, 0, 255), -1)


'''circles2 = cv2.HoughCircles(tresh1,cv2.HOUGH_GRADIENT,1,2)
circles2=np.uint8(np.around(circles))
for i in circles2[0,:]:
    # draw the outer circle
    cv2.circles2(tresh1,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circles2(tresh1,(i[0],i[1]),2,(0,0,255),3)'''
cv2.namedWindow('detected circles',cv2.WINDOW_NORMAL)
cv2.imshow('detected circles', img)
# cv2.imshow('binary',tresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# identifying the center of the circle


# With this center, dividing the lines by 360/n


# Identifying the starting point.  ie. the horizontal line.

# counting in clockwise direction from the segmenation made
# from step 3.
'''
cv2.namedWindow("output",cv2.WINDOW_NORMAL)
cv2.imshow("output",img)
#cv2.imshow("output2",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
