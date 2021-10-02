import cv2
import numpy as np

src = cv2.imread(r'apple.jpg', 0)

dst = cv2.equalizeHist(src)

cv2.imwrite("output4.jpg", dst)
