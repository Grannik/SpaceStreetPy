#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Подключение необходимых модулей
import math  # Модуль для математических операций
import time  # Модуль для работы со временем
from tkinter import *  # Импорт библиотеки для создания графического интерфейса

# Создание главного окна приложения
root = Tk()
root.title("Аналоговые часы")  # Заголовок окна

# Создание холста для рисования
canvas = Canvas(root, width=683, height=768, highlightthickness=0)  # Создание холста размером 500x550
canvas.place(x=0, y=0)  # Указание положения холста в окне (координаты x и y)

# Вставка фоновой картинки на холст
image = PhotoImage(file="SpaceStreetGifA0x683x768.gif")
#image = PhotoImage(file="SpaceStreetTime.gif")
canvas.create_image(0, 0, anchor=NW, image=image)

# Рисование прозрачной окружности циферблата
canvas.create_oval(88, 69, 595, 577, outline="LightCyan", width=1)  # Рисование окружности без обводки

# Рисование прозрачной окружности циферблата
canvas.create_oval(147, 128, 538, 519, outline="LightCyan", width=3)  # Рисование окружности без обводки

# Рисование прозрачной окружности циферблата
canvas.create_oval(168, 149, 516, 497, outline="LightCyan", width=1)  # Рисование окружности без обводки

# Рисование прозрачной окружности циферблата
canvas.create_oval(176, 157, 508, 489, outline="LightCyan", width=1)  # Рисование окружности без обводки

# Рисование 60 кружочков между окружностями
for i in range(60):
    angle = -i * 6 * math.pi / 180 + math.pi / 2  # Вычисление угла для каждого кружочка
    x = 342 + (170) * math.cos(angle) # Вычисление координаты x
    y = 323 - (170) * math.sin(angle) # Вычисление координаты y
    canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill="LightCyan", outline="LightCyan")

# Рисование 12 кружочков между окружностями
for i in range(12):
    angle = -i * 30 * math.pi / 180 + math.pi / 2  # Вычисление угла для каждого кружочка
    x = 342 + (185) * math.cos(angle) # Вычисление координаты x
    y = 323 - (185) * math.sin(angle) # Вычисление координаты y
    canvas.create_oval(x - 9, y - 9, x + 9, y + 9, outline="LightCyan", width=3)

# Рисование 12 кружочков между окружностями
for i in range(12):
    angle = -i * 30 * math.pi / 180 + math.pi / 2  # Вычисление угла для каждого кружочка
    x = 342 + (225) * math.cos(angle) # Вычисление координаты x
    y = 323 - (225) * math.sin(angle) # Вычисление координаты y
    canvas.create_oval(x - 28, y - 28, x + 28, y + 28, outline="LightCyan")

# Рисование линии 1-й час
canvas.create_line(455, 99, 455, 130, fill="LightCyan")

# Рисование линии 2-й час
canvas.create_line(536, 183, 536, 240, fill="LightCyan")

# Рисование линии 3-й час
for i in range(3):
    angle = -i * 120 * math.pi / 180 + math.pi / 2
    radius = 28
    center_x = 568
    center_y = 323
    x1 = center_x + (radius) * math.cos(angle)
    y1 = center_y - (radius) * math.sin(angle)
    next_i = (i + 1) % 3
    next_angle = -next_i * 120 * math.pi / 180 + math.pi / 2
    x2 = center_x + (radius) * math.cos(next_angle)
    y2 = center_y - (radius) * math.sin(next_angle)
    canvas.create_line(x1, y1, x2, y2, fill="LightCyan", width=1)

# Рисование линии 4-й час
for i in range(4):
    center_x = 538
    center_y = 435
    radius = 28
    angle = -i * 90 * math.pi / 180 + math.pi / 4  # Начало построения смещено на 45 градусов
    x1 = center_x + (radius) * math.cos(angle)
    y1 = center_y - (radius) * math.sin(angle)
    next_i = (i + 1) % 4
    next_angle = -next_i * 90 * math.pi / 180 + math.pi / 4
    x2 = center_x + (radius) * math.cos(next_angle)
    y2 = center_y - (radius) * math.sin(next_angle)
    canvas.create_line(x1, y1, x2, y2, fill="LightCyan", width=1)

