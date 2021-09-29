import cv2

#Reads image
img = cv2.imread(r'apple.jpg')

if img is None:
    print ("image is not valid")

h, w, c = img.shape

print (f'     width:  {w}')
print (f'    height:  {h}')
print (f'  channels:  {c}')

img_blur = cv2.blur(img, (25,25))
cv2.imwrite("blur.jpg",img_blur)