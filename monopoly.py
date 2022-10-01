from cgitb import grey
from hashlib import blake2b
from string import whitespace
from time import monotonic
from turtle import clear, width
import pygame, sys
from pygame.locals import *


#Set up pygame
pygame.init()



screen = (1400, 800)
windowSurface = pygame.display.set_mode(screen)
pygame.display.set_caption("Monopoly")

width = windowSurface.get_width()
height = windowSurface.get_height()

#Set up the colors
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,96,255)
WHITE = (255,255,255)


#Set up fonts
basicFont = pygame.font.SysFont(None, 48)
Largefont = pygame.font.SysFont(None, 80)

#background
windowSurface.fill(BLACK)
moneybag = pygame.image.load('./moneysign.jpg').convert()
background = pygame.image.load('./monopoly_men.png').convert()
windowSurface.blit(moneybag,(800,0))
windowSurface.blit(background,(0, 0))

text = basicFont.render('Play', True, RED)
Monopoly = Largefont.render('Monopoly',True, BLUE)



while True:
      
    for event in pygame.event.get():
          
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

               #checks if a mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
              
            #if the mouse is clicked on the
            # button the game is terminated
            if width/2-50 <= mouse[0] <= width/2+90 and height/2 <= mouse[1] <= height/2+40:
                windowSurface.fill(BLACK)
                Monopoly = Largefont.render('Players',True, BLUE)
                pygame.display.update() 


    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()
      
    # if mouse is hovered on a button it
    # changes to lighter shade 
    if width/2-50 <= mouse[0] <= width/2+90 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(windowSurface,GREEN,[width/2-50,height/2,120,40])
          
    else:
        pygame.draw.rect(windowSurface,BLACK,[width/2-50,height/2,120,40])
              

    # superimposing the text onto our button
    windowSurface.blit(text , (width/2-20,height/2))
    # set monopoly
    windowSurface.blit(Monopoly, (width/2-120,height-200))
    #Draw the window onto the screen
    pygame.display.update() 

