import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread("Photos/park.jpg")
cv.imshow("Boston",img)

plt.imshow(img)
plt.show()


#BGR to GrayScale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

#BGR to L*a*b
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)

#bGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)
""" you cannot convert gray to hsv directly
    gray to bgr and from there to hsv
    gray to bgr and from there to lab
"""
#HSV to BGR
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow("HSV--> BGR",hsv_bgr)

#LAB to BGR
lab_bgr=cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow("LAB--> BGR",lab_bgr)


plt.imshow(rgb)
plt.show()




cv.waitKey(0)

