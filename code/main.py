import pygame, sys
from settings import *

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
fps_clock = pygame.time.Clock()

# osu cirlce
osu_size = 100
osu_surf_old = pygame.image.load('images/Osulogo.png').convert_alpha()
osu_surf = pygame.transform.scale(osu_surf_old, (osu_size, osu_size))
osu_rect = osu_surf.get_rect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
acce = 0

while (True):
	for event in pygame.event.get():
		# if function to close the program
		if (event.type == pygame.QUIT):
			pygame.quit()
			sys.exit()

		if (event.type == pygame.MOUSEBUTTONDOWN):
			if (osu_rect.collidepoint(event.pos)):
				print('clicked')
				osu_size = 120
				acce = 0
				print(osu_size)

	# Circle
	screen.blit(osu_surf,osu_rect)
	acce -= 1
	osu_size += acce	
	if (osu_size <= 100): osu_size = 100

	osu_surf = pygame.transform.scale(osu_surf_old, (osu_size, osu_size))
	osu_rect = osu_surf.get_rect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))

	pygame.display.update()
	fps_clock.tick(60)