import cv2
import numpy as np 
#mat img = cv2.imread
img = cv2.imread("E:/x/CircleCode/images/4.jpg",0)
#cv2.imshow("before", img)

ret,tresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('detected circles', tresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''tpx=img.shape
height=img.shape[0]
width=img.shape[1]
channels=img.shape[2]
print('Image Dimension    : ',tpx)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)
print (img.size)
print(img.dtype)
'''
'''px=img[100,100]
print(px)
blue=img[]
'''
#np.set_printoptions(threshold=np.inf)
#print(np.)
