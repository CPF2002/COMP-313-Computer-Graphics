'''
Student Author Name: Compton French
Project 2
Fall 2022
COMP 313: Computer Graphics
Professor Schiffer
'''
import sys

import matplotlib.pyplot as plt
from math import sin, cos, radians

import numpy as np

plane_x = []    # coordinates
plane_y = []
plane_z = []
plane_f = []    # faces

rotd_sequence_coords = []


def importObj():
    # might have to rename to model-plane.obj ; it was changing while I moved the file around
    file = open('model-plane.obj')

    list_of_lines = file.readlines()
    for line in list_of_lines:
        if line[0] == 'vn':
            pass
        elif line[0] == 'v':
            # print(line)
            line_v = line.strip('v \n')
            # print(line_v)
            pnt_vect = line_v.split(' ')

            for index, str in enumerate(pnt_vect):
                pnt_vect[index] = float(str)
            # print(pnt_vect)

            plane_x.append(pnt_vect[0])
            plane_y.append(pnt_vect[1])
            plane_z.append(pnt_vect[2])

        if line[0] == 'f':

            line_f = line.strip('f \n')

            face = line_f.split(' ')

            for index, str_num in enumerate(face):
                face[index] = int(str_num) - 1
            # print(face)
            plane_f.append(face)
    pass


def plot_sequential_rotation(rotd_coords):
    # still have to write for plane
    x = 0
    y = 1
    # col = (np.random.random(), np.random.random(), np.random.random()) # was having fun with random colors
    col = (0.5, 0, 0.5)
    # for each of the num of faces, and each edge in each face, plot the vertex to the next vertex
    for face_num in range(0, len(plane_f)):
        for edge_num in range(0, len(rotd_coords[face_num]) - 1):
            '''print('edge_num: ')
            print(edge_num)
            print('len(rotd_coords[face_num])')
            print(len(rotd_coords[face_num]))'''

            # make line size smaller (medium color)
            # decrease alpha (0.2 - 0.5)
            vertex = plane_f[face_num][edge_num]
            vertex2 = plane_f[face_num][edge_num + 1]
            plt.plot([rotd_coords[vertex][x], rotd_coords[vertex2][x]],
                     [rotd_coords[vertex][y], rotd_coords[vertex2][y]],
                     color=col, alpha=0.5)

    # print(len(plane_f))
    # print(len(rotd_coords))
    # print(len(rotd_coords[face_num]))

    pass


