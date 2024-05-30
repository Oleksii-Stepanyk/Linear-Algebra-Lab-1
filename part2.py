import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

YLIM = (-4, 7)
XLIM = (-4, 7)
is_object = True

vectors = np.array([[1, 3, 4, 2, 1], [1, 1, 3, 3, 1], [0, 0, 0, 0, 0]])
img = cv.imread("img.jpg")


def transformate(image, transformation_matrix, color="#A020F0"):
    rows, cols, dim = image.shape
    image = cv.warpAffine(image, transformation_matrix, (cols, rows))
    cv.imshow("img", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return image


def rotate(image, angle):
    rows, cols, dim = image.shape
    transformation_matrix = cv.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    image = cv.warpAffine(image, transformation_matrix, (cols, rows))
    cv.imshow("img", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return image


def scale(image, scale):
    rows, cols, dim = image.shape
    image = cv.resize(img, None, fx=scale, fy=scale) 
    cv.imshow("img", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return image

rotate(img, 90)
scale(img, 2)
transformate(img, np.float32([[1, 0, 100], [0, 1, 50]]))