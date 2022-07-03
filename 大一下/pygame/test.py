import pygame
import random

FPS=60
WHITE=(255,255,255)
GREEN=(0,255,0)
WIDTH=800
HEIGHT=600

#遊戲初始化and視窗
pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("GAME")
clock=pygame.time.Clock()
font_name=pygame.font.match_font('arail')
#文字
def draw_text(surf,text,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,GREEN)
    text_rect=text_surface.get_rect()
    text_rect.centerx=x
    text_rect.top=y
    surf.blit(text_surface,text_rect)
#重生
def reborn():
    rl=random.randrange(-1,2)
    if rl==1:
        enemyl=Enemyl()
        all_sprites.add(enemyl)
        Enemys.add(enemyl)
    else:
        enemyr=Enemyr()
        all_sprites.add(enemyr)
        Enemys.add(enemyr)

def Sreborn():
    rl=random.randrange(-1,2)
    if rl==1:
        EnemySr=SkyEnemyr()
        all_sprites.add(EnemySr)
        SkyEnemys.add(EnemySr)
    else:
        EnemySl=SkyEnemyl()
        all_sprites.add(EnemySl)
        SkyEnemys.add(EnemySl)

def Boss_reborn():
    Bosses=Boss()
    all_sprites.add(Bosses)
    BOSS.add(Bosses)
#生命值
def draw_health(surf,hp,x,y):
    if hp<0:
        hp=0
    BAR_lenth=100
    BAR_height=10
    fill=(hp/10)*BAR_lenth
    outline_rect=pygame.Rect(x,y,BAR_lenth,BAR_height)
    fill_rect=pygame.Rect(x,y,fill,BAR_height)
    pygame.draw.rect(surf,GREEN,fill_rect)
    pygame.draw.rect(surf,WHITE,outline_rect,2)


#sprites 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,40))
        self.image.fill(GREEN)
        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH/2
        self.rect.bottom=HEIGHT-10
        self.speedy=8
        self.isJump = False
        self.jumpCount = 15
        self.face=1
        self.health=10
    def jump(self) :
        key_pressed=pygame.key.get_pressed()
        if key_pressed[pygame.K_SPACE]:
            self.isJump = True
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
    def update(self):
        key_pressed=pygame.key.get_pressed()
        if key_pressed[pygame.K_d]:
            self.face=1
            self.rect.x+=self.speedy
        if key_pressed[pygame.K_a]:
            self.face=-1
            self.rect.x-=self.speedy
        if key_pressed[pygame.K_SPACE]:
            self.isJump = True
        if self.rect.right>WIDTH:
            self.rect.right=WIDTH
        if self.rect.left<0:
            self.rect.left=0

        if self.isJump :
            if self.jumpCount >= -15 :
                direction = 1
                if self.jumpCount < 0 :
                    direction = -1
                self.rect.y -= (self.jumpCount ** 2) * 0.1 * direction
                self.jumpCount -= 1
            else :
                self.isJump = False
                self.rect.bottom=HEIGHT-10
                self.jumpCount = 15
    def shoot(self):
        bullet=Bullet(self.rect.centerx,self.rect.bottom,self.face)
        all_sprites.add(bullet)
        bullets.add(bullet)
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y,face):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill((255,25,35))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10
        self.face=face
        self.health=1
    def update(self):
        if self.face>0:
            self.rect.x -= self.speedy
        elif self.face<0:
            self.rect.x += self.speedy
        if self.rect.bottom < 0:
            self.kill()
class Enemyl(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,20))
        self.image.fill((255,180,35))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-20,-10)
        self.rect.bottom = HEIGHT-10
        self.speedy = random.randrange(2,4)
        self.health=1
    def update(self):
        self.rect.x+=self.speedy
        if self.rect.left>WIDTH:
            self.rect.x = random.randrange(-20,-10)
class Enemyr(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,20))
        self.image.fill((255,180,35))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(800,820)
        self.rect.bottom = HEIGHT-10
        self.speedy =random.randrange(2,4)
        self.health=1
    def update(self):
        self.rect.x-=self.speedy
        if self.rect.right<0:
            self.rect.x = random.randrange(800,820)
class SkyEnemyr(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,20))
        self.image.fill((255,180,35))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(800,820)
        self.rect.bottom = HEIGHT-150
        self.speedy =random.randrange(2,4)
        self.health=1
    def update(self):
        self.rect.x-=self.speedy
        if self.rect.right<0:
            self.rect.x = random.randrange(800,820)
class SkyEnemyl(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,20))
        self.image.fill((255,180,35))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-20,-10)
        self.rect.bottom = HEIGHT-150
        self.speedy =random.randrange(2,4)
        self.health=1
    def update(self):
        self.rect.x+=self.speedy
        if self.rect.right<0:
            self.rect.x = random.randrange(800,820)
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,160))
        self.image.fill((255,180,100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-20,-10)
        self.rect.bottom = HEIGHT-10
        self.speedy = random.randrange(5,8)
        self.health=4
    def update(self):
        self.rect.x+=self.speedy
        if self.rect.left>WIDTH:
            self.rect.x = random.randrange(-20,-10)
            print(self.health)
        B_hits=pygame.sprite.groupcollide(BOSS,bullets,False,True)
        for hit in B_hits:
            self.health-=1
        if self.health<=0:
            self.kill()

all_sprites=pygame.sprite.Group()
Enemys=pygame.sprite.Group()
SkyEnemys=pygame.sprite.Group()
BOSS=pygame.sprite.Group()
bullets=pygame.sprite.Group()
player=Player()
bosses=Boss()
all_sprites.add(player)
for i in range(2):
    enemyl=Enemyl()
    all_sprites.add(enemyl)
    Enemys.add(enemyl)
    enemyr=Enemyr()
    all_sprites.add(enemyr)
    Enemys.add(enemyr)
    EnemySr=SkyEnemyr()
    EnemySl=SkyEnemyl()
    all_sprites.add(EnemySr)
    all_sprites.add(EnemySl)
    SkyEnemys.add(EnemySr)
    SkyEnemys.add(EnemySl)
re=False
bosscount=0
score=00
#遊戲迴圈
running= True
while running:
    clock.tick(FPS)
    #取得輸入
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                player.shoot()
    #更新遊戲
    all_sprites.update()
    hits=pygame.sprite.groupcollide(Enemys,bullets,True,True)
    S_hits=pygame.sprite.groupcollide(SkyEnemys,bullets,False,True)
    #敵人重生
    for hit in hits:
        score+=1
        reborn()
    for hit in S_hits:
        score+=1
        Sreborn()


    if score%10==0 and score>0 and bosscount<score//10:
        re=True
    if re:
        Boss_reborn()
        bosscount+=1
        re=False
    hits=pygame.sprite.spritecollide(player,Enemys,True)
    S_hits=pygame.sprite.spritecollide(player,SkyEnemys,True)
    B_hits=pygame.sprite.spritecollide(player,BOSS,True)
    if hits:
        player.health-=1
        reborn()
        if player.health<=0:
            running=False
    if S_hits:
        player.health-=1
        Sreborn()
        if player.health<=0:
            running=False
    if B_hits:
        player.health-=3
        if player.health<=0:
            running=False

    



    screen.fill(WHITE)
    all_sprites.draw(screen)
    draw_text(screen,str(score),50,WIDTH/2,10)
    draw_health(screen,player.health,5,10)
    pygame.display.update()