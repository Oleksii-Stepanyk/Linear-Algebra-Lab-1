import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

YLIM = (-10, 10)
XLIM = (-10, 10)

vectors = np.array([[[1, 1], [4, 1], [5, 3], [2, 3], [1, 1]]], dtype = np.float32)
img = cv.imread("img.jpg")


def draw(matrix, color):
    plt.axline((XLIM[0], 0), (XLIM[1], 0), color="#000000")
    plt.axline((0, YLIM[0]), (0, YLIM[1]), color="#000000")

    plt.plot(vectors[0, :, 0], vectors[0, :, 1], color="black")
    plt.plot(matrix[0, :, 0], matrix[0, :, 1], color=color)

    plt.title(f"Matrix = {matrix}")
    plt.xlim(XLIM[0], XLIM[1])
    plt.ylim(YLIM[0], YLIM[1])
    manager = plt.get_current_fig_manager()
    manager.resize(1280, 720)
    plt.show()
    return 0


def transformate_image(image, transformation_matrix, color="#A020F0"):
    rows, cols, dim = image.shape
    image = cv.warpAffine(image, transformation_matrix, (cols, rows))
    cv.imshow("img", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return image


def rotate_image(image, angle):
    rows, cols, dim = image.shape
    transformation_matrix = cv.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    image = cv.warpAffine(image, transformation_matrix, (cols, rows))
    cv.imshow("img", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return image


def scale_image(image, scale):
    rows, cols, dim = image.shape
    image = cv.resize(img, None, fx=scale, fy=scale)
    cv.imshow("img", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return image


def rotate(matrix, angle, color="#0000FF"):
    rotation_matrix = cv.getRotationMatrix2D((0, 0), angle, 1)
    matrix = cv.transform(matrix, rotation_matrix)
    draw(matrix, color)
    return matrix


def scale(matrix, scale, color="#008000"):
    rows, cols = matrix.shape[:2]
    scale_matrix = np.array([[scale, 0, 0], [0, scale, 0]], dtype = np.float32)
    matrix = cv.transform(matrix, scale_matrix)
    draw(matrix, color)
    return matrix


def mirror(matrix, axis, color="#FFA500"):
    if axis == "x":
        mirror_matrix = np.array([[-1, 0, 0], [0, 1, 0]])
    if axis == "y":
        mirror_matrix = np.array([[1, 0, 0], [0, -1, 0]])
    if axis == "xy":
        mirror_matrix = np.array([[-1, 0, 0], [0, -1, 0]])
    matrix = cv.transform(matrix, mirror_matrix)
    draw(matrix, color)
    return matrix


def shear(matrix, axis, shear, color="#00FFFF"):
    if axis == "x":
        shear_matrix = np.array([[1, shear, 0], [0, 1, 0]], dtype = np.float32)
    if axis == "y":
        shear_matrix = np.array([[1, 0, 0], [shear, 1, 0]], dtype = np.float32)
    if axis == "xy":
        shear_matrix = np.array([[1, shear, 0], [shear, 1, 0]], dtype = np.float32)
    matrix = cv.transform(matrix, shear_matrix)
    draw(matrix, color)
    return matrix


def transformate(matrix, transformation_matrix, color="#A020F0"):
    matrix = cv.transform(matrix, transformation_matrix)
    draw(matrix, color)
    return matrix


rotate_image(img, 90)
scale_image(img, 2)
transformate_image(img, np.float32([[1, 0, 100], [0, 1, 50]]))

transformate(vectors, np.array([[2, 0, 0], [0, 2, 0]], dtype = np.float32))
mirror(vectors, "xy")
rotate(vectors, 90)
shear(vectors, "y", 5)
scale(vectors, 0.05)