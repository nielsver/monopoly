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
dubbel = 0
i = 0 
z = 0
int1 = 0
int2 = 0
speler1positie = 0
speler2positie = 0
indegevangenis1 = 0
indegevangenis2 = 0
tijdingevangenis = 0
vakjes = [0] * 40

#players
hat = pygame.image.load('./hoed.png').convert()
hat = pygame.transform.scale(hat,(25,25))
player1 = player(hat,750,750,1500,0,"player1")
dog = pygame.image.load('./dog.png').convert()
dog = pygame.transform.scale(dog,(25,25))
player2 = player(dog,750,750,1500,0,"player2")
#Set up fonts
basicFont = pygame.font.SysFont(None, 48)
Largefont = pygame.font.SysFont(None, 80)
smallfont = pygame.font.SysFont(None, 28)
#background pictures
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
construction = pygame.image.load('./UnderConstruct.jpg').convert()

#texten

text = basicFont.render('Play', True, RED)
plus25 = smallfont.render("Je wint met bingo: plus 25",True, BLACK)
plus50 = smallfont.render("Je vind een portefeuille: plus 50",TRUE, BLACK)
plus100 = smallfont.render("Je ontmoet Bill Gates: plus 100",TRUE,BLACK)
plus150 = smallfont.render("Je wint de lotto: plus 150",True,BLACK)
min25 = smallfont.render("Je verliest met poker: min 25",True, BLACK)
min50 = smallfont.render("Je verliest je portefeuille: min 50",TRUE, BLACK)
min100 = smallfont.render("Betrapt op geld witwassen boete: min 100",TRUE,BLACK)
min150 = smallfont.render("Je word overvallen: min 150",True,BLACK)
pos5 = smallfont.render("Je rijd electrisch: 5 plaatsen vooruit",True, BLACK)
pos10 = smallfont.render("Je krijgt een lift: 10 plaatsen vooruit",True, BLACK)
pos2 = smallfont.render("Je kan carpoolen: 2 plaatsen vooruit",True, BLACK)
pos12 = smallfont.render("Je vliegt privé: 12 plaatsen vooruit",True, BLACK)
posmin5 = smallfont.render("opslag benzine prijzen: 5 plaatsen terug",True, BLACK)
posmin10 = smallfont.render("vliegtuig problemen: 10 plaatsen terug",True, BLACK)
posmin2 = smallfont.render("lekke band: 2 plaatsen terug",True, BLACK)
posmin12 = smallfont.render("auto ongeluk: 12 plaatsen terug",True, BLACK)
gevangengen = smallfont.render("je zit in de gevangenis",True,BLACK)
naargevangen = smallfont.render("naar de gevangenis",True,BLACK)
opvrijparkeren = smallfont.render("Je krijgt de pot",True,BLACK)
Monopoly = Largefont.render('Monopoly',True, BLUE)
player1wint = Largefont.render('Player 1 wint', True, WHITE)
player2wint = Largefont.render('Player 2 wint', True, WHITE)
beurt1 = smallfont.render("speler 1 aan de beurt", True,WHITE)
beurt2 = smallfont.render("speler 2 is aan de beurt", True, WHITE)

tax = smallfont.render('Belastingaangift -200',TRUE,BLACK)
supertax = smallfont.render('bedrijfstaxen -100',TRUE,BLACK)
eigenaar = smallfont.render('Jij bent de eigenaar', TRUE,BLACK)
opbezoek = smallfont.render('Op bezoek',TRUE,BLACK)
opstart = smallfont.render('Start!',True,BLACK)
p1get10 = smallfont.render('player 1 kijgt 10 van player 2',TRUE,BLACK)
p1get20 = smallfont.render('player 1 kijgt 20 van player 2',TRUE,BLACK)
p1get30 = smallfont.render('player 1 kijgt 30 van player 2',TRUE,BLACK)
p1get40 = smallfont.render('player 1 kijgt 40 van player 2',TRUE,BLACK)
p1get50 = smallfont.render('player 1 kijgt 50 van player 2',TRUE,BLACK)
p1get60 = smallfont.render('player 1 kijgt 60 van player 2',TRUE,BLACK)
p1get70 = smallfont.render('player 1 kijgt 70 van player 2',TRUE,BLACK)
p1get80 = smallfont.render('player 1 kijgt 80 van player 2',TRUE,BLACK)
p1get90 = smallfont.render('player 1 kijgt 90 van player 2',TRUE,BLACK)
p1get100 = smallfont.render('player 1 kijgt 100 van player 2',TRUE,BLACK)
p1get110 = smallfont.render('player 1 kijgt 110 van player 2',TRUE,BLACK)
p1get120 = smallfont.render('player 1 kijgt 120 van player 2',TRUE,BLACK)
p1get130 = smallfont.render('player 1 kijgt 130 van player 2',TRUE,BLACK)
p1get150 = smallfont.render('player 1 kijgt 150 van player 2',TRUE,BLACK)
p1get175 = smallfont.render('player 1 kijgt 175 van player 2',TRUE,BLACK)
p1get200 = smallfont.render('player 1 kijgt 200 van player 2',TRUE,BLACK)

p2get10 = smallfont.render('player 2 kijgt 10 van player 1',TRUE,BLACK)
p2get20 = smallfont.render('player 2 kijgt 20 van player 1',TRUE,BLACK)
p2get30 = smallfont.render('player 2 kijgt 30 van player 1',TRUE,BLACK)
p2get40 = smallfont.render('player 2 kijgt 40 van player 1',TRUE,BLACK)
p2get50 = smallfont.render('player 2 kijgt 50 van player 1',TRUE,BLACK)
p2get60 = smallfont.render('player 2 kijgt 60 van player 1',TRUE,BLACK)
p2get70 = smallfont.render('player 2 kijgt 70 van player 1',TRUE,BLACK)
p2get80 = smallfont.render('player 2 kijgt 80 van player 1',TRUE,BLACK)
p2get90 = smallfont.render('player 2 kijgt 90 van player 1',TRUE,BLACK)
p2get100 = smallfont.render('player 2 kijgt 100 van player 1',TRUE,BLACK)
p2get110 = smallfont.render('player 2 kijgt 110 van player 1',TRUE,BLACK)
p2get120 = smallfont.render('player 2 kijgt 120 van player 1',TRUE,BLACK)
p2get130 = smallfont.render('player 2 kijgt 130 van player 1',TRUE,BLACK)
p2get150 = smallfont.render('player 2 kijgt 150 van player 1',TRUE,BLACK)
p2get175 = smallfont.render('player 2 kijgt 175 van player 1',TRUE,BLACK)
p2get200 = smallfont.render('player 2 kijgt 200 van player 1',TRUE,BLACK)

kost60 = smallfont.render('dit kan je kopen voor 60',TRUE,BLACK)
kost100 = smallfont.render('dit kan je kopen voor 100',TRUE,BLACK)
kost120 = smallfont.render('dit kan je kopen voor 120',TRUE,BLACK)
kost140 = smallfont.render('dit kan je kopen voor 140',TRUE,BLACK)
kost150 = smallfont.render('dit kan je kopen voor 150',TRUE,BLACK)
kost160 = smallfont.render('dit kan je kopen voor 160',TRUE,BLACK)
kost180 = smallfont.render('dit kan je kopen voor 180',TRUE,BLACK)
kost200 = smallfont.render('dit kan je kopen voor 200',TRUE,BLACK)
kost220 = smallfont.render('dit kan je kopen voor 220',TRUE,BLACK)
kost240 = smallfont.render('dit kan je kopen voor 240',TRUE,BLACK)
kost260 = smallfont.render('dit kan je kopen voor 260',TRUE,BLACK)
kost280 = smallfont.render('dit kan je kopen voor 280',TRUE,BLACK)
kost300 = smallfont.render('dit kan je kopen voor 300',TRUE,BLACK)
kost320 = smallfont.render('dit kan je kopen voor 320',TRUE,BLACK)
kost350 = smallfont.render('dit kan je kopen voor 350',TRUE,BLACK)
kost400 = smallfont.render('dit kan je kopen voor 400',TRUE,BLACK)






