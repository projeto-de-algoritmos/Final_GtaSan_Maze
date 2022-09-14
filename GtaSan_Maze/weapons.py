from generator import *
from random import randrange

class Glock(object):
    def __init__(self,game_surface):
        self.img = pygame.image.load('images/glock_gta.jpg').convert_alpha()
        self.img = pygame.transform.scale(self.img, (TILE - 10, TILE - 10))
        self.rect = self.img.get_rect()
        self.game_surface = game_surface
        self.set_pos()

    def set_pos(self):
        self.rect.topleft = randrange(cols) * TILE + 5, randrange(rows) * TILE + 5

    def draw(self):
        self.game_surface.blit(self.img, self.rect)

    def whoami(self):
        return (type(self).__name__)     

class Eletrical(object):
    def __init__(self,game_surface):
        self.img = pygame.image.load('images/eletrical.jpg').convert_alpha()
        self.img = pygame.transform.scale(self.img, (TILE - 10, TILE - 10))
        self.rect = self.img.get_rect()
        self.game_surface = game_surface
        self.set_pos()

    def set_pos(self):
        self.rect.topleft = randrange(cols) * TILE + 5, randrange(rows) * TILE + 5

    def draw(self):
        self.game_surface.blit(self.img, self.rect)
    
    def whoami(self):
        return (type(self).__name__)    

class Smg(object):
    def __init__(self,game_surface):
        self.img = pygame.image.load('images/metralha.jpg').convert_alpha()
        self.img = pygame.transform.scale(self.img, (TILE - 10, TILE - 10))
        self.rect = self.img.get_rect()
        self.game_surface = game_surface
        self.set_pos()

    def set_pos(self):
        self.rect.topleft = randrange(cols) * TILE + 5, randrange(rows) * TILE + 5

    def draw(self):
        self.game_surface.blit(self.img, self.rect)

    def whoami(self):
        return (type(self).__name__)    

class Flower(object):
    def __init__(self,game_surface):
        self.img = pygame.image.load('images/flower.jpg').convert_alpha()
        self.img = pygame.transform.scale(self.img, (TILE - 10, TILE - 10))
        self.rect = self.img.get_rect()
        self.game_surface = game_surface
        self.set_pos()

    def set_pos(self):
        self.rect.topleft = randrange(cols) * TILE + 5, randrange(rows) * TILE + 5

    def draw(self):
        self.game_surface.blit(self.img, self.rect)

    def whoami(self):
        return (type(self).__name__)    

class Binoculo(object):
    def __init__(self,game_surface):
        self.img = pygame.image.load('images/binoculo.jpg').convert_alpha()
        self.img = pygame.transform.scale(self.img, (TILE - 10, TILE - 10))
        self.rect = self.img.get_rect()
        self.game_surface = game_surface
        self.set_pos()

    def set_pos(self):
        self.rect.topleft = randrange(cols) * TILE + 5, randrange(rows) * TILE + 5

    def draw(self):
        self.game_surface.blit(self.img, self.rect)

    def whoami(self):
        return type(self).__name__    