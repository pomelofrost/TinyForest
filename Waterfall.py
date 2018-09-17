import pygame
from Stone import Stone
import random
###

class Waterfall(pygame.sprite.Sprite):
    waterfalls = []
    def __init__(self,topX,topY,topW,topH,middleX,middleY,middleW,middleH,\
    bottomX,bottomY,bottomW,bottomH):
        self.topX = topX
        self.topY = topY-10
        self.topW = topW
        self.topH = topH
        self.middleX = middleX
        self.middleY = middleY-10
        self.middleW = middleW
        self.middleH = middleH
        self.bottomX = bottomX
        self.bottomY = bottomY-10
        self.bottomW = bottomW
        self.bottomH = bottomH
        self.water = (131, 212, 252)
        self.highlight = (184, 229, 252)
        self.count = 0
        self.lightpos = [(self.topX,self.topY,5,random.randint(10,15)),
        (self.topX+35,self.topY+50,8,random.randint(10,15)),\
        (self.topX+50,self.topY+30,10,random.randint(10,15)),\
        (self.topX+self.topW-45,self.topY,15,random.randint(10,15)),\
        (self.middleX,self.middleY+100,5,random.randint(10,15)),\
        (self.middleX+20,self.middleY,10,random.randint(10,15)),\
        (self.middleX+self.middleW/2,self.middleY+45,5,random.randint(10,15)),\
        (self.bottomX+self.bottomW,self.bottomY,10,random.randint(10,15))]

    def draw(self,surf,scroll):
        #vertical
        pygame.draw.rect(surf,self.water,(self.topX+scroll,self.topY,5,
        self.topH-self.middleH))
        pygame.draw.rect(surf,self.water,(self.topX+35+scroll,self.topY,8,
        self.topH-self.middleH))
        pygame.draw.rect(surf,self.water,(self.topX+50+scroll,self.topY,10,
        self.topH-self.middleH))
        pygame.draw.rect(surf,self.water,(self.topX+self.topW-45+scroll,self.topY,15,
        self.topH-self.middleH))
        pygame.draw.rect(surf,self.water,(self.middleX+scroll,self.middleY,
        5,self.middleH-self.bottomH))
        pygame.draw.rect(surf,self.water,(self.middleX+20+scroll,self.middleY,
        10,self.middleH-self.bottomH))
        pygame.draw.rect(surf,self.water,(self.middleX+self.middleW/2+scroll,self.middleY,
        5,self.middleH-self.bottomH))
        pygame.draw.rect(surf,self.water,(self.middleX+self.middleW-45+scroll,self.middleY,
        15,self.middleH-self.bottomH))
        pygame.draw.rect(surf,self.water,(self.bottomX+self.bottomW+scroll,self.bottomY,
        10,800-self.bottomY))
        #horizontal
        pygame.draw.rect(surf,self.water,(self.topX-self.topW+scroll,self.topY-5,self.topW*2,10))
        pygame.draw.rect(surf,self.water,(self.middleX-30+scroll,self.middleY-5,
        self.middleW,10))
        pygame.draw.rect(surf,self.water,(self.bottomX-30+scroll,self.bottomY-5,self.bottomW+40,10))
        #highlights (kinetic)
        self.count +=1
        for i in range(len(self.lightpos)):
            x,y,w,h = self.lightpos[i]
            pygame.draw.rect(surf,self.highlight,(x+scroll,y,w,h))
            self.lightpos.pop(i)
            if i <= 3:
                newY = self.topY+(5*self.count)%(self.topH-self.middleH)
            elif i <= 6:
                newY = self.middleY+(5*self.count)%(self.middleH-self.bottomH)
            else:
                newY = self.bottomY+(5*self.count) % (800-self.bottomY)
            self.lightpos.insert(i,(x,newY,w,h))
    
    @staticmethod
    def generate(self,surf,scroll):
        for waterfall in Waterfall.waterfalls:
            waterfall.draw(surf,scroll)