#dobbelstenen

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
def indegevangenis(speler):
    global tijdingevangenis
    global player1
    global player2
    global indegevangenis1
    global indegevangenis2
    global dubbel
    if speler == 1:
        if tijdingevangenis < 3:
            if dubbel == 1:
                indegevangenis1 = 0
            else:
                tijdingevangenis += 1
        else:
            player1.money -= 200
            indegevangenis1 = 0
    else:
        if tijdingevangenis < 3:
            if dubbel == 1:
                indegevangenis2 = 0
            else:
                tijdingevangenis += 1
        else:
            player2.money -= 200
            indegevangenis2 = 0
    windowSurface.blit(gevangengen,(width/2+250,320))
    pygame.display.update()
       
def naardegevangenis(speler): #je print naardegevangeis af op width/2+250, 320
    #indegevangenis
    global speler1positie
    global speler2positie
    global player1, player2
    global indegevangenis1
    global indegevangenis2
    if speler == 1:
        speler1positie = 10
        player1.x_pos = 50
        player1.y_pos = 750
        indegevangenis1 = 1
    elif speler == 2:
        speler2positie = 10
        player2.x_pos = 50
        player2.y_pos = 750
        indegevangenis2 = 1
    windowSurface.fill(WHITE)
    pygame.display.update()
    windowSurface.blit(bord,(0,0))    
    player1.update(windowSurface)
    player2.update(windowSurface)
    windowSurface.blit(naargevangen,(width/2+250,320))
    
    pygame.display.update()
    pygame.display.flip()
    print("in de gevangenis")
def algemeenfonds(type): #wordt afgepritn op width/2+250, 300
    global speler1positie
    global speler2positie
    #algemeenfonds
     # we zouden nog een text moeten tonen van bv. speler 1 is zoveel posities opgeschoven
    
    list1 = [0,1,2,3,4]
    list2 = [5,6,7,8,9]
    list3 = [10,11,12,13,14]
    list4 = [15,16,17,18,19]
    list5 = [20,21,22,23,24]
    list6 = [25,26,27,28,29]
    list7 = [30,31,32,33,34]
    list8 = [35,36,37,38,39]
    kansint = random.randint(0,39)
    for x in list1:
        if kansint == x:
            if type == 1:
                speler1positie += 5
            if type == 2:
                speler2positie += 5
    for x in list2:
        if kansint == x:
            if type == 1:
                speler1positie += 10
            if type == 2:
                speler2positie += 10
    for x in list3:
        if kansint == x:
            if type == 1:
                speler1positie += 2
            if type == 2:
                speler2positie += 2

    for x in list4:
        if kansint == x:
            if type == 1:
                speler1positie +=12
            if type == 2:
                speler2positie += 12
    for x in list5:
        if kansint == x:
            if type == 1:               
                speler1positie -= 5
            if type == 2:
                speler2positie -= 5
    for x in list6:
        if kansint == x:
            if type == 1:
                speler1positie -= 10               
            if type == 2:
                speler2positie -= 10
    for x in list7:
        if kansint == x:
            if type == 1:
                speler1positie -= 2 
            if type == 2:
                speler2positie -= 2
    for x in list8:
        if kansint == x:
            if type == 1:
                speler1positie -= 12
            if type == 2:
                speler2positie -= 12

    if type == 1:
        speler1positie = positie1(0)
    else:
        speler2positie = positie2(0)

    for x in list1:
        if kansint == x:
            if type == 1:
                windowSurface.blit(pos5,(width/2+250, 280))
                pygame.display.update()
            if type == 2:
                windowSurface.blit(pos5,(width/2+250, 280))
                pygame.display.update()
    for x in list2:
        if kansint == x:
            if type == 1:                
                windowSurface.blit(pos10,(width/2+250, 280))
                pygame.display.update()
            if type == 2:               
                windowSurface.blit(pos10,(width/2+250, 280))
                pygame.display.update()
    for x in list3:
        if kansint == x:
            if type == 1:
                windowSurface.blit(pos2,(width/2+250, 280))
                pygame.display.update()
            if type == 2:
                windowSurface.blit(pos2,(width/2+250, 280))
                pygame.display.update()

    for x in list4:
        if kansint == x:
            if type == 1:
                windowSurface.blit(pos12,(width/2+250, 280))
                pygame.display.update()
            if type == 2:
                windowSurface.blit(pos12,(width/2+250, 280))
                pygame.display.update()
    for x in list5:
        if kansint == x:
            if type == 1:               
                windowSurface.blit(posmin5,(width/2+250, 280))
                pygame.display.update()
            if type == 2:
                windowSurface.blit(posmin5,(width/2+250, 280))
                pygame.display.update()
    for x in list6:
        if kansint == x:
            if type == 1:          
                windowSurface.blit(posmin10,(width/2+250, 280))
                pygame.display.update()
            if type == 2:
                windowSurface.blit(posmin10,(width/2+250, 280))
                pygame.display.update()
    for x in list7:
        if kansint == x:
            if type == 1:
                windowSurface.blit(posmin2,(width/2+250, 280))
                pygame.display.update()
            if type == 2:
                windowSurface.blit(posmin2,(width/2+250, 280))
                pygame.display.update()
    for x in list8:
        if kansint == x:
            if type == 1:
                windowSurface.blit(posmin12,(width/2+250, 280))
                pygame.display.update()
            if type == 2:
                windowSurface.blit(posmin12,(width/2+250, 280))
                pygame.display.update()

    if speler1positie >= 40:
        speler1positie = speler1positie - 40
    if speler1positie < 0:
        speler1positie = speler1positie + 40
    if speler2positie >= 40:
        speler2positie = speler2positie - 40
    if speler2positie < 0:
        speler2positie = speler2positie + 40
    if type == 1:
        kankopen = positiecheck(speler1positie,1,8)
        return kankopen
    else:
        kankopen = positiecheck(speler2positie,2,8)
        return kankopen
      
