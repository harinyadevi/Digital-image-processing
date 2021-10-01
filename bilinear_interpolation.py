import cv2
import numpy
import math

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

def resize_bilinear(src, tx, ty):
    h, w, c = src.shape
    
    hratio = h/ty
    wratio = w/tx

    image = numpy.zeros((ty,tx,c),  src.dtype)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]):
                ny = y * hratio
                nx = x * wratio
                y_ = int(ny)
                x_ = int(nx)
                xx, yy = bound(x_, y_, w, h)
                p1 = src[yy, xx, c]

                xx, yy = bound(x_, y_+1, w, h)
                p2 = src[yy, xx, c]
                xx, yy = bound(x_+1, y_, w, h)
                p3 = src[yy, xx, c]
                xx, yy = bound(x_+1, y_+1, w, h)
                p4 = src[yy, xx, c]
                xf = nx - x_
                yf = ny - y_

                b = xf * p2 + (1. - xf) * p1
                t = xf * p4 + (1. - xf) * p3
                pxv = max(0, yf * t + (1. - yf) * b)
                image[y, x, c] = int (pxv)

                
    return image

#new_image = resize_bilinear(img, 180, 140)
new_image = resize_bilinear(img, 600, 600)

cv2.imwrite("output2.jpg", new_image)
