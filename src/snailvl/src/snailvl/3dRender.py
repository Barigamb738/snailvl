import time

from sympy import false, true
from level import Level
import numpy as np
import cv2
from math import *
import pywavefront


a = Level("C:\\Users\\fille\\AppData\\Local\\Will_You_Snail\\MyFirstLevel.lvl").__new__(Level)
a.__init__("C:\\Users\\fille\\AppData\\Local\\Will_You_Snail\\MyFirstLevel.lvl")
a.localData["WIRES"] = {'QUANTITY': 0, 'WIRES': []}

scale = 500

circle_pos = [1920/2, 1080/2]

xrot = np.pi
yrot = 0
zrot = 0

scene = pywavefront.Wavefront('cube.obj', parse=True, collect_faces=True)
points = np.asarray(scene.vertices)

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])


projected_points = [
    [n, n] for n in range(len(points))
]


def connect_points(i, j):
    a.connect('fantenna' + str(i), 'fantenna' + str(j))

for face in scene.mesh_list[0].faces:
    connect_points(face[0], face[1])
    connect_points(face[1], face[2])
    connect_points(face[2], face[0])

isrun = true

while isrun:
    a.localData["PLACED OBJECTS"] = {'QUANTITY': '14', 'player': {'QUANTITY': 0}, 'wall': {'QUANTITY': 0}, 'wall_gl': {'QUANTITY': 0}, 'spike': {'QUANTITY': 0}, 'spike_thn': {'QUANTITY': 0}, 'door': {'QUANTITY': 0}, 'antenna': {'QUANTITY': 0}, 'rantenna': {'QUANTITY': 0}, 'fantenna': {'QUANTITY': 0}, 'battery': {'QUANTITY': 0}, 'trigg_ai': {'QUANTITY': 0}, 'property_picker_tool': {'QUANTITY': 0}, 'wire_tool': {'QUANTITY': 0}, 'delete_tool': {'QUANTITY': 0}}
    

    rotation_z = np.matrix([
        [cos(zrot), -sin(zrot), 0],
        [sin(zrot), cos(zrot), 0],
        [0, 0, 1],
    ])

    rotation_y = np.matrix([
        [cos(yrot), 0, sin(yrot)],
        [0, 1, 0],
        [-sin(yrot), 0, cos(yrot)],
    ])

    rotation_x = np.matrix([
        [1, 0, 0],
        [0, cos(xrot), -sin(xrot)],
        [0, sin(xrot), cos(xrot)],
    ])


    i = 0
    for point in points:
        rotated2d = np.dot(rotation_z, point.reshape((3, 1)))
        rotated2d = np.dot(rotation_y, rotated2d)
        rotated2d = np.dot(rotation_x, rotated2d)

        projected2d = np.dot(projection_matrix, rotated2d)

        x = int(projected2d[0][0] * scale) + circle_pos[0]
        y = int(projected2d[1][0] * scale) + circle_pos[1]

        projected_points[i] = [x, y]
        a.addObject('fantenna', [x, y, 0, 0, 0, 1, {'coru' : 0}])
        i += 1

    
    
    a.writeLevel(a.localData)
    time.sleep(.1)
    from pynput.keyboard import Key, Controller

    keyboard = Controller()
    key = Key.f2

    keyboard.press(key)
    keyboard.release(key)
    
    yrot += 0.1
    xrot += 0.01
    zrot += 0.001
