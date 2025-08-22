class Player:
    """Classe que representa o jogador no Lily-Valley."""

import pygame

# Inicializa o Pygame
pygame.init()

# Cria uma janela visível
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Teste Lily-Valley")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
print("O arquivo teste.py rodou corretamente! 🎉")
