import cv2
#Reads image
img = cv2.imread(r'apple.jpg')
if img is None:
    print ("image is not valid")
else:
    print ("image is valid")
img= cv2.resize(img, (100,100))
cv2.imwrite("copy.jpg",img)