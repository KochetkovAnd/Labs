from math import pi
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL.ImageQt import ImageQt

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
frameSize = 600

n = 300 # Смещение в положительную строну

from fnGraf2 import *
from fnMath2 import *



def start(R, step, n, m, img):  

    image = Image.new(mode = "RGB", size = (frameSize, frameSize), color=white)
    addAxles(image)
    figure = getSuperToroid3D(R, step, n, m)
    polygons = divisionIntoPolygons(figure)
    printPolygons(polygons, image)
    showImage(img, image)

    return figure  

def task1(figure, img):
    image = Image.new(mode = "RGB", size = (frameSize, frameSize), color=white)
    addAxles(image)

    figureAfter = affin1(figure, 1.5, 1, 1)
    polygons = divisionIntoPolygons(figureAfter)
    printPolygons(polygons, image)
    showImage(img, image)

def task2(figure, img):
    image = Image.new(mode = "RGB", size = (frameSize, frameSize), color=white)
    addAxles(image)

    figureAfter = affin2(figure, pi/ 4)
    polygons = divisionIntoPolygons(figureAfter)
    printPolygons(polygons, image)
    showImage(img, image)

def task3(figure, img):
    image = Image.new(mode = "RGB", size = (frameSize, frameSize), color=white)
    addAxles(image)

    figureAfter = affin3(figure, 100)
    polygons = divisionIntoPolygons(figureAfter)
    printPolygons(polygons, image)
    showImage(img, image)