def kans(type):
    
    list1 = [0,1,2,3,4]
    list2 = [5,6,7,8,9]
    list3 = [10,11,12,13,14]
    list4 = [15,16,17,18,19]
    list5 = [20,21,22,23,24]
    list6 = [25,26,27,28,29]
    list7 = [30,31,32,33,34]
    list8 = [35,36,37,38,39]
    kansint = random.randint(0,39)
    for x in list1:
        if kansint == x:
            if type == 1:
                player1.money += 50
                windowSurface.blit(plus50,(width/2+250, 300))
            if type == 2:
                player2.money += 50
                windowSurface.blit(plus50,(width/2+250, 300))
    for x in list2:
        if kansint == x:
            if type == 1:
                player1.money += 25
                windowSurface.blit(plus25,(width/2+250, 300))
            if type == 2:
                
                player2.money += 25
                windowSurface.blit(plus25,(width/2+250, 300))
    for x in list3:
        if kansint == x:
            if type == 1:
                player1.money += 100
                windowSurface.blit(plus100,(width/2+250, 300))
            if type == 2:
                player2.money += 100
                windowSurface.blit(plus100,(width/2+250, 300))
    for x in list4:
        if kansint == x:
            if type == 1:
                player1.money += 150
                windowSurface.blit(plus150,(width/2+250, 300))
            if type == 2:
                player2.money += 150
                windowSurface.blit(plus150,(width/2+250, 300))
    for x in list5:
        if kansint == x:
            if type == 1:
                player1.money -= 50
                windowSurface.blit(min50,(width/2+250, 300))
            if type == 2:
                player2.money -= 50
                windowSurface.blit(min50,(width/2+250, 300))
    for x in list6:
        if kansint == x:
            if type == 1:
                player1.money -= 25
                windowSurface.blit(min25,(width/2+250, 300))
            if type == 2:
                player2.money -= 25
                windowSurface.blit(min25,(width/2+250, 300))
    for x in list7:
        if kansint == x:
            if type == 1:
                player1.money -= 100
                windowSurface.blit(min100,(width/2+250, 300))
            if type == 2:
                player2.money -= 100
                windowSurface.blit(min100,(width/2+250, 300))
    for x in list8:
        if kansint == x:
            if type == 1:
                player1.money -= 150
                windowSurface.blit(min150,(width/2+250, 300))
            if type == 2:
                player2.money -= 150
                windowSurface.blit(min150,(width/2+250, 300))
    pygame.display.update()
def vrijparkeren(player): #je print de pot af op width/2+250, 320    global pot 
    global player1
    global player2
    global pot
    wintpot = smallfont.render("Je wint de pot: +" + str(pot),True,BLACK)
    if player == 1:
        player1.money = player1.money + pot
        pot = 0
    if player == 2:
        player2.money = player2.money + pot
    windowSurface.blit(wintpot,(width/2+250, 320))
    pygame.display.update()
    print("vrijparkeren")
def positie1(gedobbeltnummer): #wordt afgeprint op width/2+200,340
    global i
    global speler1positie
    global player1
    if i == 0:
        speler1positie = gedobbeltnummer
        i = 1
    else:
        speler1positie = gedobbeltnummer + speler1positie
        if (speler1positie >= 40):
            player1.money += 200
            speler1positie = speler1positie - 40
    if speler1positie <= 10:
        player1.y_pos = 750
        if speler1positie == 0:
            player1.x_pos = 750
        elif speler1positie == 1:
            player1.x_pos = 647
        elif speler1positie == 2:
             player1.x_pos = 581
        elif speler1positie == 3:
             player1.x_pos = 514
        elif speler2positie == 4:
             player1.x_pos = 442
        elif speler1positie == 5:
             player1.x_pos = 379
        elif speler1positie == 6:
             player1.x_pos = 314
        elif speler1positie == 7:
            player1.x_pos = 247
        elif speler1positie == 8:
             player1.x_pos = 187
        elif speler1positie == 9:
             player1.x_pos = 130 #changed
        elif speler1positie == 10:
            player1.x_pos = 50
    elif 10 < speler1positie <= 20:
        player1.x_pos = 50
        if speler1positie == 10:
                player1.y_pos = 750
        elif speler1positie == 11:
                player1.y_pos = 650 #changed
        elif speler1positie ==12:
                player1.y_pos = 610
        elif speler1positie == 13:
                player1.y_pos = 520
        elif speler1positie == 14:
                player1.y_pos = 470
        elif speler1positie == 15:
                player1.y_pos = 400
        elif speler1positie == 16:
                player1.y_pos = 330
        elif speler1positie == 17:
                player1.y_pos = 260
        elif speler1positie == 18:
                player1.y_pos = 190 
        elif speler1positie == 19:
                player1.y_pos = 130 #changed 
        elif speler1positie == 20:
                player1.y_pos = 50
    elif 20 < speler1positie <= 30:
        player1.y_pos = 50
        if speler1positie == 20:
            player1.x_pos = 50
        elif speler1positie == 21:
                player1.x_pos = 120
        elif speler1positie == 22:
                player1.x_pos = 187
        elif speler1positie == 23:
                player1.x_pos = 247
        elif speler1positie == 24:
                player1.x_pos = 314  
        elif speler1positie == 25:
                player1.x_pos = 379
        elif speler1positie == 26:
                player1.x_pos = 442
        elif speler1positie == 27:
                player1.x_pos = 514
        elif speler1positie == 28:
                player1.x_pos = 581
        elif speler1positie == 29:
                player1.x_pos = 647
        elif speler1positie == 30:
                player1.x_pos = 750
    else:
        player1.x_pos = 750
        if speler1positie == 30:
               player1.y_pos = 50
        elif speler1positie == 31:
            player1.y_pos = 120
        elif speler1positie ==32:
             player1.y_pos = 190
        elif speler1positie == 33:
            player1.y_pos = 260
        elif speler1positie == 34:
             player1.y_pos = 330  
        elif speler1positie == 35:
             player1.y_pos = 400
        elif speler1positie == 36:
            player1.y_pos = 470
        elif speler1positie == 37:
             player1.y_pos = 520 #changed
        elif speler1positie == 38:
            player1.y_pos = 570
        elif speler1positie == 39:
             player1.y_pos = 640
        elif speler1positie == 40:
                player1.y_pos = 750
    windowSurface.fill(WHITE)
    pygame.display.update()
    windowSurface.blit(bord,(0,0))
    player1.update(windowSurface)
    player2.update(windowSurface)
    pygame.display.update()
    pygame.display.flip()
    return speler1positie
