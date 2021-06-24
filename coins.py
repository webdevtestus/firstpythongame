"""
coins.py para generar  monedas
"""
import os
import pygame
from config import *

class Coin(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y, dir_images):
        pygame.sprite.Sprite.__init__(self)
        
        # genero superficie/moneda
        # self.image = pygame.Surface( (50, 50))
        self.image = pygame.image.load(os.path.join(dir_images, 'coin.png'))
        
        # la pintamos de amarillo
        # self.image.fill(YELLOW)
        
        # genero el rectangulo
        self.rect = self.image.get_rect()
        
        # lo posiciono
        self.rect.x = pos_x
        self.rect.y = pos_y
        
        # velocidad en X de coins
        self.vel_x = SPEED
        
    def update(self):
        self.rect.left -= self.vel_x
        
    def stop(self):
        self.vel_x = 0
        
        
        
        
