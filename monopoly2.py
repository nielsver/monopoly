from ast import Constant, Or
from cgitb import grey
from email.mime import image
from glob import glob
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

from player import player

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

#init global variables
pot = 0
double = 0
i = 0 
z = 0
speler1positie = 0
speler2positie = 0
vakjes = [0] * 40
player1 = player("./monopoly-hat-01.jpg",(600,600),1500,0,"player1")
player2 = player("./dog.jpg",(600,600),1500,0,"player2")
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
def naardegevangenis(speler):
    #indegevangenis
    global speler1positie
    global speler2positie
    if(speler == 1):
        speler1positie = 10
    elif(speler == 2):
        speler2positie = 10
    print("in de gevangenis")
def algemeenfonds():
    #algemeenfonds
    print("algemeenfonds")
def kans():
    print("kans")
def vrijparkeren(player):
    global pot 
    global player1
    global player2
    if(player == 1):
        player1.money = player1.money() + pot
        pot = 0
    if(player == 2):
        player2.money = player2.money() + pot
    print("vrijparkeren")
def positie1(gedobbeltnummer):
    global i
    global speler1positie
    if(i == 0):
        speler1positie = gedobbeltnummer
        i = 1
    else:
        speler1positie = gedobbeltnummer + speler1positie
        if (speler1positie >= 40):
            speler1positie = speler1positie - 40
    return speler1positie
def positie2(gedobbeltnummer):
    global z
    global speler2positie
    if(z == 0):
        speler2positie = gedobbeltnummer
        z = 1
    else:
        speler2positie = gedobbeltnummer + speler2positie
        if (speler2positie >= 40):
            speler2positie = speler2positie - 40
    return speler2positie
