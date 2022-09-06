from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui,QtCore
from main import *

width = 600
height = 400

loginEmail = "testkochet@gmail.com"
loginPassword = "12121212ee"
loginServerAdress = "smtp.gmail.com"
loginPort = 587

app = QApplication([])

win2 = QWidget()
win2.resize(600, 200)
win2.setWindowTitle("Данные аккаунта")

labelLogin = QLabel("Логин аккаунта: ")
labelPassword = QLabel("Пароль аккаунта: ")
labelServerAdress = QLabel("Адрес SMTP сервера: ")
labelPort = QLabel("Порт подключения к серверу: ")

editTextLogin = QLineEdit("testkochet@gmail.com")
editTextPassword = QLineEdit("12121212ee")
editTextServerAdress = QLineEdit("smtp.gmail.com")
editTextPort = QLineEdit("587")

button2 = QPushButton("Войти")

strw1 = QHBoxLayout()
strw1.addWidget(labelLogin, 30)
strw1.addWidget(editTextLogin, 70)

strw2 = QHBoxLayout()
strw2.addWidget(labelPassword, 30)
strw2.addWidget(editTextPassword, 70)

strw3 = QHBoxLayout()
strw3.addWidget(labelServerAdress, 30)
strw3.addWidget(editTextServerAdress, 70)

strw4 = QHBoxLayout()
strw4.addWidget(labelPort, 30)
strw4.addWidget(editTextPort, 70)

colw = QVBoxLayout()
colw.addLayout(strw1)
colw.addLayout(strw2)
colw.addLayout(strw3)
colw.addLayout(strw4)
colw.addWidget(button2)

win2.setLayout(colw)
#--------------------------------------
win = QWidget()
win.resize(width, height)
win.setWindowTitle("LR_4")

button = QPushButton("Отправить")
button3 = QPushButton("Прикрепить файл")

label1 = QLabel("Тема письма: ")
label2 = QLabel("Текст письма: ")
labelEmail = QLabel("Кому")

editTextEmail = QLineEdit("kochetpwr@gmail.com")
editTextSubject = QLineEdit("")
editTextMessage = QPlainTextEdit("")

label1.setFont(QtGui.QFont('Arial', 14))
label2.setFont(QtGui.QFont('Arial', 14))
labelEmail.setFont(QtGui.QFont('Arial', 14))

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
col.addWidget(button3)
col.addWidget(button)

win.setLayout(col)

win2.show()

msg = createMsg()

def onClick():    
    TO = editTextEmail.text()
    subject = editTextSubject.text()
    text = editTextMessage.toPlainText()
    sendMail(msg,loginEmail, loginPassword, loginEmail, TO, text, subject, loginServerAdress, loginPort)

def onClick2():
    global loginEmail, loginPassword, loginServerAdress, loginPort
    loginEmail = editTextLogin.text()
    loginPassword = editTextPassword.text()
    loginServerAdress = editTextServerAdress.text()
    loginPort = int(editTextPort.text())
    win2.hide()
    win.show()

def onClick3():
    add(msg) 

button.clicked.connect(onClick)
button2.clicked.connect(onClick2)
button3.clicked.connect(onClick3)
app.exec()