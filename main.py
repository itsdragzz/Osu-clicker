import pygame
import sys


from src.code.structure.setting import Settings


class Game:

    def __init__(self):
        self.screen = None
        pygame.init()
        game_settings = Settings()
        pygame.display.set_caption('Osu clicker!')

    def run(self):
        game_settings = Settings()
        self.screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
        background = pygame.image.load("src/graphics/bg.jpg")

        while True:
            self.screen.fill((0, 0, 0))
            self.screen.blit(background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
