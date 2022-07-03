import pygame
import os 
import sys
import random

WIDTH = 1000
HEIGHT = 500
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
background = pygame.image.load(os.path.join("5x", "background.png"))
background_x = 0
obstacle_top = 222

class Player(pygame.sprite.Sprite) :
    def __init__(self, x, y) :
        pygame.sprite.Sprite.__init__(self)
        self.isJump = False
        self.jumpCount = 15
        self.isAttack = False
        self.isLeft = False
        self.isShoot = False
        self.sprites_idle = list()
        self.sprites_idle_left = list()
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
        self.sprites_idle_left.append(pygame.image.load(os.path.join("5x", "idle_left_0.png")))
        self.sprites_idle_left.append(pygame.image.load(os.path.join("5x", "idle_left_1.png")))
        self.sprites_idle_left.append(pygame.image.load(os.path.join("5x", "idle_left_2.png")))
        self.sprites_idle_left.append(pygame.image.load(os.path.join("5x", "idle_left_3.png")))
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
        self.current_sprite_idle_left = 0
        self.current_sprite_run = 0
        self.current_sprite_run_left = 0
        self.current_sprite_jump = 0
        self.current_sprite_jump_left = 0
        self.current_sprite_attack = 0
        self.current_sprite_attack_left = 0
        self.image = self.sprites_idle[self.current_sprite_idle]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.y = y
    def update(self) :
        self.idle()
        self.run()
        self.jump()
        self.attack()
    def idle(self) :
        if self.isLeft :
            self.current_sprite_idle_left += 0.1
            if self.current_sprite_idle_left >= len(self.sprites_idle_left) :
                self.current_sprite_idle_left = 0   
            self.image = self.sprites_idle_left[int(self.current_sprite_idle_left)]
        else :
            self.current_sprite_idle += 0.1
            if self.current_sprite_idle >= len(self.sprites_idle) :
                self.current_sprite_idle = 0   
            self.image = self.sprites_idle[int(self.current_sprite_idle)]
    def run(self) :
        global background_x
        global obstacle_top
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d] :
            self.isLeft = False
            self.current_sprite_run += 0.1
            if self.current_sprite_run >= len(self.sprites_run) :
                self.current_sprite_run = 0
            self.image = self.sprites_run[int(self.current_sprite_run)]
            if not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top) or (obstacle.isCollide and player.rect.centerx > obstacle.rect.centerx) :
                self.rect.x += 5
                if self.rect.x >= WIDTH - 450 :
                    self.rect.x = WIDTH - 450
                    background_x -= 5
                    if background_x <= -2800 :
                        background_x = -2800
        
        elif key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a] :
            self.isLeft = True
            self.current_sprite_run_left += 0.1
            if self.current_sprite_run_left >= len(self.sprites_run_left) :
                self.current_sprite_run_left = 0
            self.image = self.sprites_run_left[int(self.current_sprite_run_left)]
            if not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)  or (obstacle.isCollide and player.rect.centerx < obstacle.rect.centerx) :
                self.rect.x -= 5
                if self.rect.x <= 200 :
                    self.rect.x = 200
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
                self.rect.bottom -= (self.jumpCount ** 2) * 0.1 * direction 
                self.jumpCount -= 1
            else :
                self.rect.bottom += 14
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
    def shoot(self) :
        bullet = Bullet(self.rect.x, self.rect.y, self.isLeft)
        all_sprites.add(bullet)
        bullets.add(bullet)
        
class Bullet(pygame.sprite.Sprite) :
    def __init__(self, x, y, face) :
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface((10,20))
        self.image.fill((255,25,35))
        self.rect = self.image.get_rect()
        self.rect.x = x + 200
        self.rect.y = y + 50
        self.speedx = 15
        self.face = face
    def update(self) :
        if self.face :
            self.rect.x -= self.speedx
        else :
            self.rect.x += self.speedx
        if self.rect.x >= 980 or self.rect.x <= 0 :
            self.kill()
        

            
