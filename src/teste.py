# pylint: disable=no-member
"""Arquivo teste.py - código de teste do Lily-Valley."""

import pygame

def main():
    """Função principal para rodar o teste do Pygame."""
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Teste Lily-Valley")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    print("teste.py rodou corretamente! 🎉")


if __name__ == "__main__":
    main()
