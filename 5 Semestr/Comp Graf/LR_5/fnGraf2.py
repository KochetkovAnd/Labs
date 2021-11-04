from math import pi
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL.ImageQt import ImageQt

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

n = 300

from fnMath2 import *

def showImage(image, picture):
    image.hide()
    qim = ImageQt(picture)
    pixmapImage = QPixmap.fromImage(qim)
    w, h = image.width(), image.height()
    pixmapImage = pixmapImage.scaled(w, h)
    #pixmapImage = pixmapImage.scaled(w, h, Qt.KeepAspectRatio)
    image.setPixmap(pixmapImage)
    image.show()

def lineBresenham(img, color, x0, y0, x1, y1): #Инкрементный алгоритм Брезенхама для линии
    if abs(x0 - x1) >= abs(y0 - y1):
        if x1 == x0:    
            for y in range(min(y0, y1), max(y0, y1)):
                img.putpixel((x0, y), color)
            
        else:
            if x0 < x1:
                x = x0
                y = y0
                dx = x1 - x0
                dy = y1 - y0
            else:
                x = x1
                y = y1
                dx = x0 - x1
                dy = y0 - y1

            m = abs(dy / dx)
            e = m - 1 / 2
            i = 0

            img.putpixel((x, y), color)

            while i < dx:
                if e >= 0:
                    if dy >= 0:
                        y += 1
                    else:
                        y -= 1
                    e += m - 1
                else:
                    e +=m
                x += 1
                img.putpixel((x, y), color)
                i+=1
    else:
        if y0 < y1:
            x = x0
            y = y0
            dy = y1 - y0
            dx = x1 - x0
            
        else:
            x = x1
            y = y1
            dy = y0 - y1
            dx = x0 - x1
            

        m = abs(dx / dy)
        e = m - 1 / 2
        i = 0

        img.putpixel((x, y), color)

        while i < dy:
            if e >= 0:
                if dx >= 0:
                    x += 1
                else:
                    x -= 1
                e += m - 1
            else:
                e +=m
            y += 1
            img.putpixel((x, y), color)
            i+=1

def addAxles(image):  
    axlesLenght = 250
    axles3D = [[(0, 0, 0),(axlesLenght,0 , 0),(0, axlesLenght, 0),(0, 0, axlesLenght)]]
    axles2D = projectionToPrint(axles3D)

    x0 = round(axles2D[0][0][0]) + n
    y0 = round(axles2D[0][0][1]) + n

    x1 = round(axles2D[0][1][0]) + n
    y1 = round(axles2D[0][1][1]) + n

    x2 = round(axles2D[0][2][0]) + n
    y2 = round(axles2D[0][2][1]) + n

    x3 = round(axles2D[0][3][0]) + n
    y3 = round(axles2D[0][3][1]) + n

    lineBresenham(image, red, x0, y0, x1, y1)
    lineBresenham(image, red, x0, y0, x2, y2)
    lineBresenham(image, red, x0, y0, x3, y3)

def printPolygons(polygons, image):

    for polygon in polygons:
        xN, yN, zN = normalVector(polygon)
        if round(xN + yN + zN) >= 0:
            M1 = polygon[0]
            M2 = polygon[1]
            M3 = polygon[2]
            M4 = polygon[3]

            x1, y1 = getXY(M1)
            x2, y2 = getXY(M2)
            x3, y3 = getXY(M3)
            x4, y4 = getXY(M4)
            x1 += n
            x2 += n
            x3 += n
            x4 += n

            y1 += n
            y2 += n
            y3 += n
            y4 += n

            lineBresenham(image, black, x1, y1, x2, y2)
            lineBresenham(image, black, x2, y2, x3, y3)
            lineBresenham(image, black, x3, y3, x4, y4)
            lineBresenham(image, black, x4, y4, x1, y1)