def positie2(gedobbeltnummer):
    global z
    global speler2positie
    global player2
    if z == 0:
        speler2positie = gedobbeltnummer
        z = 1
    else:
        speler2positie = gedobbeltnummer + speler2positie
        if (speler2positie >= 40):
            speler2positie = speler2positie - 40
            player2.money += 200
    if speler2positie <= 10:
        player2.y_pos = 750
        if speler2positie == 0:
            player2.x_pos = 750
        elif speler2positie == 1:
            player2.x_pos = 647
        elif speler2positie == 2:
             player2.x_pos = 581
        elif speler2positie == 3:
             player2.x_pos = 514
        elif speler2positie == 4:
             player2.x_pos = 442
        elif speler2positie == 5:
             player2.x_pos = 379
        elif speler2positie == 6:
             player2.x_pos = 314
        elif speler2positie == 7:
            player2.x_pos = 247
        elif speler2positie == 8:
             player2.x_pos = 187
        elif speler2positie == 9:
             player2.x_pos = 130
        elif speler2positie == 10:
            player2.x_pos = 50
    elif 10 < speler2positie <= 20 :
        player2.x_pos = 50
        if speler2positie == 10:
                player2.y_pos = 750
        elif speler2positie == 11:
                player2.y_pos = 650 #changed
        elif speler2positie ==12:
                player2.y_pos = 610
        elif speler2positie == 13:
                player2.y_pos = 540
        elif speler2positie == 14:
                player2.y_pos = 470  
        elif speler2positie == 15:
                player2.y_pos = 400
        elif speler2positie == 16:
                player2.y_pos = 330
        elif speler2positie == 17:
                player2.y_pos = 260
        elif speler2positie == 18:
                player2.y_pos = 190
        elif speler2positie == 19:
                player2.y_pos = 130 
        elif speler2positie == 20:
                player2.y_pos = 50
    elif 20 < speler2positie <= 30:
        player2.y_pos = 50
        if speler2positie == 20:
            player2.x_pos = 50
        elif speler2positie == 21:
                player2.x_pos = 120
        elif speler2positie == 22:
                player2.x_pos = 187
        elif speler2positie == 23:
                player2.x_pos = 247
        elif speler2positie == 24:
                player2.x_pos = 314 
        elif speler2positie == 25:
                player2.x_pos = 379
        elif speler2positie == 26:
                player2.x_pos = 442
        elif speler2positie == 27:
                player2.x_pos = 514
        elif speler2positie == 28:
                player2.x_pos = 581
        elif speler2positie == 29:
                player2.x_pos = 647
        elif speler2positie == 30:
                player2.x_pos = 750
    else:
        player2.x_pos = 750
        if speler2positie == 30:
               player2.y_pos = 50
        elif speler2positie == 31:
            player2.y_pos = 120
        elif speler2positie ==32:
             player2.y_pos = 190
        elif speler2positie == 33:
            player2.y_pos = 260
        elif speler2positie == 34:
             player2.y_pos = 330 
        elif speler2positie == 35:
             player2.y_pos = 400
        elif speler2positie == 36:
            player2.y_pos = 470
        elif speler2positie == 37:
             player2.y_pos = 520
        elif speler2positie == 38:
            player2.y_pos = 570
        elif speler2positie == 39:
             player2.y_pos = 640
        elif speler2positie == 40:
                player2.y_pos = 750

    windowSurface.fill(WHITE)
    pygame.display.update()
    windowSurface.blit(bord,(0,0))
    player2.update(windowSurface)
    player1.update(windowSurface)
    pygame.display.update()
    pygame.display.flip()
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
    if type == 1 or type == 2:
        if positie == 0:
            windowSurface.blit(opstart,(width/2+250,300))
            return 2
        elif positie == 1:
            if vakjes[1] == 0:
                windowSurface.blit(kost60,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[1] == 1:
                if type == 2:
                    #betalen
                    player2.money -= 10
                    player1.money += 10
                    windowSurface.blit(p1get10,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2
            elif vakjes[1] == 2:
                if type == 1:
                    #betalen
                    player1.money -= 10
                    player2.money += 10
                    windowSurface.blit(p2get10,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2
        elif positie == 2:
            #algemeen fonds
            if type == 1:
                kankopen = algemeenfonds(1)
            else:
                kankopen = algemeenfonds(2)
            return kankopen
        elif positie == 3:
            if vakjes[3] == 0:
                windowSurface.blit(kost60,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[3] == 1:
                if type == 2:
                    #betalen
                    player2.money += 20
                    player1.money += 20
                    windowSurface.blit(p1get20,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[3] == 2:
                if type == 1:
                    #betalen
                    player1.money -= 20
                    player2.money += 20
                    windowSurface.blit(p2get20,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 4:
            #taxen betalen
            if type == 1:
                windowSurface.blit(tax,(width/2+250,300))
                pygame.display.update()
                player1.money -= 200
                pot = pot + 200
            if type == 2:
                windowSurface.blit(tax,(width/2+250,300))
                pygame.display.update()
                player2.money -= 200
                pot = pot + 200
            return 2
        elif positie == 5:
            # aantal vakjes bezit checken
            if vakjes[5] == 0:
                windowSurface.blit(kost200,(width/2+250,300))
                pygame.display.update()                
                return 1
            elif vakjes[5] == 1:
                if type == 2:
                    q = 0
                    #betalen
                    if vakjes[15] == 1:
                        q = q + 1
                    if vakjes[25] == 1:
                        q = q + 1
                    if vakjes[35] == 1:
                        q = q + 1
                    if q == 0:
                        player2.money -= 25
                        player1.money += 25
                    if q == 1:
                        player2.money -= 50
                        player1.money += 50
                    if q == 2:
                        player2.money -= 100 
                        player1.money += 100       
                    if q == 3:
                        player2.money -= 200
                        player1.money += 200
                    q = 0                                         
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[5] == 2:
                if type == 1:
                    #betalen
                    q = 0
                    #betalen
                    if vakjes[15] == 2:
                        q = q + 1
                    if vakjes[25] == 2:
                        q = q + 1
                    if vakjes[35] == 2:
                        q = q + 1
                    if q == 0:
                        player1.money -= 25
                        player2.money += 25
                    if q == 1:
                        player1.money -= 50
                        player2.money += 50
                    if q == 2:
                        player1.money -= 100
                        player2.money += 100      
                    if q == 3:
                        player1.money -= 200
                        player2.money += 200
                    q = 0   
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 6:
            if vakjes[6] == 0:
                windowSurface.blit(kost100,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[6] == 1:
                if type == 2:
                    #betalen
                    player2.money -= 30
                    player1.money += 30
                    windowSurface.blit(p1get30,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[6] == 2:
                if type == 1:
                    #betalen
                    player1.money -= 30
                    player2.money += 30
                    windowSurface.blit(p2get30,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 7:
            #kans
            if type == 1:
                kans(1)
            else:
                kans(2)
            return 2
        elif positie == 8:
            if vakjes[8] == 0:
                windowSurface.blit(kost100,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[8] == 1:
                if type == 2:
                    #betalen
                    player2.money -= 30
                    player1.money += 30
                    windowSurface.blit(p1get30,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[8] == 2:
                if type == 1:
                    #betalen
                    player1.money -= 30
                    player2.money += 30
                    windowSurface.blit(p2get30,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 9:
            if vakjes[9] == 0:
                windowSurface.blit(kost120,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[9] == 1:
                if type == 2:
                    #betalen
                    player2.money -= 40
                    player1.money += 40
                    windowSurface.blit(p1get40,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[9] == 2:
                if type == 1:
                    #betalen
                    player1.money -= 40
                    player2.money += 40
                    windowSurface.blit(p2get40,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 10:
            #op bezoek
            windowSurface.blit(opbezoek,(width/2+250,300))
            return 2
        elif positie == 11:
            if vakjes[11] == 0:
                windowSurface.blit(kost140,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[11] == 1:
                if type == 2:
                    #betalen
                    player2.money = player2.money - 50
                    player1.money = player1.money + 50
                    windowSurface.blit(p1get50,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[11] == 2:
                if type == 1:
                    #betalen
                    player1.money = player1.money - 50
                    player2.money = player2.money + 50
                    windowSurface.blit(p2get50,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2
        elif positie == 12:
            #kijk hoeveel vakjes van dit die heeft anders * 10
            if vakjes[12] == 0:
                windowSurface.blit(kost150,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[12] == 1:
                if type == 2:
                    #betalen
                    if vakjes[28] == 1:
                        player2.money = player2.money - (worp * 10)
                        player1.money = player1.money + (worp * 10)
                    else:
                        player2.money = player2.money - (worp * 4)
                        player1.money = player1.money + (worp * 4)
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[12] == 2:
                if type == 1:
                    #betalen
                    if vakjes[28] == 2:
                        player1.money = player1.money - (worp * 10)
                        player2.money = player2.money + (worp * 10)
                    else:
                        player1.money = player1.money - (worp * 4)
                        player2.money = player2.money + (worp * 4)
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 13:
            if vakjes[13] == 0:
                windowSurface.blit(kost140,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[13] == 1:
                if type == 2:
                    #betalen
                    player2.money = player2.money - 50
                    player1.money = player1.money + 50
                    windowSurface.blit(p1get50,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[13] == 2:
                if type == 1:
                    #betalen
                    player1.money = player1.money - 50
                    player2.money = player2.money + 50
                    windowSurface.blit(p2get50,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 14:
            if vakjes[14] == 0:
                windowSurface.blit(kost160,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[14] == 1:
                if type == 2:
                    #betalen
                    player2.money = player2.money - 60
                    player1.money = player1.money + 60
                    windowSurface.blit(p1get60,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[14] == 2:
                if type == 1:
                    #betalen
                    player1.money = player1.money - 60
                    player2.money = player2.money + 60
                    windowSurface.blit(p2get60,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 15:
            #kijken welke andere vakjes de speler nog heeft
            if vakjes[15] == 0:
                windowSurface.blit(kost200,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[15] == 1:
                if type == 2:
                    #betalen
                    q = 0
                    if vakjes[5] == 1:
                        q = q + 1
                    if vakjes[25] == 1:
                        q = q + 1
                    if vakjes[35] == 1:
                        q = q + 1
                    if q == 0:
                        player2.money = player2.money - 25
                        player1.money = player1.money + 25
                    if q == 1:
                        player2.money = player2.money - 50
                        player1.money = player1.money + 50
                    if q == 2:
                        player2.money = player2.money - 100
                        player1.money = player1.money + 100       
                    if q == 3:
                        player2.money = player2.money - 200
                        player1.money = player1.money + 200
                    q = 0          
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[15] == 2:
                if type == 1:
                    #betalen
                    q = 0
                    if vakjes[5] == 2:
                        q = q + 1
                    if vakjes[25] == 2:
                        q = q + 1
                    if vakjes[35] == 2:
                        q = q + 1
                    if q == 0:
                        player1.money = player1.money - 25
                        player2.money = player2.money + 25
                    if q == 1:
                        player1.money = player1.money - 50
                        player2.money = player2.money + 50
                    if q == 2:
                        player1.money = player1.money - 100
                        player2.money = player2.money + 100       
                    if q == 3:
                        player1.money = player1.money - 200
                        player2.money = player2.money + 200
                    q = 0   
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 16:
            if vakjes[16] == 0:
                windowSurface.blit(kost180,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[16] == 1:
                if type == 2:
                    #betalen
                    player2.money = player2.money - 70
                    player1.money = player1.money + 70
                    windowSurface.blit(p1get70,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[16] == 2:
                if type == 1:
                    #betalen
                    player1.money = player1.money - 70
                    player2.money = player2.money + 70
                    windowSurface.blit(p2get70,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 17:
            #algemeen fonds
            if type == 1:
                kankopen = algemeenfonds(1)
            else:
                kankopen = algemeenfonds(2)
            return kankopen
        elif positie == 18:
            if vakjes[18] == 0:
                windowSurface.blit(kost180,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[18] == 1:
                if type == 2:
                    #betalen
                    player2.money = player2.money - 70
                    player1.money = player1.money + 70
                    windowSurface.blit(p1get70,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[18] == 2:
                if type == 1:
                    #betalen
                    player1.money = player1.money - 70
                    player2.money = player2.money + 70
                    windowSurface.blit(p2get70,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 19:
            if vakjes[19] == 0:
                windowSurface.blit(kost200,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[19] == 1:
                if type == 2:
                    #betalen
                    player2.money = player2.money - 80
                    player1.money = player1.money + 80
                    windowSurface.blit(p1get80,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[19] == 2:
                if type == 1:
                    #betalen
                    player1.money = player1.money - 80
                    player2.money = player2.money + 80
                    windowSurface.blit(p2get80,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 20:
            #vrij parkeren
            if type == 1:
                vrijparkeren(1)
            if type == 2:
                vrijparkeren(2)
            return 2
        elif positie == 21:
            if vakjes[21] == 0:
                windowSurface.blit(kost220,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[21] == 1:
                if type == 2:
                    #betalen
                    player2.money = player2.money - 90
                    player1.money = player1.money + 90
                    windowSurface.blit(p1get90,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[21] == 2:
                if type == 1:
                    #betalen
                    player1.money = player1.money - 90
                    player2.money = player2.money + 90
                    windowSurface.blit(p2get90,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 22:
            #kans
            if type == 1:
                kans(1)
            else:
                kans(2)
            return 2
        elif positie == 23:
            if vakjes[23] == 0:
                windowSurface.blit(kost220,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[23] == 1:
                if type == 2:
                    #betalen
                    player2.money = player2.money - 90
                    player1.money = player1.money + 90
                    windowSurface.blit(p1get90,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[23] == 2:
                if type == 1:
                    #betalen
                    player1.money = player1.money - 90
                    player2.money = player2.money + 90
                    windowSurface.blit(p2get90,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 24:
            if vakjes[24] == 0:
                windowSurface.blit(kost240,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[24] == 1:
                if type == 2:
                    #betalen
                    player2.money = player2.money - 100
                    player1.money = player1.money + 100
                    windowSurface.blit(p1get100,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[24] == 2:
                if type == 1:
                    #betalen
                    player1.money = player1.money - 100
                    player2.money = player2.money + 100
                    windowSurface.blit(p2get100,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 25:
            #kijken welke andere vakjes in bezit van speler zijn
            if vakjes[25] == 0:
                windowSurface.blit(kost200,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[25] == 1:
                if type == 2:
                    #betalen
                    q = 0
                    if vakjes[5] == 1:
                        q = q + 1
                    if vakjes[15] == 1:
                        q = q + 1
                    if vakjes[35] == 1:
                        q = q + 1
                    if q == 0:
                        player2.money = player2.money - 25
                        player1.money = player1.money + 25
                    if q == 1:
                        player2.money = player2.money - 50
                        player1.money = player1.money + 50
                    if q == 2:
                        player2.money = player2.money - 100
                        player1.money = player1.money + 100       
                    if q == 3:
                        player2.money = player2.money - 200
                        player1.money = player1.money + 200
                    q = 0    
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[25] == 2:
                if type == 1:
                    #betalen
                    q = 0
                    if vakjes[5] == 2:
                        q = q + 1
                    if vakjes[25] == 2:
                        q = q + 1
                    if vakjes[35] == 2:
                        q = q + 1
                    if q == 0:
                        player1.money = player1.money - 25
                        player2.money = player2.money + 25
                    if q == 1:
                        player1.money = player1.money - 50
                        player2.money = player2.money + 50
                    if q == 2:
                        player1.money = player1.money - 100
                        player2.money = player2.money + 100       
                    if q == 3:
                        player1.money = player1.money - 200
                        player2.money = player2.money + 200
                    q = 0  
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 26:
            if vakjes[26] == 0:
                windowSurface.blit(kost260,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[26] == 1:
                if type == 2:
                    #betalen
                    player2.money = player2.money - 110
                    player1.money = player1.money + 110
                    windowSurface.blit(p1get110,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[26] == 2:
                if type == 1:
                    #betalen
                    player1.money = player1.money -110
                    player2.money = player2.money + 110
                    windowSurface.blit(p2get110,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 27:
            if vakjes[27] == 0:
                windowSurface.blit(kost260,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[27] == 1:
                if type == 2:
                    #betalen
                    player2.money = player2.money - 110
                    player1.money = player1.money + 110
                    windowSurface.blit(p1get110,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[27] == 2:
                if type == 1:
                    #betalen
                    player1.money = player1.money - 110
                    player2.money = player2.money + 110
                    windowSurface.blit(p2get110,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 28:
            #kijken welke andere kaarten in bezit zijn speler
            if vakjes[28] == 0:
                windowSurface.blit(kost150,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[28] == 1:
                if type == 2:
                    #betalen
                    if vakjes[12] == 1:
                        player2.money = player2.money - (worp * 10)
                        player1.money = player1.money + (worp * 10)
                    else:
                        player2.money = player2.money - (worp * 4)
                        player1.money = player1.money + (worp * 4)
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[28] == 2:
                if type == 1:
                    #betalen
                    if vakjes[12] == 2:
                        player1.money = player1.money - (worp * 10)
                        player2.money = player2.money + (worp * 10)
                    else:
                        player1.money = player1.money - (worp * 4)
                        player2.money = player2.money + (worp * 4)
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 29:
            if vakjes[29] == 0:
                windowSurface.blit(kost280,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[29] == 1:
                if type == 2:
                    #betalen
                    player2.money = player2.money - 120
                    player1.money = player1.money + 120
                    windowSurface.blit(p1get120,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[29] == 2:
                if type == 1:
                    #betalen
                    player1.money = player1.money - 120
                    player2.money = player2.money + 120
                    windowSurface.blit(p2get120,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 30:
            #naar de gevangenis
            naardegevangenis(type)
            return 2
        elif positie == 31:
            if vakjes[31] == 0:
                windowSurface.blit(kost300,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[31] == 1:
                if type == 2:
                    #betalen
                    player2.money = player2.money - 130
                    player1.money = player1.money + 130
                    windowSurface.blit(p1get130,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[31] == 2:
                if type == 1:
                    #betalen
                    player1.money = player1.money - 130
                    player2.money = player2.money + 130
                    windowSurface.blit(p2get130,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 32:
            if vakjes[32] == 0:
                windowSurface.blit(kost300,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[32] == 1:
                if type == 2:
                    #betalen
                    player2.money = player2.money - 130
                    player1.money += 130
                    windowSurface.blit(p1get130,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[32] == 2:
                if type == 1:
                    #betalen
                    player1.money = player1.money - 130
                    player2.money = player2.money + 130
                    windowSurface.blit(p1get40,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 33:
            #algemeen fonds
            if type == 1:
                kankopen = algemeenfonds(1)
            else:
                kankopen = algemeenfonds(2)
            return kankopen
        elif positie == 34:
            if vakjes[34] == 0:
                windowSurface.blit(kost320,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[34] == 1:
                if type == 2:
                    #betalen
                    player2.money = player2.money - 150
                    player1.money = player1.money + 150
                    windowSurface.blit(p1get50,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[34] == 2:
                if type == 1:
                    #betalen
                    player1.money = player1.money - 150
                    player2.money = player2.money + 150
                    windowSurface.blit(p2get150,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 35:
            #kijken hoeveel vakjes er van in bezit zijn
            if vakjes[35] == 0:
                windowSurface.blit(kost200,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[35] == 1:
                if type == 2:
                    #betalen
                    q = 0
                    if vakjes[5] == 1:
                        q = q + 1
                    if vakjes[15] == 1:
                        q = q + 1
                    if vakjes[25] == 1:
                        q = q + 1
                    if q == 0:
                        player2.money = player2.money - 25
                        player1.money = player1.money + 25
                    if q == 1:
                        player2.money = player2.money - 50
                        player1.money = player1.money + 50
                    if q == 2:
                        player2.money = player2.money - 100
                        player1.money = player1.money + 100       
                    if q == 3:
                        player2.money = player2.money - 200
                        player1.money = player1.money + 200
                    q = 0   
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[35] == 2:
                if type == 1:
                    #betalen
                    q = 0
                    if vakjes[5] == 2:
                        q = q + 1
                    if vakjes[25] == 2:
                        q = q + 1
                    if vakjes[25] == 2:
                        q = q + 1
                    if q == 0:
                        player1.money = player1.money - 25
                        player2.money = player2.money + 25
                    if q == 1:
                        player1.money = player1.money - 50
                        player2.money = player2.money + 50
                    if q == 2:
                        player1.money = player1.money - 100
                        player2.money = player2.money + 100       
                    if q == 3:
                        player1.money = player1.money - 200
                        player2.money = player2.money + 200
                    q = 0 
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 36:
            #kans
            if type == 1:
                kans(1)
            else:
                kans(2)
            return 2
        elif positie == 37:
            if vakjes[37] == 0:
                windowSurface.blit(kost350,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[37] == 1:
                if type == 2:
                    #betalen
                    player2.money = player2.money - 175
                    player1.money = player1.money + 175
                    windowSurface.blit(p1get175,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[37] == 2:
                if type == 1:
                    #betalen
                    player1.money = player1.money - 175
                    player2.money = player2.money + 175
                    windowSurface.blit(p2get175,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
        elif positie == 38:
            #supertax
            if type == 2:
                windowSurface.blit(supertax,(width/2+250,300))
                pygame.display.update()
                player2.money = player2.money - 100
                pot = pot + 100
            if type == 1:
                windowSurface.blit(supertax,(width/2+250,300))
                pygame.display.update()
                player1.money = player1.money - 100
                pot = pot + 100
            return 2
        elif positie == 39:
            if vakjes[39] == 0:
                windowSurface.blit(kost400,(width/2+250,300))
                pygame.display.update()
                return 1
            elif vakjes[39] == 1:
                if type == 2:
                    #betalen
                    player2.money = player2.money - 200
                    player1.money = player1.money + 200
                    windowSurface.blit(p1get200,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
            elif vakjes[39] == 2:
                if type == 1:
                    #betalen
                    player1.money = player1.money - 200
                    player2.money = player2.money + 200
                    windowSurface.blit(p2get200,(width/2+250,300))
                    pygame.display.update()
                    return 2
                else:
                    windowSurface.blit(eigenaar,(width/2+250,300))
                    pygame.display.update()
                    return 2    
    elif type == 3:
        vakjes[positie] = 1
        if positie == 1:
            player1.money = player1.money - 60
        elif positie == 3:
            player1.money = player1.money - 60
        elif positie == 5:
            player1.money = player1.money - 200
        elif positie == 6:
            player1.money = player1.money - 100
        elif positie == 8:
            player1.money = player1.money - 100
        elif positie == 9:
            player1.money = player1.money - 120
        elif positie == 11:
            player1.money = player1.money - 140
        elif positie == 12:
            player1.money = player1.money - 150
        elif positie == 13:
            player1.money = player1.money - 140
        elif positie == 14:
            player1.money = player1.money - 160
        elif positie == 15:
            player1.money = player1.money - 200
        elif positie == 16:
            player1.money = player1.money - 180
        elif positie == 18:
            player1.money = player1.money - 180
        elif positie == 19:
            player1.money = player1.money - 200
        elif positie == 21:
            player1.money = player1.money - 220
        elif positie == 23:
            player1.money = player1.money - 220
        elif positie == 24:
            player1.money = player1.money - 240
        elif positie == 25:
            player1.money = player1.money - 200
        elif positie == 26:
            player1.money = player1.money - 260
        elif positie == 27:
            player1.money = player1.money - 260
        elif positie == 28:
            player1.money = player1.money - 150
        elif positie == 29:
            player1.money = player1.money - 280
        elif positie == 31:
            player1.money = player1.money - 300
        elif positie == 32:
            player1.money = player1.money - 300
        elif positie == 34:
            player1.money = player1.money - 320
        elif positie == 35:
            player1.money = player1.money - 200
        elif positie == 37:
            player1.money = player1.money - 350
        elif positie == 39:
            player1.money = player1.money - 400
    elif type == 4:
        vakjes[positie] = 2
        if positie == 1:
            player2.money = player2.money - 60
            windowSurface.blit(kost60,(width/2+250,300))
            pygame.display.update()
        elif positie == 3:
            player2.money = player2.money - 60
            windowSurface.blit(kost60,(width/2+250,300))
            pygame.display.update()
        elif positie == 5:
            player2.money = player2.money - 200
            windowSurface.blit(kost200,(width/2+250,300))
            pygame.display.update()
        elif positie == 6:
            player2.money = player2.money - 100
            windowSurface.blit(kost100,(width/2+250,300))
            pygame.display.update()
        elif positie == 8:
            player2.money = player2.money - 100
            windowSurface.blit(kost100,(width/2+250,300))
            pygame.display.update()
        elif positie == 9:
            player2.money = player2.money - 120
            windowSurface.blit(kost120,(width/2+250,300))
            pygame.display.update()
        elif positie == 11:
            player2.money = player2.money - 140
            windowSurface.blit(kost140,(width/2+250,300))
            pygame.display.update()
        elif positie == 12:
            player2.money = player2.money - 150
            windowSurface.blit(kost150,(width/2+250,300))
            pygame.display.update()
        elif positie == 13:
            player2.money = player2.money - 140
            windowSurface.blit(kost140,(width/2+250,300))
            pygame.display.update()
        elif positie == 14:
            player2.money = player2.money - 160
            windowSurface.blit(kost160,(width/2+250,300))
            pygame.display.update()
        elif positie == 15:
            player2.money = player2.money - 200
            windowSurface.blit(kost200,(width/2+250,300))
            pygame.display.update()
        elif positie == 16:
            player2.money = player2.money - 180
            windowSurface.blit(kost180,(width/2+250,300))
            pygame.display.update()
        elif positie == 18:
            player2.money = player2.money - 180
            windowSurface.blit(kost180,(width/2+250,300))
            pygame.display.update()
        elif positie == 19:
            player2.money = player2.money - 200
            windowSurface.blit(kost200,(width/2+250,300))
            pygame.display.update()
        elif positie == 21:
            player2.money = player2.money - 220
            windowSurface.blit(kost220,(width/2+250,300))
            pygame.display.update()
        elif positie == 23:
            player2.money = player2.money - 220
            windowSurface.blit(kost220,(width/2+250,300))
            pygame.display.update()
        elif positie == 24:
            player2.money = player2.money - 240
            windowSurface.blit(kost240,(width/2+250,300))
            pygame.display.update()
        elif positie == 25:
            player2.money = player2.money - 200
            windowSurface.blit(kost200,(width/2+250,300))
            pygame.display.update()
        elif positie == 26:
            player2.money = player2.money - 260
            windowSurface.blit(kost260,(width/2+250,300))
            pygame.display.update()
        elif positie == 27:
            player2.money = player2.money - 260
            windowSurface.blit(kost260,(width/2+250,300))
            pygame.display.update()
        elif positie == 28:
            player2.money = player2.money - 150
            windowSurface.blit(kost150,(width/2+250,300))
            pygame.display.update()
        elif positie == 29:
            player2.money = player2.money - 280
            windowSurface.blit(kost280,(width/2+250,300))
            pygame.display.update()
        elif positie == 31:
            player2.money = player2.money - 300
            windowSurface.blit(kost300,(width/2+250,300))
            pygame.display.update()
        elif positie == 32:
            player2.money = player2.money - 300
            windowSurface.blit(kost300,(width/2+250,300))
            pygame.display.update()
        elif positie == 34:
            player2.money = player2.money - 320
            windowSurface.blit(kost320,(width/2+250,300))
            pygame.display.update()
        elif positie == 35:
            player2.money = player2.money - 200
            windowSurface.blit(kost200,(width/2+250,300))
            pygame.display.update()
        elif positie == 37:
            player2.money = player2.money - 350
            windowSurface.blit(kost350,(width/2+250,300))
            pygame.display.update()
        elif positie == 39:
            player2.money = player2.money - 400   
            windowSurface.blit(kost400,(width/2+250,300))
            pygame.display.update()
def dobbelen():
    global int1
    global int2
    int1 = random.randint(1,6)
    int2 = random.randint(1,6)
    global dubbel 
    dubbel = 0
    worp = int1 + int2
    if int1 == int2:
        dubbel = dubbel + 1
    else:
        dubbel = 0

    return worp
def Player2():
    windowSurface.fill(WHITE)
    pygame.display.update()
    #image bord
    windowSurface.blit(bord,(0,0))
    #init text en variable
    global player1 
    global player2
    global dubbel
    global int1
    global int2
    global positiespeler2
    global positiespeler1
    dobbel = Button(button, pos=(width/2, 450), 
                        text_input="dobbel", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
    while True:
        #dynamische update geld
        geldplayer1 = smallfont.render("player 1: " + str(player1.money),True, RED)
        geldplayer2 = smallfont.render("player 2: " + str(player2.money),True, BLUE)
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
        if player1.money > 0: 
            while aandebeurt == 1:
                player1.update(windowSurface)
                pygame.display.update()
                mouse = pygame.mouse.get_pos()
                # display spelers beurt
                pygame.draw.ellipse(windowSurface, RED, pygame.Rect(width/2+200,175,325,75))
                windowSurface.blit(beurt1,(width/2+255, 200))
                pygame.draw.rect(windowSurface, RED, pygame.Rect(width/2+200, 500, 400,260))
                if algedobbelt == 0:
                    #button dobbelen speler heeft nog niet gedobbelt
                    dobbel = Button(button, pos=(width/2 + 400, 600), 
                                text_input="dobbel", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
                    for btn in [dobbel]:
                        #on hover dobbel
                        btn.changeColor(mouse)
                        btn.update(windowSurface)
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if dobbel.checkForInput(mouse):
                                #onclick dobbel return waarde worp
                                worp = dobbelen()
                                if indegevangenis1 == 1:
                                    #globale var indegevangenis kijkt of die er niet inzet 
                                    indegevangenis(1)
                                    aandebeurt = 2
                                else:
                                    if dubbel == 3:
                                        #kijken of dit niet je derde dubbel is
                                        naardegevangenis(1)
                                        algedobbelt = 1
                                        aandebeurt = 2
                                        dubbel = 0
                                    else:
                                        #positie van speler bepalen en zetten
                                        positiespeler1 = positie1(worp)
                                        #positie speler kijken wat te doen
                                        #kankopen 1 kan het worden gekocht anders 2
                                        kankopen = positiecheck(positiespeler1,1,worp)
                                        geldplayer1 = smallfont.render("player 1: " + str(player1.money),True, RED)
                                        geldplayer2 = smallfont.render("player 2: " + str(player2.money),True, BLUE)
                                        pygame.display.update()
                                        #geld updaten
                                        windowSurface.blit(geldplayer1,(1150,40))
                                        pygame.draw.line(windowSurface, RED,(1150,60),(1350,60),1)
                                        windowSurface.blit(geldplayer2,(1150,80))
                                        pygame.draw.line(windowSurface, BLUE,(1150,100),(1350,100),1)
                                        pygame.display.update()

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
                                        print("player1_xpos = " + str(player1.x_pos))
                                        print("player1_ypos = " + str(player1.y_pos))
                                        print("player2_xpos = " + str(player2.x_pos))
                                        print("player2_ypos = " + str(player2.y_pos))
                                        #er is al gedobbelt
                                        algedobbelt = 1
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                if aandebeurt == 1:
                    if algedobbelt == 1:
                        if kankopen == 1:
                            #wanneer er kan gekocht worden volgende button en kopen
                            kopen = Button(button, pos=(width/2 + 400, 700), 
                                        text_input="kopen", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
                            volgende = Button(button, pos=(width/2 + 400, 600), 
                                        text_input="next", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
                            for btn in [volgende,kopen]:
                                #op hover kleur
                                btn.changeColor(mouse)
                                btn.update(windowSurface)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        if volgende.checkForInput(mouse):
                                            #klik volgende
                                            if dubbel == 1 or dubbel == 2:
                                                #wanneer er is dubbel gegooid blijft speler aan de beurt en kan nog is dobbelen
                                                aandebeurt = 1
                                                algedobbelt = 0
                                                kankopen = 0
                                            else:
                                                #volgende speler aan de beurt
                                                aandebeurt = 2
                                                algedobbelt = 0
                                                kankopen = 0
                                        if kopen.checkForInput(mouse):
                                            #klik kopen kankopen niet meer van toepassing gaat naar alleen met knop volgende
                                            positiecheck(positiespeler1,3,0)
                                            kankopen = 2
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                        else:
                            #kan niet kopen
                            volgende = Button(button, pos=(width/2 + 400, 600), 
                                        text_input="next", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
                            for btn in [volgende]:
                                #op hover
                                btn.changeColor(mouse)
                                btn.update(windowSurface)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if volgende.checkForInput(mouse):
                                        #knop volgende
                                        if dubbel == 1 or dubbel == 2:
                                            #dubbel gegooid zelfde speler kan opnieuw dobbelen
                                            aandebeurt = 1
                                            algedobbelt = 0
                                        else:
                                            #geen dubbel gegooid volgende speler
                                            aandebeurt = 2
                                            algedobbelt = 0
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                pygame.display.update()
        else:
            #winst speler 2
            print("player 2 wins")
            windowSurface.fill(BLACK)
            while True:
                windowSurface.blit(player2wint,(width/2-200, height/2))
                mouse = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.display.update()
        #player two
        #update Players money
        geldplayer1 = smallfont.render("player 1: " + str(player1.money),True, RED)
        geldplayer2 = smallfont.render("player 2: " + str(player2.money),True, BLUE)
        windowSurface.blit(geldplayer1,(1150,40))
        pygame.draw.line(windowSurface, RED,(1150,60),(1350,60),1)
        windowSurface.blit(geldplayer2,(1150,80))
        pygame.draw.line(windowSurface, BLUE,(1150,100),(1350,100),1)
        pygame.display.update()
        if player2.money >= 0:
            #wanneer nog geld over
            while aandebeurt == 2:
                pygame.display.update()
                mouse = pygame.mouse.get_pos()
                #rechthoeken blauw speler 2 aan beurt
                pygame.draw.ellipse(windowSurface, BLUE, pygame.Rect(width/2+200,175,325,75))
                windowSurface.blit(beurt2,(width/2+250, 200))
                pygame.draw.rect(windowSurface, BLUE, pygame.Rect(width/2+200, 500, 400,260))
                if algedobbelt == 0:
                    #nog niet gedobbelt button dobbelen
                    dobbel = Button(button, pos=(width/2 + 400, 600), 
                                text_input="dobbel", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
                    for btn in [dobbel]:
                        #hover
                        btn.changeColor(mouse)
                        btn.update(windowSurface)
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if dobbel.checkForInput(mouse):
                                #klik dobbelen worp gereturnt
                                worp = dobbelen()
                                if indegevangenis2 == 1:
                                    #globale var indegevangenis kijkt of die er niet inzet 
                                    indegevangenis(2)
                                    aandebeurt = 2
                                else:
                                    if dubbel == 3:
                                        #kijken of er geen 3de keer dubbel is gegooid
                                        naardegevangenis(2)
                                        algedobbelt = 1
                                        aandebeurt = 1
                                    else:
                                        #positie speler bepalen
                                        positiespeler2 = positie2(worp)
                                        #kankopen 1 kan worden gekocht anders 2
                                        #wat er op de positie moet gebeuren
                                        kankopen = positiecheck(positiespeler2,2,worp)
                                        geldplayer1 = smallfont.render("player 1: " + str(player1.money),True, RED)
                                        geldplayer2 = smallfont.render("player 2: " + str(player2.money),True, BLUE)
                                        pygame.display.update()
                                        #geld updaten
                                        windowSurface.blit(geldplayer1,(1150,40))
                                        pygame.draw.line(windowSurface, RED,(1150,60),(1350,60),1)
                                        windowSurface.blit(geldplayer2,(1150,80))
                                        pygame.draw.line(windowSurface, BLUE,(1150,100),(1350,100),1)
                                        pygame.display.update()
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
                                        
                                        pygame.display.update()
                                        print("player1_xpos = " + str(player1.x_pos))
                                        print("player1_ypos = " + str(player1.y_pos))
                                        print("player2_xpos = " + str(player2.x_pos))
                                        print("player2_ypos = " + str(player2.y_pos))
                                        #er is gedobbelt
                                        algedobbelt = 1
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                if aandebeurt == 2:
                    if algedobbelt == 1:
                        if kankopen == 1:
                            #er kan worden gekocht of volgende
                            kopen = Button(button, pos=(width/2 + 400, 700), 
                                        text_input="kopen", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
                            volgende = Button(button, pos=(width/2 + 400, 600), 
                                        text_input="next", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
                            for btn in [volgende,kopen]:
                                #on hover
                                btn.changeColor(mouse)
                                btn.update(windowSurface)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        if volgende.checkForInput(mouse):
                                            #volgende
                                            if dubbel == 1 or dubbel == 2:
                                                #dubbel gegooid terug naar dobbelen
                                                aandebeurt = 2
                                                algedobbelt = 0
                                                kankopen = 0
                                            else:
                                                #volgende speler
                                                algedobbelt = 0
                                                aandebeurt = 1
                                        if kopen.checkForInput(mouse):
                                            #er word gekocht naar er kan niet meer worden gekocht
                                            positiecheck(positiespeler2,4,0)
                                            kankopen = 2
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                        else:
                            volgende = Button(button, pos=(width/2 + 400, 600), 
                                        text_input="next", font=get_font(20), base_color=WHITE, hovering_color=GREEN)
                            for btn in [volgende]:
                                #hover
                                btn.changeColor(mouse)
                                btn.update(windowSurface)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        if volgende.checkForInput(mouse):
                                            #volgende
                                            if dubbel == 1 or dubbel == 2:
                                                #dubbel gegooid terug naar dobbelen
                                                aandebeurt = 2
                                                algedobbelt = 0
                                            else:
                                                #volgende speler
                                                algedobbelt = 0
                                                aandebeurt = 1
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                pygame.display.update()
        else:
            #speler 1 wint
            print("player 1 wins")
            windowSurface.fill(BLACK)
            while True:
                windowSurface.blit(player1wint,(width/2-200, height/2))
                mouse = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.display.update()
def Player3():
    windowSurface.fill(BLACK)
    backbutton = Button(button, pos=(width/2, 700), 
                        text_input="BACK", font=get_font(20), base_color=WHITE, hovering_color=RED)
    pygame.display.update()
    windowSurface.blit(construction,(width/2 -300, height/2-300))
    while True:
        mouse = pygame.mouse.get_pos()
        for btn in [backbutton]:
            btn.changeColor(mouse)
            btn.update(windowSurface)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if backbutton.checkForInput(mouse):
                    next()


        pygame.display.update()
def Player4():
    windowSurface.fill(BLACK)
    backbutton = Button(button, pos=(width/2, 700), 
                        text_input="BACK", font=get_font(20), base_color=WHITE, hovering_color=RED)
    pygame.display.update()
    windowSurface.blit(construction,(width/2 -300, height/2-300))
    while True:
        mouse = pygame.mouse.get_pos()
        for btn in [backbutton]:
            btn.changeColor(mouse)
            btn.update(windowSurface)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if backbutton.checkForInput(mouse):
                    next()


        pygame.display.update()

    
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