# center vector in the form of a list [xcenter, ycenter, zcenter], x_angle, y_angle, z_angle, rotation_sequence
# ("RxRyRz" and each of the six combinations.)
def plot_shape(center_vector, x_angle, y_angle, z_angle, rot_seq):
    # GRID SETUP FOR SEQUENTIAL COMBINED ROTATIONS
    figure, axes = plt.subplots()
    axes.set_aspect(1)
    plt.axis([-10, 10, -10, 10])
    plt.axis('on')
    plt.grid(True)

    vert_count = len(plane_x)  # plane_x y and z all have the same vertex length

    global rotd_sequence_coords
    x = 0  # for the coord value
    y = 1
    z = 2

    # move plane_z to rotd_sequence_coords
    for vert_num in range(0, vert_count):
        rotd_sequence_coords.append([plane_x[vert_num], plane_y[vert_num], plane_z[vert_num]])

    if rot_seq == 'RxRyRz':
        #rotd_sequence_coords = rotd_x_coords
        for vert_num in range(0, vert_count):
            rotd_sequence_coords[vert_num] = rotx(center_vector, [rotd_sequence_coords[vert_num][x],
                                                                  rotd_sequence_coords[vert_num][y],
                                                                  rotd_sequence_coords[vert_num][z]], x_angle)
        for vert_num in range(0, vert_count):
            rotd_sequence_coords[vert_num] = roty(center_vector, [rotd_sequence_coords[vert_num][x],
                                                                  rotd_sequence_coords[vert_num][y],
                                                                  rotd_sequence_coords[vert_num][z]], y_angle)
        for vert_num in range(0, vert_count):
            rotd_sequence_coords[vert_num] = rotz(center_vector, [rotd_sequence_coords[vert_num][x],
                                                                  rotd_sequence_coords[vert_num][y],
                                                                  rotd_sequence_coords[vert_num][z]], z_angle)

    elif rot_seq == 'RyRxRz':
        #rotd_sequence_coords = rotd_y_coords
        for vert_num in range(0, vert_count):
            rotd_sequence_coords[vert_num] = roty(center_vector, [rotd_sequence_coords[vert_num][x],
                                                                  rotd_sequence_coords[vert_num][y],
                                                                  rotd_sequence_coords[vert_num][z]], y_angle)
        for vert_num in range(0, vert_count):
            rotd_sequence_coords[vert_num] = rotx(center_vector, [rotd_sequence_coords[vert_num][x],
                                                                  rotd_sequence_coords[vert_num][y],
                                                                  rotd_sequence_coords[vert_num][z]], x_angle)
        for vert_num in range(0, vert_count):
            rotd_sequence_coords[vert_num] = rotz(center_vector, [rotd_sequence_coords[vert_num][x],
                                                                  rotd_sequence_coords[vert_num][y],
                                                                  rotd_sequence_coords[vert_num][z]], z_angle)

    elif rot_seq == 'RzRyRx':
        #rotd_sequence_coords = rotd_z_coords
        for vert_num in range(0, vert_count):
            rotd_sequence_coords[vert_num] = rotz(center_vector, [rotd_sequence_coords[vert_num][x],
                                                                  rotd_sequence_coords[vert_num][y],
                                                                  rotd_sequence_coords[vert_num][z]], z_angle)
        for vert_num in range(0, vert_count):
            rotd_sequence_coords[vert_num] = roty(center_vector, [rotd_sequence_coords[vert_num][x],
                                                                  rotd_sequence_coords[vert_num][y],
                                                                  rotd_sequence_coords[vert_num][z]], y_angle)
        for vert_num in range(0, vert_count):
            rotd_sequence_coords[vert_num] = rotx(center_vector, [rotd_sequence_coords[vert_num][x],
                                                                  rotd_sequence_coords[vert_num][y],
                                                                  rotd_sequence_coords[vert_num][z]], x_angle)

    elif rot_seq == 'RzRxRy':
        #rotd_sequence_coords = rotd_z_coords
        for vert_num in range(0, vert_count):
            rotd_sequence_coords[vert_num] = rotz(center_vector, [rotd_sequence_coords[vert_num][x],
                                                                  rotd_sequence_coords[vert_num][y],
                                                                  rotd_sequence_coords[vert_num][z]], z_angle)
        for vert_num in range(0, vert_count):
            rotd_sequence_coords[vert_num] = rotx(center_vector, [rotd_sequence_coords[vert_num][x],
                                                                  rotd_sequence_coords[vert_num][y],
                                                                  rotd_sequence_coords[vert_num][z]], x_angle)
        for vert_num in range(0, vert_count):
            rotd_sequence_coords[vert_num] = roty(center_vector, [rotd_sequence_coords[vert_num][x],
                                                                  rotd_sequence_coords[vert_num][y],
                                                                  rotd_sequence_coords[vert_num][z]], y_angle)

    elif rot_seq == 'RxRzRy':
        #rotd_sequence_coords = rotd_x_coords
        for vert_num in range(0, vert_count):
            rotd_sequence_coords[vert_num] = rotx(center_vector, [rotd_sequence_coords[vert_num][x],
                                                                  rotd_sequence_coords[vert_num][y],
                                                                  rotd_sequence_coords[vert_num][z]], x_angle)
        for vert_num in range(0, vert_count):
            rotd_sequence_coords[vert_num] = rotz(center_vector, [rotd_sequence_coords[vert_num][x],
                                                                  rotd_sequence_coords[vert_num][y],
                                                                  rotd_sequence_coords[vert_num][z]], z_angle)
        for vert_num in range(0, vert_count):
            rotd_sequence_coords[vert_num] = roty(center_vector, [rotd_sequence_coords[vert_num][x],
                                                                  rotd_sequence_coords[vert_num][y],
                                                                  rotd_sequence_coords[vert_num][z]], y_angle)

    elif rot_seq == 'RyRzRx':
        #rotd_sequence_coords = rotd_y_coords
        for vert_num in range(0, vert_count):
            rotd_sequence_coords[vert_num] = roty(center_vector, [rotd_sequence_coords[vert_num][x],
                                                                  rotd_sequence_coords[vert_num][y],
                                                                  rotd_sequence_coords[vert_num][z]], y_angle)
        # rotate each of the coords in the y
        # rotz(center_vector, [x_coords[vert_num], y_coords[vert_num], z_coords[vert_num]], z_angle))

        for vert_num in range(0, vert_count):
            rotd_sequence_coords[vert_num] = rotz(center_vector, [rotd_sequence_coords[vert_num][x],
                                                                  rotd_sequence_coords[vert_num][y],
                                                                  rotd_sequence_coords[vert_num][z]], z_angle)
        # finally rotate on the x
        for vert_num in range(0, vert_count):
            rotd_sequence_coords[vert_num] = rotx(center_vector, [rotd_sequence_coords[vert_num][x],
                                                                  rotd_sequence_coords[vert_num][y],
                                                                  rotd_sequence_coords[vert_num][z]], x_angle)

    else:
        print('The rotation sequence is invalid.')
        sys.exit()

    print(rotd_sequence_coords)
    plot_sequential_rotation(rotd_sequence_coords)

    plt.show()


