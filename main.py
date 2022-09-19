import pygame
import sys


import src.code.structure.background as bg
from src.code.structure.setting import Settings



def run():
        
    pygame.init()
    
    while True:
        game_settings = Settings()

        bg.open_bg(game_settings.screen_width, game_settings.screen_height)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    run()