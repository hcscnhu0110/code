import pygame
import os
import sys

WIDTH = 1200
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("animation")
clock = pygame.time.Clock()

class Player() :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
        self.sprites_idle = []
        self.sprites_run = []
        self.sprites_idle.append(pygame.image.load(os.path.join("5x", "idle_0.png")))
        self.sprites_idle.append(pygame.image.load(os.path.join("5x", "idle_1.png")))
        self.sprites_idle.append(pygame.image.load(os.path.join("5x", "idle_2.png")))
        self.sprites_idle.append(pygame.image.load(os.path.join("5x", "idle_3.png")))
        self.sprites_run.append(pygame.image.load(os.path.join("5x", "run_0.png")))
        self.sprites_run.append(pygame.image.load(os.path.join("5x", "run_1.png")))
        self.sprites_run.append(pygame.image.load(os.path.join("5x", "run_2.png")))
        self.sprites_run.append(pygame.image.load(os.path.join("5x", "run_3.png")))
        self.sprites_run.append(pygame.image.load(os.path.join("5x", "run_4.png")))
        self.sprites_run.append(pygame.image.load(os.path.join("5x", "run_5.png")))
        self.current_sprite_idle = 0
        self.current_sprite_run = 0
        self.image = self.sprites_idle[self.current_sprite_idle]
    def draw(self) :
        screen.blit(self.image, (self.x, self.y))
    def update(self) :
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d] :
            self.current_sprite_run += 0.1
            if self.current_sprite_run >= len(self.sprites_run) :
                self.current_sprite_run = 0
            self.image = self.sprites_run[int(self.current_sprite_run)]
            self.x += 5
        else :
            self.current_sprite_idle += 0.1
            if self.current_sprite_idle >= 4 :
                self.current_sprite_idle = 0
            self.image = self.sprites_idle[int(self.current_sprite_idle)]

player = Player(0,HEIGHT - 145)

while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()
        
    clock.tick(FPS)
    screen.fill(WHITE)
    player.draw()
    player.update()
    pygame.display.update()