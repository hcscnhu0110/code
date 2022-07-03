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

class Player(pygame.sprite.Sprite) :
    def __init__(self, x, y) :
        pygame.sprite.Sprite.__init__(self)
        self.isJump = False
        self.jumpCount = 15
        self.isAttack = False
        self.isLeft = False
        self.isCollide = False
        self.isOut1 = False
        self.isOut2 = False
        self.isOut3 = False
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
    def update(self) :
        self.idle()
        self.run()
        self.jump()
        self.attack()
        self.fall()
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
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d] :
            self.isLeft = False
            self.current_sprite_run += 0.1
            if self.current_sprite_run >= len(self.sprites_run) :
                self.current_sprite_run = 0
            self.image = self.sprites_run[int(self.current_sprite_run)]
            if self.isCollide == False or (self.isCollide and player.rect.centerx > obstacle.rect.centerx) :
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
            if self.isCollide == False or (self.isCollide and player.rect.centerx <= obstacle.rect.centerx) :
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
                if self.isCollide : 
                    self.rect.bottom = obstacle.rect.top + 6
                    self.isOut1 = True
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
            
    def fall(self) :
        if self.isOut1 and (self.rect.centerx <= obstacle.rect.left - 50 or self.rect.centerx >= obstacle.rect.right + 50) :
            if not self.isJump :
                self.rect.bottom = 525
                self.isOut1 = False
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
        O_collide=pygame.sprite.spritecollide(self,obstacles,False,False)
        if O_collide :
            self.isRight = False
        if self.isRight :
            if player.rect.x == WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) :
                site = self.rect.x
                if background_x != -2800 and not player.isCollide :
                    self.rect.x = site
                else :
                    self.rect.x += self.speed
            else :
                if player.rect.x == 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and background_x != 0 :
                    self.rect.x += 5
                self.rect.x += self.speed
        else :
            if player.rect.x == 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) : 
                site = self.rect.x
                if background_x != 0 :
                    self.rect.x = site
                else :
                    self.rect.x -= self.speed
            else :
                if player.rect.x == WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and background_x != -2800 :
                    self.rect.x -= 5
                self.rect.x -= self.speed
        if self.rect.left > 0 :
            self.isAppear = True

        if self.isAppear and self.rect.left > WIDTH :
            self.rect.x = random.randrange(-1000, -200)
        if self.isAppear and self.rect.right < 0 and not self.isRight :
            self.rect.x = random.randrange(-1000, -200)
            self.isRight = True

        

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
        O_collide = pygame.sprite.spritecollide(self,obstacles,False,False)
        if O_collide :
            self.isLeft = False 
        if self.isLeft :
            if player.rect.x == 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) : 
                site = self.rect.x
                if background_x != 0 and not player.isCollide:
                    self.rect.x = site
                else :
                    self.rect.x -= self.speed
            else :
                if player.rect.x == WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and background_x != -2800 :
                    self.rect.x -= 5
                self.rect.x -= self.speed
        else :
            if player.rect.x == WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) :
                site = self.rect.x
                if background_x != -2800 :
                    self.rect.x = site
                else :
                    self.rect.x += self.speed
            else :
                if player.rect.x == 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and background_x != 0 :
                    self.rect.x += 5
                self.rect.x += self.speed
        if self.rect.right < WIDTH :
            self.isAppear = True
        if self.isAppear and self.rect.right < 0 :
            self.rect.x = random.randrange(1200, 2000)
        if self.isAppear and self.rect.left > WIDTH and not self.isLeft:
            self.rect.x = random.randrange(1200, 2000)
            self.isLeft = True
            
