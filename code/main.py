import pygame, sys
from settings import *

# Basic program, need to class __init__ and classes later
# Items
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
fps_clock = pygame.time.Clock()
font = pygame.font.Font('data/Walkway_Black.ttf',50)

# osu circleg
osu_size = 100
osu_surf = pygame.image.load('data/Osulogo.png').convert_alpha()
osu_surf_scaled = pygame.transform.scale(osu_surf, (osu_size, osu_size))
osu_rect = osu_surf_scaled.get_rect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
acce = 0

# basic pp counter
pp = 0
pp_surf = font.render(f'PP: {pp}', False, ('White'))
pp_rect = pp_surf.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/7*6))

while (True):
	for event in pygame.event.get():
		# if function to close the program
		if (event.type == pygame.QUIT):
			pygame.quit()
			sys.exit()

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
	pygame.display.update()
	# Controls frames per sec (60 fps)
	fps_clock.tick(60)