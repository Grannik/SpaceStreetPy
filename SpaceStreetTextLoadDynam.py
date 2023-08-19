#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Задаем размер окна
        self.setGeometry(0, 0, 683, 768)
        self.setWindowTitle("Копируемый текст")

        # Загружаем картинку и устанавливаем ее как фон окна
        pixmap = QPixmap("SpaceStreetGifA0x683x768.gif")
        self.background = QLabel(self)
        self.background.setPixmap(pixmap)
        self.background.setGeometry(0, 0, 683, 768)

        # Добавляем текстовое поле
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(0, 0, 683, 600)
        self.text_edit.setStyleSheet("background-color: rgba(0, 0, 0, 100); color: white")

        # Добавляем кнопку для вывода текста 1
        self.button_text1 = QPushButton("Текст 1", self)
        self.button_text1.setGeometry(100, 650, 100, 50)
        self.button_text1.clicked.connect(self.load_text1)

        # Добавляем кнопку для вывода текста 2
        self.button_text2 = QPushButton("Текст 2", self)
        self.button_text2.setGeometry(500, 650, 100, 50)
        self.button_text2.clicked.connect(self.load_text2)

        self.show()

    def load_text1(self):
        with open("SpaceStreetPy.txt", "r") as file:
            text1 = file.read()
        self.text_edit.setPlainText(text1)

    def load_text2(self):
        with open("ClockDidgPicture.py", "r") as file:
            text2 = file.read()
        self.text_edit.setPlainText(text2)

    def keyPressEvent(self, event):
        # Проверяем, была ли нажата комбинация клавиш Ctrl + Q
        if event.key() == Qt.Key_Q and event.modifiers() == Qt.ControlModifier:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
