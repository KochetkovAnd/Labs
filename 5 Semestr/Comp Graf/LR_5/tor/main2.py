from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QHBoxLayout, QVBoxLayout
)
from fnMain2 import *

width = 1600
height = 840

d = 35
n = 1
m = 1
numbeOfSteps = 40

app = QApplication([])
win = QWidget()
win.resize(width, height)
win.setWindowTitle("LR_5")

info = QLabel("Проекция супертороида")
button_stretch = QPushButton("Растяжение")
button_rotate_x = QPushButton("Вращение вокруг оси X")
button_rotate_z = QPushButton("Вращение вокруг оси Z")
button_move = QPushButton("Переместить")

image1 = QLabel("Картинка 1")
image2 = QLabel("Картинка 2")

row1 = QHBoxLayout()
row1.addWidget(info)
row1.addWidget(info)
row1.addWidget(button_rotate_x)
row1.addWidget(button_rotate_z)
row1.addWidget(button_stretch)
row1.addWidget(button_move)

row2 = QHBoxLayout()
row2.addWidget(image1)
row2.addWidget(image2)

col = QVBoxLayout()
col.addLayout(row1, 5)
col.addLayout(row2, 95)

win.setLayout(col)
win.show()

figure3D =  start(d, numbeOfSteps, n, m, image1)

def onStretch():
    Stretch(figure3D, image2)

def onRotateX():
    global figure3D
    figure3D = rotateX(figure3D, image2)

def onRotateZ():
    global figure3D
    figure3D = rotateZ(figure3D, image2)

def onMove():    
    Move(figure3D, image2)

button_stretch.clicked.connect(onStretch)
button_move.clicked.connect(onMove)
button_rotate_x.clicked.connect(onRotateX)
button_rotate_z.clicked.connect(onRotateZ)

app.exec()