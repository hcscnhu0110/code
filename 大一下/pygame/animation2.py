import pygame
import os 
import sys

WIDTH = 1000
HEIGHT = 500
FPS = 60
background = pygame.image.load(os.path.join("5x", "background.png"))
background_x = 0
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("animation2")
clock = pygame.time.Clock()

class Player() :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
        self.isJump = False
        self.jumpCount = 15
        self.isAttack = False
        self.isLeft = False
        self.sprites_idle = list()
        self.sprites_run = list()
        self.sprites_run_left = list()
        self.sprites_jump = list()
        self.sprites_jump_left = list()
        self.sprites_attack = list()
        self.sprites_attack_left = list()
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
        self.sprites_run_left.append(pygame.image.load(os.path.join("5x", "run_left_0.png")))
        self.sprites_run_left.append(pygame.image.load(os.path.join("5x", "run_left_1.png")))
        self.sprites_run_left.append(pygame.image.load(os.path.join("5x", "run_left_2.png")))
        self.sprites_run_left.append(pygame.image.load(os.path.join("5x", "run_left_3.png")))
        self.sprites_run_left.append(pygame.image.load(os.path.join("5x", "run_left_4.png")))
        self.sprites_run_left.append(pygame.image.load(os.path.join("5x", "run_left_5.png")))
        self.sprites_jump.append(pygame.image.load(os.path.join("5x", "jump_0.png")))
        self.sprites_jump.append(pygame.image.load(os.path.join("5x", "jump_1.png")))
        self.sprites_jump.append(pygame.image.load(os.path.join("5x", "jump_2.png")))
        self.sprites_jump.append(pygame.image.load(os.path.join("5x", "jump_3.png")))
        self.sprites_jump_left.append(pygame.image.load(os.path.join("5x", "jump_left_0.png")))
        self.sprites_jump_left.append(pygame.image.load(os.path.join("5x", "jump_left_1.png")))
        self.sprites_jump_left.append(pygame.image.load(os.path.join("5x", "jump_left_2.png")))
        self.sprites_jump_left.append(pygame.image.load(os.path.join("5x", "jump_left_3.png")))
        self.sprites_attack.append(pygame.image.load(os.path.join("5x", "attack_0.png")))
        self.sprites_attack.append(pygame.image.load(os.path.join("5x", "attack_1.png")))
        self.sprites_attack.append(pygame.image.load(os.path.join("5x", "attack_2.png")))
        self.sprites_attack.append(pygame.image.load(os.path.join("5x", "attack_3.png")))
        self.sprites_attack.append(pygame.image.load(os.path.join("5x", "attack_4.png")))
        self.sprites_attack.append(pygame.image.load(os.path.join("5x", "attack_5.png")))
        self.sprites_attack.append(pygame.image.load(os.path.join("5x", "attack_6.png")))
        self.sprites_attack.append(pygame.image.load(os.path.join("5x", "attack_7.png")))
        self.sprites_attack_left.append(pygame.image.load(os.path.join("5x", "attack_left_0.png")))
        self.sprites_attack_left.append(pygame.image.load(os.path.join("5x", "attack_left_1.png")))
        self.sprites_attack_left.append(pygame.image.load(os.path.join("5x", "attack_left_2.png")))
        self.sprites_attack_left.append(pygame.image.load(os.path.join("5x", "attack_left_3.png")))
        self.sprites_attack_left.append(pygame.image.load(os.path.join("5x", "attack_left_4.png")))
        self.sprites_attack_left.append(pygame.image.load(os.path.join("5x", "attack_left_5.png")))
        self.sprites_attack_left.append(pygame.image.load(os.path.join("5x", "attack_left_6.png")))
        self.sprites_attack_left.append(pygame.image.load(os.path.join("5x", "attack_left_7.png")))
        self.current_sprite_idle = 0
        self.current_sprite_run = 0
        self.current_sprite_run_left = 0
        self.current_sprite_jump = 0
        self.current_sprite_jump_left = 0
        self.current_sprite_attack = 0
        self.current_sprite_attack_left = 0
        self.image = self.sprites_idle[self.current_sprite_idle]
    def draw(self) :
        screen.blit(self.image, (self.x, self.y))
    def idle(self) :
        self.current_sprite_idle += 0.1
        if self.current_sprite_idle >= len(self.sprites_idle) :
            self.current_sprite_idle = 0   
        self.image = self.sprites_idle[int(self.current_sprite_idle)]
    def run(self) :
        global background_x
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d] :
            self.isLeft = False
            self.current_sprite_run += 0.1
            if self.current_sprite_run >= len(self.sprites_run) :
                self.current_sprite_run = 0
            self.image = self.sprites_run[int(self.current_sprite_run)]
            self.x += 5
            if self.x >= WIDTH - 200 :
                self.x = WIDTH - 200
                background_x -= 5
                if background_x <= -2800 :
                    background_x = -2800
        elif key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a] :
            self.isLeft = True
            self.current_sprite_run_left += 0.1
            if self.current_sprite_run_left >= len(self.sprites_run_left) :
                self.current_sprite_run_left = 0
            self.image = self.sprites_run_left[int(self.current_sprite_run_left)]
            self.x -= 5
            if self.x <= 20 :
                self.x = 20
                background_x += 5            
                if background_x >= 0 :
                    background_x = 0
    def jump(self) :
        if self.isJump :
            if self.isLeft :
                self.current_sprite_jump_left += 0.1
                if self.current_sprite_jump_left >= len(self.sprites_jump_left) :
                    self.current_sprite_jump_left = 0
                self.image = self.sprites_jump_left[int(self.current_sprite_jump_left)]
            else :
                self.current_sprite_jump += 0.1
                if self.current_sprite_jump >= len(self.sprites_jump) :
                    self.current_sprite_jump = 0
                self.image = self.sprites_jump[int(self.current_sprite_jump)]
            if self.jumpCount >= -15 :
                direction = 1
                if self.jumpCount < 0 :
                    direction = -1
                self.y -= (self.jumpCount ** 2) * 0.1 * direction
                self.jumpCount -= 1
            else :
                self.isJump = False
                self.jumpCount = 15
    def attack(self) :
        if self.isAttack :
            if self.isLeft :
                self.current_sprite_attack_left += 0.2
                if self.current_sprite_attack_left >= len(self.sprites_attack_left) :
                    self.current_sprite_attack_left = 0
                    self.isAttack = False
                self.image = self.sprites_attack_left[int(self.current_sprite_attack_left)]
            else :
                self.current_sprite_attack += 0.2
                if self.current_sprite_attack >= len(self.sprites_attack) :
                    self.current_sprite_attack = 0
                    self.isAttack = False
                self.image = self.sprites_attack[int(self.current_sprite_attack)]

player = Player(0,HEIGHT - 145)

def play_act(player) :
    player.draw()
    player.idle()
    player.run()
    player.jump()
    player.attack()

while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP or event.key == pygame.K_w :
                player.isJump = True
            elif event.key == pygame.K_SPACE :
                player.isAttack = True

    clock.tick(FPS)
    screen.blit(background,(background_x,0))
    play_act(player)
    pygame.display.update()