class Enemy_left(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 80))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-1000, -200)
        self.rect.y = HEIGHT - 80
        self.speed = 5
        self.face = False
        self.isAppear = False
        self.isRight = True
    def update(self) :
        key_pressed = pygame.key.get_pressed()
        self.rect.x += self.speed
        if player.rect.x == WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and background_x != -2800 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            self.rect.x -= self.speed
        if player.rect.x == 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and background_x != 0 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            self.rect.x += self.speed
        if self.rect.left > 0 :
            self.isAppear = True
        if self.isAppear and self.rect.left > WIDTH :
            self.rect.x = random.randrange(-1000, -200)
            self.isAppear = False
        
class Enemy_right(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 80))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1200, 2000)
        self.rect.y = HEIGHT - 80
        self.speed = 5
        self.face = False
        self.isAppear = False
        self.isLeft = True
    def update(self) :
        key_pressed = pygame.key.get_pressed()
        self.rect.x -= self.speed
        if player.rect.x == WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and background_x != -2800 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            self.rect.x -= self.speed
        if player.rect.x == 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and background_x != 0 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            self.rect.x += self.speed
        if self.rect.right < WIDTH :
            self.isAppear = True
        if self.isAppear and self.rect.right < 0 :
            self.rect.x = random.randrange(1200, 2000)
            self.isAppear = False
            
class Monster1(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 80))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 1400
        self.rect.y = 100
        self.face = -1
        self.speed = 5
    def update(self) :
        key_pressed = pygame.key.get_pressed()
        if player.rect.x ==  WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and background_x != -2800 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            self.rect.x -= self.speed
        elif player.rect.x == 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and background_x != 0 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            self.rect.x += self.speed 
        if self.rect.left >= platform4.rect.left and self.face == -1:
            self.rect.left -= self.speed
            if self.rect.left == platform4.rect.left :
                self.face = 1
        elif self.face == 1 :
            self.rect.left += self.speed
        if self.rect.right == platform4.rect.right :
            self.face = -1

class Monster2(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 80))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.left = 2730
        self.rect.bottom = 280
        self.face = 1
        self.speed = 5
    def update(self) :
        key_pressed = pygame.key.get_pressed()
        if player.rect.x ==  WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and background_x != -2800 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            self.rect.x -= self.speed
        elif player.rect.x == 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and background_x != 0 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            self.rect.x += self.speed 
        if self.rect.right <= obstacle.rect.left and self.face == 1:
            self.rect.right += self.speed
            if self.rect.right == obstacle.rect.left :
                self.face = -1
        elif self.face == -1 :
            self.rect.right -= self.speed
        if self.rect.left == platform8.rect.left :
            self.face = 1

class Monster3(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 80))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.right = 3530
        self.rect.bottom = 280
        self.face = -1
        self.speed = 5
    def update(self) :
        key_pressed = pygame.key.get_pressed()
        if player.rect.x ==  WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and background_x != -2800 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            self.rect.x -= self.speed
        elif player.rect.x == 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and background_x != 0 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            self.rect.x += self.speed 
        if self.rect.left >= obstacle.rect.right and self.face == -1:
            self.rect.left -= self.speed
            if self.rect.left == obstacle.rect.right :
                self.face = 1
        elif self.face == 1 :
            self.rect.left += self.speed
        if self.rect.right == platform8.rect.right :
            self.face = -1

class Platform2(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 10))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 430
        self.rect.y = 380
        self.isCollide = False
        self.isBack = False
    def update(self) :
        key_pressed = pygame.key.get_pressed()
        if player.rect.x >= WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and background_x != -2800 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            if background_x == -2795 :
                self.rect.x -= 5
            self.rect.x -= 5
        elif player.rect.x <= 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and background_x != 0 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            if background_x == -5 :
                self.rect.x += 5
            self.rect.x += 5

