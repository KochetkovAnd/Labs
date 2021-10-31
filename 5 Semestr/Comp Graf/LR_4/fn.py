import os
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

def cloneImg(img):
    w, h = img.size
    copyImg = Image.new(mode = "RGB", size = (w, h), color=white)

    for i in range(w):
        for j in range(h):
            copyImg.putpixel((i, j), img.getpixel((i, j)))
    return copyImg

def addNeighbors(img, i ,j):
    colors = []
    colors.append(1 if black == img.getpixel((i, j)) else 0)
    colors.append(1 if black == img.getpixel((i, j - 1)) else 0)
    colors.append(1 if black == img.getpixel((i + 1, j - 1)) else 0)
    colors.append(1 if black == img.getpixel((i + 1, j)) else 0)
    colors.append(1 if black == img.getpixel((i + 1, j + 1)) else 0)
    colors.append(1 if black == img.getpixel((i, j + 1)) else 0)
    colors.append(1 if black == img.getpixel((i - 1, j + 1)) else 0)
    colors.append(1 if black == img.getpixel((i - 1, j)) else 0)
    colors.append(1 if black == img.getpixel((i - 1, j - 1)) else 0) 
    return colors

def subiteration1(colors):

    T1 = A(colors) >= 2 and A(colors) <= 6
    T2 = B(colors) == 1
    T3 = colors[1]*colors[3]*colors[5] == 0
    T4 = colors[3]*colors[5]*colors[7] == 0

    return T1 and T2 and T3 and T4

def subiteration2(colors):

    T1 = A(colors) >= 2 and A(colors) <= 6
    T2 = B(colors) == 1
    T3 = colors[1]*colors[3]*colors[7] == 0
    T4 = colors[1]*colors[5]*colors[7] == 0

    return T1 and T2 and T3 and T4

def A(mas):
    k = 0
    for i in range(1, len(mas)):
        if mas[i] == 1:
            k += 1
    return k

def B(mas):
    k = 0
    for i in range(1,len(mas) - 1):
        if mas[i] == 0 and mas[i + 1] == 1:
            k +=1
    if mas[1] == 1 and mas[8] == 0:
        k += 1
    return k

def getGray(color):
    return round(color[0] * 0.299 + color[1] * 0.587 + color[2] * 0.114)

def showImage(image, picture):
    image.hide()
    qim = ImageQt(picture)
    pixmapImage = QPixmap.fromImage(qim)
    w, h = image.width(), image.height()
    #pixmapImage = pixmapImage.scaled(w, h)
    pixmapImage = pixmapImage.scaled(w, h, Qt.KeepAspectRatio)
    image.setPixmap(pixmapImage)
    image.show()
