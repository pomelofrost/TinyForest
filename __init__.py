'''
PygameGame template by Lukas Peraza
https://github.com/LBPeraza/Pygame-Asteroids/blob/master/pygamegame.py
'''
import random
import pygame
import numpy
import cv2
from threading import Thread
from queue import Queue
import time

##files
from Tree import Tree,MediumTree,Bush,LargeTree
from Stone import Stone
from Bridge import Bridge
from Waterfall import Waterfall
from Animals import Animal,Rabbit,Bird
###
class Main(Thread):

    def init(self):
        if self.mode == "menu": self.initMenu()
        elif self.mode == "scene1": self.initScene1()
        elif self.mode == "scene2": self.initScene2()
        elif self.mode == "gallery": self.initG()


    def mousePressed(self, x, y,scroll):
        if self.mode == "menu": self.mousePressedMenu(x, y,scroll)
        elif self.mode == "scene1":self.mousePressedScene1(x, y,scroll)
        elif self.mode == "scene2":self.mousePressedScene2(x, y,scroll)
        elif self.mode == "gallery":self.mousePressedG(x, y,scroll)


    def mouseReleased(self, x, y):
        if self.mode == "menu": self.mouseReleasedMenu(x, y)
        elif self.mode == "scene1": self.mouseReleasedScene1(x, y)
        elif self.mode == "scene2": self.mouseReleasedScene2(x, y)
        elif self.mode == "gallery": self.mouseReleasedG(x, y)

    def mouseMotion(self, x, y):
        if self.mode == "menu": self.mouseMotionMenu(x, y)
        elif self.mode == "scene1": self.mouseMotionScene1(x, y)
        elif self.mode == "scene2": self.mouseMotionScene2(x, y)
        elif self.mode == "gallery": self.mouseMotionG(x, y)

    def mouseDrag(self, x, y):
        if self.mode == "menu": self.mouseDragMenu(x, y)
        elif self.mode == "scene1": self.mouseDragScene1(x, y)
        elif self.mode == "scene2": self.mouseDragScene2(x, y)
        elif self.mode == "gallery": self.mouseDragG(x, y)

    def keyPressed(self, keyCode, modifier):
        if self.mode == "menu": self.keyPressedMenu(keyCode, modifier)
        elif self.mode == "scene1": self.keyPressedScene1(keyCode, modifier)
        elif self.mode == "scene2": self.keyPressedScene2(keyCode, modifier)
        elif self.mode == "gallery": self.keyPressedG(keyCode, modifier)

    def keyReleased(self, keyCode, modifier):
        if self.mode == "menu": self.keyReleasedMenu(keyCode, modifier)
        elif self.mode == "scene1": self.keyReleasedScene1(keyCode, modifier)
        elif self.mode == "scene2": self.keyReleasedScene2(keyCode, modifier)
        elif self.mode == "gallery": self.keyReleasedG(keyCode, modifier)

    def timerFired(self,dt,keysDown):
        if self.mode == "menu": self.timerFiredMenu(dt,keysDown)
        elif self.mode == "scene1": self.timerFiredScene1(dt,keysDown)
        elif self.mode == "scene2": self.timerFiredScene2(dt,keysDown)
        elif self.mode == "gallery": self.timerFiredG(dt,keysDown)

    def redrawAll(self, screen):
        if self.mode == "menu": self.redrawAllMenu(screen)
        elif self.mode == "scene1": self.redrawAllScene1(screen)
        elif self.mode == "scene2": self.redrawAllScene2(screen)
        elif self.mode == "gallery": self.redrawAllG(screen)

    
##### start menu
    def initMenu(self):
        self.title = pygame.image.load('menu/title.png')
        self.instruction = pygame.image.load('menu/instruction.png')
        self.titlePos = (self.width/2,300)
        self.instructionPos = (self.width/2,self.height-200)
    
    def redrawAllMenu(self,screen):
        titleRect = self.title.get_rect()
        titleRect.center = self.titlePos
        insRect = self.instruction.get_rect()
        insRect.center = self.instructionPos
        screen.blit(self.title,titleRect)
        screen.blit(self.instruction,insRect)
        
    def keyPressedMenu(self,keyCode,modifier):
        if keyCode == pygame.K_SPACE:
            self.mode = "scene1"
            import DrawingTool
            self.initScene1()
    
    def mousePressedMenu(self, x, y,scroll):
        pass

    def mouseReleasedMenu(self, x, y):
        pass

    def mouseMotionMenu(self, x, y):
        pass

    def mouseDragMenu(self, x, y):
        pass

    def keyReleasedMenu(self, keyCode, modifier):
        pass
    
    def timerFiredMenu(self,dt,keysDown):
        pass