class Platform3(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 10))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 660
        self.rect.y = 280
        self.isCollide = False
        self.isBack = False
    def update(self) :
        key_pressed = pygame.key.get_pressed()
        if player.rect.x >= WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and background_x != -2800 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            if background_x == -2795 :
                self.rect.x -= 5
            self.rect.x -= 5
        elif player.rect.x <= 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and background_x != 0 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            if background_x == -5 :
                self.rect.x += 5
            self.rect.x += 5

class Platform4(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((500, 10))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 890
        self.rect.y = 180
        self.isCollide = False
    def update(self) :
        key_pressed = pygame.key.get_pressed()
        if player.rect.x >= WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and background_x != -2800 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)):
            if background_x == -2795 :
                self.rect.x -= 5
            self.rect.x -= 5
        elif player.rect.x <= 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and background_x != 0 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            if background_x == -5 :
                self.rect.x += 5
            self.rect.x += 5

class Platform5(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 10))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 1800
        self.rect.y = 380
        self.isCollide = False
        self.isBack = False
    def update(self) :
        key_pressed = pygame.key.get_pressed()
        if player.rect.x >= WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and background_x != -2800 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            if background_x == -2795 :
                self.rect.x -= 5
            self.rect.x -= 5
        elif player.rect.x <= 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and background_x != 0 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            if background_x == -5 :
                self.rect.x += 5
            self.rect.x += 5

class Platform6(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 60))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 2030
        self.rect.y = 280
        self.isCollide = False
    def update(self) :
        key_pressed = pygame.key.get_pressed()
        if player.rect.x >= WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and background_x != -2800 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            if background_x == -2795 :
                self.rect.x -= 5
            self.rect.x -= 5
        elif player.rect.x <= 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and background_x != 0 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            if background_x == -5 :
                self.rect.x += 5
            self.rect.x += 5

class Platform7(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 10))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 2500
        self.rect.y = 380
        self.isCollide = False
        self.isBack = False
    def update(self) :
        key_pressed = pygame.key.get_pressed()
        if player.rect.x >= WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and background_x != -2800 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            if background_x == -2795 :
                self.rect.x -= 5
            self.rect.x -= 5
        elif player.rect.x <= 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and background_x != 0 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            if background_x == -5 :
                self.rect.x += 5
            self.rect.x += 5

class Platform8(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((800, 10))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 2730
        self.rect.y = 280
        self.isCollide = False
        self.isBack = False
    def update(self) :
        key_pressed = pygame.key.get_pressed()
        if player.rect.x >= WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and background_x != -2800 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            if background_x == -2795 :
                self.rect.x -= 5
            self.rect.x -= 5
        elif player.rect.x <= 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and background_x != 0 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            if background_x == -5 :
                self.rect.x += 5
            self.rect.x += 5

class Platform9(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 10))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 2550
        self.rect.y = 150
        self.isCollide = False
        self.isBack = False
    def update(self) :
        key_pressed = pygame.key.get_pressed()
        if player.rect.x >= WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and background_x != -2800 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            if background_x == -2795 :
                self.rect.x -= 5
            self.rect.x -= 5
        elif player.rect.x <= 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and background_x != 0 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            if background_x == -5 :
                self.rect.x += 5
            self.rect.x += 5

class Obstacle(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 80))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 3100
        self.rect.bottom = platform8.rect.top
        self.isRight = True
        self.isCollide = False
    def update(self) :
        key_pressed = pygame.key.get_pressed()
        if player.rect.x >= WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and background_x != -2800 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            if background_x == -2795 :
                self.rect.x -= 5
            self.rect.x -= 5
        elif player.rect.x <= 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and background_x != 0 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)):
            if background_x == -5 :
                self.rect.x += 5
            self.rect.x += 5

class Laser(pygame.sprite.Sprite):
    def __init__(self, player_centery):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2000,20))
        self.image.fill((125,180,35))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = player_centery + 10
        self.time = 0
    def update(self):
        self.time += 1
        if self.time > 60:
            self.kill()

