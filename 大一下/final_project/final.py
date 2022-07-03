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
obstacle_top = 189
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)
font_name = font_name = os.path.join("font.ttf")
startbg = pygame.image.load(os.path.join("5x", "startbg.png")).convert()
endbg = pygame.image.load(os.path.join("5x", "endbg.png")).convert()
pygame.mixer.init()
attack_sound=pygame.mixer.Sound(os.path.join("Sound", "Attack.wav"))
dead_sound=pygame.mixer.Sound(os.path.join("Sound", "deadmessage.wav"))
gothurted_sound=pygame.mixer.Sound(os.path.join("Sound", "gothurted.wav"))
Enenmydead_sound=pygame.mixer.Sound(os.path.join("Sound", "Enenmydead.wav"))
jump_sound=pygame.mixer.Sound(os.path.join("Sound", "Jump.wav"))
Laser_sound=pygame.mixer.Sound(os.path.join("Sound", "Laser.wav"))
laserwarning_sound=pygame.mixer.Sound(os.path.join("Sound", "laserwarning.wav"))
Oneknifekillinto=pygame.mixer.Sound(os.path.join("Sound", "Oneknifekillinto.wav"))
Playerdead_sound=pygame.mixer.Sound(os.path.join("Sound", "Playerdead.wav"))
pygame.mixer.music.load(os.path.join("Sound","bgm.ogg"))
pygame.mixer.music.set_volume(0.2)

class Player(pygame.sprite.Sprite) :
    def __init__(self, x, y) :
        pygame.sprite.Sprite.__init__(self)
        self.isJump = False
        self.jumpCount = 15
        self.isAttack = False
        self.isLeft = False
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
        self.health = 250
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
                if self.rect.x >= WIDTH - 300 :
                    self.rect.x = WIDTH - 300
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
        attack_sound.play()
        
