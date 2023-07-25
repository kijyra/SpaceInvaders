import pygame

class Player():

    def __init__(self, window):
        """инициализация класса Player"""
        self.window = window  # окно игры
        self.image = pygame.image.load('images/player.png') # png игрока
        self.rect = self.image.get_rect()  # получаем прямоугольник с координатами из картинки игрока
        self.window_rect = window.get_rect()  # получаем прямоугольник с координатами окна
        self.rect.centerx = self.window_rect.centerx  # задаём координаты по горизонтали
        self.center = float(self.rect.centerx)  # задаём переменную float для более плавного движения
        self.rect.bottom = self.window_rect.bottom - 20  # задаём координаты по вертикали
        self.move_right = False  # зажата ли кнопка направо?
        self.move_left = False  # зажата ли кнопка налево?

    def update(self):
        """отслеживание перемещения текстуры игрока"""
        speed = 0.02
        if self.move_right and self.rect.right < self.window_rect.right:
            self.center += speed
        if self.move_left and self.rect.left > self.window_rect.left:
            self.center -= speed
        self.rect.centerx = self.center

    def print(self):
        """отрисовка"""
        self.window.blit(self.image, self.rect)