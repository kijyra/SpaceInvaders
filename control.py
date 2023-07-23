import sys, pygame
from bullet import Bullet

def event(window, player, bullets):
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.move_right = True
                print('RIGHT DOWN, move_right = ', str(player.move_right))
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.move_left = True
                print('LEFT DOWN, move_left = ', str(player.move_left))
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(window, player)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.move_right = False
                print('RIGHT UP, move_right = ', str(player.move_right))
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.move_left = False
                print('LEFT UP, move_rleft = ', str(player.move_left))


def update_screen(bg_color, window, player, bullets):
    window.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.paint()
    player.print()
    pygame.display.flip()
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)