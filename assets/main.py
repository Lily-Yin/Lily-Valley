# pylint: disable=no-member
"""Arquivo main.py - Código principal do Lily-Valley."""

import pygame

class Player:
    """Classe que representa o jogador do jogo."""
    def __init__(self, name):
        """Inicializa o jogador com um nome."""
        self.name = name
        self.score = 0

    def move(self, direction):
        """Move o jogador para a direção fornecida ('left', 'right', 'up', 'down')."""
        print(f"{self.name} move {direction}")


def main():
    """Função principal do jogo."""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Lily-Valley")

    player = Player("Lily")
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    print("main.py rodou corretamente! 🎉")


if __name__ == "__main__":
    main()
