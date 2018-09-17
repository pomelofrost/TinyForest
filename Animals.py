import pygame
import DrawingAnalyzer2
from Stone import Stone
from operator import itemgetter

###

class Animal(pygame.sprite.Sprite):
    def __init__(self,leftBound,rightBound,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.leftBound = leftBound
        self.rightBound = rightBound-60
        self.x = x
        self.y = y
        self.reproduce = False
        self.speed = 5
        self.direction = 1 #0 is right, 1 is left
        self.stepCount = 0
        

class Rabbit(Animal):
    rabbits = []
    rabbitData = sorted(DrawingAnalyzer2.rabbitData,key=itemgetter(0))
    rabbitData.reverse()
    def __init__(self,leftBound,rightBound,x,y):
        super().__init__(leftBound,rightBound,x,y)
        self.goLeft = [pygame.image.load('rabbit/l1.png'),\
        pygame.image.load('rabbit/l2.png'),pygame.image.load('rabbit/l3.png'),\
        pygame.image.load('rabbit/l4.png'),pygame.image.load('rabbit/l5.png'),\
        pygame.image.load('rabbit/l6.png'),pygame.image.load('rabbit/l7.png')]
        self.goRight = [pygame.image.load('rabbit/r1.png'),\
        pygame.image.load('rabbit/r2.png'),pygame.image.load('rabbit/r3.png'),\
        pygame.image.load('rabbit/r4.png'),pygame.image.load('rabbit/r5.png'),\
        pygame.image.load('rabbit/r6.png'),pygame.image.load('rabbit/r7.png')]
    
    def draw(self,surf,scroll):
        if self.stepCount >= 7:
            self.stepCount = 0
        if self.direction:
            surf.blit(self.goRight[self.stepCount],(self.x+scroll,self.y))
            self.stepCount += 1
            self.x += self.speed
            if self.x >= self.rightBound:
                self.direction = 0
        else:
            surf.blit(self.goLeft[self.stepCount],(self.x+scroll,self.y))
            self.stepCount +=1
            self.x -= self.speed
            if self.x <= self.leftBound:
                self.direction = 1

class Bird(Animal):
    birds = []
    birdData = sorted(DrawingAnalyzer2.birdData,key=itemgetter(0))
    birdData.reverse()
    def __init__(self,positionList):
        self.positionList = positionList # a list of trees to fly to
        self.currPos = 0
        self.x = self.positionList[0][0]
        self.y = self.positionList[0][1]
        self.reproduce = False
        self.stepCount = 0
        self.takeOffRight = ([pygame.image.load('bird/stand.png'),
        pygame.image.load('bird/takeoff1.png'),pygame.image.load('bird/takeoff2.png'),
        pygame.image.load('bird/takeoff3.png')])
        self.landRight = ([pygame.image.load('bird/takeoff3.png'),\
        pygame.image.load('bird/takeoff2.png'),pygame.image.load('bird/takeoff1.png'),
        pygame.image.load('bird/stand.png')])
        self.flyRight = ([pygame.image.load('bird/r1.png'),\
        pygame.image.load('bird/r2.png'),pygame.image.load('bird/r3.png'),\
        pygame.image.load('bird/r4.png'),pygame.image.load('bird/r5.png'),\
        pygame.image.load('bird/r6.png'),pygame.image.load('bird/r7.png')])
        self.takeOffLeft = ([pygame.image.load('bird/standL.png'),
        pygame.image.load('bird/takeoff1L.png'),
        pygame.image.load('bird/takeoff2L.png'),
        pygame.image.load('bird/takeoff3L.png')])
        self.landLeft = ([pygame.image.load('bird/takeoff3L.png'),\
        pygame.image.load('bird/takeoff2L.png'),
        pygame.image.load('bird/takeoff1L.png'),
        pygame.image.load('bird/standL.png')])
        self.flyLeft = ([pygame.image.load('bird/l1.png'),\
        pygame.image.load('bird/l2.png'),pygame.image.load('bird/l3.png'),\
        pygame.image.load('bird/l4.png'),pygame.image.load('bird/l5.png'),\
        pygame.image.load('bird/l6.png'),pygame.image.load('bird/l7.png')])
    
    def draw(self,surf,scroll):
        if self.stepCount >=7:
            self.stepCount = 0
        # print (self.stepCount)
        currX,currY = self.positionList[self.currPos]
        nextPos = (self.currPos+1) % len(self.positionList)
        nextX,nextY = self.positionList[nextPos]
        disX = nextX - currX
        disY = nextY - currY
        speedX = disX/20
        speedY = disY/(disX/speedX)
        if disX > 0:
            if currX == self.x:
                surf.blit(self.takeOffRight[self.stepCount],(self.x+scroll,self.y))
                self.stepCount += 1
                if self.stepCount == 3:
                    self.x += speedX
                    self.y += speedY
                    self.stepCount = 0
            elif self.x >= nextX:
                if self.stepCount > 3:
                    self.stepCount = 0
                surf.blit(self.landRight[self.stepCount],(self.x+scroll,self.y))
                self.stepCount += 1
                if self.stepCount == 3:
                    self.currPos = nextPos
                    self.stepCount = 0
            else:
                surf.blit(self.flyRight[self.stepCount],(self.x+scroll,self.y))
                self.stepCount +=1
                self.x += speedX
                self.y += speedY
        else:
            if currX == self.x:
                # print ('taking off')
                surf.blit(self.takeOffLeft[self.stepCount],(self.x+scroll,self.y))
                self.stepCount += 1
                if self.stepCount == 3:
                    self.x += speedX
                    self.y += speedY
                    self.stepCount = 0
            elif self.x <= nextX:
                # print ('landing')
                if self.stepCount >3:
                    self.stepCount = 0
                surf.blit(self.landLeft[self.stepCount],(self.x+scroll,self.y))
                self.stepCount += 1
                if self.stepCount == 3:
                    self.currPos = nextPos
                    self.stepCount = 0
            else:
                # print ('flying')
                surf.blit(self.flyLeft[self.stepCount],(self.x+scroll,self.y))
                self.stepCount +=1
                self.x += speedX
                self.y += speedY
                