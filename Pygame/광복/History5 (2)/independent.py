import pygame
from pygame.locals import *

pygame.init()
screenwidth,screenheight= 640,480
width,height=1000,480

keys=[False,False]
knifepos=[0,0]
bulletpos=[]

screen=pygame.display.set_mode((screenwidth,screenheight))

knife = pygame.image.load("image/knife2.png")
bullet = pygame.image.load("image/bullet.png")
effect = pygame.image.load("image/effect.png")

class background():
    def __init__(self):
        self.backpos=[0,0]
        self.level1_back = pygame.image.load("image/level3.jpg")
        self.level1_back = pygame.transform.scale(self.level1_back,(width,height))
class player():
    def __init__(self):
        self.playerpos=[5,height-100]
        self.player = pygame.image.load("image/An.png")
        self.player = pygame.transform.scale(self.player,(40,90))
        self.jump = False
        self.peak = False
        
    def player_jump(self):
        if player.jump:
            if not player.peak:
                player.playerpos[1]-=3
                if player.playerpos[1]<height-100-150:
                    player.peak=True
            if player.peak:
                player.playerpos[1]+=3
                if player.playerpos[1]==height-100:
                    player.peak=False
                    player.jump=False

class enemy():
    def __init__(self):
        self.enemypos=[550,height-100]
        self.enemy1 = pygame.image.load("image/enemy.png")
        self.enemy1 = pygame.transform.scale(self.enemy1,(80,80))
        self.enemy2 = pygame.image.load("image/enemy2.png")
        self.enemy2 = pygame.transform.scale(self.enemy2,(80,80))


    
back = background()
player = player()
enemy = enemy()
direction = 'left'

while 1:

    screen.blit(back.level1_back,back.backpos)
        
    screen.blit(player.player,player.playerpos)

    player.player_jump()                               

    if direction == 'left':
        screen.blit(enemy.enemy1,enemy.enemypos)
        enemy.enemypos[0] -= 3
    if enemy.enemypos[0] < 10:
        direction = 'right'
    if direction == 'right':
        screen.blit(enemy.enemy2,enemy.enemypos)
        enemy.enemypos[0] += 3
    if enemy.enemypos[0] > 570:
        direction = 'left'
 

    if not len(bulletpos) == 0 :
        for pos in bulletpos:
            screen.blit(bullet, pos)
            pos[0] += 3
            distance += 3
            if distance >= 100:
                bulletpos.remove(pos)


    
        for pos in bulletpos:
                if enemy.enemypos[0] <= pos[0] or enemy.enemypos[0]+80 >= pos[0]:
                    screen.blit(effect,enemy.enemypos)
                    bulletpos.remove(pos)
                       
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_LEFT:
                if player.playerpos[0]>0:
                    keys[0]=True
                    
            elif event.key==K_RIGHT:
                keys[1]=True
                
            elif event.key==K_x:
                player.player = pygame.image.load("image/An2.png")
                player.player = pygame.transform.scale(player.player,(60,90))
                distance = 0
                screen.blit(player.player, player.playerpos)
                bulletpos.append([player.playerpos[0]+45, player.playerpos[1]+40])
                
            elif event.key==K_UP:
                player.jump=True
                
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                keys[0]=False
            elif event.key==pygame.K_RIGHT:
                keys[1]=False
            elif event.key == K_x:
                player.player = pygame.image.load("image/An.png")
                player.player = pygame.transform.scale(player.player,(40,90))
    

    if keys[0]:
        player.playerpos[0]-=2
        back.backpos[0]+=1
    elif keys[1]:
        player.playerpos[0]+=2
        back.backpos[0]-=1

    if player.playerpos[0]<0:
        keys[0]=False
    elif player.playerpos[0]>570:
        keys[1]=False
