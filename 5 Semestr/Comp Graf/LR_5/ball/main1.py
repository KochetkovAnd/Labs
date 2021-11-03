from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QHBoxLayout, QVBoxLayout
)
from fnGraf1 import *

width = 1600
height = 840

R = 100
numbeOfSteps = 20

app = QApplication([])
win = QWidget()
win.resize(width, height)
win.setWindowTitle("LR_5")

info = QLabel("Проекция шара")
button_task1 = QPushButton("Преобразование 1")
button_task2 = QPushButton("Преобразование 2")
button_task3 = QPushButton("Преобразование 3")

image1 = QLabel("Картинка 1")
image2 = QLabel("Картинка 2")

row1 = QHBoxLayout()
row1.addWidget(info)
row1.addWidget(button_task1)
row1.addWidget(button_task2)
row1.addWidget(button_task3)

row2 = QHBoxLayout()
row2.addWidget(image1)
row2.addWidget(image2)

col = QVBoxLayout()
col.addLayout(row1, 5)
col.addLayout(row2, 95)

win.setLayout(col)
win.show()

figure3D =  start(R, numbeOfSteps, image1)

def onClick1():
    task1(figure3D, image2)

def onClick2():
    task2(figure3D, image2)

def onClick3():    
    task3(figure3D, image2)

button_task1.clicked.connect(onClick1)
button_task2.clicked.connect(onClick2)
button_task3.clicked.connect(onClick3)

app.exec()