class Platform1(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 60))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 2000
        self.rect.y = 300
        self.isRight = True
        self.isCollide = False
    def update(self) :
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d] :
            if self.isRight == False :
                if player.rect.x >= WIDTH - 450 :
                    self.isRight = True
            else :
                if self.isCollide == False :
                    self.rect.x -= 5
        if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]:
            self.isRight = False
            if player.rect.x <= 200 and background_x != 0:
                self.rect.x += 5

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
        if player.rect.x >= WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and background_x != -2800 :
            if background_x == -2795 :
                self.rect.x -= 5
            self.rect.x -= 5
        elif player.rect.x <= 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and background_x != 0 :
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
    def update(self) :
        key_pressed = pygame.key.get_pressed()
        if player.rect.x >= WIDTH - 450 and (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and background_x != -2800 :
            if background_x == -2795 :
                self.rect.x -= 5
            self.rect.x -= 5
        elif player.rect.x <= 200 and (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and background_x != 0 :
            if background_x == -5 :
                self.rect.x += 5
            self.rect.x += 5

class Obstacle(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 80))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 2500
        self.rect.y = HEIGHT - 80
        self.isRight = True
        self.isCollide = False
    def update(self) :
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d] :
            if self.isRight == False :
                if player.rect.x >= WIDTH - 450 :
                    self.isRight = True
            else :
                if self.isCollide == False :
                    self.rect.x -= 5
        if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_d] :
            self.isRight = False
            if player.rect.x <= 200 and background_x != 0 and not self.isCollide:
                self.rect.x += 5

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2000,20))
        self.image.fill((125,180,35))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.time = 0
    def update(self):
        self.rect.bottom = HEIGHT-10
        self.time += 1
        if self.time > 60:
            self.kill()

class LaserWarning(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2000,10))
        self.image.fill((225,80,235))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.time = 0
    def update(self):
        self.rect.bottom = HEIGHT-10
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

def player_obstacle_hit(obstacles, player_group) :
    hits = pygame.sprite.groupcollide(obstacles, player_group, False, False, pygame.sprite.collide_rect_ratio(0.5))
    if hits :
        player.isCollide = True
        obstacle.isCollide = True
        platform1.isCollide = True
    else :
        player.isCollide = False
        obstacle.isCollide = False
        platform1.isCollide = False

def enemy_reborn():
    r = random.randrange(-1,2)
    if r == 1 or r == 2:
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

    if platform3.isCollide and not player.isJump and not platform2.isCollide :
        if player.rect.centerx <= platform3.rect.left - 60 or player.rect.centerx >= platform3.rect.right + 60 :
            player.rect.bottom = 525
            platform3.isCollide = False
    
    
def Laser_beam(lasertime):
    global warning
    if lasertime >= 300 and lasertime <= 420:
        warning += 1
        laser_warning = LaserWarning()
        all_sprites.add(laser_warning)
        if warning >= 120 :
            laser = Laser()
            all_sprites.add(laser)
            laserbeam.add(laser)
            warning = 0
            lasertime = 0
    

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

platform1 = Platform1() 
all_sprites.add(platform1)
platform2 = Platform2()
platform2_group = pygame.sprite.Group()
platform2_group.add(platform2)
all_sprites.add(platform2)
platform3 = Platform3()
platform3_group = pygame.sprite.Group()
platform3_group.add(platform3)
all_sprites.add(platform3)
obstacle = Obstacle()
all_sprites.add(obstacle)
obstacles = pygame.sprite.Group()
obstacles.add(obstacle)
all_sprites.add(platform1)
laserbeam = pygame.sprite.Group()
warning = 0 
def main() :
    pygame.init()
    pygame.display.set_caption("game")
    laser_time = 0
   
    while True :
        command()
        clock.tick(FPS)
        screen.blit(background,(background_x,0))
        all_sprites.draw(screen)
        all_sprites.update()
        player_obstacle_hit(obstacles, player_group)
        bullet_enemy_hit(bullets, enemys)
        player_platform2_hit(platform2_group, player_group)
        player_platform3_hit(platform3_group, player_group)
        laser_time += 1
        Laser_beam(laser_time)
        pygame.display.update()
    
if __name__ == '__main__' :
    main()