from ast import Or
from cgitb import grey
from email.mime import image
from hashlib import blake2b
from os import remove
from pickle import TRUE
from re import T
from sre_parse import WHITESPACE
from string import whitespace
from telnetlib import STATUS
from time import monotonic
from tokenize import Whitespace
from tracemalloc import start
from turtle import clear, width
from xmlrpc.client import TRANSPORT_ERROR
from button import Button
import pygame, sys
from pygame.locals import *
import random

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
ORANGE = (255, 173, 1)


#Set up fonts
basicFont = pygame.font.SysFont(None, 48)
Largefont = pygame.font.SysFont(None, 80)
smallfont = pygame.font.SysFont(None, 28)
#background
moneybag = pygame.image.load('./moneysign.jpg').convert()
moneybag = pygame.transform.scale(moneybag, (300,300))
Monopolymen = pygame.image.load('./monopoly_men.png').convert()
#Monopolymen = pygame.image.load('./Monopoly-Man-1.png').convert()
Monopolymen = pygame.transform.scale(Monopolymen, (300,300))
monopolylogo = pygame.image.load('./monopolylogo.jpg').convert()
monopolylogo = pygame.transform.scale(monopolylogo, (700,150))
button=pygame.image.load("button.png").convert()
button = pygame.transform.scale(button, (200,50))
bord = pygame.image.load('./n6IaB.jpg').convert()
bord = pygame.transform.rotate(bord, 90)
text = basicFont.render('Play', True, RED)
Monopoly = Largefont.render('Monopoly',True, BLUE)

dobbelsteen1 = pygame.image.load("./dobbelstenen/dobbelsteen1.PNG").convert()
dobbelsteen1 = pygame.transform.scale(dobbelsteen1, (100,100))
dobbelsteen2 = pygame.image.load("./dobbelstenen/dobbelsteen2.PNG").convert()
dobbelsteen2 = pygame.transform.scale(dobbelsteen2, (100,100))
dobbelsteen3 = pygame.image.load("./dobbelstenen/dobbelsteen3.PNG").convert()
dobbelsteen3 = pygame.transform.scale(dobbelsteen3, (100,100))
dobbelsteen4 = pygame.image.load("./dobbelstenen/dobbelsteen4.PNG").convert()
dobbelsteen4 = pygame.transform.scale(dobbelsteen4, (100,100))
dobbelsteen5 = pygame.image.load("./dobbelstenen/dobbelsteen5.PNG").convert()
dobbelsteen5 = pygame.transform.scale(dobbelsteen5, (100,100))
dobbelsteen6 = pygame.image.load("./dobbelstenen/dobbelsteen6.PNG").convert()
dobbelsteen6 = pygame.transform.scale(dobbelsteen6, (100,100))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("./font.ttf", size)

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
def positie1(gedobbeltnummer):
    i = 0
    if(i == 0):
        x = gedobbeltnummer
        i = 1
    else:
        x = gedobbeltnummer + x
        if (x >= 40):
            x - 40
    return x
def positie2(gedobbeltnummer):
    i = 0
    if(i == 0):
        x = gedobbeltnummer
        i = 1
    else:
        x = gedobbeltnummer + x
        if (x >= 40):
            x - 40
    return x
