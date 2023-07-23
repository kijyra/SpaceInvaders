import pygame

class Player():

    def __init__(self, window):
        self.window = window
        self.image = pygame.image.load('images/player.png')
        self.rect = self.image.get_rect()
        self.window_rect = window.get_rect()
        self.rect.centerx = self.window_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.window_rect.bottom - 20
        self.move_right = False
        self.move_left = False

    def update(self):
        if self.move_right and self.rect.right < self.window_rect.right:
            self.center += 0.02
        if self.move_left and self.rect.left > self.window_rect.left:
            self.center -= 0.02
        self.rect.centerx = self.center

    def print(self):
        self.window.blit(self.image, self.rect)