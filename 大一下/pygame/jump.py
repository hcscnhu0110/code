import pygame
import sys

WIDTH = 600
HEIGHT = 300
FPS = 60
WHITE = (255,255,255)
background = pygame.image.load("test.png")
background_x = 0

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("JUMP")
clock = pygame.time.Clock()

class Player() :
    def __init__(self,x,y) :
        self.x = x
        self.y = y
        self.isJump = False
        self.jumpCount = 15
    def draw(self) :
        player_img = pygame.image.load("player.png")
        screen.blit(player_img,(self.x,self.y - 10))
    def move(self) :
        global background_x
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d] :
            self.x += 3
            if self.x > 500 :
                background_x -= 3
        if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a] :
            self.x -= 3
            if self.x < 100 :
                background_x += 3
        if self.x >= WIDTH - 70:
            self.x = WIDTH - 70
        if self.x < 20 :
            self.x = 20 
    def jump(self) :
        if self.isJump :
            if self.jumpCount >= -15 :
                direction = 1
                if self.jumpCount < 0 :
                    direction = -1
                self.y -= (self.jumpCount ** 2) * 0.1 * direction
                self.jumpCount -= 1
            else :
                self.isJump = False
                self.jumpCount = 15

player = Player(0,HEIGHT - 40)

def player_act(player) :
    player.draw()
    player.move()
    player.jump()

while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                player.isJump = True
    clock.tick(FPS)
    screen.fill(WHITE)
    screen.blit(background,(background_x,0))
    player_act(player)
    pygame.display.update()
   