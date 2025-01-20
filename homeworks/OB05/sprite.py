import pygame
import random
import os

NO_IMAGES = True
wnSize,fpS =(600,800),60
# WIDTH = 800  # ширина игрового окна
# HEIGHT = 600 # высота игрового окна
# FPS = 30 # частота кадров в секунду
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        if NO_IMAGES:
            self.image = pygame.Surface((50, 40))
            self.image.fill(GREEN)
        else:
            self.image = pygame.transform.scale(player_img, (50, 38))
            self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center =  ( wnSize[0]//2, wnSize[1] - 20 )
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > wnSize[0]:
            self.rect.right = wnSize[0]
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        if NO_IMAGES:
            self.image = pygame.Surface((30, 40))
            self.image.fill(RED)
        else:
            self.image = pygame.transform.scale(meteor_img,  (50, 38))
            self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(wnSize[0] - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > wnSize[1] + 10 or self.rect.left < -25 or self.rect.right > wnSize[0] + 20:
            self.rect.x = random.randrange(wnSize[0]- self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        if  NO_IMAGES:
            self.image = pygame.Surface((10, 20))
            self.image.fill(YELLOW)
        else:
            self.image = pygame.transform.scale(bullet_img,  (10, 20))
            self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode(wnSize)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock(  )

background_img = pygame.image.load(os.path.join(img_folder, 'starfield.png')).convert()
background = pygame.transform.scale(background_img,  wnSize )
background_rect = background.get_rect()
player_img = pygame.image.load(os.path.join(img_folder, "playerShip2_orange.png")).convert()
meteor_img = pygame.image.load(os.path.join(img_folder, "meteorBrown_med1.png")).convert()
bullet_img = pygame.image.load(os.path.join(img_folder, "laserRed16.png")).convert()

all_sprites,mobs,bullets = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
player= Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

running = True
while running:
    clock.tick(fpS)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False

    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()