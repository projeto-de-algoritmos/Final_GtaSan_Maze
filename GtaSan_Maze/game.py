from generator import *
from assets import *
from weapons import *
from random import randint
from knapasackDP import *

def passTime():

    global bestvalue,weightedKnapasack, record, recordTimeExecution,wieghtedTotal
    global time, FPS, record,n
    global glock_qtde , eletrical_qtde, smg_qtde, flower_qtde, binoculo_qtde
    global penalidades, val, wt
    global cjvalue, last_score
    
    cjvalue = knapSack(wieghtedTotal,wt,val,weightedKnapasack)
    lastscore = set_score(bestvalue,cjvalue,penalidades)
    last_score = lastscore
    set_record(record,lastscore)
    
    pygame.time.wait(700)
    glock_qtde , eletrical_qtde, smg_qtde, flower_qtde, binoculo_qtde = 0, 0, 0, 0, 0
    if float(lastscore) > float(recordTimeExecution):
        recordTimeExecution = lastscore
    player_rect.center = TILE // 2, TILE // 2
    [glocks.set_pos() for glocks in Glock_list]
    [eletrical.set_pos() for eletrical in Eletrical_list]
    [smg.set_pos() for smg in Smg_list]
    [flower.set_pos() for flower in Flower_list]
    [binoculo.set_pos() for binoculo in Binoculo_list]
    time, FPS = 60, 60
    wieghtedTotal = randint(40,100)


def removeItemKnapsack():
    global flag
    global glock_qtde , eletrical_qtde, smg_qtde, flower_qtde, binoculo_qtde
    global penalidades

    if(flag == 1):
        glock_qtde -= 1
        penalidades += 1
        val.pop()
        wt.pop()
    elif(flag == 2):
        smg_qtde -= 1
        penalidades += 1
        val.pop()
        wt.pop()
    elif(flag == 3):
        eletrical_qtde -= 1
        penalidades += 1
        val.pop()
        wt.pop()
    elif(flag == 4):
        flower_qtde -= 1
        penalidades += 1
        val.pop()
        wt.pop()
    elif(flag == 5):
        binoculo_qtde -= 1
        penalidades += 1
        val.pop()
        wt.pop()
    else:
        flag = flag              


def get_record():
    try:
        with open('record') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record', 'w') as f:
            f.write('0')
            return 0

def set_record(record, score):
    rec = max(float(record), score)
    with open('record', 'w') as f:
        f.write(str(rec))

def is_game_over():
    global time, record, FPS
    global glock_qtde , eletrical_qtde, smg_qtde, flower_qtde, binoculo_qtde
    global bestvalue,weightedKnapasack
    global recordTimeExecution, wieghtedTotal
    global penalidades, last_score
    global cjvalue,val, wt
    
    cjvalue = knapSack(wieghtedTotal,wt,val,weightedKnapasack)

    if time < 0:
        x = set_score(bestvalue,cjvalue,penalidades)
        last_score = x
        set_record(record, x)
        pygame.time.wait(700)
        player_rect.center = TILE // 2, TILE // 2
        [glocks.set_pos() for glocks in Glock_list]
        [eletrical.set_pos() for eletrical in Eletrical_list]
        [smg.set_pos() for smg in Smg_list]
        [flower.set_pos() for flower in Flower_list]
        [binoculo.set_pos() for binoculo in Binoculo_list]
        time, FPS = 60, 60
        wieghtedTotal = randint(40,100)
        if float(x) > float(recordTimeExecution):
            recordTimeExecution = x
        glock_qtde , eletrical_qtde, smg_qtde, flower_qtde, binoculo_qtde = 0, 0, 0, 0, 0

penalidades = 0
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
lastscore_font = pygame.font.SysFont('Impact', 20)
score_font = pygame.font.SysFont('Impact', 30)

maze = gamemap()

# player settings
player_speed,player_img, player_rect, directions, direction, keys = cj_move(maze)
glocks_img, glocks_rect, eletrical_img, eletrical_rect, smg_img, smg_rect, flower_img, flower_rect, binoculo_img,binoculo_rect = drawWeapons(maze)
glock_qtde , eletrical_qtde, smg_qtde, flower_qtde, binoculo_qtde = 0, 0, 0, 0, 0
 

# Respawn weapons no mapa
Glock_list = [Glock(game_surface) for i in range(randint(4,6))]
Eletrical_list = [Eletrical(game_surface) for i in range(randint(4,6))]
Smg_list = [Smg(game_surface) for i in range(randint(4,6))]
Flower_list = [Flower(game_surface) for i in range(randint(4,6))]
Binoculo_list = [Binoculo(game_surface) for i in range(randint(4,6))]


