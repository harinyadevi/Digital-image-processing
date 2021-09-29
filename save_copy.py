import cv2

#Reads image
img = cv2.imread(r'apple.jpg')

if img is None:
    print ("image is not valid")

#saving a copy of the image
cv2.imwrite('copy_of_image.jpg', img)