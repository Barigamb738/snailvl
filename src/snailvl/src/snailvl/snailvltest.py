import math
from level import Level
import numpy as np
import cv2



def placePixel(level, intensity, x, y):
    for r in range(round(intensity*10)):
        level.addObject('spike', [math.sin(math.radians(r*20))*30 + 29 + x*60, math.cos(math.radians(r*20))*28 + 31 + y*60, r*20, 1, 1, 0, {}])


def printImage(level, path):
    img = cv2.resize(cv2.imread(path), [64, 36])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for y in range(len(gray)):
        for x in range(len(gray[0])):
            placePixel(level, gray[y][x], x, y)
            print(f"X:{x} Y:{y}")

def addPortal(level, x, y):
    for _y in range(90):
        level.addObject("spike", [29 + x*60, 179 - _y + y*60, 0, 1, 1, 0, {}])
        level.addObject("spike", [29 + x*60, 1 + _y + y*60, 0, 1, -1, 0, {}])

import math
from level import Level
import numpy as np
import cv2
#settings
topX = 0
leftX = 0
xSize = 16*30
ySize = 9*30
imgName = "unknown"
sensetivity = 127




path = "./" + imgName + ".png"
a = Level("C:\\Users\\fille\\AppData\\Local\\Will_You_Snail\\MyFirstLevel.lvl").__new__(Level)
a.__init__("C:\\Users\\fille\\AppData\\Local\\Will_You_Snail\\MyFirstLevel.lvl")
a.localData["PLACED OBJECTS"] = {'QUANTITY': '14', 'player': {'QUANTITY': 0}, 'wall': {'QUANTITY': 0}, 'wall_gl': {'QUANTITY': 0}, 'spike': {'QUANTITY': 0}, 'spike_thn': {'QUANTITY': 0}, 'door': {'QUANTITY': 0}, 'antenna': {'QUANTITY': 0}, 'rantenna': {'QUANTITY': 0}, 'fantenna': {'QUANTITY': 0}, 'battery': {'QUANTITY': 0}, 'trigg_ai': {'QUANTITY': 0}, 'property_picker_tool': {'QUANTITY': 0}, 'wire_tool': {'QUANTITY': 0}, 'delete_tool': {'QUANTITY': 0}}

img = cv2.resize(cv2.imread(path), [xSize, ySize])
b,g,r = cv2.split(img)

pixelSize = 0.1
for y in range(ySize):
    for x in range(xSize):
        if r[y][x] > sensetivity:
            a.addObject("wall_gl", [topX + x*pixelSize*60, leftX + y*pixelSize*60, 0, pixelSize/3, pixelSize*(r[y][x]/255), 0, {}])
        if g[y][x] > sensetivity:
            a.addObject("wall", [topX + x*pixelSize*60 + pixelSize*60/3, leftX + y*pixelSize*60, 0, pixelSize/3, pixelSize*(g[y][x]/255), 0, {}])
        if b[y][x] > sensetivity:
            #a.addObject("spike", [topX + x*pixelSize*60 + 2*pixelSize*60/3 + pixelSize*60/6, leftX + (y+1)*pixelSize*60, 0, pixelSize/3, pixelSize*(r[y][x]/255), 0, {}])
            a.addObject("spike", [topX + x*pixelSize*60 + 2*pixelSize*60/3 + pixelSize*60/6, leftX + y*pixelSize*60, 180, pixelSize/3, pixelSize*(b[y][x]/255), 0, {}])


a.writeLevel(a.localData)