class Bullet(pygame.sprite.Sprite) :
    def __init__(self, x, y, face) :
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("5x", "sword_wave.png")), (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x + 200
        self.rect.y = y + 50
        self.speedx = 15
        self.face = face
    def update(self) :
        if self.face :
            self.image = pygame.transform.scale(pygame.image.load(os.path.join("5x", "sword_wave_left.png")), (80, 80))
            self.rect.x -= self.speedx
        else :
            self.image = pygame.transform.scale(pygame.image.load(os.path.join("5x", "sword_wave.png")), (80, 80))
            self.rect.x += self.speedx
        if self.rect.x >= 980 or self.rect.x <= 0 :
            self.kill()
                
class Enemy_left(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.sprites_fly = list()
        self.sprites_fly.append(pygame.image.load(os.path.join("bat", "32x32-bat-sprite1.png")))
        self.sprites_fly.append(pygame.image.load(os.path.join("bat", "32x32-bat-sprite2.png")))
        self.sprites_fly.append(pygame.image.load(os.path.join("bat", "32x32-bat-sprite3.png")))
        self.sprites_fly.append(pygame.image.load(os.path.join("bat", "32x32-bat-sprite4.png")))
        self.current_sprite_fly = 0
        self.image = pygame.transform.scale(self.sprites_fly[self.current_sprite_fly], (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-1000, -200)
        self.rect.y = HEIGHT - 80
        self.speed = 5
        self.face = False
        self.isAppear = False
        self.isRight = True
    def update(self) :
        self.current_sprite_fly += 0.1
        if self.current_sprite_fly >= len(self.sprites_fly) :
            self.current_sprite_fly = 0   
        self.image = pygame.transform.scale(self.sprites_fly[int(self.current_sprite_fly)], (60, 60))
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
        self.sprites_fly = list()
        self.sprites_fly.append(pygame.image.load(os.path.join("bat", "32x32-bat-sprite5.png")))
        self.sprites_fly.append(pygame.image.load(os.path.join("bat", "32x32-bat-sprite6.png")))
        self.sprites_fly.append(pygame.image.load(os.path.join("bat", "32x32-bat-sprite7.png")))
        self.sprites_fly.append(pygame.image.load(os.path.join("bat", "32x32-bat-sprite8.png")))
        self.current_sprite_fly = 0
        self.image = pygame.transform.scale(self.sprites_fly[self.current_sprite_fly], (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1200, 2000)
        self.rect.y = HEIGHT - 80
        self.speed = 5
        self.face = False
        self.isAppear = False
        self.isLeft = True
    def update(self) :
        self.current_sprite_fly += 0.1
        if self.current_sprite_fly >= len(self.sprites_fly) :
            self.current_sprite_fly = 0   
        self.image = pygame.transform.scale(self.sprites_fly[int(self.current_sprite_fly)], (60, 60))
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
        self.sprites_walk = list()
        self.sprites_walk_left = list()
        self.sprites_walk.append(pygame.image.load(os.path.join("walk", "walk - pitchfork1.png")))
        self.sprites_walk.append(pygame.image.load(os.path.join("walk", "walk - pitchfork2.png")))
        self.sprites_walk.append(pygame.image.load(os.path.join("walk", "walk - pitchfork3.png")))
        self.sprites_walk.append(pygame.image.load(os.path.join("walk", "walk - pitchfork4.png")))
        self.sprites_walk_left.append(pygame.image.load(os.path.join("walk", "walk - pitchfork5.png")))
        self.sprites_walk_left.append(pygame.image.load(os.path.join("walk", "walk - pitchfork6.png")))
        self.sprites_walk_left.append(pygame.image.load(os.path.join("walk", "walk - pitchfork7.png")))
        self.sprites_walk_left.append(pygame.image.load(os.path.join("walk", "walk - pitchfork8.png")))
        self.current_sprite_walk = 0
        self.current_sprite_walk_left = 0
        self.image = pygame.transform.scale(self.sprites_walk[self.current_sprite_walk], (90, 90))
        self.rect = self.image.get_rect()
        self.rect.x = 1400
        self.rect.y = 100
        self.face = -1
        self.speed = 5
        self.health = 5
    def update(self) :
        if self.face == 1 :
            self.current_sprite_walk += 0.1
            if self.current_sprite_walk >= len(self.sprites_walk) :
                self.current_sprite_walk = 0   
            self.image = pygame.transform.scale(self.sprites_walk[int(self.current_sprite_walk)], (90, 90))
        elif self.face == -1 :
            self.current_sprite_walk_left += 0.1
            if self.current_sprite_walk_left >= len(self.sprites_walk_left) :
                self.current_sprite_walk_left = 0   
            self.image = pygame.transform.scale(self.sprites_walk_left[int(self.current_sprite_walk_left)], (90, 90))
        key_pressed = pygame.key.get_pressed()
        if player.rect.x ==  WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and background_x != -2800 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            self.rect.x -= self.speed
        elif player.rect.x == 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and background_x != 0 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            self.rect.x += self.speed 
        if self.rect.left >= platform4.rect.left and self.face == -1:
            self.rect.left -= self.speed
            if self.rect.left <= platform4.rect.left :
                self.face = 1
        elif self.face == 1 :
            self.rect.left += self.speed
        if self.rect.right >= platform4.rect.right :
            self.face = -1

class Monster2(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.sprites_fly = list()
        self.sprites_fly_left = list()
        self.sprites_fly.append(pygame.image.load(os.path.join("dragon", "flying_dragon-red-RGB4.png")))
        self.sprites_fly.append(pygame.image.load(os.path.join("dragon", "flying_dragon-red-RGB5.png")))
        self.sprites_fly.append(pygame.image.load(os.path.join("dragon", "flying_dragon-red-RGB6.png")))
        self.sprites_fly_left.append(pygame.image.load(os.path.join("dragon", "flying_dragon-red-RGB1.png")))
        self.sprites_fly_left.append(pygame.image.load(os.path.join("dragon", "flying_dragon-red-RGB2.png")))
        self.sprites_fly_left.append(pygame.image.load(os.path.join("dragon", "flying_dragon-red-RGB3.png")))
        self.current_sprite_fly = 0
        self.current_sprite_fly_left = 0
        self.image = pygame.transform.scale(self.sprites_fly[self.current_sprite_fly], (120, 120))
        self.rect = self.image.get_rect()
        self.rect.left = 2730
        self.rect.bottom = 280
        self.face = 1
        self.speed = 5
        self.health = 10
    def update(self) :
        if self.face == 1 :
            self.current_sprite_fly += 0.1
            if self.current_sprite_fly >= len(self.sprites_fly) :
                self.current_sprite_fly = 0   
            self.image = pygame.transform.scale(self.sprites_fly[int(self.current_sprite_fly)], (120, 120))
        elif self.face == -1 :
            self.current_sprite_fly_left += 0.1
            if self.current_sprite_fly_left >= len(self.sprites_fly_left) :
                self.current_sprite_fly_left = 0   
            self.image = pygame.transform.scale(self.sprites_fly_left[int(self.current_sprite_fly_left)], (120, 120))
        key_pressed = pygame.key.get_pressed()
        if player.rect.x ==  WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and background_x != -2800 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            self.rect.x -= self.speed
        elif player.rect.x == 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and background_x != 0 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            self.rect.x += self.speed 
        if self.rect.right <= obstacle.rect.left and self.face == 1:
            self.rect.right += self.speed
            if self.rect.right >= obstacle.rect.left :
                self.face = -1
        elif self.face == -1 :
            self.rect.right -= self.speed
        if self.rect.left <= platform8.rect.left :
            self.face = 1

class Monster3(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.sprites_fly = list()
        self.sprites_fly_left = list()
        self.sprites_fly.append(pygame.image.load(os.path.join("dragon", "flying_dragon-red-RGB4.png")))
        self.sprites_fly.append(pygame.image.load(os.path.join("dragon", "flying_dragon-red-RGB5.png")))
        self.sprites_fly.append(pygame.image.load(os.path.join("dragon", "flying_dragon-red-RGB6.png")))
        self.sprites_fly_left.append(pygame.image.load(os.path.join("dragon", "flying_dragon-red-RGB1.png")))
        self.sprites_fly_left.append(pygame.image.load(os.path.join("dragon", "flying_dragon-red-RGB2.png")))
        self.sprites_fly_left.append(pygame.image.load(os.path.join("dragon", "flying_dragon-red-RGB3.png")))
        self.current_sprite_fly = 0
        self.current_sprite_fly_left = 0
        self.image = pygame.transform.scale(self.sprites_fly[self.current_sprite_fly], (120, 120))
        self.rect = self.image.get_rect()
        self.rect.right = 3530
        self.rect.bottom = 280
        self.face = -1
        self.speed = 5
        self.health = 10
    def update(self) :
        if self.face == 1 :
            self.current_sprite_fly += 0.1
            if self.current_sprite_fly >= len(self.sprites_fly) :
                self.current_sprite_fly = 0   
            self.image = pygame.transform.scale(self.sprites_fly[int(self.current_sprite_fly)], (120, 120))
        elif self.face == -1 :
            self.current_sprite_fly_left += 0.1
            if self.current_sprite_fly_left >= len(self.sprites_fly_left) :
                self.current_sprite_fly_left = 0   
            self.image = pygame.transform.scale(self.sprites_fly_left[int(self.current_sprite_fly_left)], (120, 120))
        key_pressed = pygame.key.get_pressed()
        if player.rect.x ==  WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and background_x != -2800 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            self.rect.x -= self.speed
        elif player.rect.x == 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and background_x != 0 and (not obstacle.isCollide or (obstacle.isCollide and player.rect.bottom == obstacle_top)) :
            self.rect.x += self.speed 
        if self.rect.left >= obstacle.rect.right and self.face == -1:
            self.rect.left -= self.speed
            if self.rect.left <= obstacle.rect.right :
                self.face = 1
        elif self.face == 1 :
            self.rect.left += self.speed
        if self.rect.right >= platform8.rect.right :
            self.face = -1

class Platform2(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("ground", "platform1.png"))
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
        self.image = pygame.image.load(os.path.join("ground", "platform1.png"))
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
        self.image = pygame.image.load(os.path.join("ground", "platform2.png"))
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
        self.image = pygame.image.load(os.path.join("ground", "platform1.png"))
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
        self.image = pygame.image.load(os.path.join("ground", "platform6.png"))
        self.rect = self.image.get_rect()
        self.rect.x = 2030
        self.rect.y = 250
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
        self.image = pygame.image.load(os.path.join("ground", "platform4.png"))
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
        self.image = pygame.image.load(os.path.join("ground", "platform5.png"))
        self.rect = self.image.get_rect()
        self.rect.x = 2680
        self.rect.y = 280
        self.isCollide = False
        self.isBack = False
        self.Can = False
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
        self.image = pygame.image.load(os.path.join("ground", "platform3.png"))
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
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("ground", "Tree.png")), (60, 140))
        self.rect = self.image.get_rect()
        self.rect.x = 3000
        self.rect.bottom = platform8.rect.top + 20
        self.isRight = True
        self.isCollide = False
        self.Can = False
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

class Star1(pygame.sprite.Sprite) :
    def __init__(self, platform6_centerx, platform6_top) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("5x", "Heart.png")), (80, 80))
        self.rect = self.image.get_rect()
        self.rect.centerx = platform6_centerx
        self.rect.bottom = platform6_top - 5
        self.face = 1
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
        if self.rect.bottom <= platform6.rect.top - 5 and self.face == 1 :
            self.rect.bottom -= 1
            if self.rect.bottom == 201 :
                self.face = -1
        elif self.face == -1 :
            self.rect.bottom += 1
            if  self.rect.bottom == platform6.rect.top - 5 :
                self.face = 1

class Star2(pygame.sprite.Sprite) :
    def __init__(self, platform9_centerx, platform9_top) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("5x", "Heart.png")), (80, 80))
        self.rect = self.image.get_rect()
        self.rect.centerx = platform9_centerx
        self.rect.bottom = platform9_top - 5
        self.face = 1
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
        if self.rect.bottom <= platform9.rect.top - 5 and self.face == 1 :
            self.rect.bottom -= 1
            if self.rect.bottom == 110 :
                self.face = -1
        elif self.face == -1 :
            self.rect.bottom += 1
            if  self.rect.bottom == platform9.rect.top - 5 :
                self.face = 1

