import random
import pygame
from pygame.locals import *

pygame.init()
screenwidth,screenheight= 640,480
width,height=1000,480

keys=[False,False]
knifepos=[0,0]
bulletpos=[]
boompos=[]
firepos=[]

screen=pygame.display.set_mode((screenwidth,screenheight))

knife = pygame.image.load("image/knife2.png")
bullet = pygame.image.load("image/bullet.png")
bullet = pygame.transform.scale(bullet,(20,10))
boom = pygame.image.load("image/boom.png")
boom = pygame.transform.scale(boom,(30,30))
fire = pygame.image.load("image/fire2.png")
fire = pygame.transform.scale(fire,(50,30))
fire1 = pygame.image.load("image/fire1.png")
fire1 = pygame.transform.scale(fire1,(50,30))

font=pygame.font.Font("image/ARLRDBD.TTF",20)
effect = pygame.image.load("image/effect.png")
pygame.time.set_timer(USEREVENT+1,800)

gameoverScreen = pygame.image.load("image/gameover.png")
youwinScreen = pygame.image.load("image/youwin.png")

def youwin():
    winfont=pygame.font.Font(None,25)

    screen.blit(youwinScreen,(0,0))
    
    pygame.display.update()
    while 1:
        pass
    
def gameover():
    
    losefont=pygame.font.Font(None,25)
    
    screen.blit(gameoverScreen,(0,0))
    
    pygame.display.update()
    while 1:
        pass
    
class startgame():
    def __init__(self):
        self.s_width=640
        self.s_height=480
        self.startscreen=pygame.image.load("image/startmenu.png")
        self.startscreen=pygame.transform.scale(self.startscreen,(self.s_width,self.s_height))
        self.startmessage=pygame.image.load("image/startmessage.png")
        self.startmessage=pygame.transform.scale(self.startmessage,(80,40))
        self.controlmessage=pygame.image.load("image/controlmessage.png")
        self.controlmessage=pygame.transform.scale(self.controlmessage,(80,40))
        self.arrow=pygame.image.load("image/arrow.png")
        self.arrow=pygame.transform.scale(self.arrow,(30,30))
        self.arrowpos=[self.s_width/2-70,self.s_height/2]
        self.c_select=True
        self.char1=pygame.image.load("image/An.png")
        self.char1=pygame.transform.scale(self.char1,(100,150))
        self.char2=pygame.image.load("image/Yoon.png")
        self.char2=pygame.transform.scale(self.char2,(100,150))
        self.char3=pygame.image.load("image/264.png")
        self.char3=pygame.transform.scale(self.char3,(100,150))
        self.char4=pygame.image.load("image/Kim.png")
        self.char4=pygame.transform.scale(self.char4,(100,150))

        self.arrow2=pygame.image.load("image/arrow2.png")
        self.arrow2=pygame.transform.scale(self.arrow2,(30,30))
        self.selection=[[85,self.s_height/2-30],[235,self.s_height/2-30],[385,self.s_height/2-30],[535,self.s_height/2-30]]
        self.arrowcount=0
        self.play=False

    def startmenu(self):
        while 1:
        
            screen.blit(self.startscreen,(0,0))
            if self.c_select==False:
                screen.blit(self.startmessage,(self.s_width/2-40,self.s_height/2))
##                screen.blit(self.controlmessage,(self.s_width/2-40,self.s_height/2+40))
                screen.blit(self.arrow,self.arrowpos)

            
            if self.c_select==True:
                screen.blit(self.char1,(50,self.s_height/2))
                screen.blit(self.char2,(200,self.s_height/2))
                screen.blit(self.char3,(350,self.s_height/2))
                screen.blit(self.char4,(500,self.s_height/2))
                screen.blit(self.arrow2,self.selection[self.arrowcount])
            
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit(0)
            if event.type==pygame.KEYDOWN:
                if event.key==K_UP:
                  self.arrowpos=[self.s_width/2-70,self.s_height/2]
                if event.key==K_DOWN:
                  self.arrowpos=[self.s_width/2-70,self.s_height/2+40]
