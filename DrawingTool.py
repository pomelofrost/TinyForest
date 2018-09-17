import pygame,sys
from pygame.locals import *
import random
import __init__

#Inspired by
#https://www.cs.iupui.edu/~aharris/pygame/ch05/paint.py
###


pygame.init()

screen = pygame.display.set_mode ((1280,800))
drawArea = screen.subsurface(pygame.Rect(0,0,1280,750))
screen.fill ((255,255,255))

pygame.display.update()
clock = pygame.time.Clock()

lineWidth = 2
lineStart = (0,0)
drawColor = (0,0,0)
drawing = True

prompt = random.choice (['YOUR FIRST MEMORY','YOUR DREAM PET',\
'YOUR HOMETOWN','YOUR BEST FRIEND','YOUR DREAM VACATION','YOUR FAVORITE SWEATER',\
'IMPRESSION OF YOUR FATHER','UNDERWATER WRESTLING','A TOY DINOSAUR',\
'ANTARCTICA','ALIGATOR DANCING'])

class DrawingTool(object):
    prompt = prompt

while drawing:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
        #drawing function
        elif event.type == pygame.MOUSEMOTION:
            lineEnd = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed() == (1, 0, 0):
                pygame.draw.line(drawArea, drawColor, lineStart, lineEnd, lineWidth)
            lineStart = lineEnd

    # DONE button
    buttonPos = (1200,760)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    onHoverFont = pygame.font.Font('Pixeled.ttf',15)
    #on hover
    if 1180 < mouse[0] < 1220 and 740 < mouse[1] < 780:
        TextSurf = onHoverFont.render('DONE', True, (0,0,0))
        TextRect = TextSurf.get_rect()
        TextRect.center = buttonPos
        #clicked
        if click[0] == 1 and lineStart != (0,0):
            #save image
            screen.blit(screen,(0,0))
            pygame.image.save(drawArea,'input.jpg')
            drawing = False
    #not on hover
    else:
        TextSurf = onHoverFont.render('DONE',True, (0,0,0))
        TextRect = TextSurf.get_rect()
        TextRect.center = buttonPos
    QuestionSurf = onHoverFont.render(prompt, True, (0,0,0))
    QuestionRect = QuestionSurf.get_rect()
    screen.blit (TextSurf,TextRect)
    QuestionRect.center = (200,760)
    
    screen.blit(QuestionSurf,QuestionRect)

    pygame.display.flip()