# Рисование линии 5-й час
for i in range(5):
    center_x = 455
    center_y = 518
    radius = 28
    angle = -i * 144 * math.pi / 180 + math.pi / 2  # Угол поворота на 144 градуса для пятиконечной звезды
    x1 = center_x + (radius) * math.cos(angle)
    y1 = center_y - (radius) * math.sin(angle)
    next_i = (i + 1) % 5
    next_angle = -next_i * 144 * math.pi / 180 + math.pi / 2
    x2 = center_x + (radius) * math.cos(next_angle)
    y2 = center_y - (radius) * math.sin(next_angle)
    canvas.create_line(x1, y1, x2, y2, fill="LightCyan", width=1)

# Рисование линии 6-й час
for i in range(3):
    angle = -i * 120 * math.pi / 180 + math.pi / 2
    radius = 28
    center_x = 342
    center_y = 549
    x1 = center_x + (radius) * math.cos(angle)
    y1 = center_y - (radius) * math.sin(angle)
    next_i = (i + 1) % 3
    next_angle = -next_i * 120 * math.pi / 180 + math.pi / 2
    x2 = center_x + (radius) * math.cos(next_angle)
    y2 = center_y - (radius) * math.sin(next_angle)
    canvas.create_line(x1, y1, x2, y2, fill="LightCyan", width=1)

for i in range(3):
    angle = -i * 120 * math.pi / 180 + math.pi / 6
    radius = 28
    center_x = 342
    center_y = 549
    x1 = center_x + (radius) * math.cos(angle)
    y1 = center_y - (radius) * math.sin(angle)
    next_i = (i + 1) % 3
    next_angle = -next_i * 120 * math.pi / 180 + math.pi / 6
    x2 = center_x + (radius) * math.cos(next_angle)
    y2 = center_y - (radius) * math.sin(next_angle)
    canvas.create_line(x1, y1, x2, y2, fill="LightCyan", width=1)

canvas.create_line(327, 548, 359, 548, fill="LightCyan")
canvas.create_line(333, 534, 350, 563, fill="LightCyan")
canvas.create_line(350, 534, 333, 563, fill="LightCyan")

# Рисование линии 7-й час
for i in range(7):
    center_x = 219
    center_y = 519
    radius = 28
    angle = -i * (360 / 7) * math.pi / 180 + math.pi / 2  # Угол поворота для семиконечной звезды
    x1 = center_x + (radius) * math.cos(angle) + 10
    y1 = center_y - (radius) * math.sin(angle) - 1
    next_i = (i + 3) % 7  # Для семиконечной звезды меняем смещение на 3 шага
    next_angle = -next_i * (360 / 7) * math.pi / 180 + math.pi / 2
    x2 = center_x + (radius) * math.cos(next_angle) + 10
    y2 = center_y - (radius) * math.sin(next_angle) - 1
    canvas.create_line(x1, y1, x2, y2, fill="LightCyan", width=1)

# Рисование линии 8-й час
for i in range(4):
    angle = -i * 90 * math.pi / 180 + math.pi / 2
    radius = 27
    x1 = 147 + (radius) * math.cos(angle)
    y1 = 436 - (radius) * math.sin(angle)
    next_i = (i + 1) % 4
    next_angle = -next_i * 90 * math.pi / 180 + math.pi / 2
    x2 = 147 + (radius) * math.cos(next_angle)
    y2 = 436 - (radius) * math.sin(next_angle)
    canvas.create_line(x1, y1, x2, y2, fill="LightCyan", width=1)

for i in range(4):
    angle = -i * 90 * math.pi / 180 + math.pi / 4
    radius = 27
    x1 = 147 + (radius) * math.cos(angle)
    y1 = 436 - (radius) * math.sin(angle)
    next_i = (i + 1) % 4
    next_angle = -next_i * 90 * math.pi / 180 + math.pi / 4
    x2 = 147 + (radius) * math.cos(next_angle)
    y2 = 436 - (radius) * math.sin(next_angle)
    canvas.create_line(x1, y1, x2, y2, fill="LightCyan", width=1)

# Рисование линии 9-й час
for i in range(3):
    angle = -i * 120 * math.pi / 180 + math.pi / 2
    radius = 28
    center_x = 118
    center_y = 323
    x1 = center_x + (radius) * math.cos(angle)
    y1 = center_y - (radius) * math.sin(angle)
    next_i = (i + 1) % 3
    next_angle = -next_i * 120 * math.pi / 180 + math.pi / 2
    x2 = center_x + (radius) * math.cos(next_angle)
    y2 = center_y - (radius) * math.sin(next_angle)
    canvas.create_line(x1, y1, x2, y2, fill="LightCyan", width=1)

