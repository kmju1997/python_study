import pygame
from pygame.locals import *

pygame.init()
width,height = 640,480
keys=[False,False]
playerpos=[5,height-100]
knifepos=[0,0]
bulletpos=[]

screen=pygame.display.set_mode((width,height))

manjoo = pygame.image.load("image/manjoo.jpg")
ha = pygame.image.load("image/kyungsung.png")
last = pygame.image.load("image/level3.jpg")
knife = pygame.image.load("image/knife2.png")
bullet = pygame.image.load("image/bullet.png")

An = pygame.image.load("image/An.png")
#Lee = pygame.image.load("image/264.png")
#Yoon = pygame.image.load("image/Yoon.png")
#Kim = pygame.image.load("image/Kim.png")

player = An


manjoo = pygame.transform.scale(manjoo,(width,height))
player = pygame.transform.scale(player,(40,90))

while 1:
    screen.fill(0)
    screen.blit(manjoo,(0,0))
    screen.blit(player,playerpos)
    
    if not len(bulletpos) == 0 :
        for pos in bulletpos:
            screen.blit(bullet, pos)
            pos[0] += 3
            distance += 3
            if distance >= 100:
                bulletpos.remove(pos)
                   
    
    pygame.display.flip()
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_LEFT:
                keys[0]=True
            elif event.key==K_RIGHT:
                keys[1]=True
            elif event.key==K_x:
                player = pygame.image.load("image/An2.png")
                player = pygame.transform.scale(player,(60,90))
                distance = 0
                screen.blit(player, playerpos)
                bulletpos.append([playerpos[0]+45, playerpos[1]+40])                
                
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                keys[0]=False
            elif event.key==pygame.K_RIGHT:
                keys[1]=False
            elif event.key == K_x:
                player = pygame.image.load("image/An.png")
                player = pygame.transform.scale(player,(40,90))
    
    if keys[0]:
        playerpos[0]-=5
    elif keys[1]:
        playerpos[0]+=5
