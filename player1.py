"""
player.py genero jugador
"""
import os
import pygame

from config import *

# defino la clase Player que hereda de pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    # ejecutamos el metodo __init__ de la clase padre
    def __init__(self, left, bottom, dir_images): # tenemos dos argumento; left y bottom
        pygame.sprite.Sprite.__init__(self)
        # generamos TUPLa  para imagens asi se puede animar
        self.images = (
            pygame.image.load(os.path.join(dir_images, 'player_run.png')),
            pygame.image.load(os.path.join(dir_images, 'player_jump.png'))            
            )
        
        # ahora selecciono la imagen x default - indice 0
        self.image = self.images[0]
        
        # generamos una superficie para elpersonaje
        # self.image = pygame.Surface((50, 50))
        # self.image = pygame.image.load(os.path.join(dir_images, 'player_run.png'))

        # pinto la superficie
        # self.image.fill(BLUE)
        
        # genero el atributo rect
        self.rect = self.image.get_rect()
        # le asigno al atributo rect unas coordenadas lefy y bottom
        self.rect.left = left
        self.rect.bottom = bottom
        
        # creo los dos atributos que usare en elmetodo update_pos()
        self.pos_y = self.rect.bottom
        self.vel_y = 0
        
        self.can_jump = False
        
        self.playing = True
        
    # metodo detecta colisiones wlass y player
    def collide_with(self, sprites): # recibe como parametro lista de sprites
        # Usamos la función spritecollide() para detectar colisiones
        objects = pygame.sprite.spritecollide(self, sprites, False)
        # retornamos el elemento con el cual colisiono
        if objects:
            return objects[0]
        
    # metodo para colision tope de walls. Recibe como parametro una wall
    def collide_bottom(self, wall):
        return self.rect.colliderect(wall.rect_top)
    
    # metodo para seguir si colisiono parte superior
    def skid(self, wall):
        self.pos_x = wall.rect.top
        self.vel_y = 0
        self.can_jump= True
        
        # cuando cae sobre un wall carga la imagen de corriendo
        self.image = self.images[0]
        
    
    
    # chequeo si el sprite choca contra el suelo/platform
    def validate_platform(self, platform):
        result = pygame.sprite.collide_rect(self, platform)
        if result:
            self.vel_y = 0
            self.pos_y = platform.rect.top
            # si el jugador colisiona contra plataforma
            # puede vovler a saltar
            self.can_jump = True
            
            # cuando cae del salto vuelve a la imagen de corriendo
            self.image = self.images[0]
            
    #  generamos metodo de salto- recordar se modifica en forma NEGATIVA
    def jump(self):
        # validamos que SOLO salte si se presiona la barra
        if self.can_jump:# si es True
            self.vel_y = -3.5 # salta
            self.can_jump =False # y vuelve a ser False
            
            # cambiamos imagen cuando jugador salta
            self.image = self.images[1]
        
    def update_pos(self):
        # incremento los valores de self.pos_y / self.vel_y
        self.vel_y += PLAYER_GRAV
        # ahora generamos una aceleracion sobre el atributo pos_y
        self.pos_y += self.vel_y + 0.5 * PLAYER_GRAV
        
    # actualizamos el metodo update para uqe tome elmovimiento
    def update(self):
        if self.playing:
            self.update_pos()
        
            self.rect.bottom = self.pos_y
        
    # generamos metodo stop
    def stop(self):
        self.playing = False
        
        
    
        
    
        
        
        
    