from generator import *
from assets import *
from weapons import *
from random import randint
from knapasackDP import *




def is_game_over():
    global time, score, record, FPS
    if time < 0:
        pygame.time.wait(700)
        player_rect.center = TILE // 2, TILE // 2
        time, score, FPS = 60, 0, 60

FPS = 60
pygame.init()
game_surface = pygame.Surface(RES)
surface = pygame.display.set_mode((WIDTH + 600, HEIGHT))
clock = pygame.time.Clock()

game_background = pygame.image.load('images/gamebackground.jpg').convert()
gta_background = pygame.image.load('images/logogta.jpg').convert()
text_font = pygame.font.SysFont('Impact', 80)
weapons_font = pygame.font.SysFont('Impact', 30)
knapasack_font = pygame.font.SysFont('Impact', 30)
weighted_font  = pygame.font.SysFont('Impact', 15)

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

# val = [60, 100, 120]
# wt = [10, 20, 30]
# W = 50
# n = len(val)
# print(knapSack(W, wt, val, n))
tam_glock = 3
tam_eltrical = 2
tam_smg = 2
tam_flower = 2
binoculo = 2
val = [tam_glock,tam_eltrical,tam_smg,tam_flower,binoculo]
wt =  [10, 8 ,5, 3, 1]
n = len(val)
print(val)

walls_collide_list = sum([cell.get_rects() for cell in maze], [])

pygame.time.set_timer(pygame.USEREVENT, 1000)
time = 60
weightedKnapasack = 0
wieghtedTotal = randint(40,100)
print(wieghtedTotal)


bestvalue = knapSack(wieghtedTotal,wt,val,n)
print(bestvalue)

while True:
    
    surface.blit(gta_background, (1190, 0))
    surface.blit(game_surface, (0, 0))
    game_surface.blit(game_background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.USEREVENT:
            time -= 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_v:
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

    weightedKnapasack = pesoMochila(glock_qtde ,eletrical_qtde ,  smg_qtde ,  flower_qtde , binoculo_qtde)
           

    is_game_over()     
        
    game_surface.blit(player_img, player_rect)

    [glocks.draw() for glocks in Glock_list]

    [eletrical.draw() for eletrical in Eletrical_list]

    [smg.draw() for smg in Smg_list]

    [flower.draw() for flower in Flower_list]

    [binoculo.draw() for binoculo in Binoculo_list]

    surface.blit(text_font.render('TIME', True, pygame.Color('grey'), True), (WIDTH + 150 , 370))
    surface.blit(text_font.render(f'{time}s', True, pygame.Color('grey')), (WIDTH + 350, 370))
    surface.blit(knapasack_font.render(f'Peso Atual - {weightedKnapasack}', True, pygame.Color('green')), (WIDTH + 210, 800))
    surface.blit(knapasack_font.render(f'Capacidade Total Inventário - {wieghtedTotal}', True, pygame.Color('green')), (WIDTH + 110, 850))

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

    surface.blit(weighted_font.render(f'Peso 10kg', True, pygame.Color('blue'), True), (WIDTH + 160, 510))
    surface.blit(weighted_font.render(f'Peso 8kg', True, pygame.Color('red'), True), (WIDTH + 160, 560))
    surface.blit(weighted_font.render(f'Peso 5kg', True, pygame.Color('yellow'), True), (WIDTH + 160, 610))
    surface.blit(weighted_font.render(f'Peso 3kg', True, pygame.Color('white'), True), (WIDTH + 160, 660))
    surface.blit(weighted_font.render(f'Peso 2kg', True, pygame.Color('purple'), True), (WIDTH + 160, 710))
    
    
    pygame.display.flip()
    clock.tick(FPS)