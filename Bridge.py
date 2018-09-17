import pygame
from Stone import Stone

###

class Bridge(pygame.sprite.Sprite):
    bridges= []
    seasonIndex = 1
    def __init__(self,originX,destinationX,originY,destinationY):
        pygame.sprite.Sprite.__init__(self)
        self.originX = originX
        self.destinationX = destinationX
        self.originY = originY
        self.destinationY = destinationY
        self.height = 80
        self.width = 10
        self.topwidth = 15
        if Bridge.seasonIndex == 1:
            self.shadow = (112,127,123)
            self.highlight = (169,191,185)
        elif Bridge.seasonIndex == 0:
            self.shadow = (114,100,102)
            self.highlight = (186,163,165)
        elif Bridge.seasonIndex == 2:
            self.shadow = (114,99,83)
            self.highlight = (153,132,111)
        elif Bridge.seasonIndex == 3:
            self.shadow = (103,109,114)
            self.highlight = (138,146,153)
    
    def draw(self,surf,scroll):
        if abs(self.destinationY-self.originY) <=200 and \
        abs(self.destinationX-self.originX) >= 100:
            #first layer
            #two sides
            pygame.draw.rect(surf,self.shadow,(self.originX-self.width+scroll,\
            self.originY-self.height,self.width,self.height))
            pygame.draw.rect(surf,self.shadow,(self.destinationX-self.width+scroll,\
            self.destinationY-self.height,self.width,self.height))
            #connecting arc
            length = (self.destinationX - self.originX)/3
            gap = self.destinationY - self.originY
            dy = gap/3
            pygame.draw.polygon(surf,self.shadow,[(self.originX+scroll,\
            self.originY-self.width),(self.originX+scroll,self.originY),\
            (self.originX+length+scroll,self.originY+self.width+dy),\
            (self.originX+length+scroll,self.originY+dy)])
            pygame.draw.polygon(surf,self.shadow,\
            [(self.originX+scroll+length,self.originY+dy),\
            (self.originX+length+scroll,self.originY+self.width+dy),\
            (self.originX+length*2+scroll,self.originY+self.width+dy*2),\
            (self.originX+length*2+scroll,self.originY+dy*2)])
            pygame.draw.polygon(surf,self.shadow,[\
            (self.originX+length*2+scroll,self.originY+dy*2),\
            (self.originX+length*2+scroll,self.originY+self.width+dy*2),\
            (self.destinationX+scroll,self.destinationY),\
            (self.destinationX+scroll,self.destinationY-self.width)])
            #second layer
            offset = 10
            #two sides
            pygame.draw.rect(surf,self.highlight,(self.originX-self.topwidth+scroll+offset,\
            self.originY-self.height,self.topwidth,self.height))
            pygame.draw.rect(surf,self.highlight,(self.destinationX-self.topwidth+scroll+offset,\
            self.destinationY-self.height,self.topwidth,self.height))
            #connecting arc
            pygame.draw.polygon(surf,self.highlight,[(self.originX+scroll+5,\
            self.originY-self.topwidth-offset),(self.originX+scroll+5,self.originY-offset),\
            (self.originX+length+scroll+offset,self.originY+self.topwidth-offset+dy),\
            (self.originX+length+scroll+offset,self.originY-offset+dy)])
            pygame.draw.polygon(surf,self.highlight,\
            [(self.originX+scroll+length+offset,self.originY-offset+dy),\
            (self.originX+length+scroll+offset,self.originY+self.topwidth-offset+dy),\
            (self.originX+length*2+scroll+offset,self.originY+self.topwidth+dy*2-offset),\
            (self.originX+length*2+scroll+offset,self.originY+dy*2-offset)])
            pygame.draw.polygon(surf,self.highlight,[\
            (self.originX+length*2+scroll+offset,self.originY+dy*2-offset),\
            (self.originX+length*2+scroll+offset,self.originY+self.topwidth+dy*2-offset),\
            (self.destinationX+scroll+offset,self.destinationY-offset),\
            (self.destinationX+scroll+offset,self.destinationY-self.topwidth-offset)])
    
    @staticmethod
    def generate(self,surf,scroll):
        for bridge in Bridge.bridges:
            bridge.draw(surf,scroll)