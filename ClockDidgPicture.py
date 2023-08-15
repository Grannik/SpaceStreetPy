#!/usr/bin/env python3
import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap, QFont, QColor
from PyQt5.QtCore import Qt, QTimer

class ClockWidget(QWidget):
    def __init__(self, left_margin=0, top_margin=0, left_margin_big=0, top_margin_big=0):
        super().__init__()
        self.left_margin = left_margin
        self.top_margin = top_margin
        self.left_margin_big = left_margin_big
        self.top_margin_big = top_margin_big
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 768, 256)
        self.setWindowTitle("Часы")

        # Загружаем картинку и устанавливаем ее как фон окна 683x768
        pixmap = QPixmap("SpaceStreetGifA0x683x768.gif")
        self.background = QLabel(self)
        self.background.setPixmap(pixmap)
        self.background.setGeometry(0, 0, 683, 768)

        # Добавляем часы с большими цифрами и цветом Black (нижний слой)
        self.clock_label_big = QLabel(self)
        font_big = QFont()
        font_big.setPointSize(41)  # Больший размер
        self.clock_label_big.setFont(font_big)
        self.clock_label_big.setAlignment(Qt.AlignCenter)
        black_color = QColor(0, 0, 0, 5)  # Черный цвет с прозрачностью (значение альфа-канала = 150)
        self.clock_label_big.setStyleSheet(f"color: {black_color.name()};")

        # Создаем эффект для обводки MidnightBlue у черных часов (нижний слой)
        shadow_effect_big = QGraphicsDropShadowEffect(self)
        shadow_effect_big.setBlurRadius(30)  # Более сильная обводка
        shadow_effect_big.setColor(QColor("MidnightBlue"))
        shadow_effect_big.setOffset(0, 0)
        self.clock_label_big.setGraphicsEffect(shadow_effect_big)

        # Добавляем часы с маленькими цифрами и цветом Azure (верхний слой)
        self.clock_label_small = QLabel(self)
        font_small = QFont()
        font_small.setPointSize(40)
        self.clock_label_small.setFont(font_small)
        self.clock_label_small.setAlignment(Qt.AlignCenter)
        azure_color = QColor(240, 255, 255, 150)  # Цвет Azure с прозрачностью (значение альфа-канала = 150)
        self.clock_label_small.setStyleSheet(f"color: {azure_color.name()};")

        # Создаем эффект для обводки MidnightBlue у маленьких часов (верхний слой)
        shadow_effect_small = QGraphicsDropShadowEffect(self)
        shadow_effect_small.setBlurRadius(10)
        shadow_effect_small.setColor(QColor("MidnightBlue"))
        shadow_effect_small.setOffset(0, 0)
        self.clock_label_small.setGraphicsEffect(shadow_effect_small)

        # Размещаем оба QLabel на виджете (верхний слой над нижним)
        self.clock_label_small.move(self.left_margin, self.top_margin)
        self.clock_label_big.move(self.left_margin_big, self.top_margin_big)

        self.updateTime()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)

    def updateTime(self):
        current_time = time.strftime("%H:%M:%S")
        self.clock_label_small.setText(current_time)
        self.clock_label_big.setText(current_time)

    def keyPressEvent(self, event):
        # Проверяем, была ли нажата комбинация клавиш Ctrl + Q
        if event.key() == Qt.Key_Q and event.modifiers() == Qt.ControlModifier:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Здесь можно указать отступы сверху и слева (в пикселях) для каждой пары часов
    left_margin = 238
    top_margin = 78

    left_margin_big = 233
    top_margin_big = 76

    clock_widget = ClockWidget(left_margin, top_margin, left_margin_big, top_margin_big)
    clock_widget.show()
    sys.exit(app.exec_())

