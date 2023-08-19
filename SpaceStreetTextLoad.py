#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QLabel
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

        # Добавляем текст
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(0, 0, 683, 768)
        self.text_edit.setStyleSheet("background-color: rgba(0, 0, 0, 100); color: white")

        # Загружаем текст из файла
        with open("SpaceStreetPy.txt", "r") as file:
            initial_text = file.read()
        self.text_edit.setPlainText(initial_text)

        self.show()

    def keyPressEvent(self, event):
        # Проверяем, была ли нажата комбинация клавиш Ctrl + Q
        if event.key() == Qt.Key_Q and event.modifiers() == Qt.ControlModifier:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