##                if event.key==K_SPACE and self.arrowpos[0]==self.s_width/2-70:
##                    self.c_select=True
                if event.key==K_RIGHT:
                    self.arrowcount+=1
                    pygame.time.delay(200)
                    if self.arrowcount==4:
                        self.arrowcount=0
                if event.key==K_LEFT:
                    self.arrowcount-=1
                    pygame.time.delay(200)
                    if self.arrowcount==-1:
                         self.arrowcount=3
                if event.key==K_SPACE and self.arrowcount==0 and self.c_select==True:
                    self.play=True
                    return self.char1
                    break
                if event.key==K_SPACE and self.arrowcount==1:
                    self.play=True
                    return self.char2
                    break
                if event.key==K_SPACE and self.arrowcount==2:
                    self.play=True
                    return self.char3
                    break
                if event.key==K_SPACE and self.arrowcount==3:
                    self.play=True
                    return self.char4
                    break


                
                
class background():
    def __init__(self):
        self.backpos=[0,0]
        self.level1_back = pygame.image.load("image/level3.jpg")
        self.level1_back = pygame.transform.scale(self.level1_back,(width,height))
        self.life=font.render("Life : %d" % player.life, 1, (255,0,0))
        self.lifepos = [20, 20]
class player():
    def __init__(self,selection):
        self.playerpos=[0,height-100]            
        self.life = 200
        self.player1 = selection
        self.player1 = pygame.transform.scale(selection,(60,90))
        self.jump = False
        self.peak = False
        self.u_dir = 1
        
    def player_jump(self):
        if player.jump:
            if not player.peak:
                player.playerpos[1]-=5
                if player.playerpos[1]<height-100-150:
                    player.peak=True
            if player.peak:
                player.playerpos[1]+=5
                if player.playerpos[1]==height-100:
                    player.peak=False
                    player.jump=False

class enemy():
    def __init__(self):
        self.enebulletpos=[]
        self.lifenum = 100
        self.rannum = random.randint(0,640) 
        self.enemypos=[self.rannum,height-100]
        self.life=font.render("%d" % self.lifenum, 1, (255,0,0))
        self.lifepos = [self.rannum+20, height-120]
        self.enemy1 = pygame.image.load("image/enemy.png")
        self.enemy1 = pygame.transform.scale(self.enemy1,(80,80))
        self.enemy2 = pygame.image.load("image/enemy2.png")
        self.enemy2 = pygame.transform.scale(self.enemy2,(80,80))
        self.direction = 'left'
gamestart = startgame()

selection=gamestart.startmenu()

player = player(selection)
back = background()
enemies = [enemy(), enemy()]


