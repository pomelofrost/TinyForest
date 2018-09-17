import random
import pygame
import numpy
import DrawingAnalyzer
from operator import itemgetter
###


 
class Stone(pygame.sprite.Sprite):
    #color palettes
    seasonIndex = 1
    backStones = []
    middleStones = []
    frontStones = []
    dims = []
    cornerData = sorted(DrawingAnalyzer.cornerData,key=itemgetter(0))
    cornerData.reverse() #order data from right to left so draw from left to right
    stoneSurface = dict()
    backSurface = dict()
    middleSurface = dict()
    frontSurface = dict()
    
    
    def __init__(self,x,y,w,h,layer,snowed):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.layer = layer
        self.season = Stone.seasonIndex
        self.snowed = snowed
        if Stone.seasonIndex == 1:
            self.light = (141, 199, 190)
            self.dark = (98, 138, 131)
            self.medium = (116, 163, 155)
            self.shadow = (36,46,44)
            self.highlight = (142,181,172)
            self.dim = (200,255,243)
        elif Stone.seasonIndex == 0:
            self.light = (216, 156, 164)
            self.dark = (138, 99, 104)
            self.medium = (163, 117, 123)
            self.shadow = (64,46,48)
            self.highlight = (255,184,193)
            self.dim = (242,175,183)
        elif Stone.seasonIndex == 2:
            self.light = (153, 91, 24)
            self.dark = (108, 64, 17)
            self.medium = (166, 98, 26)
            self.shadow = (64,27,6)
            self.highlight = (255,151,41)
            self.dim = (224,133,20)
        elif Stone.seasonIndex == 3:
            self.light = (168, 184, 196)
            self.dark = (96, 105, 112)
            self.medium = (142, 155, 166)
            self.shadow = (57,62,67)
            self.highlight = (219,239,255)
            self.dim = (188,205,219)
        self.colors = [self.light,self.medium,self.dark]


    def draw(self,msurf,scroll):
        #light side
        pygame.draw.rect(msurf,self.colors[self.layer],\
        (self.x+scroll,self.y-self.h,self.w,self.h))
        #dark side
        pygame.draw.rect(msurf,self.shadow,\
        (self.x-self.w+scroll,self.y-10-self.h,self.w,self.h+10))
        #hightlights
        pygame.draw.rect(msurf,self.highlight,\
        (self.x+scroll,self.y-self.h,5,self.h))
        pygame.draw.rect(msurf,self.highlight,\
        (self.x+scroll,self.y-10-self.h,self.w,10))
        pygame.draw.rect(msurf,self.highlight,\
        (self.x+self.w-5+scroll,self.y-self.h,5,self.h/3))
        #dims
        for dim in Stone.dims:
            length,dimx,dimy = dim
            pygame.draw.rect(msurf,self.dim,(dimx+scroll,dimy,length,10))
        if self.snowed == True:
            pygame.draw.rect(msurf,(255,255,255),(self.x+scroll,self.y-self.h-10, self.w,10))
            pygame.draw.rect(msurf,(255,255,255),(self.x+scroll-15,self.y-self.h-20,self.w-30,10))
    
    @staticmethod
    def generate(self,msurf,displayWidth,displayHeight,scroll,snowed):
        #draw back stone first, then front
        for stoneData in Stone.backStones:
            stone  = Stone(stoneData[0],stoneData[1],stoneData[2],stoneData[3],stoneData[4],snowed)
            stone.draw(msurf,scroll)
        for stoneData in Stone.middleStones:
            stone  = Stone(stoneData[0],stoneData[1],stoneData[2],stoneData[3],stoneData[4],snowed)
            stone.draw(msurf,scroll)
        for stoneData in Stone.frontStones:
            stone  = Stone(stoneData[0],stoneData[1],stoneData[2],stoneData[3],stoneData[4],snowed)
            stone.draw(msurf,scroll)
    
    @staticmethod
    def findBiggestGap(self,dataSet):
        #returns a tuple of biggest gap
        coveredX = []
        for key in dataSet:
            coveredX.append(key)
        coveredX = sorted(coveredX)
        largestGap = 0
        if len(coveredX)>=2:
            for i in range(len(coveredX)):
                distance = coveredX[i]-coveredX[i-1]
                if distance > largestGap:
                    largestGap = distance
                    gapOriginX = coveredX[i-1]
                    gapOriginY = dataSet[coveredX[i-1]]
                    gapDestinationX = coveredX[i]
                    gapDestinationY = dataSet[coveredX[i]]
            return (gapOriginX,gapDestinationX,gapOriginY,gapDestinationY)
        else:
            return None