class Laser(pygame.sprite.Sprite) :
    def __init__(self, site) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2000,20))
        self.image.fill((125,180,35))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = site
        self.time = 0
    def update(self) :
        self.time += 1
        if self.time > 60:
            self.kill()

class LaserWarning(pygame.sprite.Sprite) : 
    def __init__(self,site) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2000,10))
        self.image.fill((225,80,235))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = site
        self.time = 0
    def update(self) :
        self.time += 1
        if self.time > 1:
            self.kill()
                    
def enemy_reborn() :
    r = random.randrange(1, 3)
    if r == 1 :
        enemy_left = Enemy_left()
        all_sprites.add(enemy_left)
        enemys.add(enemy_left)
        
    else :
        enemy_right = Enemy_right()
        all_sprites.add(enemy_right)
        enemys.add(enemy_right)

def bullet_enemy_hit(bullets, enemys) :
    global score
    hits = pygame.sprite.groupcollide(bullets, enemys, True, True, pygame.sprite.collide_rect_ratio(0.5))
    for hit in hits :
        score += 1
        enemy_reborn()
        Enenmydead_sound.play()

def bullet_monster1_hit(bullets, monster1s) :
    global score
    hits = pygame.sprite.groupcollide(bullets, monster1s, True, False, pygame.sprite.collide_rect_ratio(0.8))
    if hits :
        monster1.health -= 1
    if monster1.health == 0 :
        for hit in hits :
            score += 10
        monster1.kill()


