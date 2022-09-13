from generator import *


FPS = 60
pygame.init()
game_surface = pygame.Surface(RES)
surface = pygame.display.set_mode((WIDTH + 600, HEIGHT))
clock = pygame.time.Clock()


maze = gamemap()


while True:
    
    surface.blit(game_surface, (0, 0))
    
    # draw maze
    [cell.draw(game_surface) for cell in maze]

    pygame.display.flip()
    clock.tick(FPS)