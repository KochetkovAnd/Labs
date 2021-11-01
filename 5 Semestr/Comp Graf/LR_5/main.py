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


width = 800
height = 500

R = 50
numbeOfSteps = 8

app = QApplication([])
win = QWidget()
win.resize(width, height)
win.setWindowTitle("LR_5")

info = QLabel("Проекция шара")

image1 = QLabel("Картинка 1")
image2 = QLabel("Картинка 2")


row1 = QHBoxLayout()
row1.addWidget(image1)
row1.addWidget(image2)

col = QVBoxLayout()
col.addWidget(info, 20)
col.addLayout(row1, 80)

win.setLayout(col)
win.show()

start(R, numbeOfSteps, image1)

app.exec()