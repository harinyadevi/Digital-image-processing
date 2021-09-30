import cv2
import numpy

image = cv2.imread(r'apple.jpg')

ret, thresh_image = cv2.threshold(image,100,255,cv2.THRESH_BINARY)

cv2.imwrite("simple_thresh.jpg", thresh_image)
