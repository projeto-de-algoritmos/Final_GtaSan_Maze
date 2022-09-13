from generator import *
from assets import *

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
    game_surface.blit(player_img, player_rect)

    pygame.display.flip()
    clock.tick(FPS)