import pygame, sys
from pygame.locals import *

#Set up pygame
pygame.init()


(width, height) = (1000, 500)
windowSurface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Monopoly")

#Set up the colors
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)


#Set up fonts
basicFont = pygame.font.SysFont(None, 48)

#Draw the white background onto the surface
windowSurface.fill(WHITE)


text = basicFont.render('HELLO WORLD', True, RED)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

#Draw the text onto the surface
windowSurface.blit(text,textRect)

#Draw the window onto the screen
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()