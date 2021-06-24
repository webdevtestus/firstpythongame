
import os
import sys
import pygame
import random

from config import *
from platform1 import Platform
from player1 import Player
from walls import Wall
from coins import Coin

class Game:
    def __init__(self):
        pygame.init()
        
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        
        self.running = True
                
        self.clock = pygame.time.Clock()
        
        self.font = pygame.font.match_font(FONT)
        
        # generamos ruta aboluta a path Sonidos e imagenes
        self.dir = os.path.dirname(__file__)
        self.dir_sounds = os.path.join(self.dir, 'Sonidos')
        self.dir_images = os.path.join(self.dir, 'Sprites')
        
    def start(self):
        self.menu()
        self.new()

    def new(self):
        # ejecutamos los elementos ANTES del run
        self.score = 0
        self.level = 0
        self.playing = True
        self.background = pygame.image.load(os.path.join(self.dir_images, 'background2.jpg'))
        
        self.generate_elements()
        self.run()
        
    def generate_elements(self):
        self.platform = Platform()
        self.player = Player(100, self.platform.rect.top - 400, self.dir_images)
        
        # ahora genero un grupo de sprites para agrupar los que
        # vaya a utilizar; plataforma, personaje, obstaculos, monedas, etc
        self.sprites = pygame.sprite.Group()
        
        # agrego grupo obstaculos/walls
        self.walls = pygame.sprite.Group()
        
        # agrego grupo monedas/coin
        self.coin = pygame.sprite.Group()
        
        # agregamos la plataforma a la lista
        self.sprites.add(self.platform)
        # agrego el player
        self.sprites.add(self.player)
        # generar obstaculos walls
        self.generate_walls()
        
        
    def generate_walls(self):
        # variable para generar obstaculos separados entre si
        last_position = WIDTH + 100
        
        # si NO hay obstaculo, genero
        if not len(self.walls) > 0:
            # genero en grupos de a 10
            for w in range(0, MAX_WALLS):
                
                # left genero random apariciones
                left = random.randrange(last_position + 150, last_position + 340)
                # genero objetos de tipo wall
                wall = Wall(left, self.platform.rect.top, self.dir_images)
                
                # modificamos el valor de last position cada vez
                last_position = wall.rect.right
                
                # agregamos elobstaculo a la lista de sprites y de walls
                self.sprites.add(wall)
                self.walls.add(wall)
                
            # incremento en uno el nivel de juego
            self.level += 1
            
            # cada vez que generamos las walls, generamos tambien las coins
            self.generate_coin()
                
    def generate_coin(self):
        last_position = WIDTH
        
        for c in range(0, MAX_COINS):
            pos_x = random.randrange(last_position + 80,  last_position + 380)
            
            coin = Coin(pos_x, 250, self.dir_images)
            
            last_position = coin.rect.right
            
            # almacenamos dicho objeto en sprite
            self.sprites.add(coin)
            self.coin.add(coin)
            
                     
                
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
                        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running == False
                pygame.quit()
                sys.exit()
                
        key = pygame.key.get_pressed()
        
        if key[pygame.K_SPACE]:
            self.player.jump()
            
        if key[pygame.K_r] and not self.playing:
            self.new()

    def draw(self):
        # self.surface.fill(BACKGROUND)
        self.surface.blit(self.background, (0, 0))
        
        self.draw_text()
        
        # dibujmos TODOS los sprites de neustra lista
        # el metodo recibe como argumento DONDE queremos que se pinte sprite
        self.sprites.draw(self.surface)# pintamos la plataforma en la superficie
        
        pygame.display.flip()


    def update(self):
        if self.playing:
        
            
            # detectamos colision entre obstaculos y player
            wall = self.player.collide_with(self.walls) # argumeto-> lista de obstaculos
            if wall: # si HAY colision
                if self.player.collide_bottom(wall): # si colisiona con parte superior
                    # mantiene jugador en mismas coordenadas llamando a metodo skid()
                    self.player.skid(wall)
                else: # si NO colisiono en parte superior termina juego
                    self.stop()
                    
            coin = self.player.collide_with(self.coin)
            if coin:
                self.score += 1
                coin.kill()
                
             
                sound = pygame.mixer.Sound(os.path.join(self.dir_sounds, 'coins.mp3'))
                sound.play()
                    
            self.sprites.update()
            
            self.player.validate_platform(self.platform)
            
            self.update_elements(self.walls)
            self.update_elements(self.coin)
            
            # vuelvo a generar walls ya que se borran al llegar alfin dela pantalla
            self.generate_walls()
            
    # metodo para eliminar elementos auno NO visibles enpantalla        
    def update_elements(self, elements):
        for element in elements:
            # si NO es visible
            if not element.rect.right > 0:
                # ejecuto el metodo kill()
                element.kill()
                 
    def stop(self):
        
        sound = pygame.mixer.Sound(os.path.join(self.dir_sounds, 'Shotgun_Blast.mp3'))
        sound.play()
        self.player.stop()
        self.stop_elements(self.walls) # creamos el metodo stop para objeto walls en walls.py
        
        self.playing = False
        
    # genero detencion de elementos si hay colision
    def stop_elements(self, elements):
        for element in elements:
            element.stop()
            
    def score_format(self):
        return 'Score : {}'.format(self.score)
    
    def level_format(self):
        return 'Level : {}'.format(self.level)
        
    def draw_text(self):
        self.display_text(self.score_format(), 36, BLACK, WIDTH // 2, TEXT_POSY)
        self.display_text(self.level_format(), 36, BLACK, 65, TEXT_POSY)
        
        if not self.playing:
            self.display_text('GAME OVER', 70, RED, WIDTH // 2, HEIGHT // 2)
            self.display_text('Presiona r para una nueva partida', 50, BLACK, WIDTH // 2, 125)


            
    # metodo que genera el font
    def display_text(self, text, size, color, pos_x, pos_y):
        # creamos la fuente
        font = pygame.font.Font(self.font, size)
        # generamos el texto
        text = font.render(text, True, color)
        # generamos el rectangulo
        rect = text.get_rect()
        # asignamos posicion al texto
        rect.midtop = (pos_x, pos_y)
        
        # pinto el texto en la surface
        self.surface.blit(text, rect)
        
    def menu(self):
        self.surface.fill(GREEN_LIGHT) # pintamos de verde claro y mostramos mensaj
        self.display_text('Presiona una tecla para comenzar!', 36, BLACK, WIDTH // 2, 10)
        # actualizamos pantalla
        pygame.display.flip()
        # ejecuto menu
        self.wait()
        
    def wait(self):
        wait = True
        #y defino ciclco While
        while wait: # while True actualizo los FPS
            self.clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wait = False
                    self.running = False
                    pygame.quit()
                    sys.exit()
                # si presiono una tecla comienza el juego
                if event.type == pygame.KEYDOWN:
                    wait = False
                
                    
                    
            
    
