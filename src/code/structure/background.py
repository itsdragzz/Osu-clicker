import pygame




def open_bg(screen_width, screen_height):

    screen = pygame.display.set_mode((screen_width, screen_height))

    background = pygame.image.load("src/graphics/bg.jpg")

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))