def bullet_monster2_hit(bullets, monster2s) :
    global score
    hits = pygame.sprite.groupcollide(bullets, monster2s, True, False, pygame.sprite.collide_rect_ratio(0.8))
    if hits :
        monster2.health -= 1
    if monster2.health == 0 :
        for hit in hits :
            score += 20
        monster2.kill()


def bullet_monster3_hit(bullets, monster3s) :
    global score
    hits = pygame.sprite.groupcollide(bullets, monster3s, True, False, pygame.sprite.collide_rect_ratio(0.8))
    if hits :
        monster3.health -= 1
    if monster3.health == 0 :
        for hit in hits :
            score += 20
        monster3.kill()


def bullet_obstacle_hit(bullets, obstacle_group) :
    pygame.sprite.groupcollide(bullets, obstacle_group, True, False, pygame.sprite.collide_rect_ratio(0.8))

def player_obstacle_hit(obstacle_group, player_group) :
    key_pressed = pygame.key.get_pressed()
    hit = pygame.sprite.groupcollide(obstacle_group, player_group, False, False, pygame.sprite.collide_rect_ratio(0.4))
    if hit :
        obstacle.isCollide = True
    if obstacle.isCollide and player.rect.bottom >= obstacle.rect.top and player.isJump :
        player.rect.bottom = obstacle.rect.top + 15
        obstacle.Can = True
    elif obstacle.Can :
        if (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) or (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) :
            obstacle.isCollide = False
        if player.rect.centerx <= obstacle.rect.left - 20 or player.rect.centerx >= obstacle.rect.right + 40 :
            obstacle.Can = False
            player.rect.bottom = platform8.rect.top
    if obstacle.isCollide :
        if player.rect.centerx <= obstacle.rect.left - 20 or player.rect.centerx >= obstacle.rect.right + 40 :
            obstacle.isCollide = False
            player.rect.bottom = platform8.rect.top
            obstacle.Can = False

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
        platform2.isBack = False
    if platform4.isCollide and not player.isJump and not platform3.isCollide :
        if player.rect.centerx <= platform4.rect.left - 40 or player.rect.centerx >= platform4.rect.right + 40 :
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
    hit = pygame.sprite.groupcollide(platform6_group, player_group, False, False, pygame.sprite.collide_rect_ratio(0.3))
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
        platform8.Can = True
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
    if platform8.isCollide and player.rect.bottom >= platform8.rect.top and platform8.Can :
        player.rect.bottom = platform8.rect.top + 20
        platform7.isCollide = False
        platform7.isBack = True
    elif platform8.isBack and  player.rect.bottom >= platform8.rect.top and platform8.Can :
        player.rect.bottom = platform8.rect.top + 20
        platform9.isCollide = False
        platform8.isCollide = True
        platform8.isBack = False
    if platform8.isCollide and not player.isJump and not platform7.isCollide :
        if player.rect.centerx <= platform8.rect.left - 50 or player.rect.centerx >= platform8.rect.right + 50 :
            player.rect.bottom = 525
            platform8.isCollide = False
            platform8.Can = False
    

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
            if player.isLeft :
                platform8.Can = False
            
