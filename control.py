import sys, pygame

from bullet import Bullet
from enemy import Enemy


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


def update_screen(bg_color, window, player, bullets, enemies):
    """отрисовка экрана"""
    window.fill(bg_color)  # заполнение фона
    for bullet in bullets.sprites():  # отрисовка пуль
        bullet.paint()
    enemies.draw(window)
    player.print()  # отрисовка модели игрока
    pygame.display.flip()


def update_bullets(bullets):
    """удаление пуль за экраном"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_enemy(enemies):
    """обновление позиции врагов"""
    Enemy.update(enemies)


def create_army(window, enemies, screen_width, screen_height):
    """создание армии врагов"""
    enemy = Enemy(window)
    enemy_width = enemy.rect.width
    count_enemy_x = int((screen_width - 2 * enemy_width) / enemy_width)
    enemy_height = enemy.rect.height
    count_enemy_y = int((screen_height - 100 - 2 * enemy_height) / enemy_height)
    for count_row in range(count_enemy_y):
        for count_enemy in range(count_enemy_x):
            enemy = Enemy(window)
            enemy.x = enemy_width + (enemy_width * count_enemy)
            enemy.y = enemy_height + (enemy_height * count_row)
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.rect.height + (enemy.rect.height * count_enemy)
            enemies.add(enemy)
