import pygame
import sys
from src.code.structure.setting import Settings

def pp():
    pp = 0
    return pp

def main(SCREEN_WIDTH, SCREEN_HEIGHT):
    
    font = pygame.font.Font(None, 50)
    
# osu circleg
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    osu_size = 100
    osu_surf = pygame.image.load('src\graphics\osu_logo.png').convert_alpha()
    osu_surf_scaled = pygame.transform.scale(osu_surf, (osu_size, osu_size))
    osu_rect = osu_surf_scaled.get_rect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
    acce = 0

    # basic pp counter

    pp = pp()
    
    pp_surf = font.render(f'PP: {pp}', False, ('White'))
    pp_rect = pp_surf.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/7*6))

   
    for event in pygame.event.get():

        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (osu_rect.collidepoint(event.pos)):
                acce = 3.6
                pp += 1

        # Basic screen background, enable frames to load correctly without stacking on one another
        screen.fill('Pink')

        # Circle
        screen.blit(osu_surf_scaled,osu_rect)
        acce -= 1
        osu_size += acce	
        if (osu_size <= 100): osu_size = 100
        osu_surf_scaled = pygame.transform.scale(osu_surf, (osu_size, osu_size))
        osu_rect = osu_surf_scaled.get_rect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))

        # pp counter
        pp_surf = font.render(f'PP: {pp}', False, ('White'))
        screen.blit(pp_surf,pp_rect)

        # Updates the frames on the display surface (screen/terminal)
        # Controls frames per sec (60 fps)
        