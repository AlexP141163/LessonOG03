# Импортируем и инициализируем "pygame":
import pygame

pygame.init() # Инициализация:

SCRIN_WIDTH = 800  # Переменные, задают ширину и высоту экрана в пикселях:
SCRIN_HEIGHT = 600
# Создпем переменную "screen", в которой будем хранить экран с заданными шириной и высотой экрана:
screen = pygame.display.set_mode((SCRIN_WIDTH, SCRIN_HEIGHT))
# Создаем заголовок экрана (set_caption - установить заголовок):
pygame.display.set_caption("Игра Тир")


# Условие цикла непрерывной работы программы. Как только переменная "running = false", программа
# закончиться работой "pygame.quit()"
running = True
while running:
    pass


pygame.quit()