tam_glock = len(Glock_list)
tam_eltrical = len(Eletrical_list)
tam_smg =  len(Smg_list)
tam_flower = len(Flower_list)
tam_binoculo = len(Binoculo_list)


val = []
wt = []

valbest = []
wtbest = []

for i in range(tam_glock):
    valbest.append(23)
    wtbest.append(10)

for i in range(tam_eltrical):
    valbest.append(14)
    wtbest.append(8)

for i in range(tam_smg):
    valbest.append(19)
    wtbest.append(5)

for i in range(tam_flower):
    valbest.append(2)
    wtbest.append(3)

for i in range(tam_binoculo):
    valbest.append(2)
    wtbest.append(2)    


nbest = (tam_glock + tam_eltrical + tam_smg + tam_flower + tam_binoculo) 



walls_collide_list = sum([cell.get_rects() for cell in maze], [])

pygame.time.set_timer(pygame.USEREVENT, 1000)
time = 60
weightedKnapasack = 0
wieghtedTotal = randint(40,100)

record = get_record()
recordTimeExecution = record
last_score = record

flag = 0
bestvalue = knapSack(wieghtedTotal,wtbest,valbest,nbest)

cjvalue = None

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
                passTime()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                removeItemKnapsack()           

    pressed_key = pygame.key.get_pressed()
    for key, key_value in keys.items():
        if pressed_key[key_value] and not is_collide(*directions[key],player_rect,walls_collide_list):
            direction = directions[key]
            break
    if not is_collide(*direction,player_rect,walls_collide_list):
        player_rect.move_ip(direction)        
    
    # draw maze
    [cell.draw(game_surface) for cell in maze]

    if lastColide(Glock_list,player_rect):
        flag = 1
    if lastColide(Smg_list,player_rect):
        flag = 2
    if lastColide(Eletrical_list,player_rect):
        flag = 3  
    if lastColide(Flower_list,player_rect):
        flag = 4 
    if lastColide(Binoculo_list,player_rect):
        flag = 5          

    if get_weapons(Glock_list,player_rect):
        time += 4
        glock_qtde += 1
        val.append(23)
        wt.append(10)

    if get_weapons(Smg_list,player_rect):
        FPS += 1  
        time += 2
        smg_qtde += 1
        val.append(19)
        wt.append(5)

    if get_weapons(Flower_list,player_rect):
        time += 3
        flower_qtde += 1
        val.append(5)
        wt.append(3)

    if get_weapons(Binoculo_list,player_rect):
        FPS += 1
        time += 1
        binoculo_qtde += 1
        val.append(2)
        wt.append(2)

    if get_weapons(Eletrical_list,player_rect):
        FPS += 1 
        time += 9  
        eletrical_qtde += 1
        val.append(14)
        wt.append(8)

    weightedKnapasack = pesoMochila(glock_qtde ,eletrical_qtde,smg_qtde,flower_qtde,binoculo_qtde)
           

    is_game_over()     
        
    game_surface.blit(player_img, player_rect)

    [glocks.draw() for glocks in Glock_list]

    [eletrical.draw() for eletrical in Eletrical_list]

    [smg.draw() for smg in Smg_list]

    [flower.draw() for flower in Flower_list]

    [binoculo.draw() for binoculo in Binoculo_list]

    surface.blit(text_font.render('TIME', True, pygame.Color('grey'), True), (WIDTH + 150 , 380))
    surface.blit(text_font.render(f'{time}s', True, pygame.Color('grey')), (WIDTH + 350, 380))
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

    surface.blit(weighted_font.render(f'23$', True, pygame.Color('blue'), True), (WIDTH + 370, 510))
    surface.blit(weighted_font.render(f'14$', True, pygame.Color('red'), True), (WIDTH + 370, 560))
    surface.blit(weighted_font.render(f'19$', True, pygame.Color('yellow'), True), (WIDTH + 370, 610))
    surface.blit(weighted_font.render(f'5$', True, pygame.Color('white'), True), (WIDTH + 370, 660))
    surface.blit(weighted_font.render(f'2$', True, pygame.Color('purple'), True), (WIDTH + 370, 710))

    #record
    surface.blit(score_font.render(f'RECORD  :  {recordTimeExecution} pontos', True, pygame.Color('magenta'), True), (WIDTH + 160, 340))
    surface.blit(lastscore_font.render(f'Pontuação Anterior  :  {last_score} pontos', True, pygame.Color('Orange'), True), (WIDTH + 160, 760))
    
    pygame.display.flip()
    clock.tick(FPS)