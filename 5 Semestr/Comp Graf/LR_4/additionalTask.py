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

from fn import *

width = 1400
height = 800

white = (255, 255, 255)
black = (0, 0, 0)

img = Image.new(mode = "RGB", size = (1,1), color=white)

app2 = QApplication([])
win = QWidget()
win.resize(width, height)
win.setWindowTitle("Дополнительные задания")

image1 = QLabel("Картинка 1")
image2 = QLabel("Картинка 2")
image3 = QLabel("Картинка 3")

button_loading = QPushButton("Загрузка изображения")
button_first_task = QPushButton("Зонга-Суэна")
button_third_task = QPushButton("Волновой Алгоритм")

row1 = QHBoxLayout()
row2 = QHBoxLayout()

row1.addWidget(image1)
row1.addWidget(image2)
row1.addWidget(image3)
row2.addWidget(button_loading)
row2.addWidget(button_first_task)
row2.addWidget(button_third_task)

col = QVBoxLayout()

col.addLayout(row1)
col.addLayout(row2)

win.setLayout(col)
win.show()

def onClick():
    global img
    img = start()



def onClickFirstTask():

    w, h = img.size
    img2, img2test = cloneImg(img),cloneImg(img)

    key = True
    while key:
        key = False
        for i in range(1, w - 1):
            for j in range(1, h - 1):
                if img2.getpixel((i, j)) == black:
                    colors = addNeighbors(img2, i , j)
                    if subiteration1(colors) :
                        img2test.putpixel((i, j), white)
                        key = True

        img2 = cloneImg(img2test)

        for i in range(1, w - 1):
            for j in range(1, h - 1):
                if img2.getpixel((i, j)) == black:
                    colors = addNeighbors(img2, i , j)
                    if subiteration2(colors):
                        img2test.putpixel((i, j), white)
                        key = True

        img2 = cloneImg(img2test)    
    
    showImage(image2, img2)

def onClickThirdTask():
    pass

   
def start():
    workdir = QFileDialog.getOpenFileName()[0]
    img = Image.open(workdir)
    w, h = img.size

    for i in range(w):
        for j in range(h):
            color = getGray(img.getpixel((i, j)))

            if color > 120:
                img.putpixel((i, j), white)
            else:
                img.putpixel((i, j), black)
    showImage(image1, img)
    return img


button_loading.clicked.connect(onClick)
button_first_task.clicked.connect(onClickFirstTask)
button_third_task.clicked.connect(onClickThirdTask)

app2.exec()