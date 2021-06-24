"""
clase Wall para definir obstaculos tipo muros
"""
import os
import pygame
from config import *

# definimos la clase que heredara de sprite.Sprite
class Wall(pygame.sprite.Sprite):
    
    # ejecutamos elmetodo init dela clase padre
    def __init__(self, left, bottom, dir_images):
        pygame.sprite.Sprite.__init__(self)
    
        # generamos la superficie
        # self.image = pygame.Surface( (60, 86) )
        self.image = pygame.image.load(os.path.join(dir_images, 'wall.png'))

        
        # le damos un color
        # self.image.fill(RED)
        
        # obtengo el rectangulo
        self.rect = self.image.get_rect()
        
        # posiciono el rectangulo
        self.rect.left = left
        self.rect.bottom = bottom
        
        # asigno SPEED a un atributo vel_x
        self.vel_x = SPEED
        
        # generamos rectangulo superior en walls
        self.rect_top = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 1)
        
    # sobreescribimos el metodo update gara generar la animacion
    def update(self):
        self.rect.left -= self.vel_x
        
        # actualizamos posicion de rect_top
        self.rect_top.x = self.rect.x
                      
    # genero metodo stop para walls
    def stop(self):
        self.vel_x = 0
        
        
    
    
    