while gamestart.play:

    screen.blit(back.level1_back,back.backpos)  
    screen.blit(player.player1,player.playerpos)
    screen.blit(back.life, back.lifepos)
      
    player.player_jump()                               

    if gamestart.arrowcount == 0:
        if not len(bulletpos) == 0 :
            for pos in bulletpos:
                screen.blit(bullet, pos)
                if player.u_dir == 1:
                    pos[0] += 5
                    distance += 3
                elif player.u_dir == 0:
                    pos[0] -= 5
                    distance += 3
                if distance >= 100:
                    bulletpos.remove(pos)

    elif gamestart.arrowcount == 1:
        if not len(boompos) == 0 :
            for pos in boompos:
                screen.blit(boom, pos)
                if player.u_dir == 1:
                    pos[0] += 5
                    distance += 3
                elif player.u_dir == 0:
                    pos[0] -= 5
                    distance += 3
                if distance >= 100:
                    boompos.remove(pos)
                    
    elif gamestart.arrowcount == 3:
        if not len(firepos) == 0 :
            for pos in firepos:
                if player.u_dir == 1:
                    screen.blit(fire, pos)
                elif player.u_dir == 0:
                    screen.blit(fire1, pos)
                if player.u_dir == 1:
                    pos[0] += 5
                    distance += 3
                elif player.u_dir == 0:
                    pos[0] -= 5
                    distance += 3
                if distance >= 100:
                    firepos.remove(pos)
    
    for enemy in enemies:
        if not len(enemy.enebulletpos) == 0 :
            for pos in enemy.enebulletpos:
                screen.blit(bullet, pos)
                if enemy.direction == 'right':
                    pos[0] += 5
                    enedistance += 5
                elif enemy.direction == 'left':
                    pos[0] -= 5
                    enedistance += 5
            if enedistance >= 300:
                enemy.enebulletpos.remove(pos)
                
    for enemy in enemies:
        for pos in bulletpos:
            if enemy.enemypos[0] <= pos[0] and enemy.enemypos[0]+80 >= pos[0] and enemy.enemypos[1] <= pos[1] and enemy.enemypos[1]+80 >= pos[1]:
                    screen.blit(effect,enemy.enemypos)
                    bulletpos.remove(pos)
                    enemy.lifenum -=20
                    enemy.life=font.render("%d" % enemy.lifenum, 1, (255,0,0))
                    
        for pos in boompos:
            if enemy.enemypos[0] <= pos[0] and enemy.enemypos[0]+80 >= pos[0] and enemy.enemypos[1] <= pos[1] and enemy.enemypos[1]+80 >= pos[1]:
                    screen.blit(effect,enemy.enemypos)
                    boompos.remove(pos)
                    enemy.lifenum -=20
                    enemy.life=font.render("%d" % enemy.lifenum, 1, (255,0,0))

        for pos in firepos:
            if enemy.enemypos[0] <= pos[0] and enemy.enemypos[0]+80 >= pos[0] and enemy.enemypos[1] <= pos[1] and enemy.enemypos[1]+80 >= pos[1]:
                    screen.blit(effect,enemy.enemypos)
                    firepos.remove(pos)
                    enemy.lifenum -=20
                    enemy.life=font.render("%d" % enemy.lifenum, 1, (255,0,0))
                    
        if enemy.lifenum == 0:
            enemies.remove(enemy)

    for enemy in enemies:
        for pos in enemy.enebulletpos:
            if player.playerpos[0] <= pos[0] and player.playerpos[0]+80 >= pos[0] and player.playerpos[1] <= pos[1] and player.playerpos[1]+80 >= pos[1]:
                    screen.blit(effect,player.playerpos)
                    enemy.enebulletpos.remove(pos)
                    player.life -=20
                    back.life=font.render("Life: %d" % player.life, 1, (255,0,0))
        if enemy.lifenum == 0:
            enemies.remove(enemy)    

    for enemy in enemies:
        if enemy.direction == 'left':
            screen.blit(enemy.enemy1,enemy.enemypos)
            screen.blit(enemy.life,enemy.lifepos)
            enemy.enemypos[0] -= 3
            enemy.lifepos[0] -=3
        if enemy.enemypos[0] < 10:
            enemy.direction = 'right'
        if enemy.direction == 'right':
            screen.blit(enemy.enemy2,enemy.enemypos)
            screen.blit(enemy.life,enemy.lifepos)
            enemy.enemypos[0] += 3
            enemy.lifepos[0]+=3
        if enemy.enemypos[0] > 570:
            enemy.direction = 'left'
    
