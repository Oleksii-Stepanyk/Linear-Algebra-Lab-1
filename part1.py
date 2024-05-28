import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

YLIM = (-4, 7)
XLIM = (-4, 7)
is_object = False

def draw(matrix, color):
    global is_object
    
    plt.axline((XLIM[0], 0), (XLIM[1], 0), color="#000000")
    plt.axline((0, YLIM[0]), (0, YLIM[1]), color="#000000")
    
    if is_object:
        plt.plot(vectors[0, :], vectors[1, :], color="#000000")
        plt.plot(matrix[0, :], matrix[1, :], color)
    else:
        plt.quiver([0] * len(vectors[0]), [0] * len(vectors[1]), vectors[0, :], vectors[1, :], color = "#000000", angles="xy", scale_units="xy", scale=1)
        plt.quiver([0] * len(matrix[0]), [0] * len(matrix[1]), matrix[0, :], matrix[1, :], color=color, angles="xy", scale_units="xy", scale=1)

    plt.title(f'''Matrix = {matrix}''')
    plt.xlim(XLIM[0], XLIM[1])
    plt.ylim(YLIM[0], YLIM[1])
    plt.show()
    return 0;


def rotate(matrix, angle, color="#0000FF"):
    angle = np.deg2rad(angle)
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], 
                                [np.sin(angle), np.cos(angle)]])
    matrix = np.dot(rotation_matrix, matrix)
    draw(matrix, color)
    return matrix;


def scaling(matrix, scale, color="#008000"):
    scale_matrix = np.array([[scale, 0], 
                             [0, scale]])
    matrix = np.dot(scale_matrix, matrix)
    draw(matrix, color)
    return matrix;


def mirror(matrix, axis, color="#FFA500"):
    if axis == "x":
        mirror_matrix = np.array([[1, 0], 
                                  [0, -1]])
    if axis == "y":
        mirror_matrix = np.array([[-1, 0], 
                                  [0, 1]])
    matrix = np.dot(mirror_matrix, matrix)
    draw(matrix, color)
    return matrix;


def shear(matrix, axis, shear, color="#00FFFF"):
    if axis == "x":
        shear_matrix = np.array([[1, shear], 
                                 [0, 1]])
    if axis == "y":
        shear_matrix = np.array([[1, 0], 
                                 [shear, 1]])
    matrix = np.dot(shear_matrix, matrix)
    draw(matrix, color)
    return matrix;


def transformate(matrix, transformation_matrix, color="#A020F0"):
    matrix = np.dot(transformation_matrix, matrix)
    draw(matrix, color)
    return matrix;


vectors = np.array([[1, 3, 4, 2, 1], 
                    [1, 1, 3, 3, 1]])

user_input = input("Switch to objects? Y/N: ").upper()
if user_input == "Y":
    is_object = True

mirror(vectors, "x")
rotate(vectors, 195)
scaling(vectors, -0.75)
shear(vectors, "y", 0.5)
transformate(vectors, np.array([[0,2],[1,0]]))