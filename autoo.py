import pygame, random, math
import sys
from pygame.locals import *
from random import randint
pygame.init()
#FPS
FPS = 30
#ventana
ALTO = 690
ANCHO = 460
clock = pygame.time.Clock()
screen = pygame.display.set_mode([690, 450])
superficie = pygame.Surface([900, 400])
pygame.display.set_caption("auto")
done = False
fondo = pygame.image.load("imgg.jpg")
score = 0

#sonido de fondo
pygame.mixer.music.load("tokyo.mp3.mpeg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

isJump = False


class autoo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("carrr.png").convert()
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect()
        self.rect.bottom = (40)
        self.rect.x = 200
        self.rect.y = 240
        self.velocidad = 0
        self.isJump = False
        self.salto = 10
        self.al = 450

    def update(self):
        teclas = pygame.key.get_pressed()
        if event.type == pygame.K_SPACE:
            self.isJump = True
            if self.isJump:
               if self.salto>= -10:
                self.al -= (self.salto * abs(self.salto))*0.5
                self.salto-=1
            else:
                self.salto=10
                self.isJump = False


auto_list = pygame.sprite.Group()
auto = autoo()
auto_list.add(auto)


class piedraa(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("piedra.jpg").convert()
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 280
    def update(self):
        self.rect.x -= 10
        if self.rect.right < 0:
            self.rect.left = ANCHO

piedra_list = pygame.sprite.Group()
piedra = piedraa()
piedra_list.add(piedra)

colision = pygame.sprite.spritecollide(auto, piedra_list, False)
if colision:
   image = pygame.image.load("over.JPG")
   image.set_colorkey([255, 255, 255])



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    piedra_list.update()
    auto_list.update()

    screen.blit(fondo, [ 0, 0])
    screen.blit(superficie, (0 ,390))
    piedra_list.draw(screen)
    auto_list.draw(screen)

    clock.tick(60)
    pygame.display.update()
pygame.quit()