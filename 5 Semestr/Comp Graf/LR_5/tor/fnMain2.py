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

def Stretch(figure, img):
    image = Image.new(mode = "RGB", size = (frameSize, frameSize), color=white)
    addAxles(image)

    figureAfter = affinStretch(figure, 0.5, 0.5, 2)
    polygons = divisionIntoPolygons(figureAfter)
    printPolygons(polygons, image)
    showImage(img, image)

def rotateX(figure, img):
    image = Image.new(mode = "RGB", size = (frameSize, frameSize), color=white)
    addAxles(image)
    figureAfter = affinRotateX(figure, pi/ 16)
    polygons = divisionIntoPolygons(figureAfter)
    printPolygons(polygons, image)
    showImage(img, image)
    return figureAfter

def rotateZ(figure, img):
    image = Image.new(mode = "RGB", size = (frameSize, frameSize), color=white)
    addAxles(image)
    figureAfter = affinRotateZ(figure, pi/ 16)
    polygons = divisionIntoPolygons(figureAfter)
    printPolygons(polygons, image)
    showImage(img, image)
    return figureAfter

def Move(figure, img):
    image = Image.new(mode = "RGB", size = (frameSize, frameSize), color=white)
    addAxles(image)
    figureAfter = affinMove(figure, 100)
    polygons = divisionIntoPolygons(figureAfter)
    printPolygons(polygons, image)
    showImage(img, image)