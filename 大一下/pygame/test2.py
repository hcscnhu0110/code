import pygame
import os 
import sys
import random

WIDTH = 1000
HEIGHT = 500
FPS = 60
WHITE=(255,255,255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("animation2")
clock = pygame.time.Clock()

class Obstacle(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 80))
        #self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.radius = 10
        pygame.draw.circle(self.image, WHITE, self.rect.center, self.radius)
        self.rect.x = 10
        self.rect.y = HEIGHT - 80
        self.isRight = True
        self.isCollide = False
        print(self.rect.center)
    def draw(self) :
        screen.blit(self.image, (self.rect.x, self.rect.y))

obstacle = Obstacle()

while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()

    clock.tick(FPS)
    screen.fill(WHITE)
    obstacle.draw()
    pygame.display.update()