##    if player.playerpos[0]>570 and len(enemies)==0:
##        
##        player.playerpos=[0,screenheight-100]
##        player.life=200
    if player.life==0:
        gameover()
    if player.playerpos[0]>570 and len(enemies)==0:
        youwin()
        

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
                distance = 0
                
                if gamestart.arrowcount == 0:
                    if player.u_dir == 0:
                        player.player1 = pygame.image.load("image/An4.png")
                        player.player1 = pygame.transform.scale(player.player1,(80,90))
                        screen.blit(player.player1, player.playerpos)
                        bulletpos.append([player.playerpos[0]-5, player.playerpos[1]+40])
                    else:
                        player.player1 = pygame.image.load("image/An2.png")
                        player.player1 = pygame.transform.scale(player.player1,(80,90))
                        screen.blit(player.player1, player.playerpos)
                        bulletpos.append([player.playerpos[0]+45, player.playerpos[1]+40])
                
                elif gamestart.arrowcount == 1:

                    if player.u_dir == 0:
                        player.player1 = pygame.image.load("image/Yoon4.png")
                        player.player1 = pygame.transform.scale(player.player1,(60,90))
                        screen.blit(player.player1, player.playerpos)
                        boompos.append([player.playerpos[0]-5, player.playerpos[1]+40])
                    else:
                        player.player1 = pygame.image.load("image/Yoon2.png")
                        player.player1 = pygame.transform.scale(player.player1,(60,90))
                        screen.blit(player.player1, player.playerpos)
                        boompos.append([player.playerpos[0]+45, player.playerpos[1]+40])
                
                    
                elif gamestart.arrowcount == 2:                    
                    if player.u_dir == 0:
                        player.player1 = pygame.image.load("image/2644.png")
                        player.player1 = pygame.transform.scale(player.player1,(80,90))
                        screen.blit(player.player1, player.playerpos)
                        
                    else:
                        player.player1 = pygame.image.load("image/2642.png")
                        player.player1 = pygame.transform.scale(player.player1,(80,90))
                        screen.blit(player.player1, player.playerpos)
                
                elif gamestart.arrowcount == 3:
                    if player.u_dir == 0:
                        player.player1 = pygame.image.load("image/Kim4.png")
                        player.player1 = pygame.transform.scale(player.player1,(80,90))
                        screen.blit(player.player1, player.playerpos)
                        firepos.append([player.playerpos[0]-5, player.playerpos[1]+40])
                    else:
                        player.player1 = pygame.image.load("image/Kim2.png")
                        player.player1 = pygame.transform.scale(player.player1,(80,90))
                        screen.blit(player.player1, player.playerpos)
                        firepos.append([player.playerpos[0]+45, player.playerpos[1]+40])    
                
            elif event.key==K_UP:
                player.jump=True
                
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                keys[0]=False
               
            elif event.key==pygame.K_RIGHT:
                keys[1]=False
                               
            elif event.key == K_x:
                
                if gamestart.arrowcount == 0:
                    if player.u_dir == 0:
                        player.player1 = pygame.image.load("image/An.png")
                        player.player1 = pygame.transform.scale(player.player1,(60,90))
                    else:
                        player.player1 = pygame.image.load("image/An3.png")
                        player.player1 = pygame.transform.scale(player.player1,(60,90))
                elif gamestart.arrowcount == 1:
                    if player.u_dir == 0:
                        player.player1 = pygame.image.load("image/Yoon.png")
                        player.player1 = pygame.transform.scale(player.player1,(60,90))
                    else:
                        player.player1 = pygame.image.load("image/Yoon3.png")
                        player.player1 = pygame.transform.scale(player.player1,(60,90))
                elif gamestart.arrowcount == 2:
                    if player.u_dir == 0:
                        player.player1 = pygame.image.load("image/264.png")
                        player.player1 = pygame.transform.scale(player.player1,(60,90))
                    else:
                        player.player1 = pygame.image.load("image/2643.png")
                        player.player1 = pygame.transform.scale(player.player1,(60,90))
                elif gamestart.arrowcount == 3:
                    if player.u_dir == 0:
                        player.player1 = pygame.image.load("image/Kim.png")
                        player.player1 = pygame.transform.scale(player.player1,(60,90))
                    else:
                        player.player1 = pygame.image.load("image/Kim3.png")
                        player.player1 = pygame.transform.scale(player.player1,(60,90))

        if event.type == USEREVENT+1:
            
             if len(enemies) > 0:
                    enedistance = 0 
                    rannum = random.randint(0,len(enemies)-1)
                    enebulletx = enemies[rannum].enemypos[0]
                    enebullety = enemies[rannum].enemypos[1]
                    enebullet = [enebulletx, enebullety+55]
                    enemies[rannum].enebulletpos.append(enebullet)           

    if keys[0]:
        player.playerpos[0]-=2
        back.backpos[0]+=1
        player.u_dir=0
    elif keys[1]:
        player.playerpos[0]+=2
        back.backpos[0]-=1
        player.u_dir=1
        
    if player.playerpos[0]<0:
        keys[0]=False
    elif player.playerpos[0]>570:
        keys[1]=False
