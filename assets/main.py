"""Arquivo principal do Lily-Valley. Aqui roda o jogo e controla o jogador."""

"""Módulo principal do jogo Lily-Valley."""

# pylint: disable=no-member

import sys  # módulos padrão
import pygame  # terceiros

class Player:
    """Classe que representa o jogador e seus movimentos."""

    def __init__(self):
        """Inicializa o jogador."""
        self.x = 0
        self.y = 0

    def move(self, player_keys):
        """Move o jogador baseado nas teclas pressionadas."""
        if player_keys[pygame.K_LEFT] or player_keys[pygame.K_a]:
            self.x -= 5
        if player_keys[pygame.K_RIGHT] or player_keys[pygame.K_d]:
            self.x += 5
        if player_keys[pygame.K_UP] or player_keys[pygame.K_w]:
            self.y -= 5

class Game:
    """Classe que controla o loop principal do jogo."""

    def __init__(self):
        """Inicializa o Pygame e a janela."""
        pygame.init()
        self.running = True
        self.player = Player()

    def run(self):
        """Loop principal do jogo."""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            self.player.move(keys)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
