
import pygame, control
from player import Player
from pygame.sprite import Group

def start():
    _running = True
    pygame.init()
    screen_width = 350
    screen_height = 500

    window = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("The Game")
    bg_color = (0, 0, 0)
    player = Player(window)
    bullets = Group()
    while True:
        control.event(window, player, bullets)
        player.update()
        control.update_screen(bg_color, window, player, bullets)
        control.update_bullets(bullets)

start()