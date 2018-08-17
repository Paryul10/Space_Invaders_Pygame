import pygame
pygame.init()
class Spaceship:

    def __init__(self,sx = 350,sy = 640):
        self.img = pygame.image.load("spaceship-new.png")
        self.sx = sx
        self.sy = sy
        self.xmove = 0
    
    def move(self,change):
        self.sx += change
