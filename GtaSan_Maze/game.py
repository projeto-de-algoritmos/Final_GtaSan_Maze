from generator import *
from assets import *
from weapons import *


FPS = 60
pygame.init()
game_surface = pygame.Surface(RES)
surface = pygame.display.set_mode((WIDTH + 600, HEIGHT))
clock = pygame.time.Clock()

game_background = pygame.image.load('images/gamebackground.jpg').convert()
gta_background = pygame.image.load('images/logogta.jpg').convert()


maze = gamemap()

# player settings
player_speed,player_img, player_rect, directions, direction, keys = cj_move(maze)

# Respawn weapons no mapa
Glock_list = [Glock(game_surface) for i in range(3)]
Eletrical_list = [Eletrical(game_surface) for i in range(2)]
Smg_list = [Smg(game_surface) for i in range(2)]
Flower_list = [Flower(game_surface) for i in range(2)]
Binoculo_list = [Binoculo(game_surface) for i in range(2)]

walls_collide_list = sum([cell.get_rects() for cell in maze], [])


while True:
    
    surface.blit(gta_background, (1190, 0))
    surface.blit(game_surface, (0, 0))
    game_surface.blit(game_background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pressed_key = pygame.key.get_pressed()
    for key, key_value in keys.items():
        if pressed_key[key_value] and not is_collide(*directions[key],player_rect,walls_collide_list):
            direction = directions[key]
            break
    if not is_collide(*direction,player_rect,walls_collide_list):
        player_rect.move_ip(direction)        
    
    # draw maze
    [cell.draw(game_surface) for cell in maze]

    if get_weapons(Glock_list,player_rect):
        FPS += 1

    if get_weapons(Smg_list,player_rect):
        FPS += 1  

    if get_weapons(Flower_list,player_rect):
        FPS += 1

    if get_weapons(Binoculo_list,player_rect):
        FPS += 1

    if get_weapons(Eletrical_list,player_rect):
        FPS += 1                 
        


    


    game_surface.blit(player_img, player_rect)

    [glocks.draw() for glocks in Glock_list]

    [eletrical.draw() for eletrical in Eletrical_list]

    [smg.draw() for smg in Smg_list]

    [flower.draw() for flower in Flower_list]

    [binoculo.draw() for binoculo in Binoculo_list]

    pygame.display.flip()
    clock.tick(FPS)