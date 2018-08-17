#!/usr/bin/env python
import pygame
import sys
import time
import random
from pygame.locals import * #helps grab input from keyboard or mouse

from spaceship_new import * #imports all functions and classes from spaceship module
from bullet1 import *
from alien import *

font = pygame.font.SysFont("comicsansms", 50)

ship = Spaceship()#creating a ship instance of spaceship class


pygame.init()  #some inbuilt functions need to be invoked
background_color=(0, 34 , 0)
CYAN = (0, 255 , 255)
(width,height)=(800, 800)

clock = pygame.time.Clock() #sper fast . unplayable . to limit our game to 60fps
screen = pygame.display.set_mode((width,height)) #opens pygame window
pygame.display.set_caption('Space Invaders')
ship = Spaceship()

def game_loop():
    score = 0
    bullets1 = []
    bullets2=[]
    aliens=[]
    initial_time=(round(time.time()))
    create = 1
    game = True
    while game:
        change=0  
        clock.tick(30)#60 fps
        screen.fill(background_color) # r , g ,b
        
        #keys=pygame.key.get_pressed()
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:#quits when we cross x ,, event is an object.
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if ship.sx >= 50:
                        change=-50
                elif event.key == pygame.K_d:
                    if ship.sx <= 650:
                        change=50
                elif event.key == pygame.K_SPACE:
                    b1=missile_1(ship.sx+45,ship.sy,0)
                    bullets1.append(b1)
                elif event.key == pygame.K_s:
                    b1=missile_2(ship.sx+45,ship.sy,1)
                    bullets2.append(b1)
                elif event.key == pygame.K_q:
                    pygame.QUIT
                    quit()

        times = (round(time.time()))
        iftime = times-initial_time
        count = 0
        if iftime%10 == 0 and create == 1:
            count += 1
            alien = Alien(times)
            if alien not in aliens:
                aliens.append(alien)
            create = 0
        if iftime%10 == 9:
            create = 1

        for  alien in aliens:
            if alien.type == 1:
                if times - alien.made  == 8:
                    aliens.remove(alien)
        for alien in aliens:
            if alien.type == 0:
                if times - alien.made == 5:
                    aliens.remove(alien)
        if len(aliens) == 0:
            alien = Alien(times)
            aliens.append(alien)
            
        for bullet in bullets1:
            for alien in aliens:
                if bullet.bx >= alien.x and bullet.bx <= alien.x+80:
                    if bullet.by == alien.y+60:
                        bullets1.remove(bullet)
                        aliens.remove(alien)
                        score += 1
        
        for bullet in bullets2:
            for alien in aliens:
                if bullet.bx >= alien.x and bullet.bx <= alien.x+80:
                    if bullet.by == alien.y+60:
                        bullets2.remove(bullet)
                        alien.made = round(time.time())
                        alien.type = 0
                        alien.img = pygame.image.load("half_alien.jpeg")

        for alien in aliens:
            screen.blit(alien.img,(alien.x,alien.y))
                
        for bullet in bullets1:
            bullet.move_missile()
            screen.blit(bullet.img,(bullet.bx,bullet.by))
        
        for bullet in bullets2:
            bullet.move_missile()
            screen.blit(bullet.img,(bullet.bx,bullet.by))
            
        ship.move(change)     
        screen.blit(ship.img,(ship.sx,ship.sy))
        Score = font.render("Score: " + str(score), True, CYAN)
        screen.blit(Score, (0, 0))
        pygame.display.update()
        
    quit()

game_loop()