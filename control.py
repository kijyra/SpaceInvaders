import sys, pygame
from bullet import Bullet


def event(window, player, bullets):
    """обработчик событий"""
    # закрытие окна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # если нажата кнопка
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.move_right = True
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.move_left = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(window, player)
                bullets.add(new_bullet)
        # если отпущена кнопка
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.move_right = False
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.move_left = False


def update_screen(bg_color, window, player, bullets):
    """отрисовка экрана"""
    window.fill(bg_color)  # заполнение фона
    for bullet in bullets.sprites():  # отрисовка пуль
        bullet.paint()
    player.print()  # отрисовка модели игрока
    pygame.display.flip()


def update_bullets(bullets):
    """удаление пуль за экраном"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
