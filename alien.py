import pygame
import random
pygame.init()


class Alien:

    def __init__(self,made):
        self.made = made
        self.x = random.randint(0,9)*80
        self.y = random.randint(0,1)*80
        self.type = 1  #1 i full health
        self.img = pygame.image.load("full_alien.png")
        
    

    