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
        self.isOut = False
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
    def draw(self) :
        screen.blit(self.image, (self.rect.x, self.rect.y))
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
                if self.rect.x >= WIDTH - 200 :
                    self.rect.x = WIDTH - 200
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
                if self.rect.x <= 20 :
                    self.rect.x = 20
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
                    self.isOut = True
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
        if self.isOut and (self.rect.centerx <= obstacle.rect.left - 50 or self.rect.centerx >= obstacle.rect.right + 50) :
            if not self.isJump :
                self.rect.bottom = 525
                self.isOut = False
        
class Enemy(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 80))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = -(random.randrange(200, 1000))
        self.rect.y = HEIGHT - 80
        self.speed = 1
        #random.randrange(1, 4)
    def update(self) :
        self.rect.x += self.speed

class Platform(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 60))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 2000
        self.rect.y = 300
        self.isRight = True
        self.isCollide = False
    def draw(self) :
        screen.blit(self.image, (self.rect.x, self.rect.y))
    def move(self) :
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            if self.isRight == False :
                if player.rect.x >= WIDTH - 200 :
                    self.isRight = True
            else :
                if self.isCollide == False :
                    self.rect.x -= 5
        if key_pressed[pygame.K_LEFT] :
            self.isRight = False
            if player.rect.x <= 20 :
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
    def draw(self) :
        screen.blit(self.image, (self.rect.x, self.rect.y))
    def move(self) :
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            if self.isRight == False :
                if player.rect.x >= WIDTH - 200 :
                    self.isRight = True
            else :
                if self.isCollide == False :
                    self.rect.x -= 5
        if key_pressed[pygame.K_LEFT] :
            self.isRight = False
            if player.rect.x <= 20 :
                self.rect.x += 5
            
def player_act(player) :
    player.draw()
    player.idle()
    player.run()
    player.jump()
    player.attack()
    player.fall()

def enemys_act(enemys) :
    enemys.draw(screen)
    enemys.update()

def platform_act(platform) :
    platform.draw()
    platform.move()

def obstacle_act(obstacle) :
    obstacle.draw()
    obstacle.move()

def command() :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP or event.key == pygame.K_w :
                player.isJump = True
            elif event.key == pygame.K_SPACE :
                player.isAttack = True

def judge_hit(obstacles, player_group) :
    hits = pygame.sprite.groupcollide(obstacles, player_group, False, False, pygame.sprite.collide_rect_ratio(0.5))
    if hits :
        player.isCollide = True
        obstacle.isCollide = True
        platform.isCollide = True    
    else :
        player.isCollide = False
        obstacle.isCollide = False
        platform.isCollide = False
    
player = Player(0,HEIGHT - 120)
player_group = pygame.sprite.Group()
player_group.add(player)

enemys = pygame.sprite.Group()
for i in range(1) :
    enemy = Enemy()
    enemys.add(enemy)

platform = Platform() 

obstacle = Obstacle()
obstacles = pygame.sprite.Group()
obstacles.add(obstacle)

def main() :
    pygame.init()
    pygame.display.set_caption("game")
    
    while True :
        command()
        clock.tick(FPS)
        screen.blit(background,(background_x,0))
        player_act(player)  
        enemys_act(enemys)
        platform_act(platform)
        obstacle_act(obstacle)
        judge_hit(obstacles, player_group)
        
        pygame.display.update()

if __name__ == '__main__' :
    main()