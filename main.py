import sys
import pygame

from scripts.entity import Entity


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tank mania 1")

        self.screen = pygame.display.set_mode((900, 650))
        self.clock = pygame.time.Clock()

        self.crashed = False

        self.entity = Entity(
            self,
            self.crashed,
            "player",
            "poly",
            self.screen,
            surface = self.screen,
            color = (59, 68, 255),
            position=(100, 100),
            speed = [0, 0],
            size = [100, 50]
        )

    def load_level(self):
        pass

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((33, 255, 38))

            self.entity.update()
            self.entity.render()

            pygame.display.update()

            self.clock.tick(60)


Game().run()
