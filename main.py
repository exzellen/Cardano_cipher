import math
import random
import string

import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(761, 614)
        MainWindow.setStyleSheet("background-color: rgb(31, 40, 51);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 450, 831, 161))
        self.frame.setStyleSheet("background-color: rgb(20, 167, 108);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icon.png"))
        self.label.setObjectName("label")
        self.codeBtn = QtWidgets.QPushButton(self.frame)
        self.codeBtn.setGeometry(QtCore.QRect(190, 50, 260, 81))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(24)
        self.codeBtn.setFont(font)
        self.codeBtn.setStyleSheet("background-color: white;\n"
                                   "color: rgb(31, 40, 51);\n"
                                   "border: 3px outset #F64C72;\n"
                                   "border-radius: 10px;")
        self.codeBtn.setObjectName("codeBtn")
        self.uncodeBtn = QtWidgets.QPushButton(self.frame)
        self.uncodeBtn.setGeometry(QtCore.QRect(480, 50, 260, 81))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(24)
        self.uncodeBtn.setFont(font)
        self.uncodeBtn.setStyleSheet("background-color: white;\n"
                                     "color: rgb(31, 40, 51);\n"
                                     "border: 3px inset #F64C72;\n"
                                     "border-radius: 10px;")
        self.uncodeBtn.setObjectName("uncodeBtn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 0, 309, 41))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.label_2.setStyleSheet("color: rgb(254, 255, 255)")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.inputText.setGeometry(QtCore.QRect(190, 50, 551, 151))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        self.inputText.setFont(font)
        self.inputText.setStyleSheet("background-color: rgb(132, 132, 132);\n"
                                     "border: 4px outset #14A76C;\n"
                                     "border-radius: 40px;\n"
                                     "color: white;")
        self.inputText.setAlignment(QtCore.Qt.AlignCenter)
        self.inputText.setObjectName("inputText")
        self.printText = QtWidgets.QLineEdit(self.centralwidget)
        self.printText.setGeometry(QtCore.QRect(190, 280, 551, 151))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        self.printText.setFont(font)
        self.printText.setStyleSheet("background-color: rgb(132, 132, 132);\n"
                                     "border: 4px inset #14A76C;\n"
                                     "border-radius: 40px;\n"
                                     "color: white;")
        self.printText.setAlignment(QtCore.Qt.AlignCenter)
        self.printText.setObjectName("printText")
        self.key = QtWidgets.QLineEdit(self.centralwidget)
        self.key.setGeometry(QtCore.QRect(190, 220, 551, 41))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        self.key.setFont(font)
        self.key.setStyleSheet("background-color: rgb(132, 132, 132);\n"
                               "border: 4px solid #14A76C;\n"
                               "border-radius: 20px;\n"
                               "color: white;")
        self.key.setAlignment(QtCore.Qt.AlignCenter)
        self.key.setObjectName("key")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(63, 238, 230)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 51, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(63, 238, 230)")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 320, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(63, 238, 230)")
        self.label_5.setObjectName("label_5")
        self.reversBtn = QtWidgets.QPushButton(self.centralwidget)
        self.reversBtn.setGeometry(QtCore.QRect(80, 170, 101, 131))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.reversBtn.setFont(font)
        self.reversBtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.reversBtn.setStyleSheet("color: rgb(31, 40, 51);\n"
                                     "background-color: rgb(31, 40, 51);\n"
                                     "background-image: url(\"revers.png\");\n"
                                     "")
        self.reversBtn.setText("")
        self.reversBtn.setObjectName("reversBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 761, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "color: rgb(0, 0, 0);")
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionClicked()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Шифр Кардано"))
        MainWindow.setWindowIcon(QIcon("icon.png"))
        self.codeBtn.setText(_translate("MainWindow", "Закодировать"))
        self.uncodeBtn.setText(_translate("MainWindow", "Раскодировать"))
        self.label_2.setText(_translate("MainWindow", "Решетка Кардано"))
        self.inputText.setPlaceholderText("Hello!")
        self.printText.setPlaceholderText("@#$&^!")
        self.key.setPlaceholderText("100110")
        self.label_3.setText(_translate("MainWindow", "Исходный\n"
                                                      "текст"))
        self.label_4.setText(_translate("MainWindow", "Ключ"))
        self.label_5.setText(_translate("MainWindow", "Обработанный\n"
                                                      "текст"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))

    def actionClicked(self):
        self.codeBtn.clicked.connect(lambda: self.codeText())
        self.uncodeBtn.clicked.connect(lambda: self.decodeText())
        self.reversBtn.clicked.connect(lambda: self.reverseText())

    def reverseText(self):
        s = self.inputText.text()

        self.inputText.setText(str(self.printText.text()))
        self.printText.setText(s)

    def codeText(self):
        if not self.inputText.text().__len__():
            wnd = QMessageBox()
            wnd.setText("Некорректные данные!")
            wnd.setWindowTitle("Error")
            wnd.setIcon(QMessageBox.Critical)
            wnd.setWindowIcon(QIcon("favicon.ico"))
            wnd.exec_()

        else:
            msg = self.inputText.text()
            msg += "|"

            #размерность матрицы
            n = int(math.ceil((msg.__len__() / 4) ** (1 / 2)))

            codedRes = codeByCardanGrille(msg, n)

            encodeMsg = arrayToString(codedRes[0])
            keyMsg = arrayToString(codedRes[1])
            self.printText.setText(encodeMsg)
            self.key.setText(keyMsg)

    def decodeText(self):
        self.printText.clear()
        msg = self.inputText.text()
        key = self.key.text()

        decodedMsg = decodeByCardanGrille(msg, key)
        self.printText.setText(decodedMsg.split("|")[0])


def arrayToString(array):
    return "".join(s for s in np.array_str(array) if s not in "[ ]'" and s.isprintable())


def generateGrille(n: int):
    size = n * 2
    grille = np.zeros((size, size), dtype='uint8')

    # Прямой обход (0)
    seq = np.arange(1, n * n + 1)
    random.shuffle(seq)
    quant = random.randint(1, seq.shape[0] // 2) if seq.shape[0] > 1 else 0
    k = 1
    for i in range(size // 2):
        for j in range(size // 2):
            if k in seq[:quant]:
                grille[i, j] = 1
            k += 1

    # Обход при повороте 90
    seq = seq[quant:]
    quant = random.randint(1, seq.shape[0] // 2) if seq.shape[0] > 1 else 0
    k = 1
    for i in range(size // 2):
        for j in range(size // 2):
            if k in seq[:quant]:
                grille[j, size - i - 1] = 1
            k += 1

    # Обход при повороте 180
    seq = seq[quant:]
    quant = random.randint(1, seq.shape[0] // 2) if seq.shape[0] > 1 else 0
    k = 1
    for i in range(size // 2):
        for j in range(size // 2):
            if k in seq[:quant]:
                grille[size - i - 1, size - j - 1] = 1
            k += 1

    # Обход при повороте 270
    seq = seq[quant:]
    quant = seq.shape[0]
    k = 1
    for i in range(size // 2):
        for j in range(size // 2):
            if k in seq[:quant]:
                grille[size - j - 1, i] = 1
            k += 1

    return grille


def codeByCardanGrille(msg: str, n: int):
    msg = msg.replace(' ', '_')
    grille = generateGrille(n)
    codedGrl = np.zeros(grille.shape, 'U1')
    size = n * 2
    symbols = string.ascii_letters + string.digits + "_.,!?"

    # Прямой обход (0)
    for i in range(size):
        for j in range(size):
            if grille[i, j] == 1:
                if msg != '':
                    letter = msg[0]
                    msg = msg[1:]
                else:
                    letter = random.choice(symbols)
                codedGrl[i, j] = letter

    # Обход при повороте 90
    for i in range(size):
        for j in range(size):
            if grille[j, size - i - 1] == 1:
                if msg != '':
                    letter = msg[0]
                    msg = msg[1:]
                else:
                    letter = random.choice(symbols)
                codedGrl[i, j] = letter

    # Обход при повороте 180
    for i in range(size):
        for j in range(size):
            if grille[size - i - 1, size - j - 1] == 1:
                if msg != '':
                    letter = msg[0]
                    msg = msg[1:]
                else:
                    letter = random.choice(symbols)
                codedGrl[i, j] = letter

    # Обход при повороте 270
    for i in range(size):
        for j in range(size):
            if grille[size - j - 1, i] == 1:
                if msg != '':
                    letter = msg[0]
                    msg = msg[1:]
                else:
                    letter = random.choice(symbols)
                codedGrl[i, j] = letter

    return [codedGrl, grille]


def decodeByCardanGrille(codedMsg, key):
    codedGrl = np.array(list(codedMsg), dtype='U1')
    codedGrl = codedGrl.reshape((int(math.sqrt(codedGrl.shape[0])), -1))
    grille = np.array(list(key), dtype='uint8')
    grille = grille.reshape((int(math.sqrt(grille.shape[0])), -1))

    size = grille.shape[0]
    decodedMsg = ""

    # Прямой обход (0)
    for i in range(size):
        for j in range(size):
            if grille[i, j] == 1:
                decodedMsg += codedGrl[i, j]

    # Обход при повороте 90
    for i in range(size):
        for j in range(size):
            if grille[j, size - i - 1] == 1:
                decodedMsg += codedGrl[i, j]

    # Обход при повороте 180
    for i in range(size):
        for j in range(size):
            if grille[size - i - 1, size - j - 1] == 1:
                decodedMsg += codedGrl[i, j]

    # Обход при повороте 270
    for i in range(size):
        for j in range(size):
            if grille[size - j - 1, i] == 1:
                decodedMsg += codedGrl[i, j]

    decodedMsg = decodedMsg.replace('_', ' ')
    return decodedMsg


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
