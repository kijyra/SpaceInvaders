import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, window, player):
        """инициализация пули"""
        super(Bullet, self).__init__()  # родительский класс Bullet из pygame
        self.window = window  # присваиваем значение нашего окна
        self.rect = pygame.Rect(0, 0, 2, 8)  # задаём размеры
        self.color = 255, 47, 100  # цвет пули
        self.speed = 0.1  # скорость пули
        self.rect.centerx = player.rect.centerx  # задаём положение пули по вертикали
        self.rect.top = player.rect.top  # задаём положение пули по горизонтали
        self.y = float(self.rect.y)  # доп.переменная float для более плавного движения

    def update(self):
        """обновление позиции пули"""
        self.y -= self.speed  # смена координат пули (движение)
        self.rect.y = self.y  # запись координат из float

    def paint(self):
        """отрисовка пули"""
        pygame.draw.rect(self.window, self.color, self.rect)