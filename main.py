import pygame, control
from player import Player
from pygame.sprite import Group


def start():
    """основная функция"""
    pygame.init()  # инициализация pygame
    screen_width = 350  # переменная ширины окна
    screen_height = 500  # переменная высоты окна
    window = pygame.display.set_mode((screen_width, screen_height))  # создание окна
    pygame.display.set_caption("The Game")  # название окна
    bg_color = (0, 0, 0)  # background color (цвет фона)
    player = Player(window)  # создаём игрока из модуля player.py
    bullets = Group()  # создаём группу пуль
    while True:  # основной цикл программы
        control.event(window, player, bullets)  # вызываем обработчик событий из модуля control.py
        player.update()  # вызываем функцию отслеживания позиции игрока
        control.update_screen(bg_color, window, player, bullets)  # обновляем экран
        control.update_bullets(bullets)  # проверка на то вылетели ли пуль за пределы экрана


start()  # вызов основной функции