def positiecheck(positie, type):
    if(type == 1 or type == 2):
        if positie == 0:
            print("0")
        elif positie == 1:
            print("1")
        elif positie == 2:
            print("2")
        elif positie == 3:
            print("3")
        elif positie == 4:
            print("4")
        elif positie == 5:
            print("5")
        elif positie == 6:
            print("6")
        elif positie == 7:
            print("7")
        elif positie == 8:
            print("8")
        elif positie == 9:
            print("9")
        elif positie == 10:
            print("10")
        elif positie == 11:
            print("11")
        elif positie == 12:
            print("12")
        elif positie == 13:
            print("13")
        elif positie == 14:
            print("14")
        elif positie == 15:
            print("15")
        elif positie == 16:
            print("16")
        elif positie == 17:
            print("17")
        elif positie == 18:
            print("18")
        elif positie == 19:
            print("19")
        elif positie == 20:
            print("20")
        elif positie == 21:
            print("21")
        elif positie == 22:
            print("22")
        elif positie == 23:
            print("23")
        elif positie == 24:
            print("24")
        elif positie == 25:
            print("25")
        elif positie == 26:
            print("26")
        elif positie == 27:
            print("27")
        elif positie == 28:
            print("28")
        elif positie == 29:
            print("29")
        elif positie == 30:
            print("30")
        elif positie == 31:
            print("31")
        elif positie == 32:
            print("32")
        elif positie == 33:
            print("30")
        elif positie == 34:
            print("34")
        elif positie == 35:
            print("35")
        elif positie == 36:
            print("36")
        elif positie == 37:
            print("37")
        elif positie == 38:
            print("38")
        elif positie == 39:
            print("39")

    
def dobbelen():
    int1 = random.randint(1,6)
    int2 = random.randint(1,6)
    worp = int1 + int2

    #dobbelsteen 1 op het scherm tonen
    if int1 == 1:
        windowSurface.blit(dobbelsteen1,(250, 400))
    if int1 ==2:
        windowSurface.blit(dobbelsteen2,(250, 400))
    if int1 ==3:
        windowSurface.blit(dobbelsteen3,(250, 400))
    if int1 ==4:
        windowSurface.blit(dobbelsteen4,(250, 400))
    if int1 ==5:
        windowSurface.blit(dobbelsteen5,(250, 400))
    if int1 ==6:
        windowSurface.blit(dobbelsteen6,(250, 400))
    
    #dobbelsteen 2 tonen op scherm
    if int2 == 1:
        windowSurface.blit(dobbelsteen1,(450, 400))
    if int2 ==2:
        windowSurface.blit(dobbelsteen2,(450, 400))
    if int2 ==3:
        windowSurface.blit(dobbelsteen3,(450, 400))
    if int2 ==4:
        windowSurface.blit(dobbelsteen4,(450, 400))
    if int2 ==5:
        windowSurface.blit(dobbelsteen5,(450, 400))
    if int2 ==6:
        windowSurface.blit(dobbelsteen6,(450, 400))
    return worp

