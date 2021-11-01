from math import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QFileDialog, QLineEdit,
    QHBoxLayout, QVBoxLayout
)

from PyQt5.QtCore import Qt, center # нужна константа Qt.KeepAspectRatio для изменения размеров с сохранением пропорций
from PyQt5.QtGui import QPixmap # оптимизированная для показа на экране картинка

from PIL import Image
from PIL.ImageQt import ImageQt

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
magenta = (255, 0, 255)

colors = [red, green, blue, black, magenta]

def getBall3D(R, numberOfSteps):    
    ball3D = []

    z = - R
    stepZ = round(2 * R / (numberOfSteps - 1)) 
    
    for i in range(numberOfSteps):
        temp = []
        Rz = round(sqrt(pow(R, 2) - pow(z, 2))) 
        x = - Rz
        stepX = round(2 * Rz / (numberOfSteps - 1))
        for j in range(numberOfSteps):
            y1 = round(sqrt(pow(Rz, 2) - pow(x, 2)))
            y2 = round(-sqrt(pow(Rz, 2) - pow(x, 2)))
            temp.append((x, y1, z))
            temp.append((x, y2, z))
            x += stepX
        ball3D.append(temp)
        z += stepZ
    return ball3D

def getProjection(ball3D):
    ball2D = []
    for i in range(len(ball3D)):
        temp = []
        for j in range(len(ball3D[0])):
            dot = ball3D[i][j]
            xOld = dot[0]
            yOld = dot[1]
            zOld = dot[2]
            x =  round(- xOld * cos(pi / 4) + yOld * cos(pi / 4))
            y = round(zOld - xOld * sin(pi / 4)  - yOld * sin(pi / 4))
            temp.append((x, y))
        ball2D.append(temp)
    testPrint(ball2D)
    return ball2D

def start(R, step, img):

    image = Image.new(mode = "RGB", size = (400, 400), color=white)
    
    ball3D = getBall3D(R, step)
    ball2D = getProjection(ball3D)

    for i in range (len(ball2D)):
        for j in range (len(ball2D[0]) - 2):

            n = 200 # Смещение в положительную строну

            x0 = round(ball2D[i][j][0]) + n
            y0 = round(ball2D[i][j][1]) + n

            x1 = round(ball2D[i][j + 2][0]) + n
            y1 = round(ball2D[i][j + 2][1]) + n
            
            lineBresenham(image, colors[i % len(colors)], x0, y0, x1, y1)
        

        #lineBresenham(image, colors[i % len(colors)], x0, y0, x2, y2)
        #lineBresenham(image, colors[i % len(colors)], x0, y0, x2, y2)

    showImage(img, image)
        


def showImage(image, picture):
    image.hide()
    qim = ImageQt(picture)
    pixmapImage = QPixmap.fromImage(qim)
    w, h = image.width(), image.height()
    pixmapImage = pixmapImage.scaled(w, h)
    #pixmapImage = pixmapImage.scaled(w, h, Qt.KeepAspectRatio)
    image.setPixmap(pixmapImage)
    image.show()

def testPrint(mas):
    print("kz")
    for i in range(len(mas)):
        for j in range(len(mas[0])):
            print(mas[i][j], end='')
        print("")

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


