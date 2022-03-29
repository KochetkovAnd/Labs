from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui,QtCore
from FTPlib import *

width = 600
height = 400

app = QApplication([])
win = QWidget()
win.resize(width, height)
win.setWindowTitle("LR_3")

button = QPushButton("Посчитать размер файлов")
label1 = QLabel("Суммарный вес")
label2 = QLabel("")

label1.setFont(QtGui.QFont('Arial', 20))
label2.setFont(QtGui.QFont('Arial', 20))


col = QVBoxLayout()
col.addWidget(label1)
col.addWidget(label2)
col.addWidget(button)

win.setLayout(col)
win.show()

def onClick():
    size  = start() # Реализовать получение веса через функцию
    label2.setText(str(size))

button.clicked.connect(onClick)
app.exec()