def positiecheck(positie, type, worp):
    #type = 1 speler1
    #type = 2 speler2
    #type = 3 speler1 koopt
    #type = 4 speler2 koopt
    #vakjes = 0 van niemand
    #vakjes = 1 van speler 1
    #vakjes = 2 van speler 2
    #bij return 1 kan de speler kopen
    #bij return 2 kan de speler niet kopen
    global vakjes
    global player1
    global player2
    global pot
    if(type == 1 or type == 2):
        if positie == 0:
            #geld ontvangen 
            if(type == 1):
                player1.addmoney(200)
                #player1.addmoney(200)
            if(type == 2):
                player2.addmoney(200)
            return 2
        elif positie == 1:
            if(vakjes[1] == 0):
                return 1
            elif(vakjes[1] == 1):
                if(type == 2):
                    #betalen
                    player2.subtractmoney(10)
                    player1.addmoney(10)
                    return 2
            elif(vakjes[1] == 2):
                if(type == 1):
                    #betalen
                    player1.subtractmoney(10)
                    player2.addmoney(10)
                    return 2
        elif positie == 2:
            #algemeen fonds
            algemeenfonds()
            return 2
        elif positie == 3:
            if(vakjes[3] == 0):
                return 1
            elif(vakjes[3] == 1):
                if(type == 2):
                    #betalen
                    player2.addmoney(20)
                    player1.addmoney(20)
                    return 2
            elif(vakjes[3] == 2):
                if(type == 1):
                    #betalen
                    player1.subtractmoney(20)
                    player2.addmoney(20)
                    return 2
        elif positie == 4:
            #taxen betalen
            if(type == 1):
                player1.subtractmoney(200)
                pot = pot + 200
            if(type == 2):
                player2.subtractmoney(200)
                pot = pot + 200
            return 2
        elif positie == 5:
            # aantal vakjes bezit checken
            if(vakjes[5] == 0):
                return 1
            elif(vakjes[5] == 1):
                if(type == 2):
                    q = 0
                    #betalen
                    if(vakjes[15] == 1):
                        q = q + 1
                    if(vakjes[25] == 1):
                        q = q + 1
                    if(vakjes[35] == 1):
                        q = q + 1
                    if(q == 0):
                        player2.subtractmoney(25)
                        player1.addmoney(25)
                    if(q == 1):
                        player2.subtractmoney(50)
                        player1.addmoney(50)
                    if(q == 2):
                        player2.subtractmoney(50)
                        player1.addmoney(50)       
                    if(q == 3):
                        player2.subtractmoney(100)
                        player1.addmoney(100)
                    q = 0                                         
                    return 2
            elif(vakjes[5] == 2):
                if(type == 1):
                    #betalen
                    q = 0
                    #betalen
                    if(vakjes[15] == 2):
                        q = q + 1
                    if(vakjes[25] == 2):
                        q = q + 1
                    if(vakjes[35] == 2):
                        q = q + 1
                    if(q == 0):
                        player1.subtractmoney(25)
                        player2.addmoney(25)
                    if(q == 1):
                        player1.subtractmoney(50)
                        player2.addmoney(50)
                    if(q == 2):
                        player1.subtractmoney(50)
                        player2.addmoney(50)       
                    if(q == 3):
                        player1.subtractmoney(100)
                        player2.addmoney(100)
                    q = 0   
                    return 2
        elif positie == 6:
            if(vakjes[6] == 0):
                return 1
            elif(vakjes[6] == 1):
                if(type == 2):
                    #betalen
                    player2.subtractmoney(30)
                    player1.addmoney(30)
                    return 2
            elif(vakjes[6] == 2):
                if(type == 1):
                    #betalen
                    player1.subtractmoney(30)
                    player2.addmoney(30)
                    return 2
        elif positie == 7:
            #kans
            kans()
            return 2
        elif positie == 8:
            if(vakjes[8] == 0):
                return 1
            elif(vakjes[8] == 1):
                if(type == 2):
                    #betalen
                    player2.subtractmoney(30)
                    player1.addmoney(30)
                    return 2
            elif(vakjes[8] == 2):
                if(type == 1):
                    #betalen
                    player1.subtractmoney(30)
                    player2.addmoney(30)
                    return 2
        elif positie == 9:
            if(vakjes[9] == 0):
                return 1
            elif(vakjes[9] == 1):
                if(type == 2):
                    #betalen
                    player2.subtractmoney(40)
                    player1.addmoney(40)
                    return 2
            elif(vakjes[9] == 2):
                if(type == 1):
                    #betalen
                    player1.subtractmoney(40)
                    player2.addmoney(40)
                    return 2
        elif positie == 10:
            #op bezoek
            return 2
        elif positie == 11:
            if(vakjes[11] == 0):
                return 1
            elif(vakjes[11] == 1):
                if(type == 2):
                    #betalen
                    player2.money = player2.money() - 50
                    player1.money = player1.money() + 50
                    return 2
            elif(vakjes[11] == 2):
                if(type == 1):
                    #betalen
                    player1.money = player1.money() - 50
                    player2.money = player2.money() + 50
                    return 2
        elif positie == 12:
            #kijk hoeveel vakjes van dit die heeft anders * 10
            if(vakjes[12] == 0):
                return 1
            elif(vakjes[12] == 1):
                if(type == 2):
                    #betalen
                    if(vakjes[28] == 1):
                        player2.money = player2.money() - (worp * 10)
                        player1.money = player1.money() + (worp * 10)
                    else:
                        player2.money = player2.money() - (worp * 4)
                        player1.money = player1.money() + (worp * 4)
                    return 2
            elif(vakjes[12] == 2):
                if(type == 1):
                    #betalen
                    if(vakjes[28] == 2):
                        player1.money = player1.money() - (worp * 10)
                        player2.money = player2.money() + (worp * 10)
                    else:
                        player1.money = player1.money() - (worp * 4)
                        player2.money = player2.money() + (worp * 4)
                    return 2
        elif positie == 13:
            if(vakjes[13] == 0):
                return 1
            elif(vakjes[13] == 1):
                if(type == 2):
                    #betalen
                    player2.money = player2.money() - 50
                    player1.money = player1.money() + 50
                    return 2
            elif(vakjes[13] == 2):
                if(type == 1):
                    #betalen
                    player1.money = player1.money() - 50
                    player2.money = player2.money() + 50
                    return 2
        elif positie == 14:
            if(vakjes[14] == 0):
                return 1
            elif(vakjes[14] == 1):
                if(type == 2):
                    #betalen
                    player2.money = player2.money() - 60
                    player1.money = player1.money() + 60
                    return 2
            elif(vakjes[14] == 2):
                if(type == 1):
                    #betalen
                    player1.money = player1.money() - 60
                    player2.money = player2.money() + 60
                    return 2
        elif positie == 15:
            #kijken welke andere vakjes de speler nog heeft
            if(vakjes[15] == 0):
                return 1
            elif(vakjes[15] == 1):
                if(type == 2):
                    #betalen
                    q = 0
                    if(vakjes[5] == 1):
                        q = q + 1
                    if(vakjes[25] == 1):
                        q = q + 1
                    if(vakjes[35] == 1):
                        q = q + 1
                    if(q == 0):
                        player2.money = player2.money() - 25
                        player1.money = player1.money() + 25
                    if(q == 1):
                        player2.money = player2.money() - 50
                        player1.money = player1.money() + 50
                    if(q == 2):
                        player2.money = player2.money() - 100
                        player1.money = player1.money() + 100       
                    if(q == 3):
                        player2.money = player2.money() - 200
                        player1.money = player1.money() + 200
                    q = 0          
                    return 2
            elif(vakjes[15] == 2):
                if(type == 1):
                    #betalen
                    q = 0
                    if(vakjes[5] == 2):
                        q = q + 1
                    if(vakjes[25] == 2):
                        q = q + 1
                    if(vakjes[35] == 2):
                        q = q + 1
                    if(q == 0):
                        player1.money = player1.money() - 25
                        player2.money = player2.money() + 25
                    if(q == 1):
                        player1.money = player1.money() - 50
                        player2.money = player2.money() + 50
                    if(q == 2):
                        player1.money = player1.money() - 100
                        player2.money = player2.money() + 100       
                    if(q == 3):
                        player1.money = player1.money() - 200
                        player2.money = player2.money() + 200
                    q = 0   
                    return 2
        elif positie == 16:
            if(vakjes[16] == 0):
                return 1
            elif(vakjes[16] == 1):
                if(type == 2):
                    #betalen
                    player2.money = player2.money() - 70
                    player1.money = player1.money() + 70
                    return 2
            elif(vakjes[16] == 2):
                if(type == 1):
                    #betalen
                    player1.money = player1.money() - 70
                    player2.money = player2.money() + 70
                    return 2
        elif positie == 17:
            #algemeen fonds
            algemeenfonds()
            return 2
        elif positie == 18:
            if(vakjes[18] == 0):
                return 1
            elif(vakjes[18] == 1):
                if(type == 2):
                    #betalen
                    player2.money = player2.money() - 70
                    player1.money = player1.money() + 70
                    return 2
            elif(vakjes[18] == 2):
                if(type == 1):
                    #betalen
                    player1.money = player1.money() - 70
                    player2.money = player2.money() + 70
                    return 2
        elif positie == 19:
            if(vakjes[19] == 0):
                return 1
            elif(vakjes[19] == 1):
                if(type == 2):
                    #betalen
                    player2.money = player2.money() - 80
                    player1.money = player1.money() + 80
                    return 2
            elif(vakjes[19] == 2):
                if(type == 1):
                    #betalen
                    player1.money = player1.money() - 80
                    player2.money = player2.money() + 80
                    return 2
        elif positie == 20:
            #vrij parkeren
            if(type == 1):
                vrijparkeren(1)
            if(type == 2):
                vrijparkeren(2)
            return 2
        elif positie == 21:
            if(vakjes[21] == 0):
                return 1
            elif(vakjes[21] == 1):
                if(type == 2):
                    #betalen
                    player2.money = player2.money() - 90
                    player1.money = player1.money() + 90
                    return 2
            elif(vakjes[21] == 2):
                if(type == 1):
                    #betalen
                    player1.money = player1.money() - 90
                    player2.money = player2.money() + 90
                    return 2
        elif positie == 22:
            #kans
            kans()
            return 2
        elif positie == 23:
            if(vakjes[23] == 0):
                return 1
            elif(vakjes[23] == 1):
                if(type == 2):
                    #betalen
                    player2.money = player2.money() - 90
                    player1.money = player1.money() + 90
                    return 2
            elif(vakjes[23] == 2):
                if(type == 1):
                    #betalen
                    player1.money = player1.money() - 90
                    player2.money = player2.money() + 90
                    return 2
        elif positie == 24:
            if(vakjes[24] == 0):
                return 1
            elif(vakjes[24] == 1):
                if(type == 2):
                    #betalen
                    player2.money = player2.money() - 100
                    player1.money = player1.money() + 100
                    return 2
            elif(vakjes[24] == 2):
                if(type == 1):
                    #betalen
                    player1.money = player1.money() - 100
                    player2.money = player2.money() + 100
                    return 2
        elif positie == 25:
            #kijken welke andere vakjes in bezit van speler zijn
            if(vakjes[25] == 0):
                return 1
            elif(vakjes[25] == 1):
                if(type == 2):
                    #betalen
                    q = 0
                    if(vakjes[5] == 1):
                        q = q + 1
                    if(vakjes[15] == 1):
                        q = q + 1
                    if(vakjes[35] == 1):
                        q = q + 1
                    if(q == 0):
                        player2.money = player2.money() - 25
                        player1.money = player1.money() + 25
                    if(q == 1):
                        player2.money = player2.money() - 50
                        player1.money = player1.money() + 50
                    if(q == 2):
                        player2.money = player2.money() - 100
                        player1.money = player1.money() + 100       
                    if(q == 3):
                        player2.money = player2.money() - 200
                        player1.money = player1.money() + 200
                    q = 0    
                    return 2
            elif(vakjes[25] == 2):
                if(type == 1):
                    #betalen
                    q = 0
                    if(vakjes[5] == 2):
                        q = q + 1
                    if(vakjes[25] == 2):
                        q = q + 1
                    if(vakjes[35] == 2):
                        q = q + 1
                    if(q == 0):
                        player1.money = player1.money() - 25
                        player2.money = player2.money() + 25
                    if(q == 1):
                        player1.money = player1.money() - 50
                        player2.money = player2.money() + 50
                    if(q == 2):
                        player1.money = player1.money() - 100
                        player2.money = player2.money() + 100       
                    if(q == 3):
                        player1.money = player1.money() - 200
                        player2.money = player2.money() + 200
                    q = 0  
                    return 2
        elif positie == 26:
            if(vakjes[26] == 0):
                return 1
            elif(vakjes[26] == 1):
                if(type == 2):
                    #betalen
                    player2.money = player2.money() - 110
                    player1.money = player1.money() + 110
                    return 2
            elif(vakjes[26] == 2):
                if(type == 1):
                    #betalen
                    player1.money = player1.money() -110
                    player2.money = player2.money() + 110
                    return 2
        elif positie == 27:
            if(vakjes[27] == 0):
                return 1
            elif(vakjes[27] == 1):
                if(type == 2):
                    #betalen
                    player2.money = player2.money() - 110
                    player1.money = player1.money() + 110
                    return 2
            elif(vakjes[27] == 2):
                if(type == 1):
                    #betalen
                    player1.money = player1.money() - 110
                    player2.money = player2.money() + 110
                    return 2
        elif positie == 28:
            #kijken welke andere kaarten in bezit zijn speler
            if(vakjes[28] == 0):
                return 1
            elif(vakjes[28] == 1):
                if(type == 2):
                    #betalen
                    if(vakjes[12] == 1):
                        player2.money = player2.money() - (worp * 10)
                        player1.money = player1.money() + (worp * 10)
                    else:
                        player2.money = player2.money() - (worp * 4)
                        player1.money = player1.money() + (worp * 4)
                    return 2
            elif(vakjes[28] == 2):
                if(type == 1):
                    #betalen
                    if(vakjes[12] == 2):
                        player1.money = player1.money() - (worp * 10)
                        player2.money = player2.money() + (worp * 10)
                    else:
                        player1.money = player1.money() - (worp * 4)
                        player2.money = player2.money() + (worp * 4)
                    return 2
        elif positie == 29:
            if(vakjes[29] == 0):
                return 1
            elif(vakjes[29] == 1):
                if(type == 2):
                    #betalen
                    player2.money = player2.money() - 120
                    player1.money = player1.money() + 120
                    return 2
            elif(vakjes[29] == 2):
                if(type == 1):
                    #betalen
                    player1.money = player1.money() - 120
                    player2.money = player2.money() + 120
                    return 2
        elif positie == 30:
            #naar de gevangenis
            naardegevangenis(type)
            return 2
        elif positie == 31:
            if(vakjes[31] == 0):
                return 1
            elif(vakjes[31] == 1):
                if(type == 2):
                    #betalen
                    player2.money = player2.money() - 130
                    player1.money = player1.money() + 130
                    return 2
            elif(vakjes[31] == 2):
                if(type == 1):
                    #betalen
                    player1.money = player1.money() - 130
                    player2.money = player2.money() + 130
                    return 2
        elif positie == 32:
            if(vakjes[32] == 0):
                return 1
            elif(vakjes[32] == 1):
                if(type == 2):
                    #betalen
                    player2.money = player2.money() - 130
                    player1.money() + 130
                    return 2
            elif(vakjes[32] == 2):
                if(type == 1):
                    #betalen
                    player1.money = player1.money() - 130
                    player2.money = player2.money() + 130
                    return 2
        elif positie == 33:
            #algemeen fonds
            algemeenfonds()
            return 2
        elif positie == 34:
            if(vakjes[34] == 0):
                return 1
            elif(vakjes[34] == 1):
                if(type == 2):
                    #betalen
                    player2.money = player2.money() - 150
                    player1.money = player1.money() + 150
                    return 2
            elif(vakjes[34] == 2):
                if(type == 1):
                    #betalen
                    player1.money = player1.money() - 150
                    player2.money = player2.money() + 150
                    return 2
        elif positie == 35:
            #kijken hoeveel vakjes er van in bezit zijn
            if(vakjes[35] == 0):
                return 1
            elif(vakjes[35] == 1):
                if(type == 2):
                    #betalen
                    q = 0
                    if(vakjes[5] == 1):
                        q = q + 1
                    if(vakjes[15] == 1):
                        q = q + 1
                    if(vakjes[25] == 1):
                        q = q + 1
                    if(q == 0):
                        player2.money = player2.money() - 25
                        player1.money = player1.money() + 25
                    if(q == 1):
                        player2.money = player2.money() - 50
                        player1.money = player1.money() + 50
                    if(q == 2):
                        player2.money = player2.money() - 100
                        player1.money = player1.money() + 100       
                    if(q == 3):
                        player2.money = player2.money() - 200
                        player1.money = player1.money() + 200
                    q = 0   
                    return 2
            elif(vakjes[35] == 2):
                if(type == 1):
                    #betalen
                    q = 0
                    if(vakjes[5] == 2):
                        q = q + 1
                    if(vakjes[25] == 2):
                        q = q + 1
                    if(vakjes[25] == 2):
                        q = q + 1
                    if(q == 0):
                        player1.money = player1.money() - 25
                        player2.money = player2.money() + 25
                    if(q == 1):
                        player1.money = player1.money() - 50
                        player2.money = player2.money() + 50
                    if(q == 2):
                        player1.money = player1.money() - 100
                        player2.money = player2.money() + 100       
                    if(q == 3):
                        player1.money = player1.money() - 200
                        player2.money = player2.money() + 200
                    q = 0 
                    return 2
        elif positie == 36:
            #kans
            kans()
            return 2
        elif positie == 37:
            if(vakjes[37] == 0):
                return 1
            elif(vakjes[37] == 1):
                if(type == 2):
                    #betalen
                    player2.money = player2.money() - 175
                    player1.money = player1.money() + 175
                    return 2
            elif(vakjes[37] == 2):
                if(type == 1):
                    #betalen
                    player1.money = player1.money() - 175
                    player2.money = player2.money() + 175
                    return 2
        elif positie == 38:
            #supertax
            if(type == 2):
                player2.money = player2.money() - 100
                pot = pot + 100
            if(type == 3):
                player1.money = player1.money() - 100
                pot = pot + 100
            return 2
        elif positie == 39:
            if(vakjes[39] == 0):
                return 1
            elif(vakjes[39] == 1):
                if(type == 2):
                    #betalen
                    player2.money = player2.money() - 200
                    player1.money = player1.money() + 200
                    return 2
            elif(vakjes[39] == 2):
                if(type == 1):
                    #betalen
                    player1.money = player1.money() - 200
                    player2.money = player2.money() + 200
                    return 2
    elif(type == 3):
        vakjes[positie] = 1
        if(positie == 1):
            player1.money = player1.money() - 60
        elif(positie == 3):
            player1.money = player1.money() - 60
        elif(positie == 5):
            player1.money = player1.money() - 200
        elif(positie == 6):
            player1.money = player1.money() - 100
        elif(positie == 8):
            player1.money = player1.money() - 100
        elif(positie == 9):
            player1.money = player1.money() - 120
        elif(positie == 11):
            player1.money = player1.money() - 140
        elif(positie == 12):
            player1.money = player1.money() - 150
        elif(positie == 13):
            player1.money = player1.money() - 140
        elif(positie == 14):
            player1.money = player1.money() - 160
        elif(positie == 15):
            player1.money = player1.money() - 200
        elif(positie == 16):
            player1.money = player1.money() - 180
        elif(positie == 18):
            player1.money = player1.money() - 180
        elif(positie == 19):
            player1.money = player1.money() - 200
        elif(positie == 21):
            player1.money = player1.money() - 220
        elif(positie == 23):
            player1.money = player1.money() - 220
        elif(positie == 24):
            player1.money = player1.money() - 240
        elif(positie == 25):
            player1.money = player1.money() - 200
        elif(positie == 26):
            player1.money = player1.money() - 260
        elif(positie == 27):
            player1.money = player1.money() - 260
        elif(positie == 28):
            player1.money = player1.money() - 150
        elif(positie == 29):
            player1.money = player1.money() - 280
        elif(positie == 31):
            player1.money = player1.money() - 300
        elif(positie == 32):
            player1.money = player1.money() - 300
        elif(positie == 34):
            player1.money = player1.money() - 320
        elif(positie == 35):
            player1.money = player1.money() - 200
        elif(positie == 37):
            player1.money = player1.money() - 350
        elif(positie == 39):
            player1.money = player1.money() - 400
    elif(type == 4):
        vakjes[positie] = 2
        if(positie == 1):
            player2.money = player2.money() - 60
        elif(positie == 3):
            player2.money = player2.money() - 60
        elif(positie == 5):
            player2.money = player2.money() - 200
        elif(positie == 6):
            player2.money = player2.money() - 100
        elif(positie == 8):
            player2.money = player2.money() - 100
        elif(positie == 9):
            player2.money = player2.money() - 120
        elif(positie == 11):
            player2.money = player2.money() - 140
        elif(positie == 12):
            player2.money = player2.money() - 150
        elif(positie == 13):
            player2.money = player2.money() - 140
        elif(positie == 14):
            player2.money = player2.money() - 160
        elif(positie == 15):
            player2.money = player2.money() - 200
        elif(positie == 16):
            player2.money = player2.money() - 180
        elif(positie == 18):
            player2.money = player2.money() - 180
        elif(positie == 19):
            player2.money = player2.money() - 200
        elif(positie == 21):
            player2.money = player2.money() - 220
        elif(positie == 23):
            player2.money = player2.money() - 220
        elif(positie == 24):
            player2.money = player2.money() - 240
        elif(positie == 25):
            player2.money = player2.money() - 200
        elif(positie == 26):
            player2.money = player2.money() - 260
        elif(positie == 27):
            player2.money = player2.money() - 260
        elif(positie == 28):
            player2.money = player2.money() - 150
        elif(positie == 29):
            player2.money = player2.money() - 280
        elif(positie == 31):
            player2.money = player2.money() - 300
        elif(positie == 32):
            player2.money = player2.money() - 300
        elif(positie == 34):
            player2.money = player2.money() - 320
        elif(positie == 35):
            player2.money = player2.money() - 200
        elif(positie == 37):
            player2.money = player2.money() - 350
        elif(positie == 39):
            player2.money = player2.money() - 400
    
