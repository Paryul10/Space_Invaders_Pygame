import pygame
pygame.init()
class Missile:
    
    def __init__(self,x, y, det):
        #ship is passed because each time we spawn a missile we need the co-ordinates
        ''' missile constructor '''
        self.bx = x
        self.by = y 
        self.det = det 

    def move_missile(self):
        if self.det == 1:  #determines the type of missile
            self.by += -20 #fast bullet // spawned by S 

        if self.det == 0:
            self.by += -10 #slow bullet // spawned by space
            
class missile_1(Missile):

    def __init__(self, x, y, det):

        self.img = pygame.image.load("b1.jpeg")
        Missile.__init__(self,x,y, det)

class missile_2(Missile):
    
    def __init__(self, x, y, det):

        self.img = pygame.image.load("b2.png")
        Missile.__init__(self,x,y, det)
    