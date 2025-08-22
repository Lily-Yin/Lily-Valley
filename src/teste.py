# pylint: disable=no-member, unused-variable
"""Arquivo teste.py - Código de teste do Lily-Valley."""

import pygame

def run_game_loop():
    """Função que roda o loop principal do Pygame."""
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Teste Lily-Valley")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


def main():
    """Função principal do teste."""
    pygame.init()
    run_game_loop()
    print("teste.py rodou corretamente! 🎉")


if __name__ == "__main__":
    main()
