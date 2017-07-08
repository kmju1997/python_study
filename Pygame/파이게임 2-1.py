import random
import pygame
from pygame.locals import *

pygame.init()
width,height = 640, 480
screen=pygame.display.set_mode((width,height))

player=pygame.image.load("resource/spacecraft.png")
space=pygame.image.load("resource/space.jpg")
ufo=pygame.image.load("resource/alien.png")
bullet=pygame.image.load("resource/bullet.png")
bullet2=pygame.image.load("resource/bullet2.png")
youwinscreen=pygame.image.load("resource/win.png")
youlosescreen=pygame.image.load("resource/lose.png")
                         
space=pygame.transform.scale(space,(width,height))
font=pygame.font.Font("resource/ARLRDBD.TTF",20)

winmessage=font.render("To continue press X", 1, (74,255,100))
losemessage=font.render("To restart press X", 1, (225,0,0))

gamestate=False

keys = [False,False]

playerpos=[300,380]

bulletpos=[]

ufobulletpos=[]

blockdirectionpos=[[106,270],[480,270]]
ufodirectionpos=[[20,50],[420,50]]

class Platform1():
    def makePlatform(self) : 
        
        self.block = pygame.image.load("resource/block.png")
        self.block = pygame.transform.scale(self.block,(20,20))
        self.blockpos=[]
        for i in range(3):
            self.blockpos.append([i*20,270])
        for i in range(3):
            self.blockpos.append([i*20,290])
        for i in range(3):
            self.blockpos.append([120+(i*20),270])
        for i in range(3):
            self.blockpos.append([120+(i*20),290])
        for i in range(3):
            self.blockpos.append([240+(i*20),270])
        for i in range(3):
            self.blockpos.append([240+(i*20),290])
        for i in range(3):
            self.blockpos.append([360+(i*20),270])
        for i in range(3):
            self.blockpos.append([360+(i*20),290])
        for i in range(3):
            self.blockpos.append([480+(i*20),270])
        for i in range(3):
            self.blockpos.append([480+(i*20),290])
        for i in range(3):
            self.blockpos.append([600+(i*20),270])
        for i in range(3):
            self.blockpos.append([600+(i*20),290])

    def drawPlatform(self):
        for pos in self.blockpos:
            screen.blit(self.block,pos)

    def printPlatform(self):
        print(self.blockpos)


class Platform2():
    def makePlatform(self) : 
        
        self.block = pygame.image.load("resource/block2.png")
        self.block = pygame.transform.scale(self.block,(20,20))
        self.blockpos=[]
        for i in range(3):
            self.blockpos.append([i*20,270])
        for i in range(3):
            self.blockpos.append([i*20,290])
        for i in range(3):
            self.blockpos.append([120+(i*20),270])
        for i in range(3):
            self.blockpos.append([120+(i*20),290])
        for i in range(3):
            self.blockpos.append([240+(i*20),270])
        for i in range(3):
            self.blockpos.append([240+(i*20),290])
        for i in range(3):
            self.blockpos.append([360+(i*20),270])
        for i in range(3):
            self.blockpos.append([360+(i*20),290])
        for i in range(3):
            self.blockpos.append([480+(i*20),270])
        for i in range(3):
            self.blockpos.append([480+(i*20),290])
        for i in range(3):
            self.blockpos.append([600+(i*20),270])
        for i in range(3):
            self.blockpos.append([600+(i*20),290])

    def drawPlatform(self):
        for pos in self.blockpos:
            screen.blit(self.block,pos)

    def printPlatform(self):
        print(self.blockpos)






ufoposlist=[]
for i in range(20, 520, 100):
    for j in range(50, 170, 40):
        ufopos=[i,j]
        ufoposlist.append(ufopos)
        
moveufo='right'
moveblock='left'

number = 0

level = 1

end = 5

n = 800

life = 3

platform1 = Platform1() 
platform1.makePlatform()

platform2 = Platform2()
platform2.makePlatform()

def ufo_display1() :

    for i in range (len(ufoposlist)):
       screen.blit(ufo,ufoposlist[i])
       
pygame.time.set_timer(USEREVENT+1,n)