for i in range(3):
    angle = -i * 120 * math.pi / 180 + math.pi / 2 + 2 * math.pi / 9  # Поворот на одну девятую окружности вправо
    radius = 28
    center_x = 118
    center_y = 323
    x1 = center_x + radius * math.cos(angle)
    y1 = center_y - radius * math.sin(angle)
    next_i = (i + 1) % 3
    next_angle = -next_i * 120 * math.pi / 180 + math.pi / 2 + 2 * math.pi / 9  # Поворот на одну девятую окружности вправо
    x2 = center_x + radius * math.cos(next_angle)
    y2 = center_y - radius * math.sin(next_angle)
    canvas.create_line(x1, y1, x2, y2, fill="LightCyan", width=1)

for i in range(3):
    angle = -i * 120 * math.pi / 180 + math.pi / 2 - 2 * math.pi / 9  # Поворот на одну девятую окружности вправо
    radius = 28
    center_x = 118
    center_y = 323
    x1 = center_x + radius * math.cos(angle)
    y1 = center_y - radius * math.sin(angle)
    next_i = (i + 1) % 3
    next_angle = -next_i * 120 * math.pi / 180 + math.pi / 2 - 2 * math.pi / 9  # Поворот на одну девятую окружности вправо
    x2 = center_x + radius * math.cos(next_angle)
    y2 = center_y - radius * math.sin(next_angle)
    canvas.create_line(x1, y1, x2, y2, fill="LightCyan", width=1)

# Рисование линии 10-й час
for i in range(5):
    center_x = 147
    center_y = 210
    radius = 28
    angle = -i * 144 * math.pi / 180 + math.pi / 2  # Угол поворота на 144 градуса для пятиконечной звезды
    x1 = center_x + (radius) * math.cos(angle)
    y1 = center_y - (radius) * math.sin(angle)
    next_i = (i + 1) % 5
    next_angle = -next_i * 144 * math.pi / 180 + math.pi / 2
    x2 = center_x + (radius) * math.cos(next_angle)
    y2 = center_y - (radius) * math.sin(next_angle)
    canvas.create_line(x1, y1, x2, y2, fill="LightCyan", width=1)

for i in range(5):
    center_x = 147
    center_y = 210
    radius = 28
    angle = -i * 144 * math.pi / 180 + math.pi / 2  # Угол поворота на 144 градуса для пятиконечной звезды
    x1 = center_x + radius * math.cos(angle)
    y1 = center_y + radius * math.sin(angle)  # Здесь изменение знака
    next_i = (i + 1) % 5
    next_angle = -next_i * 144 * math.pi / 180 + math.pi / 2
    x2 = center_x + radius * math.cos(next_angle)
    y2 = center_y + radius * math.sin(next_angle)  # Здесь изменение знака
    canvas.create_line(x1, y1, x2, y2, fill="LightCyan", width=1)

# Рисование линии 11-й час
for i in range(11):
    angle_increment = 360 / 11
    center_x = 230
    center_y = 128
    radius = 28
    angle = -i * angle_increment * math.pi / 180 + math.pi / 2
    x1 = center_x + radius * math.cos(angle)
    y1 = center_y - radius * math.sin(angle)
    next_i = (i + 4) % 11 # Смещение на 4 шага вперед для 11-конечной звезды
    next_angle = -next_i * angle_increment * math.pi / 180 + math.pi / 2
    x2 = center_x + radius * math.cos(next_angle)
    y2 = center_y - radius * math.sin(next_angle)
    canvas.create_line(x1, y1, x2, y2, fill="LightCyan", width=1)

# Рисование линии 12-й час
for i in range(12):
    center_x = 342
    center_y = 98
    radius = 28
    angle = -i * 30 * math.pi / 180 + math.pi / 2 + 2 * math.pi / 24  # Поворот на одну 24-ю окружность
    x1 = center_x + radius * math.cos(angle)
    y1 = center_y - radius * math.sin(angle)
    next_i = (i + 1) % 12
    next_angle = -next_i * 30 * math.pi / 180 + math.pi / 2 + 2 * math.pi / 24  # Поворот на одну 24-ю окружность
    x2 = center_x + radius * math.cos(next_angle)
    y2 = center_y - radius * math.sin(next_angle)
    canvas.create_line(x1, y1, x2, y2, fill="LightCyan", width=1)