def Laser_beam():
    global warning
    global laser_time
    global site
    if laser_time == 300 :
        laserwarning_sound.play()
        site = player.rect.centery + 10
    if laser_time >= 300 and laser_time <= 420:
        warning += 1
        laser_warning = LaserWarning(site)
        all_sprites.add(laser_warning)
        if warning==120:
            Laser_sound.play()        
        if warning >= 120 :
            laser = Laser(site)
            all_sprites.add(laser)
            laserbeam.add(laser)
            warning = 0
            laser_time = 0
            site = 0

def cure1(player, star1_group):
    hit = pygame.sprite.spritecollide(player, star1_group, True, pygame.sprite.collide_rect_ratio(0.4))
    if hit :
        player.health += 10

def cure2(player, star2_group):
    hit = pygame.sprite.spritecollide(player, star2_group, True, pygame.sprite.collide_rect_ratio(0.4))
    if hit :
        player.health += 10

def damages(player, enemys):
    hit = pygame.sprite.spritecollide(player, enemys, True, pygame.sprite.collide_rect_ratio(0.4))
    if hit and not platform2.isBack and not platform3.isBack and not platform5.isBack and not platform8.isBack :
        player.health -= 3
        gothurted_sound.play()
        enemy_reborn()

def laserdamages(player, laserbeam):
    hit = pygame.sprite.spritecollide(player, laserbeam, False)
    if hit :
        player.health -= 0.25