def dobbelen():
    int1 = random.randint(1,6)
    int2 = random.randint(1,6)
    global double 
    double = 0
    worp = int1 + int2
    if(int1 == int2):
        double = double + 1
    else:
        double = 0

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
    global player1 
    global player2
    global double
    geldplayer1 = smallfont.render("player 1: " + str(player1.money),True, RED)
    geldplayer2 = smallfont.render("player 2: " + str(player2.money),True, BLUE)
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
        windowSurface.blit(geldplayer1,(1150,40))
        pygame.draw.line(windowSurface, RED,(1150,60),(1350,60),1)
        windowSurface.blit(geldplayer2,(1150,80))
        pygame.draw.line(windowSurface, BLUE,(1150,100),(1350,100),1)
        pygame.display.update()
        if(player1.money >= 0): 
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
                                if(double == 3):
                                    naardegevangenis(1)
                                    algedobbelt = 1
                                    aandebeurt = 2
                                else:
                                    positiespeler1 = positie1(worp)
                                    #kankopen 1 kan het worden gekocht anders 2
                                    kankopen = positiecheck(positiespeler1,1,worp)
                                    algedobbelt = 1
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                if(aandebeurt == 1):
                    if(algedobbelt == 1):
                        if(kankopen == 1):
                            kopen = Button(button, pos=(width/2 + 400, 700), 
                                        text_input="kopen", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
                            volgende = Button(button, pos=(width/2 + 400, 600), 
                                        text_input="next", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
                            for btn in [volgende,kopen]:
                                btn.changeColor(mouse)
                                btn.update(windowSurface)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        if volgende.checkForInput(mouse):
                                            if(double == 1 or double == 2):
                                                aandebeurt = 1
                                                algedobbelt = 0
                                                kankopen = 0
                                            else:
                                                aandebeurt = 2
                                                algedobbelt = 0
                                                kankopen = 0
                                        if kopen.checkForInput(mouse):
                                            positiecheck(positiespeler1,3,0)
                                            kankopen = 2
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                        else:
                            volgende = Button(button, pos=(width/2 + 400, 600), 
                                        text_input="next", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
                            for btn in [volgende]:
                                btn.changeColor(mouse)
                                btn.update(windowSurface)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if volgende.checkForInput(mouse):
                                        if(double == 1 or double == 2):
                                            aandebeurt = 1
                                            algedobbelt = 0
                                        else:
                                            aandebeurt = 2
                                            algedobbelt = 0
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                pygame.display.update()
        else:
            print("player 2 wins")
            sys.exit()
        #player two
        #update Players money
        windowSurface.blit(geldplayer1,(1150,40))
        pygame.draw.line(windowSurface, RED,(1150,60),(1350,60),1)
        windowSurface.blit(geldplayer2,(1150,80))
        pygame.draw.line(windowSurface, BLUE,(1150,100),(1350,100),1)
        pygame.display.update()
        if(player2.money >= 0):
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
                                if(double == 3):
                                    naardegevangenis(2)
                                    algedobbelt = 1
                                    aandebeurt = 1
                                else:
                                    positiespeler2 = positie2(worp)
                                    #kankopen 1 kan worden gekocht anders 2
                                    kankopen = positiecheck(positiespeler2,1,worp)
                                    algedobbelt = 1
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                if(aandebeurt == 2):
                    if(algedobbelt == 1):
                        if(kankopen == 1):
                            kopen = Button(button, pos=(width/2 + 400, 700), 
                                        text_input="kopen", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
                            volgende = Button(button, pos=(width/2 + 400, 600), 
                                        text_input="next", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
                            for btn in [volgende,kopen]:
                                btn.changeColor(mouse)
                                btn.update(windowSurface)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        if volgende.checkForInput(mouse):
                                            if(double == 1 or double == 2):
                                                aandebeurt = 2
                                                algedobbelt = 0
                                                kankopen = 0
                                            else:
                                                algedobbelt = 0
                                                aandebeurt = 1
                                        if kopen.checkForInput(mouse):
                                            positiecheck(positiespeler2,4,0)
                                            kankopen = 2
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                        else:
                            volgende = Button(button, pos=(width/2 + 400, 600), 
                                        text_input="next", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
                            for btn in [volgende]:
                                btn.changeColor(mouse)
                                btn.update(windowSurface)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        if volgende.checkForInput(mouse):
                                            if(double == 1 or double == 2):
                                                aandebeurt = 2
                                                algedobbelt = 0
                                            else:
                                                algedobbelt = 0
                                                aandebeurt = 1
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                pygame.display.update()
            else:
                print("player 1 wint")
                sys.exit()
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
                    Player4()

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