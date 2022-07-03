import pygame

WIDTH = 600
HEIGHT = 300
FPS = 60
WHITE = (255,255,255)

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("MOVE")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = HEIGHT

    def update(self) :
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]:
            self.rect.x += 2
        if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]:
            self.rect.x -= 2
        if key_pressed[pygame.K_UP] or key_pressed[pygame.K_w]:
            self.rect.y -= 2
        if key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_s] :
            self.rect.y += 2
    
        if self.rect.right > WIDTH :
            self.rect.right = WIDTH
        if self.rect.left < 0 :
            self.rect.left = 0
        if self.rect.top  < 0 :
            self.rect.top = 0
        if self.rect.bottom > HEIGHT :
            self.rect.bottom = HEIGHT

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True

while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
    clock.tick(FPS)
    screen.fill(WHITE)
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.update()


pygame.quit