while  end :

    screen.fill(0)
    screen.blit(space,(0,0))
    ufo_display1()
    
    score= font.render( "Score : %d" % number,1,(255,0,0))
    message=font.render("Level %d" %level, 1,(255,0,0)) 
    lifemessage = font.render("Life %d" %life ,1,(255,0,0))
    
    screen.blit(message,(width/2-30,8))    
    screen.blit(score,(5,450))
    screen.blit(lifemessage, (580,450))
    screen.blit(player,playerpos)

    
    # bullet moving
    
    if not len(bulletpos)==0 :
            for pos in bulletpos:
                screen.blit(bullet,pos)
                pos[1]-=5
                if pos[1]==-5 :
                    bulletpos.remove(pos) 

    if level >= 2:
         if not len(ufobulletpos)==0 :
            for pos in ufobulletpos:
                screen.blit(bullet2,pos)
                pos[1]+=5
                if pos[1]==485 :
                      ufobulletpos.remove(pos)
   
    if level == 4:
        
        platform1.drawPlatform()

    if level == 5:

        platform2.drawPlatform()
    
    if len(ufoposlist) == 0 :
        screen.blit(youwinscreen,(0,0))
        screen.blit(winmessage,(width/2-100,height/2+20))
        gamestate = True
        end-=1
        bulletpos = []
        if level >= 2 : 
            n = n-200

  
    if life == 0 :
        screen.blit(youlosescreen,(0,0))
        screen.blit(losemessage,(width/2-100,height/2+20))   
        gamestate = True
    
    pygame.display.flip()


    # player moving

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
     
    if moveufo=='right':
        for i in range(len(ufoposlist)):
            ufoposlist[i][0]+=2
        ufodirectionpos[0][0]+=2    
        ufodirectionpos[1][0]+=2    
            
    elif moveufo=='left':
        for i in range(len(ufoposlist)):
            ufoposlist[i][0]-=2
        ufodirectionpos[0][0]-=2    
        ufodirectionpos[1][0]-=2    
 
    if ufodirectionpos[0][0]<=20:
            moveufo='right'

    if ufodirectionpos[1][0]>=580:
            moveufo= 'left'

    # block moving
     
    if level ==4:
        if moveblock=='right':
            for i in range(len(platform1.blockpos)):
                platform1.blockpos[i][0]+=2
            blockdirectionpos[0][0]+=2    
            blockdirectionpos[1][0]+=2    
            
        elif moveblock=='left':
            for i in range(len(platform1.blockpos)):
                platform1.blockpos[i][0]-=2
            blockdirectionpos[0][0]-=2    
            blockdirectionpos[1][0]-=2    
 
        if blockdirectionpos[0][0]<=20:
                moveblock='right'

        if blockdirectionpos[1][0]>=580:
                moveblock= 'left'


    if level ==5:
        if moveblock=='right':
            for i in range(len(platform2.blockpos)):
                platform2.blockpos[i][0]+=2
            blockdirectionpos[0][0]+=2    
            blockdirectionpos[1][0]+=2    
            
        elif moveblock=='left':
            for i in range(len(platform2.blockpos)):
                platform2.blockpos[i][0]-=2
            blockdirectionpos[0][0]-=2    
            blockdirectionpos[1][0]-=2    
 
        if blockdirectionpos[0][0]<=20:
                moveblock='right'

        if blockdirectionpos[1][0]>=580:
                moveblock= 'left'







    # remove ufo

    for i in ufoposlist :
       for j in bulletpos :
           if i[1]<=j[1] and i[1]+28 >= j[1] and i[0]<=j[0] and i[0]+28 >= j[0]:
                ufoposlist.remove(i)
                bulletpos.remove(j)
                number+=1
                
    # remove life

    for i in ufobulletpos :     
        if i[0] >= playerpos[0] and i[0] <= playerpos[0]+60 and i[1]+24 >= playerpos[1] and i[1]+24 <= playerpos[1]+60:
                ufobulletpos.remove(i)
                life-=1

    #remove bullet
    if level == 4:
        for i in platform1.blockpos :
            for j in bulletpos :
                if i[1]<=j[1] and i[1]+20 >= j[1] and i[0]<=j[0] and i[0]+20 >= j[0]:
                        bulletpos.remove(j)
                        platform1.blockpos.remove(i)

    if level ==5:
        for i in platform2.blockpos :
            for j in bulletpos :
                if i[1]<=j[1] and i[1]+20 >= j[1] and i[0]<=j[0] and i[0]+20 >= j[0]:
                        bulletpos.remove(j)
                        
  
                
    for event in pygame.event.get():
            
        if event.type==pygame.KEYDOWN:
    
            if event.key==K_a:
               keys[0]=True
            elif event.key==K_d:
                keys[1]=True

            if len(bulletpos) < 4:     
                if event.key==K_m:
                    bulletpos.append([playerpos[0]+28,playerpos[1]])

            if event.key==K_x:
                gamestate = False
             
        if event.type == pygame.KEYUP:
            
            if event.key==pygame.K_a:
                keys[0]=False
            elif event.key==pygame.K_d:
                keys[1]=False

        if level >= 2 :    
            if event.type == USEREVENT+1:
                if len(ufoposlist) > 0:
                    rannum = random.randint(0,len(ufoposlist)-1)
                    ufobulletx = ufoposlist[rannum][0]
                    ufobullety = ufoposlist[rannum][1]
                    ufobullet = [ufobulletx+13, ufobullety+28]
                    ufobulletpos.append(ufobullet)
        

        if event.type == QUIT:
            break

        
    while gamestate:
        
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:

                if event.key==K_x:
                    if life == 0 :
                        ufoposlist.clear()
                        for i in range(20, 520, 100):
                            for j in range(50, 170, 40):
                                ufopos=[i,j]
                                ufoposlist.append(ufopos)

                        ufodirectionpos=[[20,50],[420,50]]
                        number = 0
                        life = 3
                        level = 1
                        gamestate = False
                    else :
                        for i in range(20, 520, 100):
                            for j in range(50, 170, 40):
                                ufopos=[i,j]
                                ufoposlist.append(ufopos)
                            
                        ufodirectionpos=[[20,50],[420,50]]
                        level+=1
                        gamestate=False

    
        if event.type==pygame.QUIT:
             pygame.quit()
             exit(0)
                    
                        
