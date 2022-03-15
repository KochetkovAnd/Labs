from main import *
from helperFunctions import *
from PyQt5.QtWidgets import *

width = 1600
height = 800

app = QApplication([])
win = QWidget()
win.resize(width, height)
win.setWindowTitle("LR_2")

button = QPushButton("Построить\nдерево")
editText = QLineEdit()
treeText1 = QTextEdit()
treeText2 = QTextEdit()

label1 = QLabel("Список ссылок")
label2 = QLabel("Дерево ссылок")
label3 = QLabel("Введите адрес сайта:")


row1 = QHBoxLayout()
row1.addWidget(treeText1, 40)
row1.addWidget(treeText2, 60)

row2 = QHBoxLayout()
row2.addWidget(label3, 30)
row2.addWidget(editText, 60)
row2.addWidget(button, 10)

row3 = QHBoxLayout()
row3.addWidget(label1, 40)
row3.addWidget(label2, 60)

col = QVBoxLayout()
col.addLayout(row3, 10)
col.addLayout(row1, 80)
col.addLayout(row2, 10)

win.setLayout(col)
win.show()

def onClick():
    host = editText.text()
    list = removeURLWithV(getListByHost(host))
    treeText1.setText(listToText(list))
    treeText2.setText(Tree(list).onPrint())

button.clicked.connect(onClick)
app.exec()