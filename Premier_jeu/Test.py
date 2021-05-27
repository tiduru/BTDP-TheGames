#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('game base')
screenX = 950
screenY = 950
screen = pygame.display.set_mode((screenX, screenY), 0, 32)
font = pygame.font.SysFont(None, 30)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False

def affichage_carte(x, y, id):
    # Affichage des cartes
    image_x = screenX
    image_y = screenY
    display_surface = pygame.display.set_mode((image_x, image_y))
    image = pygame.image.load('D:\School\BDTP\Games2.5\BTDP-TheGames\Premier_jeu\Images\JcTheLastAirbender.jpg')
    # Affichage carte i
    display_surface.blit(image, (x, y))


def main_menu():
    while True:

        mx, my = pygame.mouse.get_pos()


        #Affichage background
        screen.fill((0, 153, 51))
        affichage_carte(200, 500, 2)
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)



        #Affichage des boutons
        button_1 = pygame.Rect(50, 100, 45, 30)
        button_2 = pygame.Rect(50, 150, 65, 30)
        button_3 = pygame.Rect(50, 200, 60, 30)
        button_4 = pygame.Rect(50, 250, 40, 30)
        button_5 = pygame.Rect(200, 500, 620, 376)
        pygame.draw.rect(screen, (255, 0, 102), button_1)
        draw_text('Fold', font, (255, 255, 255), screen, 50, 100)
        pygame.draw.rect(screen, (255, 0, 102), button_2)
        draw_text('Check', font, (255, 255, 255), screen, 50, 150)
        pygame.draw.rect(screen, (255, 0, 102), button_3)
        draw_text('Raise', font, (255, 255, 255), screen, 50, 200)
        pygame.draw.rect(screen, (255, 0, 102), button_4)
        draw_text('Call', font, (255, 255, 255), screen, 50, 250)





        if button_1.collidepoint((mx, my)):
            if click:
                Fold()
        if button_2.collidepoint((mx, my)):
            if click:
                Check()
        if button_3.collidepoint((mx, my)):
            if click:
                Raise()
        if button_4.collidepoint((mx, my)):
            if click:
                Call()
        if button_5.collidepoint((mx, my)):
            if click:
                EasterEgg()


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def Fold():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('Fold', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)


def Check():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('Check', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

def Raise():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('Raise', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

def Call():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('Call', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

def EasterEgg():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('WOW THIS IS SECRET', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)


main_menu()