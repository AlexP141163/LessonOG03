# Импортируем и инициализируем "pygame":
import pygame
import random
import time

pygame.init() # Инициализация:

# Переменные

SCRIN_WIDTH = 800  # Переменные, задают ширину и высоту экрана в пикселях:
SCRIN_HEIGHT = 600

# Создпем переменную "screen", в которой будем хранить экран с заданными шириной и высотой экрана:
screen = pygame.display.set_mode((SCRIN_WIDTH, SCRIN_HEIGHT))

# Создаем заголовок экрана (set_caption - установить заголовок):
pygame.display.set_caption("Игра Тир, Победа - 100 Очков")

font = pygame.font.Font(None, 36) # Шривт для счета:
score = 0  # Инициализация переменной для счета:
text = "Счет:"
text_final = "Вы Победили!"
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
target_speed_x = 0.5  # Скорость движения мишени по горизонтали "Включено для непрерывного движения"
target_speed_y = 0.5  # Скорость движения мишени по вертикали   "Включено для непрерывного движения"

# Зададим Рамдомный цвет экрана: Цвет экрана в новой версии будет постоянный:
#color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
color = (0, 190, 180)

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
# Условие определяет попала ли координата мышки по оси "Х" ("mouse_x") в координаты цели "target_x, target_width"
# Другими словами координаты мышк должны быть в промежутке координат цели по оси "Х" и "У"
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCRIN_WIDTH - target_width)
                target_y = random.randint(0, SCRIN_HEIGHT - target_height)
                score += 10

    # Обновляем координаты мишени
    target_x += target_speed_x      # В новой версии при движении мишени постоянно:
    target_y += target_speed_y      # В новой версии при движении мишени постоянно:

    # Проверяем, не вышла ли мишень за пределы экрана, и меняем направление движения, если это так:
    if target_x + target_width > SCRIN_WIDTH or target_x < 0:
        target_speed_x = -target_speed_x
    if target_y + target_height > SCRIN_HEIGHT or target_y < 0:
        target_speed_y = -target_speed_y

    # Отрисовываем на экране мишень  с координатами ("target_img, (target_x, target_y") оператором ("screen.blit"):
    screen.blit(target_img, (target_x, target_y))

    # Создание текстовой поверхности
    #text_surface = font.render(text, True, 0)
    text_surface = font.render(f"{text} {score}", True, (0, 0, 0))
    # Отображение текста
    screen.blit(text_surface, (10, 20))
    # Создание текстовой поверхности с числовым значением, преобразованным в строку
    #text_surface = font.render(str(score), True, 0)
    # Отображение текста
    #screen.blit(text_surface, (80, 20))
    # Условие завершения игры - 100 Очков. Игра завершиться через 5 секунд.
    if score > 90:
        # Создание текстовой поверхности с числовым значением, преобразованным в строку
        text_surface = font.render(str(text_final), True, 0)
        # Отображение текста
        screen.blit(text_surface, (300, 280))
        pygame.display.update()
        time.sleep(5)  # Пауза на 5 секунд
        running = False

    pygame.display.update() # Обновление экрана, Обязательно вставляем со смещением для цикла "while":

pygame.quit()