canvas.create_line(335, 71, 335, 86, fill="LightCyan")
canvas.create_line(350, 71, 350, 86, fill="LightCyan")
#
canvas.create_line(364, 78, 350, 86, fill="LightCyan")
canvas.create_line(368, 91, 356, 98, fill="LightCyan")
#
canvas.create_line(321, 78, 335, 86, fill="LightCyan")
canvas.create_line(317, 91, 328, 98, fill="LightCyan")
# Вторая пара.
canvas.create_line(350, 109, 350, 126, fill="LightCyan")
canvas.create_line(335, 109, 335, 126, fill="LightCyan")
#
canvas.create_line(328, 99, 314, 106, fill="LightCyan")
canvas.create_line(334, 111, 319, 118, fill="LightCyan")
#
canvas.create_line(354, 98, 371, 106, fill="LightCyan")
canvas.create_line(351, 110, 365, 119, fill="LightCyan")
# Снежинка
canvas.create_line(327, 98, 360, 98, fill="LightCyan")
canvas.create_line(334, 84, 351, 113, fill="LightCyan")
canvas.create_line(351, 84, 334, 112, fill="LightCyan")

for i in range(6):
    center_x = 342
    center_y = 98
    radius = 16
    angle = -i * 60 * math.pi / 180 + math.pi / 2 + 2 * math.pi / 12  # Поворот на одну 12-ю окружность
    x1 = center_x + radius * math.cos(angle)
    y1 = center_y - radius * math.sin(angle)
    next_i = (i + 1) % 6
    next_angle = -next_i * 60 * math.pi / 180 + math.pi / 2 + 2 * math.pi / 12  # Поворот на одну 12-ю окружность
    x2 = center_x + radius * math.cos(next_angle)
    y2 = center_y - radius * math.sin(next_angle)
    canvas.create_line(x1, y1, x2, y2, fill="LightCyan", width=1)

# Основной бесконечный цикл
def close_app(event):
    root.quit()  # Завершение работы приложения

# Привязываем функцию закрытия к событию "Control + Q"
root.bind("<Control-q>", close_app)

def update_clock():
    canvas.delete("clock_hands")  # Удаление предыдущих стрелок

    # Получение текущего времени
    time_now = time.localtime()
    time_sec = int(time.strftime("%S", time_now))
    time_hour = int(time.strftime("%I", time_now))
    time_min = int(time.strftime("%M", time_now))

    # Вычисление углов для стрелок
    sec_angle = 6 * time_sec
    min_angle = 6 * (time_min + (1 / 60) * time_sec)
    hour_angle = 30 * (time_hour + (1 / 60) * time_min)

    # Вычисление координаты центра циферблата
    center_x = 341
    center_y = 323

    # Регулирование длины минутной стрелки
    minute_hand_length = 173  # Новая длина стрелки
    x_end_min = center_x - minute_hand_length * math.cos(min_angle * math.pi / 180 + math.pi / 2)
    y_end_min = center_y - minute_hand_length * math.sin(min_angle * math.pi / 180 + math.pi / 2)

    line_min = canvas.create_line(
        center_x, center_y,
        x_end_min, y_end_min,
        width=3,
        fill='LightCyan',
        tags="clock_hands"
    )

    # Регулирование длины часовой стрелки
    hour_hand_length = 167  # Новая длина стрелки
    x_end_hour = center_x - hour_hand_length * math.cos(hour_angle * math.pi / 180 + math.pi / 2)
    y_end_hour = center_y - hour_hand_length * math.sin(hour_angle * math.pi / 180 + math.pi / 2)

    line_hour = canvas.create_line(
        center_x, center_y,
        x_end_hour, y_end_hour,
        width=5,
        fill='LightCyan',
        tags="clock_hands"
    )

    # Регулирование длины секундной стрелки
    second_hand_length = 194  # Новая длина стрелки
    x_end_sec = center_x - second_hand_length * math.cos(sec_angle * math.pi / 180 + math.pi / 2)
    y_end_sec = center_y - second_hand_length * math.sin(sec_angle * math.pi / 180 + math.pi / 2)

    line_sec = canvas.create_line(
        center_x, center_y,
        x_end_sec, y_end_sec,
        width=2,
        fill='LightCyan',
        tags="clock_hands"
    )


    # Перезапуск функции обновления через 1000 миллисекунд (1 секунда)
    root.after(1000, update_clock)

# Запуск первичного обновления часов
update_clock()

# Запуск главного цикла обработки событий Tkinter
root.mainloop()
