# Импортируем и инициализируем "pygame":
import pygame
import random
pygame.init() # Инициализация:

SCRIN_WIDTH = 800  # Переменные, задают ширину и высоту экрана в пикселях:
SCRIN_HEIGHT = 600
# Создпем переменную "screen", в которой будем хранить экран с заданными шириной и высотой экрана:
screen = pygame.display.set_mode((SCRIN_WIDTH, SCRIN_HEIGHT))
# Создаем заголовок экрана (set_caption - установить заголовок):
pygame.display.set_caption("Игра Тир")

# Загрузим иконку игры. Сохраним файл иконки в папкн "img":
icon = pygame.image.load("img/4123.jpg")
pygame.display.set_icon(icon) # Устанавливаем переменную "icon" с изображением как иконку:

# Создаим и загрузим картинку цели с высотой и шириной 80 пик:
target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

# Задаем координаты "Цели". Ширина (по иси - Х) - Это ширина экрана минус ширина картинки, чтобы
# каритнка не выходила за пределы экрана и также по высоте по оси - У:
target_x = random.randint(0, SCRIN_WIDTH - target_width)
target_y = random.randint(0, SCRIN_HEIGHT - target_height)
# Зададим Рамдомный цвет экрана:
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Условие цикла непрерывной работы программы. Как только переменная "running = false", программа
# закончиться работой "pygame.quit()"
running = True
while running:
    screen.fill(color) # Зальем экран рандомным цветом (fill - заливать), аргумент - переменная "color":
    for event in pygame.event.get(): # Цикл с переменной "event" будет присваивать события "pygame.event.get()"
        if event.type == pygame.QUIT: # Если тип события "event.type" равен "pygame.QUIT":
            running = False           # Тогда цикл завершиться и игра закончиться:
        if event.type == pygame.MOUSEBUTTONDOWN: # Если тип события "event.type" равен нажатию клавиши мыши:
# Координаты нажатия клавиши мышки на экране будут браться и присваиваться процедурой "pygame.mouse.get_pos()"
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = mouse_x


pygame.quit()