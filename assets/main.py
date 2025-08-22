import pygame
import sys

# Inicializar pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo com Player e Zumbi")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Carregar imagens
background_img = pygame.image.load("background.png").convert()
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

player_img = pygame.image.load("player_fixed.png").convert_alpha()
zombie_img = pygame.image.load("zombie_fixed.png").convert_alpha()
tile_img = pygame.image.load("tile_fixed.png").convert_alpha()

# Escalar imagens
player_img = pygame.transform.scale(player_img, (64, 64))
zombie_img = pygame.transform.scale(zombie_img, (64, 64))
tile_img = pygame.transform.scale(tile_img, (64, 64))

# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(midbottom=(100, HEIGHT - 64))
        self.vel_y = 0
        self.speed = 5
        self.jump_power = -15
        self.on_ground = True

    def update(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False

        self.vel_y += 1
        self.rect.y += self.vel_y

        if self.rect.bottom >= HEIGHT - 64:
            self.rect.bottom = HEIGHT - 64
            self.vel_y = 0
            self.on_ground = True

class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = zombie_img
        self.rect = self.image.get_rect(midbottom=(WIDTH - 100, HEIGHT - 64))
        self.speed = 2

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.left = WIDTH

player = Player()
zombie = Zombie()

all_sprites = pygame.sprite.Group()
all_sprites.add(player, zombie)

def draw_ground():
    for x in range(0, WIDTH, 64):
        screen.blit(tile_img, (x, HEIGHT - 64))

# Loop principal
running = True
while running:
    clock.tick(FPS)

    # Desenhar fundo
    screen.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys)
    zombie.update()

    if player.rect.colliderect(zombie.rect):
        print("Colidiu com o zumbi!")

    draw_ground()
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
