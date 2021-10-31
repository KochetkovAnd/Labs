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

width = 1200
height = 800



white = (255, 255, 255)
black = (0, 0, 0)

img = Image.new(mode = "RGB", size = (1,1), color=white)

app = QApplication([])
win = QWidget()
win.resize(width, height)
win.setWindowTitle("LR_4")


image1 = QLabel("Картинка 1")
image2 = QLabel("Картинка 2")
image3 = QLabel("Картинка 3")
image4 = QLabel("Картинка 4")


button_loading = QPushButton("Загрузка изображения")


editText_1 = QLineEdit()
editText_2 = QLineEdit()
button_task2 = QPushButton("Выполнить Задание 2")

col1 = QVBoxLayout()
col1.addWidget(editText_1)
col1.addWidget(editText_2)
row3 = QHBoxLayout()
row3.addWidget(button_loading, 30)
row3.addLayout(col1, 40)
row3.addWidget(button_task2, 30)


row1 = QHBoxLayout()
row2 = QHBoxLayout()

row1.addWidget(image1)
row1.addWidget(image2)
row2.addWidget(image3)
row2.addWidget(image4)

col = QVBoxLayout()
col.addLayout(row1)
col.addLayout(row2)
col.addLayout(row3)

win.setLayout(col)
win.show()

def onClick():
    global img

    img = start()

    firstTask(img)
    thirdTask(img)

def onClickSecond():
    global img
    secondTask(img)
   
def start():
    workdir = QFileDialog.getOpenFileName()[0]
    img = Image.open(workdir)
    showImage(image1, img)
    return img

def firstTask(image):
    w, h = image.size
    img2 = Image.new(mode = "RGB", size = (w, h), color=white)
    for i in range(w):
        for j in range(h):
            color = image.getpixel((i, j))
            partNewColor = getGray(color)
            newColor = (partNewColor, partNewColor, partNewColor)
            img2.putpixel((i, j), newColor)
    showImage(image2, img2)

def secondTask(image):
    w, h = image.size
    a, b = editText_1.text(),editText_2.text()

    limit1 = int(editText_1.text())
    limit2 = int(editText_2.text())
    #limit1 = 240
    #limit2 = 50

    img3 = Image.new(mode = "RGB", size = (w, h), color=white)
    for i in range(w):
        for j in range(h):
            color = image.getpixel((i, j))
            colorFinal = colorAdapt(color, limit1, limit2)                
            img3.putpixel((i, j), colorFinal)
    showImage(image3, img3)

def thirdTask(image):
    w, h = image.size
    img4 = Image.new(mode = "RGB", size = (w, h), color=white)

    for i in range(w):
        for j in range(h):
            color = image.getpixel((i, j))
            partNewColor = getGray(color)
            newColor = (partNewColor, partNewColor, partNewColor)
            img4.putpixel((i, j), newColor)

    for i in range(w):
        for j in range(h):
            if i >= 1 and i <= w - 2 and j >= 1 and j <= h - 2:
                mas = getNeighbors(image, i, j, orentation= "all")                
            elif i == 0 and  j >= 1 and j <= h - 2:
                mas = getNeighbors(image, i, j, orentation= "right")
            elif i == w - 1 and j >= 1 and j <= h - 2:
                mas = getNeighbors(image, i, j, orentation= "left")
            elif i >= 1 and i <= w - 2 and j == 0:
                mas = getNeighbors(image, i, j, orentation= "down")
            elif i >= 1 and i <= w - 2 and j == h - 1:
                mas = getNeighbors(image, i, j, orentation= "up")
            elif i == 0 and j == 0:
                mas = getNeighbors(image, i, j, orentation= "rightup")
            elif i == 0 and j == h - 1:
                mas = getNeighbors(image, i, j, orentation= "rightdown")
            elif i == w - 1 and j == 0:
                mas = getNeighbors(image, i, j, orentation= "leftup")
            elif i == w - 1 and j == h - 1:
                mas = getNeighbors(image, i, j, orentation= "leftdown")
            mas = mySort(mas)
            median = mas[int(len(mas) / 2)]
            newColor = (median, median, median)
            img4.putpixel((i, j), newColor)


    showImage(image4, img4)


def getNeighbors(image, i, j, orentation = "all"):
    neighbors = []
    if orentation == "all":
        r1,l1,r2,l2 = -1, 2, -1, 2

    elif orentation  == "right":
        r1,l1,r2,l2 = 0, 2, -1, 2
    elif orentation  == "left":
        r1,l1,r2,l2 = -1, 1, -1, 2
    elif orentation  == "down":
        r1,l1,r2,l2 = -1, 2, 0, 2
    elif orentation  == "up":
        r1,l1,r2,l2 = -1, 2, -1, 1

    elif orentation  == "rightup":
        r1,l1,r2,l2 = 0, 2, 0, 2
    elif orentation  == "rightdown":
        r1,l1,r2,l2 = 0, 2, -1, 1
    elif orentation  == "leftup":
        r1,l1,r2,l2 = -1, 1, 0, 2
    elif orentation  == "leftdown":
        r1,l1,r2,l2 = -1, 1, -1, 1   

    for h1 in  range(r1, l1):
        for h2 in  range(r2, l2):
            neighbors.append(getGray(image.getpixel((i + h1, j + h2))))
    return neighbors

def mySort(mas):
    for i in range(len(mas)):
        min = mas[0]
        minNumber = 0 
        for j in range(i, len(mas)):            
            if mas[j] < min:
                min = mas[j]
                minNumber = j
        mas[minNumber] = mas[i]
        mas[i] = min
    return mas

def getGray(color):
    return round(color[0] * 0.299 + color[1] * 0.587 + color[2] * 0.114)

def colorAdapt(color, limit1, limit2):
    if getGray(color) > limit1:
        return black
    elif getGray(color) < limit2:
        return white
    else:
        limit1 -= limit2
        gray = getGray(color)
        gray -= limit2
        limit2 = 0
        pr = 255 / (limit1 - limit2)
        gray *= pr
        gray = round(255 - gray)
        return(gray, gray, gray)


def showImage(image, picture):
    image.hide()
    qim = ImageQt(picture)
    pixmapImage = QPixmap.fromImage(qim)
    w, h = image.width(), image.height()
    pixmapImage = pixmapImage.scaled(w, h)
    #pixmapImage = pixmapImage.scaled(w, h, Qt.KeepAspectRatio)
    image.setPixmap(pixmapImage)
    image.show()






button_loading.clicked.connect(onClick)

button_task2.clicked.connect(onClickSecond)


app.exec()