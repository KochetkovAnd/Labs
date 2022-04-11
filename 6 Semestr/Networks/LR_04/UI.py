from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui,QtCore
from main import *

width = 600
height = 400

app = QApplication([])
win = QWidget()
win.resize(width, height)
win.setWindowTitle("LR_4")

button = QPushButton("Отправить")

label1 = QLabel("Тема письма: ")
label2 = QLabel("Текст письма: ")
labelEmail = QLabel("Кому")

editTextEmail = QLineEdit("KochetPWR@yandex.ru")
editTextSubject = QLineEdit("")
editTextMessage = QPlainTextEdit("")

label1.setFont(QtGui.QFont('Arial', 16))
label2.setFont(QtGui.QFont('Arial', 16))
labelEmail.setFont(QtGui.QFont('Arial', 16))

str1 = QHBoxLayout()
str1.addWidget(labelEmail, 30)
str1.addWidget(editTextEmail, 70)

str2 = QHBoxLayout()
str2.addWidget(label1, 30)
str2.addWidget(editTextSubject, 70)

str3 = QHBoxLayout()
str3.addWidget(label2, 30)
str3.addWidget(editTextMessage, 70)

col = QVBoxLayout()
col.addLayout(str1)
col.addLayout(str2)
col.addLayout(str3)
col.addWidget(button)

win.setLayout(col)
win.show()

def onClick():
    email = ""
    password = ""
    FROM = ""
    TO = editTextEmail.text()
    subject = editTextSubject.text()
    text = editTextMessage.toPlainText()
    sendMail(email, password, FROM, TO, text, subject)

button.clicked.connect(onClick)
app.exec()