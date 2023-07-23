import pygame
class Bullet(pygame.sprite.Sprite):

    def __init__(self, window, player):
        super(Bullet, self).__init__()
        self.window = window
        self.rect = pygame.Rect(0, 0, 2, 8)
        self.color = 255, 47, 100
        self.speed = 0.05
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def paint(self):
        pygame.draw.rect(self.window, self.color, self.rect)