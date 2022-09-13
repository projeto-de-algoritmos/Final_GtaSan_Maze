from generator import *
from weapons import *



def is_collide(x, y,player_rect,walls_collide_list):
    tmp_rect = player_rect.move(x, y)
    if tmp_rect.collidelist(walls_collide_list) == -1:
        return False
    return True

# movimentação do cj

def cj_move(maze):
    player_speed = 5
    player_img = pygame.image.load('images/cj_rindo.jpg').convert_alpha()
    player_img = pygame.transform.scale(player_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
    player_rect = player_img.get_rect()
    player_rect.center = TILE // 2, TILE // 2
    directions = {'a': (-player_speed, 0), 'd': (player_speed, 0), 'w': (0, -player_speed), 's': (0, player_speed)}
    keys = {'a': pygame.K_a, 'd': pygame.K_d, 'w': pygame.K_w, 's': pygame.K_s}
    direction = (0, 0)

    return player_speed,player_img, player_rect, directions, direction, keys

def get_weapons(weapon_list,player_rect):
    for glock in weapon_list:
        if player_rect.collidepoint(glock.rect.center):
            glock.set_pos()
            return True
    return False