# ROTATIONAL MATRIX FUNCTIONS

# Rotates a point vector from a given center a given number of degrees CC for + numbers on the x-axis
def rotx(center_vector, point_vector, angle):

    angle = radians(angle)

    rotx_mat = [
                [1, 0,          0],
                [0, cos(angle), -sin(angle)],
                [0, sin(angle), cos(angle)]
              ]

    xprod = rotx_mat[0][0] * point_vector[0] + rotx_mat[0][1] * point_vector[1] + rotx_mat[0][2] * point_vector[2]
    yprod = rotx_mat[1][0] * point_vector[0] + rotx_mat[1][1] * point_vector[1] + rotx_mat[1][2] * point_vector[2]
    zprod = rotx_mat[2][0] * point_vector[0] + rotx_mat[2][1] * point_vector[1] + rotx_mat[2][2] * point_vector[2]

    xg = xprod + center_vector[0]
    yg = yprod + center_vector[1]
    zg = zprod + center_vector[2]

    return [xg, yg, zg]


def roty(center_vector, point_vector, angle):

    angle = radians(angle)

    roty_mat = [
                [cos(angle),  0, sin(angle)],
                [0,           1,          0],
                [-sin(angle), 0, cos(angle)]
               ]

    xprod = roty_mat[0][0] * point_vector[0] + roty_mat[0][1] * point_vector[1] + roty_mat[0][2] * point_vector[2]
    yprod = roty_mat[1][0] * point_vector[0] + roty_mat[1][1] * point_vector[1] + roty_mat[1][2] * point_vector[2]
    zprod = roty_mat[2][0] * point_vector[0] + roty_mat[2][1] * point_vector[1] + roty_mat[2][2] * point_vector[2]

    xg = xprod + center_vector[0]
    yg = yprod + center_vector[1]
    zg = zprod + center_vector[2]

    return [xg, yg, zg]


def rotz(center_vector, point_vector, angle):

    angle = radians(angle)

    rotz_mat = [
                [cos(angle), -sin(angle),  0],
                [sin(angle),  cos(angle),  0],
                [0,           0,           1]
               ]

    xprod = rotz_mat[0][0] * point_vector[0] + rotz_mat[0][1] * point_vector[1] + rotz_mat[0][2] * point_vector[2]
    yprod = rotz_mat[1][0] * point_vector[0] + rotz_mat[1][1] * point_vector[1] + rotz_mat[1][2] * point_vector[2]
    zprod = rotz_mat[2][0] * point_vector[0] + rotz_mat[2][1] * point_vector[1] + rotz_mat[2][2] * point_vector[2]

    xg = xprod + center_vector[0]
    yg = yprod + center_vector[1]
    zg = zprod + center_vector[2]

    return [xg, yg, zg]


def main():
    importObj()
    plot_shape([0, 0, 0], 20, 30, 50, 'RxRyRz')     # photo 1
    #plot_shape([1, 1, 1], 20, 30, 50, 'RxRyRz')
    #plot_shape([0, 0, 0], 20, 30, 50, 'RyRxRz')
    #plot_shape([1, 1, 1], 20, 30, 50, 'RyRxRz')
    #plot_shape([0, 0, 0], 20, 30, 50, 'RzRyRx')
    #plot_shape([1, 1, 1], 20, 30, 50, 'RzRyRx')
    #plot_shape([0, 0, 0], 20, 30, 50, 'RzRxRy')
    #plot_shape([1, 1, 1], 20, 30, 50, 'RzRxRy')
    #plot_shape([0, 0, 0], 20, 30, 50, 'RxRzRy')
    #plot_shape([1, 1, 1], 20, 30, 50, 'RxRzRy')
    #plot_shape([0, 0, 0], 20, 30, 50, 'RyRzRx')
    #plot_shape([1, 1, 1], 20, 30, 50, 'RyRzRx')     # photo 2
    pass


main()



