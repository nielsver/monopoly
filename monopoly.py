import pygame
from sys import exit
(width, height) = (1000, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
pygame.display.set_caption("Hello World")
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()