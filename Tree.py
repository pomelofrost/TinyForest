import random
import pygame
import numpy
import cv2
import DrawingAnalyzer

class Tree(pygame.sprite.Sprite):
    
    mediumTreeData = DrawingAnalyzer.mediumTreeData
    bushData = DrawingAnalyzer.bushData
    largeTreeData = DrawingAnalyzer.largeTreeData
    mediumTrees = []
    bushes = []
    largeTrees = []
    treeShadows = []
    
    def __init__(self,x,y,season):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.trunkColor = (29, 41, 39)
        if season == 'summer':
            self.leafColor = (51, 71, 68)
            self.highlightColor = (154, 216, 206)
            self.dimColor = (99,140,133)
        elif season == 'fall':
            self.leafColor = (140,60,14)
            self.highlightColor = (216,93,22)
            self.dimColor = (153,66,15)
        elif season == 'spring':
            self.leafColor = (255,165,183)
            self.highlightColor = (255, 255, 255)
            self.dimColor = (255,194,183)
        elif season == 'winter':
            self.leafColor = (180, 209, 209)
            self.highlightColor = (255, 255, 255)
            self.dimColor = (203,236,236)

    
class MediumTree(Tree):
    surf = None
    def __init__(self,x,y,season):
        super().__init__(x,y,season)
        self.height = 200
        self.size = 50
        self.light = 10
        self.lights = []
        self.dims = []
        self.bloomed = False
        self.leafFell = False
        for i in range(self.light):
            lightx = random.randint(self.x-self.size, self.x + self.size)
            lighty = random.randint(self.y-self.height-self.size*2,\
            self.y-self.height-self.size)
            self.lights.append((lightx,lighty))
        for j in range(self.light//2):
            dimx = random.randint(self.x-self.size, self.x + self.size)
            dimy = random.randint(self.y-self.height-self.size*2,\
            self.y-self.height-self.size)
            self.dims.append((dimx,dimy))
    
    def draw(self,surf,scroll):
        #trunk
        pygame.draw.line(surf,self.trunkColor,(self.x+scroll,self.y),\
        (self.x+scroll,self.y-self.height),10)
        #crown of the tree
        pygame.draw.rect(surf,self.leafColor,\
        (self.x-self.size+scroll,self.y-self.height-self.size*2,self.size*2,self.size*3))
        #bottom
        pygame.draw.rect(surf,self.leafColor, \
        (self.x-self.size+5+scroll,self.y-self.height+self.size,self.size*2-10,10))
        pygame.draw.rect(surf,self.leafColor, \
        (self.x-20+scroll,self.y-self.height+self.size+10,40,10))
        
        #left
        pygame.draw.rect(surf,self.leafColor,\
        (self.x-self.size-20+scroll,self.y-self.height-self.size*2+20,10,self.size*3-40))
        pygame.draw.rect(surf,self.leafColor,\
        (self.x-self.size-10+scroll,self.y-self.height-self.size*2+10,10,self.size*3-20))
        pygame.draw.rect(surf,self.leafColor,\
        (self.x-self.size-30+scroll,self.y-self.height-self.size,10,20))
        pygame.draw.rect(surf,self.leafColor,\
        (self.x-self.size-30+scroll,self.y-self.height-self.size+30,10,10))
        #top
        pygame.draw.rect(surf,self.leafColor,\
        (self.x-self.size+15+scroll,self.y-self.height-self.size*2-20,20,10))
        pygame.draw.rect(surf,self.leafColor, \
        (self.x-self.size+5+scroll,self.y-self.height-self.size*2-10,self.size*2-10,10))
        pygame.draw.rect(surf,self.leafColor,\
        (self.x-25+scroll,self.y-self.height-self.size*2-20,50,10))
        pygame.draw.rect(surf,self.leafColor,\
        (self.x+5+scroll,self.y-self.height-self.size*2-25,10,5))
        pygame.draw.rect(surf,self.leafColor,\
        (self.x-20+scroll,self.y-self.height-self.size*2-25,15,5))
        #right
        pygame.draw.rect(surf,self.leafColor,\
        (self.x+self.size+10+scroll,self.y-self.height-self.size*2+20,10,self.size*3-40))
        pygame.draw.rect(surf,self.leafColor,\
        (self.x+self.size+scroll,self.y-self.height-self.size*2+10,10,self.size*3-20))
        pygame.draw.rect(surf,self.leafColor,\
        (self.x+self.size+20+scroll,self.y-self.height-self.size+34,10,20))
        pygame.draw.rect(surf,self.leafColor,\
        (self.x+self.size+20+scroll,self.y-self.height-self.size-10,10,15))
        pygame.draw.rect(surf,self.leafColor,\
        (self.x+self.size+20+scroll,self.y-self.height-self.size+10,10,10))
        
        #light
        for light in self.lights:
            pygame.draw.rect(surf,self.highlightColor,(light[0]+scroll,light[1],5,5))
        for dim in self.dims:
            pygame.draw.rect(surf,self.dimColor,(dim[0]+scroll,dim[1],6,6))
        #blinking lights
        status = random.choice(['blink','static'])
        if status == 'blink':
            blinkx = random.randint(self.x-self.size, self.x + self.size)
            blinky = random.randint(self.y-self.height-self.size*2,\
            self.y-self.height-self.size)
            pygame.draw.rect(surf,self.highlightColor,(blinkx+scroll,blinky,5,5))
    
    def bloom(self,surf,count,scroll):

        for flower in range(count):
            flowerx = random.randint(self.x-self.size+scroll, self.x + self.size+scroll)
            flowery = random.randint(self.y-self.height-self.size*2,\
            self.y-self.height-self.size)
            pygame.draw.rect(surf,self.dimColor, \
            (flowerx,flowery,8,8),3)
        for highlightFlower in range(count//2):
            flowerx = random.randint(self.x-self.size+scroll, self.x + self.size+scroll)
            flowery = random.randint(self.y-self.height-self.size*2,\
            self.y-self.height-self.size)
            pygame.draw.rect(surf,self.highlightColor, \
            (flowerx,flowery,8,8),3)
    
    def leafFall (self,surf,scroll):
        self.size = 40
        for leaf in range(6):
            leafx = random.randint(self.x-self.size+scroll,self.x+self.size+scroll)
            leafy = random.randint(self.y-self.height,self.y)
            pygame.draw.rect(surf,self.leafColor,(leafx,leafy,10,5))
        
    @staticmethod
    def generate(self,surf,scroll):
        Tree.surf = surf
        for tree in Tree.mediumTrees:
            tree.draw(surf,scroll)
            if tree.bloomed == True:
                tree.bloom(surf,5,scroll)
            if tree.leafFell == True:
                tree.leafFall(surf,scroll)
            
class Bush(Tree):
    def __init__(self,x,y,season):
        super().__init__(x,y,season)
        self.height = 80
        self.size = 50
        self.light = 10
        if season == 'summer':
            self.leafColor = (43,90,79)
        elif season == 'fall':
            self.leafColor = (191,74,13)
        elif season == 'spring':
            self.leafColor = (255,185,202)
        elif season == 'winter':
            self.leafColor = (135, 182, 191)
        self.lights = []
        self.dims = []
        for i in range(self.light):
            lightx = random.randint(self.x-self.size, self.x + self.size)
            lighty = random.randint(self.y-self.height,self.y-50)
            self.lights.append((lightx,lighty))
        for j in range(self.light//2):
            dimx = random.randint(self.x-self.size, self.x + self.size)
            dimy = random.randint(self.y-self.height,self.y-30)
            self.dims.append((dimx,dimy))
        
    def draw(self,surf,scroll):
        #mainbody
        pygame.draw.rect(surf,self.leafColor,\
        (self.x-self.size+scroll,self.y-self.height,self.size*2,self.height))
        #left
        for layer in range(1,3):
            pygame.draw.rect(surf,self.leafColor,\
            (self.x-self.size-10*layer+scroll,self.y-self.height+10*layer,10,self.height-20*layer))
        #right
            pygame.draw.rect(surf,self.leafColor,\
            (self.x+self.size+10*(layer-1)+scroll,self.y-self.height+10*layer,10,self.height-20*layer))
        #top
            pygame.draw.rect(surf,self.leafColor,\
            (self.x-self.size+15*layer+scroll,self.y-self.height-10*layer,self.size*2-25*layer,10))
        #light
        for light in self.lights:
            pygame.draw.rect(surf,self.highlightColor,(light[0]+scroll,light[1],5,5))
        for dim in self.dims:
            pygame.draw.rect(surf,self.dimColor,(dim[0]+scroll,dim[1],6,6))
    
    def bloom(self,surf,count):
        for flower in range(count):
            flowerx = random.randint(self.x-self.size, self.x + self.size)
            flowery = random.randint(self.y-self.height,self.y-30)
            pygame.draw.rect(surf,self.dimColor, \
            (flowerx,flowery,8,8),3)
        for highlightFlower in range(count//2):
            flowerx = random.randint(self.x-self.size, self.x + self.size)
            flowery = random.randint(self.y-self.height,self.y-50)
            pygame.draw.rect(surf,self.highlightColor, \
            (flowerx,flowery,8,8),3)
    @staticmethod
    def generate(self,surf,scroll):
        for tree in Tree.bushes:
            tree.draw(surf,scroll)
            
class LargeTree(Tree):
    def __init__(self,x,y,height,season):
        super().__init__(x,y,season)
        self.height = height
        self. size = 100
        self.light = 10
        self.width = 25
        self.crownheight = self.size*3
        if season == 'summer':
            self.leafColor = (38,54,51)
        elif season == 'fall':
            self.leafColor = (158, 56, 0)
        elif season == 'spring':
            self.leafColor = (186, 92, 117)
        elif season == 'winter':
            self.leafColor = (103, 118, 142)
    
    def draw(self,surf,scroll):
        #trunk
        pygame.draw.rect(surf,self.trunkColor,\
        (self.x-self.width+scroll,self.y-self.height,self.width*2,self.height))
        #crown of the tree
        #main
        pygame.draw.rect(surf,self.leafColor,(self.x-self.size+scroll,\
        self.y-self.height-self.crownheight,self.size*2,self.crownheight))
        #top
        pygame.draw.rect(surf,self.leafColor,(self.x-self.size+30+scroll,\
        self.y-self.height-self.crownheight-30,self.size*2-60,30))
        pygame.draw.rect(surf,self.leafColor,(self.x-self.size+60+scroll,\
        self.y-self.height-self.crownheight-60,self.size*2-120,30))
        #bottom
        pygame.draw.rect(surf,self.leafColor,(self.x-self.size+30+scroll,\
        self.y-self.height,self.size*2-60,30))
        pygame.draw.rect(surf,self.leafColor,(self.x-self.size+60+scroll,\
        self.y-self.height+30,self.size*2-120,30))
        #left
        pygame.draw.rect(surf,self.leafColor,(self.x-self.size-30+scroll,\
        self.y-self.height-self.crownheight+30,30,self.crownheight-30))
        pygame.draw.rect(surf,self.leafColor,(self.x-self.size-60+scroll,\
        self.y-self.height-self.crownheight+60,30,self.crownheight-120))
        #right
        pygame.draw.rect(surf,self.leafColor,(self.x+self.size+scroll,\
        self.y-self.height-self.crownheight+30,30,self.crownheight-30))
        pygame.draw.rect(surf,self.leafColor,(self.x+self.size+30+scroll,\
        self.y-self.height-self.crownheight+60,30,self.crownheight-120))

    @staticmethod
    def generate(self,surf,scroll):
        for tree in Tree.largeTrees:
            tree.draw(surf,scroll)
        