class LaserWarning(pygame.sprite.Sprite):
    def __init__(self,player_centery):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2000,10))
        self.image.fill((225,80,235))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = player_centery + 10
        self.time = 0
    def update(self):
        self.time += 1
        if self.time > 1:
            self.kill()
            
def command() :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP or event.key == pygame.K_w :
                player.isJump = True
            elif event.key == pygame.K_SPACE :
                player.isAttack = True
                player.shoot()
        
def enemy_reborn():
    r = random.randrange(1, 3)
    if r == 1 :
        enemy_left = Enemy_left()
        all_sprites.add(enemy_left)
        enemys.add(enemy_left)
    else:
        enemy_right = Enemy_right()
        all_sprites.add(enemy_right)
        enemys.add(enemy_right)

def bullet_enemy_hit(bullets, enemys) :
    hits = pygame.sprite.groupcollide(bullets, enemys, True, True, pygame.sprite.collide_rect_ratio(0.5))
    for hit in hits :
        enemy_reborn()

def bullet_obstacle_hit(bullets, obstacle_group) :
    pygame.sprite.groupcollide(bullets, obstacle_group, True, False, pygame.sprite.collide_rect_ratio(0.8))

def player_obstacle_hit(obstacle_group, player_group) :
    hits = pygame.sprite.groupcollide(obstacle_group, player_group, False, False, pygame.sprite.collide_rect_ratio(0.4))
    if hits :
        obstacle.isCollide = True
    if obstacle.isCollide and player.rect.bottom >= obstacle.rect.top and player.isJump:
        player.rect.bottom = obstacle.rect.top + 8
    if obstacle.isCollide :
        if player.rect.centerx <= obstacle.rect.left - 60 or player.rect.centerx >= obstacle.rect.right + 60 :
            obstacle.isCollide = False
            player.rect.bottom = platform8.rect.top

def player_platform2_hit(platform2_group, player_group) :
    hit = pygame.sprite.groupcollide(platform2_group, player_group, False, False, pygame.sprite.collide_rect_ratio(0.4))
    if hit :
        platform2.isCollide = True
    if platform2.isCollide and player.rect.bottom >= platform2.rect.top :
        player.rect.bottom = platform2.rect.top + 20
    elif platform2.isBack and  player.rect.bottom >= platform2.rect.top :
        player.rect.bottom = platform2.rect.top + 20
        platform3.isCollide = False
        platform2.isCollide = True
        platform2.isBack = False
    if platform2.isCollide and not player.isJump and not platform3.isCollide :
        if player.rect.centerx <= platform2.rect.left - 60 or player.rect.centerx >= platform2.rect.right + 60 :
            player.rect.bottom = 525
            platform2.isCollide = False
    
    
def player_platform3_hit(platform3_group, player_group) :
    hit = pygame.sprite.groupcollide(platform3_group, player_group, False, False, pygame.sprite.collide_rect_ratio(0.4))
    if hit :
        platform3.isCollide = True
    if platform3.isCollide and player.rect.bottom >= platform3.rect.top :
        player.rect.bottom = platform3.rect.top + 20
        platform2.isCollide = False
        platform2.isBack = True
    elif platform3.isBack and  player.rect.bottom >= platform3.rect.top :
        player.rect.bottom = platform3.rect.top + 20
        platform4.isCollide = False
        platform3.isCollide = True
        platform3.isBack = False
    if platform3.isCollide and not player.isJump and not platform2.isCollide :
        if player.rect.centerx <= platform3.rect.left - 60 or player.rect.centerx >= platform3.rect.right + 60 :
            player.rect.bottom = 525
            platform3.isCollide = False
    
def player_platform4_hit(platform4_group, player_group) :
    hit = pygame.sprite.groupcollide(platform4_group, player_group, False, False, pygame.sprite.collide_rect_ratio(0.7))
    if hit :
        platform4.isCollide = True
    if platform4.isCollide and player.rect.bottom >= platform4.rect.top :
        player.rect.bottom = platform4.rect.top + 20
        platform3.isCollide = False
        platform3.isBack = True
    if platform4.isCollide and not player.isJump and not platform3.isCollide :
        if player.rect.centerx <= platform4.rect.left - 60 or player.rect.centerx >= platform4.rect.right + 60 :
            player.rect.bottom = 525
            platform4.isCollide = False