def monster1damages(player, monster1s) :
    hit = pygame.sprite.spritecollide(player, monster1s, False, pygame.sprite.collide_rect_ratio(0.5))
    if hit :
        player.health -= 10
        gothurted_sound.play()
        if monster1.face == -1 :
            monster1.rect.left = player.rect.right
            monster1.face = 1
        elif monster1.face == 1 :
            monster1.rect.right = player.rect.left
            monster1.face = -1

def monster2damages(player, monster2s) :
    hit = pygame.sprite.spritecollide(player, monster2s, False, pygame.sprite.collide_rect_ratio(0.5))
    if hit :
        player.health -= 20
        gothurted_sound.play()
        if monster2.face == -1 :
            player.rect.right = monster2.rect.left
            monster2.face = 1
        elif monster2.face == 1 :
            monster2.rect.right = player.rect.left
            monster2.face = -1
    
def monster3damages(player, monster3s) :
    hit = pygame.sprite.spritecollide(player, monster3s, False, pygame.sprite.collide_rect_ratio(0.5))
    if hit :
        player.health -= 20
        gothurted_sound.play()
        if monster3.face == -1 :
            monster3.rect.left = player.rect.right
            monster3.face = 1
        elif monster3.face == 1 :
            player.rect.left = monster3.rect.right
            monster3.face = -1

def draw_health(surf, hp, x, y):
    if hp < 0:
        hp = 0
    if hp > 250 :
        hp = 250
    BAR_lenth = 990
    BAR_height = 10
    fill = (hp / 250) * BAR_lenth
    outline_rect = pygame.Rect(x, y, BAR_lenth, BAR_height)
    fill_rect = pygame.Rect(x, y, fill, BAR_height)
    if hp > 50:
        pygame.draw.rect(surf, GREEN, fill_rect)
    else :
        pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

def draw_monster1_health(surf, monster1_hp, x, y):
    if monster1.health > 0 :
        BAR_lenth = 60
        BAR_height = 10
        fill =  (monster1_hp / 5) * BAR_lenth
        outline_rect = pygame.Rect(x, y, BAR_lenth, BAR_height)
        fill_rect = pygame.Rect(x, y, fill, BAR_height)
        pygame.draw.rect(surf, RED, fill_rect)
        pygame.draw.rect(surf, WHITE, outline_rect, 2)

def draw_monster2_health(surf, monster2_hp, x, y):
    if monster2.health > 0 :
        BAR_lenth = 60
        BAR_height = 10
        fill =  (monster2_hp / 10) * BAR_lenth
        outline_rect = pygame.Rect(x, y, BAR_lenth, BAR_height)
        fill_rect = pygame.Rect(x, y, fill, BAR_height)
        pygame.draw.rect(surf, RED, fill_rect)
        pygame.draw.rect(surf, WHITE, outline_rect, 2)

def draw_monster3_health(surf, monster3_hp, x, y):
    if monster3.health > 0 :
        BAR_lenth = 60
        BAR_height = 10
        fill =  (monster3_hp / 10) * BAR_lenth
        outline_rect = pygame.Rect(x, y, BAR_lenth, BAR_height)
        fill_rect = pygame.Rect(x, y, fill, BAR_height)
        pygame.draw.rect(surf, RED, fill_rect)
        pygame.draw.rect(surf, WHITE, outline_rect, 2)

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, GREEN)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface,text_rect)
    
def start():    
    global show_start
    waiting = True
    if show_start:
        start_bg = pygame.transform.scale(startbg,(WIDTH,HEIGHT))
        screen.blit(start_bg,(0,0))
        draw_text(screen, "一刀殺進去!", 64, WIDTH/2, HEIGHT/4)
        draw_text(screen, "←(a) →(d)移動  ↑(w)跳躍  SPACE(空白鍵)射擊", 24, WIDTH/2, HEIGHT/2)
        draw_text(screen, "按任意鍵開始遊戲", 18, WIDTH/2, HEIGHT*3/4)
        pygame.display.update()
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYUP:
                    waiting = False
                    Oneknifekillinto.play()
    show_start = False

