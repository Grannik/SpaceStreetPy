#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Задаем размер окна
        self.setGeometry(0, 0, 683, 768)
        self.setWindowTitle("Повторяющиеся изображения")

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        # Создаем виджет для фона
        self.background = QWidget(self)
        self.background.setGeometry(0, 0, 683, 768)

        # Список с именами файлов изображений
        self.image_files = ["img1.gif", "img2.gif", "img3.gif", "img4.gif", "img5.gif"]
        self.current_image_index = 0

        # Запускаем таймер для смены фонового изображения
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.change_background)
        self.timer.start(1000)  # Изменяйте интервал в миллисекундах, как вам нужно

        self.show()

    def change_background(self):
        pixmap = QPixmap(self.image_files[self.current_image_index])
        self.background.setStyleSheet(f"background-image: url('{self.image_files[self.current_image_index]}'); background-repeat: repeat;")
        self.current_image_index = (self.current_image_index + 1) % len(self.image_files)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q and event.modifiers() == Qt.ControlModifier:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