def player_platform5_hit(platform5_group, player_group) :
    hit = pygame.sprite.groupcollide(platform5_group, player_group, False, False, pygame.sprite.collide_rect_ratio(0.3))
    if hit :
        platform5.isCollide = True
    if platform5.isCollide and player.rect.bottom >= platform5.rect.top :
        player.rect.bottom = platform5.rect.top + 20
    elif platform5.isBack and  player.rect.bottom >= platform5.rect.top :
        player.rect.bottom = platform5.rect.top + 20
        platform6.isCollide = False
        platform5.isCollide = True
        platform5.isBack = False
    if platform5.isCollide and not player.isJump and not platform6.isCollide :
        if player.rect.centerx <= platform5.rect.left - 60 or player.rect.centerx >= platform5.rect.right + 60 :
            player.rect.bottom = 525
            platform5.isCollide = False

def player_platform6_hit(platform6_group, player_group) :
    hit = pygame.sprite.groupcollide(platform6_group, player_group, False, False, pygame.sprite.collide_rect_ratio(0.4))
    if hit :
        platform6.isCollide = True
    if platform6.isCollide and player.rect.bottom >= platform6.rect.top :
        player.rect.bottom = platform6.rect.top + 20
        platform5.isCollide = False
        platform5.isBack = True
    if platform6.isCollide and not player.isJump and not platform5.isCollide :
        if player.rect.centerx <= platform6.rect.left - 60 or player.rect.centerx >= platform6.rect.right + 60 :
            player.rect.bottom = 525
            platform6.isCollide = False

def player_platform7_hit(platform7_group, player_group) :
    hit = pygame.sprite.groupcollide(platform7_group, player_group, False, False, pygame.sprite.collide_rect_ratio(0.4))
    if hit :
        platform7.isCollide = True
    if platform7.isCollide and player.rect.bottom >= platform7.rect.top :
        player.rect.bottom = platform7.rect.top + 20
    elif platform7.isBack and  player.rect.bottom >= platform7.rect.top :
        player.rect.bottom = platform7.rect.top + 20
        platform8.isCollide = False
        platform7.isCollide = True
        platform7.isBack = False
    if platform7.isCollide and not player.isJump and not platform8.isCollide :
        if player.rect.centerx <= platform7.rect.left - 60 or player.rect.centerx >= platform7.rect.right + 50 :
            player.rect.bottom = 525
            platform7.isCollide = False

def player_platform8_hit(platform8_group, player_group) :
    hit = pygame.sprite.groupcollide(platform8_group, player_group, False, False, pygame.sprite.collide_rect_ratio(0.78))
    if hit :
        platform8.isCollide = True
    if platform8.isCollide and player.rect.bottom >= platform8.rect.top :
        player.rect.bottom = platform8.rect.top + 20
        platform7.isCollide = False
        platform7.isBack = True
    elif platform8.isBack and  player.rect.bottom >= platform8.rect.top :
        player.rect.bottom = platform8.rect.top + 20
        platform9.isCollide = False
        platform8.isCollide = True
        platform8.isBack = False
    if platform8.isCollide and not player.isJump and not platform7.isCollide :
        if player.rect.centerx <= platform8.rect.left - 60 or player.rect.centerx >= platform8.rect.right + 60 :
            player.rect.bottom = 525
            platform8.isCollide = False

def player_platform9_hit(platform9_group, player_group) :
    hit = pygame.sprite.groupcollide(platform9_group, player_group, False, False, pygame.sprite.collide_rect_ratio(0.4))
    if hit :
        platform9.isCollide = True
    if platform9.isCollide and player.rect.bottom >= platform9.rect.top and not platform7.isCollide :
        player.rect.bottom = platform9.rect.top + 20
        platform8.isCollide = False
        platform8.isBack = True
    if platform9.isCollide and not player.isJump and not platform8.isCollide :
        if player.rect.centerx <= platform9.rect.left - 60 or player.rect.centerx >= platform9.rect.right + 50 :
            player.rect.bottom = 525
            platform9.isCollide = False
            