##### main scene #2
    def initScene1(self):
        season = self.seasons[self.currSeason]
        #reset everything before changing the season
        Stone.backStones = []
        Stone.middleStones = []
        Stone.frontStones = []
        Stone.dims = []
        Stone.stoneSurface = dict()
        Stone.backSurface = dict()
        Stone.middleSurface = dict()
        Stone.frontSurface = dict()
        Tree.mediumTrees = []
        Tree.bushes = []
        Tree.largeTrees = []
        Bridge.bridges = []
        Waterfall.waterfalls = []
        #generate stones
        for corner in Stone.cornerData:
            if corner[1] <= self.height/3:
                layer = 0
                h = random.randint(500,800)
                w = random.randint(50,100)
                for dim in range(random.randint(0,4)):
                    length = random.randint(5,w//3)
                    dimx = random.randint(corner[0],corner[0]+w*2//3)
                    dimy = 790-h
                    Stone.dims.append((length,dimx,dimy))
                Stone.backStones.append((corner[0],800,w,h,layer))
                #add to surface dictionary
                for i in range(corner[0],corner[0]+w):
                    Stone.stoneSurface[i]=789-h
                    Stone.backSurface[i]=789-h
            elif corner[1] <= self.height*2/3:
                layer = 1
                h = random.randint(100,500)
                w = random.randint(100,150)
                for dim in range(random.randint(0,4)):
                    length = random.randint(5,w//3)
                    dimx = random.randint(corner[0],corner[0]+w*2//3)
                    dimy = 790-h
                    Stone.dims.append((length,dimx,dimy))
                for i in range(corner[0],corner[0]+w):
                    Stone.stoneSurface[i]=789-h
                    Stone.middleSurface[i]=789-h
                Stone.middleStones.append((corner[0],800,w,h,layer))

            else:
                layer = 2
                h = random.randint(20,100)
                w = random.randint(50,150)
                for dim in range(random.randint(0,4)):
                    length = random.randint(5,w//3)
                    dimx = random.randint(corner[0],corner[0]+w*2//3)
                    dimy = 790-h
                    Stone.dims.append((length,dimx,dimy))
                for i in range(corner[0],corner[0]+w):
                    Stone.stoneSurface[i]=789-h
                    Stone.frontSurface[i]=789-h
                Stone.frontStones.append((corner[0],800,w,h,layer))

        #trees
        for tree in Tree.mediumTreeData:
            a = tree[0]+800
            b = Stone.stoneSurface.get(a,800)
            if b != 800:
                Tree.mediumTrees.append(MediumTree(a,b,season))
            x = tree[0]
            y = Stone.stoneSurface.get(x,800)
            Tree.mediumTrees.append(MediumTree(x,y,season))
            c = tree[0]-800
            d = Stone.stoneSurface.get(c,800)
            if d!= 800:
                Tree.mediumTrees.append(MediumTree(c,d,season))        
        for bush in Tree.bushData:
            a = bush[0]+800
            b = Stone.stoneSurface.get(a,800)
            if b != 800:
                Tree.bushes.append(Bush(a,b,season))
            x = bush[0]
            y = Stone.stoneSurface.get(x,800)
            Tree.bushes.append(Bush(x,y,season))
            c = bush[0]-800
            d = Stone.stoneSurface.get(c,800)
            if d!= 800:
                Tree.bushes.append(Bush(c,d,season))
        for largeTree in Tree.largeTreeData:
            x = largeTree[0]
            y = 800
            height = random.randint(300,600)
            Tree.largeTrees.append(LargeTree(x,y,height,season))
            Tree.largeTrees.append(LargeTree(x+800,y,height,season))
            Tree.largeTrees.append(LargeTree(x-800,y,height,season))
        #identify biggest gap
        gapOriginX,gapDestinationX,gapOriginY,gapDestinationY =\
        Stone.findBiggestGap(Stone,Stone.stoneSurface)
        #setup back stones for waterfall
        self.backStoneX = gapOriginX+(gapOriginX-gapDestinationX)/2
        self.backStoneH = random.randint(500,800)
        self.backStoneW = random.randint(50,100)
        Stone.backStones.append((self.backStoneX,800,self.backStoneW,self.backStoneH,0))
        self.middleStoneX = self.backStoneX+30
        self.middleStoneH = random.randint(100,500)
        self.middleStoneW = random.randint(100,150)
        Stone.middleStones.append((self.middleStoneX,800,self.middleStoneW,self.middleStoneH,1))
        self.frontStoneX = self.middleStoneX+30
        self.frontStoneH = random.randint(20,100)
        self.frontStoneW = random.randint(50,150)
        Stone.frontStones.append((self.frontStoneX,800,self.frontStoneW,self.frontStoneH,2))
        Waterfall.waterfalls.append(Waterfall(self.backStoneX,800-self.backStoneH,\
        self.backStoneW,self.backStoneH,self.middleStoneX,800-self.middleStoneH,\
        self.middleStoneW,self.middleStoneH,self.frontStoneX,800-self.frontStoneH,
        self.frontStoneW,self.frontStoneH))
        #identify bridge gaps
        #back
        if Stone.findBiggestGap(Stone,Stone.backSurface) != None:
            backX1,backX2,backY1,backY2 =\
            Stone.findBiggestGap(Stone,Stone.backSurface)
            Bridge.bridges.append(\
            Bridge(backX1,backX2,backY1,backY2))
        #middle
        if Stone.findBiggestGap(Stone,Stone.middleSurface) != None:
            middleX1,middleX2,middleY1,middleY2 =\
            Stone.findBiggestGap(Stone,Stone.middleSurface)
            Bridge.bridges.append(\
            Bridge(middleX1,middleX2,middleY1,middleY2))
        #front
        if Stone.findBiggestGap(Stone,Stone.frontSurface) != None:
            frontX1,frontX2,frontY1,frontY2 =\
            Stone.findBiggestGap(Stone,Stone.frontSurface)
            Bridge.bridges.append(\
            Bridge(frontX1,frontX2,frontY1,frontY2))
        
        #instruction
        self.showInstruction = False
        self.showNavigation = True
        self.timer = 0
        self.leftArrow = pygame.image.load('menu/leftarrow.png')
        self.rightArrow = pygame.image.load('menu/rightarrow.png')
        self.leftArrowRect = self.leftArrow.get_rect()
        self.rightArrowRect = self.rightArrow.get_rect()
        self.leftArrowRect.center =(50,self.height/2)
        self.rightArrowRect.center = (1230,self.height/2)
        self.navigation = pygame.image.load('menu/lookaround.png')
        self.navRect = self.navigation.get_rect()
        self.navRect.center = (self.width/2,30)
        
        #menubar
        self.menuBar = pygame.image.load('menu/menu.png')
        self.menuPos = (1150,20)
        self.menuExpanded = False
        self.seasonBar = pygame.image.load('menu/seasons.png')
        self.seaPos = (960,20)
        self.seasonExpanded = False
        self.arrow = pygame.image.load('menu/downarrow.png')
        self.arrowPos = (1055,75)
        self.arrowShow = False
        self.spring = pygame.image.load('menu/spring.png')
        self.spring1 = pygame.image.load('menu/spring1.png')
        self.springPos = (960,70)
        self.summer = pygame.image.load('menu/summer.png')
        self.summer1 = pygame.image.load('menu/summer1.png')
        self.summerPos = (960,120)
        self.autumn = pygame.image.load('menu/autumn.png')
        self.autumn1 = pygame.image.load('menu/autumn1.png')
        self.autumnPos = (960,170)
        self.winter = pygame.image.load('menu/winter.png')
        self.winter1 = pygame.image.load('menu/winter1.png')
        self.winterPos = (960,220)
        self.makeitsnow = pygame.image.load('menu/makeitsnow.png')
        self.makePos = (20,20)
        self.snowed = False
        #snow
        self.snowDensity = 30
        self.snowSpeed = 10
        self.snowflakes = []
        self.snowflake = pygame.image.load('menu/snowflake.png')
        for i in range(self.snowDensity):
            snowX = random.randint(0,1280)
            snowY = random.randint(0,800)
            self.snowflakes.append((snowX,snowY))
        
    def mousePressedScene1(self, x, y,scroll): 
        for tree in Tree.mediumTrees:
            treeRect = pygame.Rect(tree.x-tree.size,tree.y-tree.height-tree.size*2,tree.size*2,tree.size*3)
            if treeRect.collidepoint(x-scroll,y)==True:
                tree.bloomed = not tree.bloomed
                tree.generate(tree,Tree.surf,scroll)
        if 1150 < x < 1260 and 20 < y < 70:
            self.menuExpanded = not self.menuExpanded
            self.arrowShow = True
        if self.menuExpanded == True and 960 < x < 1150 and 20<y<70:
            self.seasonExpanded = not self.seasonExpanded
            self.arrowShow = not self.seasonExpanded
        if self.seasonExpanded == True and  960 < x < 1150 and 70<y<120:
            self.currSeason = 0
            self.bgColor = (153,116,113)
            Bridge.seasonIndex = 0
            Stone.seasonIndex = 0
            self.initScene1()
        if self.seasonExpanded == True and  960 < x < 1150 and 120<y<170:
            self.currSeason = 1
            self.bgColor = (61, 94, 83)
            Bridge.seasonIndex = 1
            Stone.seasonIndex = 1
            self.initScene1()
        if self.seasonExpanded == True and  960 < x < 1150 and 170<y<220:
            self.currSeason = 2
            self.bgColor = (216,177,94)
            Bridge.seasonIndex = 2
            Stone.seasonIndex = 2
            self.initScene1()
        if self.seasonExpanded == True and  960 < x < 1150 and 220<y<270:
            self.currSeason = 3
            self.bgColor = (138,200,216) 
            Bridge.seasonIndex = 3
            Stone.seasonIndex = 3
            self.initScene1()
        if self.currSeason == 3 and 20 < x < 255 and 20 < y < 70:
            self.snowed = True
        

    def mouseReleasedScene1(self, x, y):
        pass

    def mouseMotionScene1(self, x, y):
        pass

    def mouseDragScene1(self, x, y):
        pass

    def keyPressedScene1(self, keyCode, modifier):
        if keyCode == pygame.K_SPACE:
            import DrawingTool2
            self.mode = 'scene2'
            self.initScene2()
        
    def keyReleasedScene1(self, keyCode, modifier):
        pass

    def timerFiredScene1(self, dt,keysDown):
        if keysDown(pygame.K_RIGHT) and self.scrollX > -800:
            self.scrollX -= 30
        elif keysDown(pygame.K_LEFT) and self.scrollX < 800:
            self.scrollX +=30
        self.timer += 1
        if self.timer > 50:
            self.showInstruction = True
            self.showNavigation = False
        for snowflake in self.snowflakes:
            snowindex = self.snowflakes.index(snowflake)
            newX = snowflake[0]
            newY = (snowflake[1]+self.snowSpeed)%800
            self.snowflakes.pop(snowindex)
            self.snowflakes.insert(snowindex,(newX,newY))      
      
    def redrawAllScene1(self, screen):
        LargeTree.generate(LargeTree,screen,self.scrollX)
        Stone.generate(Stone,screen,self.width,self.height,self.scrollX,self.snowed)
        Waterfall.generate(Waterfall,screen,self.scrollX)
        Bush.generate(Bush,screen,self.scrollX)
        Bridge.generate(Bridge,screen,self.scrollX)
        MediumTree.generate(MediumTree,screen,self.scrollX)
        #snow
        if self.snowed == True:
            for snowflake in self.snowflakes:
                screen.blit(self.snowflake,snowflake)
        if self.showInstruction == True:
            pixel = pygame.font.Font('Pixeled.ttf',15)
            instructionSurf = pixel.render("PRESS 'SPACE' TO ADD ANIMALS", True, (255,255,255))
            instructionRect = instructionSurf.get_rect()
            instructionRect.center = (self.width/2,775)
            screen.blit(instructionSurf,instructionRect)
        if self.showNavigation == True:
            screen.blit(self.navigation,self.navRect)
        if self.scrollX >-800:
            screen.blit(self.rightArrow,self.rightArrowRect)
        if self.scrollX <800:
            screen.blit(self.leftArrow,self.leftArrowRect)
        screen.blit(self.menuBar,self.menuPos)
        if self.menuExpanded == True:
            screen.blit(self.seasonBar,self.seaPos)
        if self.arrowShow == True:
            screen.blit(self.arrow,self.arrowPos)
        if self.seasonExpanded == True:
            screen.blit(self.spring,self.springPos)
            screen.blit(self.summer,self.summerPos)
            screen.blit(self.autumn,self.autumnPos)
            screen.blit(self.winter,self.winterPos)
            if self.currSeason == 0:
                screen.blit(self.spring1,self.springPos)
            elif self.currSeason == 1:
                screen.blit(self.summer1,self.summerPos)
            elif self.currSeason == 2:
                screen.blit(self.autumn1,self.autumnPos)
            elif self.currSeason == 3:
                screen.blit(self.winter1,self.winterPos)
        if self.currSeason == 3:
            screen.blit(self.makeitsnow,self.makePos)

    def isKeyPressed1(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

##### main scene #2
    def initScene2(self):
        #reset
        Rabbit.rabbits = []
        Bird.birds = []
        
        #rabbit
        #default rabbit
        leftBound = Stone.middleStones[-1][0]- Stone.middleStones[-1][2]
        rightBound = Stone.middleStones[-1][0]+ Stone.middleStones[-1][2]
        x = Stone.middleStones[-1][0]
        y = Stone.middleStones[-1][1]-Stone.middleStones[-1][3]-75
        Rabbit.rabbits.append(Rabbit(leftBound,rightBound,x,y))
        #input generated rabbit
        for rabbit in Rabbit.rabbitData:
            if rabbit[1] <= self.height/3:
                stoneIndex = rabbit[0]%len(Stone.frontStones)
                leftBound = Stone.frontStones[stoneIndex][0]-\
                 Stone.frontStones[stoneIndex][2]
                rightBound = Stone.middleStones[stoneIndex][0]+\
                 Stone.middleStones[stoneIndex][2]
                x = Stone.frontStones[stoneIndex][0]
                y = Stone.frontStones[stoneIndex][1]-Stone.frontStones[stoneIndex][3]-75
                Rabbit.rabbits.append(Rabbit(leftBound,rightBound,x,y))

            elif rabbit[1] <= self.height*2/3:
                stoneIndex = rabbit[0]%len(Stone.middleStones)
                leftBound = Stone.middleStones[stoneIndex][0]-\
                 Stone.middleStones[stoneIndex][2]
                rightBound = Stone.middleStones[stoneIndex][0]+\
                 Stone.middleStones[stoneIndex][2]
                x = Stone.middleStones[stoneIndex][0]
                y = Stone.middleStones[stoneIndex][1]-Stone.middleStones[stoneIndex][3]-75
                Rabbit.rabbits.append(Rabbit(leftBound,rightBound,x,y))
            else:
                stoneIndex = rabbit[0]%len(Stone.backStones)
                leftBound = Stone.backStones[stoneIndex][0]-\
                 Stone.backStones[stoneIndex][2]
                rightBound = Stone.middleStones[stoneIndex][0]+\
                 Stone.middleStones[stoneIndex][2]
                x = Stone.backStones[stoneIndex][0]
                y = Stone.backStones[stoneIndex][1]-Stone.backStones[stoneIndex][3]-75
                Rabbit.rabbits.append(Rabbit(leftBound,rightBound,x,y))

        #bird
        for bird in Bird.birdData:
            try:
                positionList = []
                startIndex = bird[0]%len(Tree.mediumTreeData)
                x1 = Tree.mediumTreeData[startIndex][0]
                y1 = Stone.stoneSurface.get(x1,800)-300
                x2 = Tree.mediumTreeData[startIndex+1][0]
                y2 = Stone.stoneSurface.get(x2,800)-300
                x3 = Tree.mediumTreeData[startIndex-1][0]
                y3 = Stone.stoneSurface.get(x3,800)-300
                x4 = Tree.mediumTreeData[startIndex-2][0]
                y4 = Stone.stoneSurface.get(x4,800)-300
                positionList.append((x1,y1))
                positionList.append((x2,y2))
                positionList.append((x3,y3))
                positionList.append((x4,y4))
                Bird.birds.append(Bird(positionList))
            except: pass
        self.timer = 0
        self.mydrawings = pygame.image.load('menu/mydrawings.png')
        self.mydrawingsPos = (730,20)
        self.snowed = False
        
    def mousePressedScene2(self, x, y,scroll):
        for tree in Tree.mediumTrees:
            treeRect = pygame.Rect(tree.x-tree.size,tree.y-tree.height-tree.size*2,tree.size*2,tree.size*3)
            if treeRect.collidepoint(x-scroll,y)==True:
                if self.currSeason == 0 or self.currSeason == 1:
                    tree.bloomed = not tree.bloomed
                else:
                    tree.leafFell = not tree.leafFell
                tree.generate(tree,Tree.surf,scroll)
        if 1150 < x < 1260 and 20 < y < 70:
            self.menuExpanded = not self.menuExpanded
            self.arrowShow = True
        if self.menuExpanded == True and 960 < x < 1150 and 20<y<70:
            self.seasonExpanded = not self.seasonExpanded
            self.arrowShow = not self.seasonExpanded
        if self.menuExpanded == True and 730 < x < 960 and 20<y<70:
            self.mode = 'gallery'
            self.initG()
        if self.seasonExpanded == True and  960 < x < 1150 and 70<y<120:
            self.currSeason = 0
            self.bgColor = (153,116,113)
            Bridge.seasonIndex = 0
            Stone.seasonIndex = 0
            self.initScene1()
            self.initScene2()
        if self.seasonExpanded == True and  960 < x < 1150 and 120<y<170:
            self.currSeason = 1
            self.bgColor = (61, 94, 83)
            Bridge.seasonIndex = 1
            Stone.seasonIndex = 1
            self.initScene1()
            self.initScene2()
        if self.seasonExpanded == True and  960 < x < 1150 and 170<y<220:
            self.currSeason = 2
            self.bgColor = (216,177,94)
            Bridge.seasonIndex = 2
            Stone.seasonIndex = 2
            self.initScene1()
            self.initScene2()
        if self.seasonExpanded == True and  960 < x < 1150 and 220<y<270:
            self.currSeason = 3
            self.bgColor = (138,200,216) 
            Bridge.seasonIndex = 3
            Stone.seasonIndex = 3
            self.initScene1()
            self.initScene2()
        if self.currSeason == 3 and 20 < x < 255 and 20 < y < 70:
            self.snowed = True

    def mouseReleasedScene2(self, x, y):
        pass

    def mouseMotionScene2(self, x, y):
        pass

    def mouseDragScene2(self, x, y):
        pass

    def keyPressedScene2(self, keyCode, modifier):
        pass
    
    def keyReleasedScene2(self, keyCode, modifier):
        pass

    def timerFiredScene2(self, dt,keysDown):
        if keysDown(pygame.K_RIGHT) and self.scrollX > -800:
            self.scrollX -= 30
        elif keysDown(pygame.K_LEFT) and self.scrollX < 800:
            self.scrollX +=30
        for snowflake in self.snowflakes:
            snowindex = self.snowflakes.index(snowflake)
            newX = snowflake[0]
            newY = (snowflake[1]+self.snowSpeed)%800
            self.snowflakes.pop(snowindex)
            self.snowflakes.insert(snowindex,(newX,newY))
            
    def redrawAllScene2(self, screen):
        LargeTree.generate(LargeTree,screen,self.scrollX)
        Stone.generate(Stone,screen,self.width,self.height,self.scrollX,self.snowed)
        Waterfall.generate(Waterfall,screen,self.scrollX)
        Bush.generate(Bush,screen,self.scrollX)
        for rabbit in Rabbit.rabbits:
            rabbit.draw(screen,self.scrollX)
        Bridge.generate(Bridge,screen,self.scrollX)
        MediumTree.generate(MediumTree,screen,self.scrollX)
        for bird in Bird.birds:
            bird.draw(screen,self.scrollX)
        if self.scrollX >-800:
            screen.blit(self.rightArrow,self.rightArrowRect)
        if self.scrollX <800:
            screen.blit(self.leftArrow,self.leftArrowRect)
        #snow
        if self.snowed == True:
            for snowflake in self.snowflakes:
                screen.blit(self.snowflake,snowflake)
        #bloom instruction
        if self.currSeason == 0 or self.currSeason == 1:
            pixel = pygame.font.Font('Pixeled.ttf',15)
            instructionSurf = pixel.render("CLICK ON TREES TO MAKE THEM BLOOM", True, (255,255,255))
            instructionRect = instructionSurf.get_rect()
            instructionRect.center = (self.width/2,775)
            screen.blit(instructionSurf,instructionRect)
        elif self.currSeason == 2 or self.currSeason == 3:
            pixel = pygame.font.Font('Pixeled.ttf',15)
            instructionSurf = pixel.render("CLICK ON TREES TO MAKE THE LEAVES FALL", True, (255,255,255))
            instructionRect = instructionSurf.get_rect()
            instructionRect.center = (self.width/2,775)
            screen.blit(instructionSurf,instructionRect)
        #menu bar
        screen.blit(self.menuBar,self.menuPos)
        if self.menuExpanded == True:
            screen.blit(self.seasonBar,self.seaPos)
            screen.blit(self.mydrawings,self.mydrawingsPos)

        if self.arrowShow == True:
            screen.blit(self.arrow,self.arrowPos)
        if self.seasonExpanded == True:
            screen.blit(self.spring,self.springPos)
            screen.blit(self.summer,self.summerPos)
            screen.blit(self.autumn,self.autumnPos)
            screen.blit(self.winter,self.winterPos)
            if self.currSeason == 0:
                screen.blit(self.spring1,self.springPos)
            elif self.currSeason == 1:
                screen.blit(self.summer1,self.summerPos)
            elif self.currSeason == 2:
                screen.blit(self.autumn1,self.autumnPos)
            elif self.currSeason == 3:
                screen.blit(self.winter1,self.winterPos)
                screen.blit(self.makeitsnow,self.makePos)
        if self.currSeason == 3:
            screen.blit(self.makeitsnow,self.makePos)

#### Gallery mode
    def initG(self):
        from DrawingTool import DrawingTool
        from DrawingTool2 import DrawingTool2
        self.backButton = pygame.image.load('menu/back.png')
        self.backPos = (1150,20)
        self.drawing1 = pygame.image.load('input.jpg')
        self.drawing2 = pygame.image.load('input2.jpg')
        self.drawing1 = pygame.transform.scale(self.drawing1,(640,400))
        self.drawing2 = pygame.transform.scale(self.drawing2,(640,400))
        self.prompt1 = "'"+ DrawingTool.prompt + "'"
        self.prompt2 = "'"+ DrawingTool2.prompt + "'"
        self.currPic = 0
        self.deco = Rabbit(320,960,self.width/2,140)

    def redrawAllG(self,screen):
        screen.blit(self.backButton,self.backPos)
        self.deco.draw(screen,0)
        if self.currPic == 0:
            screen.blit(self.drawing1,(self.width/2-320,self.height/2-200))
            pixel = pygame.font.Font('Pixeled.ttf',15)
            instructionSurf = pixel.render(self.prompt1, True, (255,255,255))
            instructionRect = instructionSurf.get_rect()
            instructionRect.center = (self.width/2,650)
            screen.blit(instructionSurf,instructionRect)
            screen.blit(self.rightArrow,self.rightArrowRect)
        else:
            screen.blit(self.drawing2,(self.width/2-320,self.height/2-200))
            pixel = pygame.font.Font('Pixeled.ttf',15)
            instructionSurf = pixel.render(self.prompt2, True, (255,255,255))
            instructionRect = instructionSurf.get_rect()
            instructionRect.center = (self.width/2,650)
            screen.blit(instructionSurf,instructionRect)
            screen.blit(self.leftArrow,self.leftArrowRect)
            
        
    def keyPressedG(self,keyCode,modifier):
        if keyCode == pygame.K_RIGHT:
            self.currPic = 1
        elif keyCode == pygame.K_LEFT:
            self.currPic = 0
    
    def mousePressedG(self, x, y,scroll):
        if 1150 < x < 1260 and 20 < y < 70:
            self.mode = 'scene2'

    def mouseReleasedG(self, x, y):
        pass

    def mouseMotionG(self, x, y):
        pass

    def mouseDragG(self, x, y):
        pass

    def keyReleasedG(self, keyCode, modifier):
        pass
    
    def timerFiredG(self,dt,keysDown):
        pass

        
##### Run Framework
    def __init__(self, width=1200, height=800, fps=10, title="Tiny Forest"):
        Thread.__init__(self)
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.mode = "menu"
        self.drawingCount = 0
        self.scrollX = 0
        self.seasons = ['spring','summer','fall','winter']
        self.currSeason = 1
        self.bgColor = (61, 94, 83)
        
        
        pygame.init()

    def run(self):
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time,self.isKeyPressed1)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos),self.scrollX)
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()


def main():
    game = Main()
    game.run()

if __name__ == '__main__':
    main()