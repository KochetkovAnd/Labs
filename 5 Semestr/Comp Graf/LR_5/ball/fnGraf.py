from math import pi
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL.ImageQt import ImageQt

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
magenta = (255, 0, 255)

colors = [red, green, blue, black, magenta]

frameSize = 600

n = 300 # Смещение в положительную строну

from fnMath import getBall3D, affinProjection, projectionToPrint, affin1, affin2, affin3


def start(R, step, img):

    image = Image.new(mode = "RGB", size = (frameSize, frameSize), color=white)
    addAxles(image)
    figure = addBall(R, step, image)   
    showImage(img, image)

    return figure

def task1(figure, img):
    image = Image.new(mode = "RGB", size = (frameSize, frameSize), color=white)
    addAxles(image)

    figureAfter = affin1(figure, 0.5, 0.5, 2)
    figure2D = projectionToPrint(figureAfter)
    printBall(figure2D, image) 

    showImage(img, image)

def task2(figure, img):
    image = Image.new(mode = "RGB", size = (frameSize, frameSize), color=white)
    addAxles(image)

    figureAfter = affin2(figure, pi/ 4)
    figure2D = projectionToPrint(figureAfter)
    printBall(figure2D, image) 

    showImage(img, image)

def task3(figure, img):
    image = Image.new(mode = "RGB", size = (frameSize, frameSize), color=white)
    addAxles(image)

    figureAfter = affin3(figure, 100)
    figure2D = projectionToPrint(figureAfter)
    printBall(figure2D, image) 

    showImage(img, image)

def addAxles(image):  
    axlesLenght = 250
    axles3D = [[(0, 0, 0),(axlesLenght,0 , 0),(0, axlesLenght, 0),(0, 0, axlesLenght)]]
    axles2D = projectionToPrint(axles3D)

    x0 = round(axles2D[0][0][0]) + n
    y0 = Ny(round(axles2D[0][0][1]) + n)

    x1 = round(axles2D[0][1][0]) + n
    y1 = Ny(round(axles2D[0][1][1]) + n)

    x2 = round(axles2D[0][2][0]) + n
    y2 = Ny(round(axles2D[0][2][1]) + n)

    x3 = round(axles2D[0][3][0]) + n
    y3 = Ny(round(axles2D[0][3][1]) + n)

    lineBresenham(image, red, x0, y0, x1, y1)
    lineBresenham(image, red, x0, y0, x2, y2)
    lineBresenham(image, red, x0, y0, x3, y3)

def addBall(R, step, image):
    ball3D = getBall3D(R, step)
    ball2D = projectionToPrint(ball3D)
    printBall(ball2D, image)   

    return ball3D

def printBall(ball2D, image):

    for i in range (len(ball2D)):
        for j in range (len(ball2D[0]) - 1):            

            x0 = round(ball2D[i][j][0]) + n
            y0 = Ny(round(ball2D[i][j][1]) + n)

            x1 = round(ball2D[i][j + 1][0]) + n
            y1 = Ny(round(ball2D[i][j + 1][1]) + n)
            
            lineBresenham(image, black, x0, y0, x1, y1)

    for i in range (len(ball2D) - 1):
        for j in range (len(ball2D[0])):

            x0 = round(ball2D[i][j][0]) + n
            y0 = Ny(round(ball2D[i][j][1]) + n)

            x1 = round(ball2D[i + 1][j][0]) + n
            y1 = Ny(round(ball2D[i + 1][j][1]) + n)
            
            lineBresenham(image, black, x0, y0, x1, y1)


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

def Ny(y):
    return frameSize - y + 1