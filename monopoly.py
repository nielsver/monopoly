from cgitb import grey
from hashlib import blake2b
from os import remove
from pickle import TRUE
from re import T
from sre_parse import WHITESPACE
from string import whitespace
from time import monotonic
from tokenize import Whitespace
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
RED = (253, 53, 0)
GREEN = (115, 254, 66)
BLUE = (8, 173, 250)
WHITE = (255,255,255)
orange = (255, 173, 1)


#Set up fonts
basicFont = pygame.font.SysFont(None, 48)
Largefont = pygame.font.SysFont(None, 80)
smallfont = pygame.font.SysFont(None, 28)
#background
windowSurface.fill(BLACK)
moneybag = pygame.image.load('./moneysign.jpg').convert()
background = pygame.image.load('./monopoly_men.png').convert()
Monopolymen = pygame.image.load('./Monopoly-Man-1.png').convert()
bord = pygame.image.load('./n6IaB.jpg').convert()
bord = pygame.transform.rotate(bord, 90)
windowSurface.blit(moneybag,(800,0))
windowSurface.blit(background,(0, 0))

text = basicFont.render('Play', True, RED)
Monopoly = Largefont.render('Monopoly',True, BLUE)

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def Player1():
    windowSurface.fill(WHITE)
    pygame.display.update()
    windowSurface.blit(bord,(325,0))
    rules = "how to play:\n-d to dobble\n-b to buy\n-h to build house\n-q to quit\n\njail:\n-1 cash\n-2 card\n -3 pass"
    money1 = 1500
    money2 = 1500
    money3 = 1500
    money4 = 1500
    player1 = smallfont.render("player 1: " + str(money1),True, RED)
    player2 = smallfont.render("player 2: " + str(money2),True, BLUE)
    player3 = smallfont.render("player 3: " + str(money3),True, GREEN)
    player4 = smallfont.render("player 4: " + str(money4),True, orange)
    blit_text(windowSurface, rules, (10, 0), smallfont)
    pygame.display.update()
    print("player 1")
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #update Players money
        windowSurface.blit(player1,(1150,40))
        pygame.draw.line(windowSurface, RED,(1150,60),(1350,60),1)
        windowSurface.blit(player2,(1150,80))
        pygame.draw.line(windowSurface, BLUE,(1150,100),(1350,100),1)
        windowSurface.blit(player3,(1150,120))
        pygame.draw.line(windowSurface, GREEN,(1150,140),(1350,140),1)
        windowSurface.blit(player4,(1150,160))
        pygame.draw.line(windowSurface, orange,(1150,180),(1350,180),1)
        pygame.display.update()


def Player2():
    windowSurface.fill(WHITE)
    pygame.display.update()
    print("player 2")
def Player3():
    windowSurface.fill(WHITE)
    pygame.display.update()
    print("player 3")
def Player4():
    windowSurface.fill(WHITE)
    pygame.display.update()
    print("player 4")
    
def next():
    windowSurface.fill(BLACK)
    windowSurface.blit(Monopolymen,(500,50))
    Players = Largefont.render('Players', True,BLUE)
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
                        Players = Largefont.render('', True,BLUE)
                        one = basicFont.render('', True, RED)
                        two = basicFont.render('', True, RED)
                        three = basicFont.render('', True, RED)
                        four = basicFont.render('', True, RED)
                        #background buttons
                        pygame.draw.ellipse(windowSurface,WHITE,[115,height/2-10,140,55])

                        pygame.draw.ellipse(windowSurface,WHITE,[460,height/2-10,140,55])          

                        pygame.draw.ellipse(windowSurface,WHITE,[825,height/2-10,140,55])

                        pygame.draw.ellipse(windowSurface,WHITE,[1160,height/2-10,140,55])
                        pygame.display.update()
                        Player1()
                    if 350 <= mouse[0] <= 650 and height/2 <= mouse[1] <= height/2+40:
                        Players = Largefont.render('', True,BLUE)
                        one = basicFont.render('', True, RED)
                        two = basicFont.render('', True, RED)
                        three = basicFont.render('', True, RED)
                        four = basicFont.render('', True, RED)
                        #background buttons
                        pygame.draw.ellipse(windowSurface,WHITE,[115,height/2-10,140,55])

                        pygame.draw.ellipse(windowSurface,WHITE,[460,height/2-10,140,55])          

                        pygame.draw.ellipse(windowSurface,WHITE,[825,height/2-10,140,55])

                        pygame.draw.ellipse(windowSurface,WHITE,[1160,height/2-10,140,55])
                        pygame.display.update()
                        Player2()
                    if 700 <= mouse[0] <= 1000 and height/2 <= mouse[1] <= height/2+40:
                        Players = Largefont.render('', True,BLUE)
                        one = basicFont.render('', True, RED)
                        two = basicFont.render('', True, RED)
                        three = basicFont.render('', True, RED)
                        four = basicFont.render('', True, RED)
                        #background buttons
                        pygame.draw.ellipse(windowSurface,WHITE,[115,height/2-10,140,55])

                        pygame.draw.ellipse(windowSurface,WHITE,[460,height/2-10,140,55])          

                        pygame.draw.ellipse(windowSurface,WHITE,[825,height/2-10,140,55])

                        pygame.draw.ellipse(windowSurface,WHITE,[1160,height/2-10,140,55])
                        pygame.display.update()
                        Player3()
                    if 1050 <= mouse[0] <= 1400 and height/2 <= mouse[1] <= height/2+40:
                        Players = Largefont.render('', True,BLUE)
                        one = basicFont.render('', True, RED)
                        two = basicFont.render('', True, RED)
                        three = basicFont.render('', True, RED)
                        four = basicFont.render('', True, RED)
                        #background buttons
                        pygame.draw.ellipse(windowSurface,WHITE,[115,height/2-10,140,55])

                        pygame.draw.ellipse(windowSurface,WHITE,[460,height/2-10,140,55])          

                        pygame.draw.ellipse(windowSurface,WHITE,[825,height/2-10,140,55])

                        pygame.draw.ellipse(windowSurface,WHITE,[1160,height/2-10,140,55])
                        pygame.display.update()
                        Player4()
    
        mouse = pygame.mouse.get_pos()
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
        windowSurface.blit(Players,(width/2-120,height-200))
        pygame.display.update()

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
                text = basicFont.render('', True, BLACK)
                pygame.draw.ellipse(windowSurface,BLACK,[width/2-55,height/2-10,140,55])
                pygame.display.update()
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

