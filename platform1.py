"""
platform1.py
genero plataforma para el jugador
"""
# importo pygame porque se va a heredar de el
import pygame
from config import *

# genero Clase Platform hereda de pygame.sprite.Sprite
class Platform(pygame.sprite.Sprite):
    
    def __init__(self):
        # ejecutamos el metodo __init__ de la clase padre
        pygame.sprite.Sprite.__init__(self)
        
        # genero superficie/plataforma para el jugador
        self.image = pygame.Surface ((WIDTH, 80))
        self.image.fill(GREEN)
        
        # ahora obtenemos el rectangulo de la superficie
        # es OBLIGATORIO generar elrectangulo para pintar el sprite
        # o sea, generar un rect y asignarle una posicion X y una Y
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = HEIGHT - 80
        
        
        