def Player2():
    windowSurface.fill(WHITE)
    pygame.display.update()
    #image bord
    windowSurface.blit(bord,(0,0))
    #init text
    money1 = 1500
    money2 = 1500
    player1 = smallfont.render("player 1: " + str(money1),True, RED)
    player2 = smallfont.render("player 2: " + str(money2),True, BLUE)
    dobbel = Button(button, pos=(width/2, 450), 
                        text_input="dobbel", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
    # rules text
    pygame.display.update()
    
    while True:
        mouse = pygame.mouse.get_pos()
        aandebeurt = 1
        algedobbelt = 0
        #player one
        #update Players money
        windowSurface.blit(player1,(1150,40))
        pygame.draw.line(windowSurface, RED,(1150,60),(1350,60),1)
        windowSurface.blit(player2,(1150,80))
        pygame.draw.line(windowSurface, BLUE,(1150,100),(1350,100),1)
        pygame.display.update()
        while aandebeurt == 1:
            mouse = pygame.mouse.get_pos()
            pygame.draw.rect(windowSurface, RED, pygame.Rect(width/2+200, 400, 400,400))
            if(algedobbelt == 0):
                dobbel = Button(button, pos=(width/2 + 400, 600), 
                            text_input="dobbel", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
                for btn in [dobbel]:
                    btn.changeColor(mouse)
                    btn.update(windowSurface)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if dobbel.checkForInput(mouse):
                            worp = dobbelen()
                            positiespeler1 = positie1(worp)
                            kankopen = positiecheck(positiespeler1,1)
                            algedobbelt = 1
                    if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
            if(algedobbelt == 1):
                volgende = Button(button, pos=(width/2 + 400, 600), 
                            text_input="next", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
                for btn in [volgende]:
                    btn.changeColor(mouse)
                    btn.update(windowSurface)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            if volgende.checkForInput(mouse):
                                aandebeurt = 2
                                algedobbelt = 0
                    if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
            pygame.display.update()
        #player two
        #update Players money
        windowSurface.blit(player1,(1150,40))
        pygame.draw.line(windowSurface, RED,(1150,60),(1350,60),1)
        windowSurface.blit(player2,(1150,80))
        pygame.draw.line(windowSurface, BLUE,(1150,100),(1350,100),1)
        pygame.display.update()
        while aandebeurt == 2:
            mouse = pygame.mouse.get_pos()
            pygame.draw.rect(windowSurface, BLUE, pygame.Rect(width/2+200, 400, 400,400))
            if(algedobbelt == 0):
                dobbel = Button(button, pos=(width/2 + 400, 600), 
                            text_input="dobbel", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
                for btn in [dobbel]:
                    btn.changeColor(mouse)
                    btn.update(windowSurface)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if dobbel.checkForInput(mouse):
                            worp = dobbelen()
                            positiespeler2 = positie2(worp)
                            kankopen = positiecheck(positiespeler2,1)
                            algedobbelt = 1
                    if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
            if(algedobbelt == 1):
                volgende = Button(button, pos=(width/2 + 400, 600), 
                            text_input="next", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
                for btn in [volgende]:
                    btn.changeColor(mouse)
                    btn.update(windowSurface)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            if volgende.checkForInput(mouse):
                                aandebeurt = 1
                                algedobbelt = 0
                    if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
            pygame.display.update()
 
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
    windowSurface.blit(moneybag,(width-300,100))
    windowSurface.blit(Monopolymen,(0, 100))
    windowSurface.blit(monopolylogo,(width/2 - 350, 150))
    backbutton = Button(button, pos=(width/2, 700), 
                        text_input="BACK", font=get_font(20), base_color=WHITE, hovering_color=RED)
    player2button = Button(button, pos=(width/2, 400), 
                        text_input="2 PLAYERS", font=get_font(20), base_color=WHITE, hovering_color=BLUE)
    player3button =  Button(button, pos=(width/2, 500), 
                        text_input="3 PLAYERS", font=get_font(20), base_color=WHITE, hovering_color=BLUE)
    player4button =  Button(button, pos=(width/2, 600), 
                        text_input="4 PLAYERS", font=get_font(20), base_color=WHITE, hovering_color=BLUE)

    while True:
        mouse = pygame.mouse.get_pos()
        for btn in [backbutton, player2button,player3button, player4button]:
            btn.changeColor(mouse)
            btn.update(windowSurface)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if backbutton.checkForInput(mouse):
                    mainmenu()
                if player2button.checkForInput(mouse):
                    Player2()
                if player3button.checkForInput(mouse):
                    Player3()
                if player4button.checkForInput(mouse):
                    Player4

        pygame.display.update()

def mainmenu():
    windowSurface.fill(BLACK)
    windowSurface.blit(moneybag,(width-300,100))
    windowSurface.blit(Monopolymen,(0, 100))
    windowSurface.blit(monopolylogo,(width/2 - 350, 150))
    startbutton = Button(button, pos=(width/2, 450), 
                        text_input="START", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
    quitbutton = Button(button, pos=(width/2, 650), 
                        text_input="QUIT", font=get_font(20), base_color=WHITE, hovering_color=RED)

    while True:
        mouse = pygame.mouse.get_pos()
        for btn in [startbutton, quitbutton]:
            btn.changeColor(mouse)
            btn.update(windowSurface)

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

                #checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startbutton.checkForInput(mouse):
                    next()
                if quitbutton.checkForInput(mouse):
                    pygame.quit()
                    sys.exit()
        pygame.display.update() 

mainmenu()