def end():
    global show_start
    global score
    waiting = True
    if player.health <= 0:
        Playerdead_sound.play()
        end_bg = pygame.transform.scale(endbg,(WIDTH,HEIGHT))
        screen.blit(end_bg,(0,0))
        draw_text(screen, f"這次得分為{score}!", 64, WIDTH/2, HEIGHT/4)
        draw_text(screen, "好爛請多多加油!", 24, WIDTH/2, HEIGHT/2)
        draw_text(screen, "按任意鍵重新開始", 18, WIDTH/2, HEIGHT*3/4)
        pygame.display.update()
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYUP:
                    waiting = False
        item()
        show_start = True

def item():
    global all_sprites,player,player_group,bullets,enemys,enemy_left,enemy_right
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

    global monsters,monster1,monster1s,monster2,monster2s,monster3,monster3s
    monsters=pygame.sprite.Group()
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
    monsters.add(monster1)
    monsters.add(monster2)
    monsters.add(monster3)

    global platform2,platform2_group,platform3,platform3_group,platform4,platform4_group,platform5,platform5_group
    global platform6,platform6_group,platform7,platform7_group,platform8,platform8_group,platform9,platform9_group
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

    global background_x,obstacle,obstacle_group,laserbeam,star1,star1_group,star2,star2_group,warning,laser_time,site,score
    obstacle = Obstacle()
    all_sprites.add(obstacle)
    obstacle_group = pygame.sprite.Group()
    obstacle_group.add(obstacle)
    laserbeam = pygame.sprite.Group()
    star1 = Star1(platform6.rect.centerx, platform6.rect.top)
    star1_group = pygame.sprite.Group()
    star1_group.add(star1)
    all_sprites.add(star1)
    star2 = Star2(platform9.rect.centerx, platform9.rect.top)
    star2_group = pygame.sprite.Group()
    star2_group.add(star2)
    all_sprites.add(star2)
    warning = 0 
    laser_time = 0
    site = 0
    score=0
    background_x = 0


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
obstacle_group = pygame.sprite.Group()
obstacle_group.add(obstacle)
all_sprites.add(obstacle)

laserbeam = pygame.sprite.Group()

star1 = Star1(platform6.rect.centerx, platform6.rect.top)
star1_group = pygame.sprite.Group()
star1_group.add(star1)
all_sprites.add(star1)
star2 = Star2(platform9.rect.centerx, platform9.rect.top)
star2_group = pygame.sprite.Group()
star2_group.add(star2)
all_sprites.add(star2)

warning = 0 
laser_time = 0
site = 0
score = 0
show_start = True
pygame.mixer.music.play(-1)
def main() :
    pygame.init()
    pygame.display.set_caption("game")
    global laser_time  
    while True :
        start()
        command()
        clock.tick(FPS)
        screen.blit(background,(background_x, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        bullet_enemy_hit(bullets, enemys)
        bullet_monster1_hit(bullets, monster1s)
        bullet_monster2_hit(bullets, monster2s)
        bullet_monster3_hit(bullets, monster3s)
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
        cure1(player, star1_group)
        cure2(player, star2_group)
        damages(player, enemys)
        laserdamages(player, laserbeam)
        monster1damages(player, monster1s)
        monster2damages(player, monster2s)
        monster3damages(player, monster3s)
        laser_time += 1
        Laser_beam()
        draw_health(screen, player.health, 5, 10)
        draw_monster1_health(screen, monster1.health, monster1.rect.left, monster1.rect.top - 15)
        draw_monster2_health(screen, monster2.health, monster2.rect.left, monster2.rect.top - 15)
        draw_monster3_health(screen, monster3.health, monster3.rect.left, monster3.rect.top - 15)
        draw_text(screen, str(score), 50, WIDTH/2, 10)
        pygame.display.update()
        end()
if __name__ == '__main__' :
    main()