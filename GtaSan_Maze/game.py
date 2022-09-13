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
text_font = pygame.font.SysFont('Impact', 80)
weapons_font = pygame.font.SysFont('Impact', 30)

maze = gamemap()

# player settings
player_speed,player_img, player_rect, directions, direction, keys = cj_move(maze)
glocks_img, glocks_rect, eletrical_img, eletrical_rect, smg_img, smg_rect, flower_img, flower_rect, binoculo_img,binoculo_rect = drawWeapons(maze)
glock_qtde , eletrical_qtde, smg_qtde, flower_qtde, binoculo_qtde = 0, 0, 0, 0, 0

# Respawn weapons no mapa
Glock_list = [Glock(game_surface) for i in range(3)]
Eletrical_list = [Eletrical(game_surface) for i in range(2)]
Smg_list = [Smg(game_surface) for i in range(2)]
Flower_list = [Flower(game_surface) for i in range(2)]
Binoculo_list = [Binoculo(game_surface) for i in range(2)]

walls_collide_list = sum([cell.get_rects() for cell in maze], [])

pygame.time.set_timer(pygame.USEREVENT, 1000)
time = 60


while True:
    
    surface.blit(gta_background, (1190, 0))
    surface.blit(game_surface, (0, 0))
    game_surface.blit(game_background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.USEREVENT:
            time -= 1

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
        time += 5
        glock_qtde += 1

    if get_weapons(Smg_list,player_rect):
        FPS += 1  
        time += 11
        smg_qtde += 1

    if get_weapons(Flower_list,player_rect):
        FPS += 1
        time += 7
        flower_qtde += 1

    if get_weapons(Binoculo_list,player_rect):
        FPS += 1
        time += 8
        binoculo_qtde += 1

    if get_weapons(Eletrical_list,player_rect):
        FPS += 1 
        time += 9  
        eletrical_qtde += 1          
        
    game_surface.blit(player_img, player_rect)

    [glocks.draw() for glocks in Glock_list]

    [eletrical.draw() for eletrical in Eletrical_list]

    [smg.draw() for smg in Smg_list]

    [flower.draw() for flower in Flower_list]

    [binoculo.draw() for binoculo in Binoculo_list]

    surface.blit(text_font.render('TIME', True, pygame.Color('grey'), True), (WIDTH + 150 , 370))
    surface.blit(text_font.render(f'{time}', True, pygame.Color('grey')), (WIDTH + 350, 370))

    surface.blit(glocks_img, glocks_rect)
    surface.blit(eletrical_img, eletrical_rect)
    surface.blit(smg_img, smg_rect)
    surface.blit(flower_img, flower_rect)
    surface.blit(binoculo_img, binoculo_rect)
    
    surface.blit(weapons_font.render(f'-  {glock_qtde}x', True, pygame.Color('grey'), True), (WIDTH + 300, 500))
    surface.blit(weapons_font.render(f'-  {eletrical_qtde}x', True, pygame.Color('grey'), True), (WIDTH + 300, 550))
    surface.blit(weapons_font.render(f'-  {smg_qtde}x', True, pygame.Color('grey'), True), (WIDTH + 300, 600))
    surface.blit(weapons_font.render(f'-  {flower_qtde}x', True, pygame.Color('grey'), True), (WIDTH + 300, 650))
    surface.blit(weapons_font.render(f'-  {binoculo_qtde}x', True, pygame.Color('grey'), True), (WIDTH + 300, 700))
    
    
    pygame.display.flip()
    clock.tick(FPS)