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
label1 = QLabel("Суммарный размер в байтах")
label2 = QLabel("Размер: ")

labelHost = QLabel("Введите хост")
labelUser = QLabel("Введите Имя")
labelPassword = QLabel("Введите пароль")
editTextHost = QLineEdit("91.222.128.11")
editTextUser = QLineEdit("testftp_guest")
editTextPassword = QLineEdit("12345")

label1.setFont(QtGui.QFont('Arial', 20))
label2.setFont(QtGui.QFont('Arial', 20))


str1 = QHBoxLayout()
str1.addWidget(labelHost, 20)
str1.addWidget(editTextHost, 80)

str2 = QHBoxLayout()
str2.addWidget(labelUser, 20)
str2.addWidget(editTextUser, 80)

str3 = QHBoxLayout()
str3.addWidget(labelPassword, 20)
str3.addWidget(editTextPassword, 80)



col = QVBoxLayout()
col.addWidget(label1)
col.addLayout(str1)
col.addLayout(str2)
col.addLayout(str3)
col.addWidget(label2)
col.addWidget(button)

win.setLayout(col)
win.show()



def onClick():
    size  = start(editTextHost.text(), editTextUser.text(), editTextPassword.text()) # Реализовать получение веса через функцию
    label2.setText("Размер: " + str(size) + " байт")

button.clicked.connect(onClick)
app.exec()