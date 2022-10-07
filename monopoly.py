from cgitb import grey
from hashlib import blake2b
from pickle import TRUE
from re import T
from string import whitespace
from time import monotonic
from turtle import clear, width
from xmlrpc.client import TRANSPORT_ERROR
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
GREEN = (34,139,34)
BLUE = (0,96,255)
WHITE = (255,255,255)


#Set up fonts
basicFont = pygame.font.SysFont(None, 48)
Largefont = pygame.font.SysFont(None, 80)

#background
windowSurface.fill(BLACK)
moneybag = pygame.image.load('./moneysign.jpg').convert()
background = pygame.image.load('./monopoly_men.png').convert()
Monopolymen = pygame.image.load('./Monopoly-Man-1.png').convert()
windowSurface.blit(moneybag,(800,0))
windowSurface.blit(background,(0, 0))

text = basicFont.render('Play', True, RED)
Monopoly = Largefont.render('Monopoly',True, BLUE)

def Player1():
    pygame.quit()
def Player2():
    pygame.quit()
def Player3():
    pygame.quit()
def Player4():
    pygame.quit()
    
def next():
    windowSurface.fill(BLACK)
    windowSurface.blit(Monopolymen,(500,0))
    one = basicFont.render('One', True, RED)
    two = basicFont.render('Two', True, RED)
    three = basicFont.render('Three', True, RED)
    four = basicFont.render('Four', True, RED)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                        
                    #if the mouse is clicked on the
                    # button the game is will go to players
                    if 0 <= mouse[0] <= 300 and height/2 <= mouse[1] <= height/2+40:
                        Player1()
                    if 350 <= mouse[0] <= 650 and height/2 <= mouse[1] <= height/2+40:
                        Player2()
                    if 700 <= mouse[0] <= 1000 and height/2 <= mouse[1] <= height/2+40:
                        Player3()
                    if 1050 <= mouse[0] <= 1400 and height/2 <= mouse[1] <= height/2+40:
                        Player4()

        
        #background buttons
        pygame.draw.ellipse(windowSurface,GREEN,[115,height/2-10,140,55])

        pygame.draw.ellipse(windowSurface,GREEN,[460,height/2-10,140,55])          

        pygame.draw.ellipse(windowSurface,GREEN,[825,height/2-10,140,55])

        pygame.draw.ellipse(windowSurface,GREEN,[1160,height/2-10,140,55])

        # superimposing the text onto our button
        windowSurface.blit(one , (150,height/2))
        windowSurface.blit(two , (500,height/2))
        windowSurface.blit(three , (850,height/2))
        windowSurface.blit(four , (1200,height/2))
        pygame.display.update

while True:
      
    for event in pygame.event.get():
          
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

               #checks if a mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
              
            #if the mouse is clicked on the
            # button the game is will go to players
            if width/2-50 <= mouse[0] <= width/2+90 and height/2 <= mouse[1] <= height/2+40:
                Monopoly = Largefont.render('Players', True, BLUE)
                text = basicFont.render('', True, BLACK)
                pygame.draw.ellipse(windowSurface,BLACK,[width/2-55,height/2-10,140,55])
                pygame.display.update
                pygame.display.flip()
                next()


    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()
      
    #background button
    pygame.draw.ellipse(windowSurface,GREEN,[width/2-55,height/2-10,140,55])
              

    # superimposing the text onto our button
    
    windowSurface.blit(text , (width/2-20,height/2))
    # set monopoly
    windowSurface.blit(Monopoly, (width/2-120,height-200))
    #Draw the window onto the screen
    pygame.display.update() 

