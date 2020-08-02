import cv2
import numpy as np


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(img[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0]), None)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(img )
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            if imgArray[x].reshape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1]))
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x])
        hor = np.hstack(imgArray)
        ver = hor
    return ver


img = cv2.imread('Resources/nayeon.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgStack = stackImages(0.5, ([img, img, img], [img, img, img]))

# imgHor = np.hstack((img,img))
# imgVer = np.vstack((img,img))
#
cv2.imshow("ImageStack", imgStack)
# cv2.imshow("Horizontal", imgHor)
# cv2.imshow("Vertical", imgVer)
cv2.waitKey(0)
