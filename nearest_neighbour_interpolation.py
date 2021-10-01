import cv2
import numpy

img = cv2.imread(r'apple.jpg')

def bound(nx, ny, w, h):
    if nx < 0:
        nx = 0
    if ny < 0:
        ny = 0
    if nx >= w:
        nx = w - 1
    if ny >= h:
        ny = h - 1
    return nx, ny

def resize_nearest(src, tx, ty):
    h, w, c = src.shape
    
    hratio = h/ty
    wratio = w/tx

    image = numpy.zeros((ty,tx,c),  src.dtype)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]):
                nx, ny = bound(tx, ty, w, h)
                ny = int (y * hratio + 0.5)
                nx = int (x * wratio + 0.5)
                image[y, x, c] = src[ny, nx, c]
    return image

new_image = resize_nearest(img, 180, 140)
#new_image = resize_nearest(img, 1080, 1040)

cv2.imwrite("output.jpg", new_image)