def Laser_beam():
    global warning
    global laser_time
    if laser_time >= 300 and laser_time <= 420:
        warning += 1
        laser_warning = LaserWarning(player.rect.centery)
        all_sprites.add(laser_warning)
        if warning >= 120 :
            laser = Laser(player.rect.centery)
            all_sprites.add(laser)
            laserbeam.add(laser)
            warning = 0
            laser_time = 0
    

all_sprites = pygame.sprite.Group()
player = Player(200, HEIGHT - 120)
player_group = pygame.sprite.Group()
player_group.add(player)
all_sprites.add(player)
bullets = pygame.sprite.Group()
enemys = pygame.sprite.Group()
for i in range(2) :
    enemy_left = Enemy_left()
    enemy_right = Enemy_right()
    enemys.add(enemy_left)
    enemys.add(enemy_right)
    all_sprites.add(enemy_left)
    all_sprites.add(enemy_right)

monster1 = Monster1()
monster1s = pygame.sprite.Group()
monster1s.add(monster1)
all_sprites.add(monster1)
monster2 = Monster2()
monster2s = pygame.sprite.Group()
monster2s.add(monster2)
all_sprites.add(monster2)
monster3 = Monster3()
monster3s = pygame.sprite.Group()
monster3s.add(monster3)
all_sprites.add(monster3)
 

platform2 = Platform2()
platform2_group = pygame.sprite.Group()
platform2_group.add(platform2)
all_sprites.add(platform2)
platform3 = Platform3()
platform3_group = pygame.sprite.Group()
platform3_group.add(platform3)
all_sprites.add(platform3)
platform4 = Platform4()
platform4_group = pygame.sprite.Group()
platform4_group.add(platform4)
all_sprites.add(platform4)
platform5 = Platform5()
platform5_group = pygame.sprite.Group()
platform5_group.add(platform5)
all_sprites.add(platform5)
platform6 = Platform6()
platform6_group = pygame.sprite.Group()
platform6_group.add(platform6)
all_sprites.add(platform6)
platform7 = Platform7()
platform7_group = pygame.sprite.Group()
platform7_group.add(platform7)
all_sprites.add(platform7)
platform8 = Platform8()
platform8_group = pygame.sprite.Group()
platform8_group.add(platform8)
all_sprites.add(platform8)
platform9 = Platform9()
platform9_group = pygame.sprite.Group()
platform9_group.add(platform9)
all_sprites.add(platform9)

obstacle = Obstacle()
all_sprites.add(obstacle)
obstacle_group = pygame.sprite.Group()
obstacle_group.add(obstacle)
laserbeam = pygame.sprite.Group()
warning = 0 
laser_time = 0
def main() :
    pygame.init()
    pygame.display.set_caption("game")
    global laser_time
    #laser_time = 0   
    while True :
        command()
        clock.tick(FPS)
        screen.blit(background,(background_x,0))
        all_sprites.draw(screen)
        all_sprites.update()
        bullet_enemy_hit(bullets, enemys)
        bullet_obstacle_hit(bullets, obstacle_group)
        player_obstacle_hit(obstacle_group, player_group)
        player_platform2_hit(platform2_group, player_group)
        player_platform3_hit(platform3_group, player_group)
        player_platform4_hit(platform4_group, player_group)
        player_platform5_hit(platform5_group, player_group)
        player_platform6_hit(platform6_group, player_group)
        player_platform7_hit(platform7_group, player_group)
        player_platform8_hit(platform8_group, player_group)
        player_platform9_hit(platform9_group, player_group)
        laser_time += 1
        Laser_beam()
        pygame.display.update()
        
if __name__ == '__main__' :
    main()