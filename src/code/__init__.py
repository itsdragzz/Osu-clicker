import pygame
import sys


import src.code.structure.background as bg
from src.code.structure.setting import Settings
import src.code.osu_click as oc


def main():


    game_settings = Settings()

    oc.main(game_settings.screen_width, game_settings.screen_height)

    #bg.open_bg(game_settings.screen_width, game_settings.screen_height)
    
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    fps_clock = pygame.time.Clock()
    fps_clock.tick(60)
    