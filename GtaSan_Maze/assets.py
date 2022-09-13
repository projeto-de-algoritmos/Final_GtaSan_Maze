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

# Coletar item para a mochila
def get_weapons(weapon_list,player_rect):
    for glock in weapon_list:
        if player_rect.collidepoint(glock.rect.center):
            glock.set_pos()
            return True
    return False

# Desenhar weapons no menu
def drawWeapons(maze):
    glocks_img = pygame.image.load('images/glock_gta.jpg').convert_alpha()
    glocks_img = pygame.transform.scale(glocks_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
    glocks_rect = glocks_img.get_rect()
    glocks_rect.topleft = WIDTH + 250, 500

    eletrical_img = pygame.image.load('images/eletrical.jpg').convert_alpha()
    eletrical_img = pygame.transform.scale(eletrical_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
    eletrical_rect = eletrical_img.get_rect()
    eletrical_rect.topleft = WIDTH + 250, 550

    smg_img = pygame.image.load('images/metralha.jpg').convert_alpha()
    smg_img = pygame.transform.scale(smg_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
    smg_rect = smg_img.get_rect()
    smg_rect.topleft = WIDTH + 250, 600

    flower_img = pygame.image.load('images/flower.jpg').convert_alpha()
    flower_img = pygame.transform.scale(flower_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
    flower_rect = flower_img.get_rect()
    flower_rect.topleft = WIDTH + 250, 650

    binoculo_img = pygame.image.load('images/binoculo.jpg').convert_alpha() 
    binoculo_img = pygame.transform.scale(binoculo_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
    binoculo_rect = binoculo_img.get_rect()
    binoculo_rect.topleft = WIDTH + 250, 700

    return glocks_img, glocks_rect, eletrical_img, eletrical_rect, smg_img, smg_rect, flower_img, flower_rect, binoculo_img,binoculo_rect 

