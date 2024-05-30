from matplotlib.axes import Axes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2 as cv

YLIM = (-4, 7)
XLIM = (-4, 7)
is_object = False


def draw_2d(matrix, color):
    global is_object

    plt.axline((XLIM[0], 0), (XLIM[1], 0), color="#000000")
    plt.axline((0, YLIM[0]), (0, YLIM[1]), color="#000000")

    if is_object:
        plt.plot(vectors[0, :], vectors[1, :], color="#000000")
        plt.plot(matrix[0, :], matrix[1, :], color)
    else:
        plt.quiver([0] * len(vectors[0]), [0] * len(vectors[1]),vectors[0, :], vectors[1, :],color="#000000",angles="xy",scale_units="xy",scale=1)
        plt.quiver([0] * len(matrix[0]), [0] * len(matrix[1]), matrix[0, :], matrix[1, :], color=color, angles="xy", scale_units="xy", scale=1)

    plt.title(f"""Matrix = {matrix}""")
    plt.xlim(XLIM[0], XLIM[1])
    plt.ylim(YLIM[0], YLIM[1])
    plt.show()
    return 0


def draw_3d(matrix, color):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(0,0,0, color="#000000", marker="o")

    ax.plot(vectors_3d[0, :], vectors_3d[1, :], vectors_3d[2, :], color="#000000")
    ax.plot(matrix[0, :], matrix[1, :], matrix[2, :], color)
    
    plt.show()
    return 0
    

def rotate(matrix, angle, color="#0000FF"):
    angle = np.deg2rad(angle)
    rotation_matrix = np.array(
        [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]
    )
    matrix = np.dot(rotation_matrix, matrix)
    draw(matrix, color)
    return matrix


def rotate_3d(matrix, angle, axis, color="#0000FF"):
    angle = np.deg2rad(angle)
    if axis == "x":
        rotation_matrix = np.array([[1, 0, 0], [0, np.cos(angle), -np.sin(angle)], [0, np.sin(angle), np.cos(angle)]])
    if axis == "y":
        rotation_matrix = np.array([[np.cos(angle),0,np.sin(angle)],[0,1,0],[-np.sin(angle),0,np.cos(angle)]])
    if axis == "z":
        rotation_matrix = np.array([[np.cos(angle),-np.sin(angle),0],[np.sin(angle),np.cos(angle),0],[0,0,1]])
    matrix = np.dot(rotation_matrix, matrix)
    draw_3d(matrix, color)
    return matrix


def scaling_3d(matrix, scale, color="#008000"):
    scale_matrix = np.array([[scale,0, 0], [0, scale,0],[0,0,scale]])
    matrix = np.dot(scale_matrix, matrix)
    draw_3d(matrix, color)
    return matrix


def scaling(matrix, scale, color="#008000"):
    scale_matrix = np.array([[scale, 0], [0, scale]])
    matrix = np.dot(scale_matrix, matrix)
    draw_2d(matrix, color)
    return matrix


def mirror_3d(matrix, axis, color="#FFA500"):
    if axis == "x":
        mirror_matrix = np.array([[1, 0, 0], [0, -1, 0],[0, 0, -1]])
    if axis == "y":
        mirror_matrix = np.array([[-1, 0, 0], [0, 1, 0],[0, 0, -1]])
    if axis == "z":
        mirror_matrix = np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])
    matrix = np.dot(mirror_matrix, matrix)
    draw_3d(matrix, color)
    return matrix


def mirror(matrix, axis, color="#FFA500"):
    if axis == "x":
        mirror_matrix = np.array([[1, 0], [0, -1]])
    if axis == "y":
        mirror_matrix = np.array([[-1, 0], [0, 1]])
    matrix = np.dot(mirror_matrix, matrix)
    draw_2d(matrix, color)
    return matrix


def shear(matrix, axis, shear, color="#00FFFF"):
    if axis == "x":
        shear_matrix = np.array([[1, shear], [0, 1]])
    if axis == "y":
        shear_matrix = np.array([[1, 0], [shear, 1]])
    matrix = np.dot(shear_matrix, matrix)
    draw_2d(matrix, color)
    return matrix


def transformate(matrix, transformation_matrix, color="#A020F0"):
    matrix = np.dot(transformation_matrix, matrix)
    draw_2d(matrix, color)
    return matrix


vectors = np.array([[1, 3, 4, 2, 1], [1, 1, 3, 3, 1]])
vectors_3d = np.array([[1, 3, 4, 2, 1], [1, 1, 3, 3, 1], [1, 1, 1, 1, 1]])

user_input = input("Switch to objects? Y/N: ").upper()
if user_input == "Y":
    is_object = True

mirror(vectors, "x")
rotate(vectors, 195)
scaling(vectors, -0.75)
shear(vectors, "y", 0.5)
transformate(vectors, np.array([[0, 2], [1, 0]]))

rotate_3d(vectors_3d, 180, "x")
scaling_3d(vectors_3d, 2)
mirror_3d(vectors_3d, "x")