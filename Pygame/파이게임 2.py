import pygame
from pygame.locals import *

pygame.init()
width,height = 640, 480
screen=pygame.display.set_mode((width,height))

player=pygame.image.load("resource/spacecraft.png")
space=pygame.image.load("resource/space.jpg")
ufo=pygame.image.load("resource/alien.png")
bullet=pygame.image.load("resource/bullet3.png")

space=pygame.transform.scale(space,(width,height))

font=pygame.font.Font("resource/ARLRDBD.TTF",30)

message=font.render("Level 1", 1,(255,0,0)) 

keys = [False,False]
playerpos=[300,380]
bulletpos=[]
move='left'

ufoposlist=[]
for i in range(20, 520, 100):
    for j in range(50, 170, 40):
        ufopos=[i,j]
        ufoposlist.append(ufopos)
        
move='right'

def ufo_display1() :
    for i in range (15):
        screen.blit(ufo,ufoposlist[i])
    

while 1:


    screen.fill(0)
    screen.blit(space,(0,0))
    ufo_display1() 
    screen.blit(message,(width/2-40,8))
    
    if not len(bulletpos)==0 :
            for pos in bulletpos:
                screen.blit(bullet,pos)
                pos[1]-=10
                if pos[1]==-10 :
                    bulletpos.remove(pos)
                
    screen.blit(player,playerpos)
    pygame.display.flip()

    if keys[0]:
        playerpos[0]-=5
        if playerpos[0]==20 :
                playerpos[0]+=5
        if playerpos[0]==22 :
                playerpos[0]+=5
        
    elif keys[1]:
        playerpos[0]+=5
        if playerpos[0]==560 :
             playerpos[0]-=5 
        if playerpos[0]==582 :
             playerpos[0]-=5

     # ufo moving
     
    if move=='right':
        for i in range(15):
            ufoposlist[i][0]+=1
        if ufoposlist[12][0]>=600:
            move='left'
            
    elif move=='left':
        for i in range(15):
            ufoposlist[i][0]-=1
        if ufoposlist[1][0]<=20:
            move='right'


    for event in pygame.event.get():
        
        if event.type==pygame.KEYDOWN:
    
            if event.key==K_a:
                keys[0]=True
            elif event.key==K_d:
                keys[1]=True
            elif event.key==K_m:
                bulletpos.append([playerpos[0]+28,playerpos[1]])    
        if event.type == pygame.KEYUP:

            if event.key==pygame.K_a:
                keys[0]=False
            elif event.key==pygame.K_d:
                keys[1]=False
           

        if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
                    
                        
