# 1 - Import library
import pygame
from pygame.locals import *
from math import floor
import random
 
pygame.init()
width, height = 640, 480
score=0
screen=pygame.display.set_mode((width, height))

# 2 - Initialize the game

pygame.init()
width, height = 640, 480
score=0
level=3
life=3
screen=pygame.display.set_mode((width, height))
font = pygame.font.Font('resources/ARLRDBD.TTF',25)
pygame.time.set_timer(USEREVENT+1,100)
# 과제
alienN=15

badguypos=[ [0 for content in range(2)] for index in range(alienN)]

for i in range(15):
    badguypos[i][0] = 10 + 100 * (i - (floor(i/5) * 5))
    badguypos[i][1] = 10 + 40 * floor(i/5)

alien_live=[True for alien in range(alienN)]

keys = [False, False]

move = True
bulletpos=[]
abulletpos=[]

# 3 - Load images
#player = pygame.image.load("resources/images/spacecraft.png")
space = pygame.image.load("resources/images/space.jpg")
badguy = pygame.image.load("resources/images/alien.png")
bullet = pygame.image.load("resources/images/bullet.png")
gameoverScreen = pygame.image.load("resources/images/gameover.png")
youwinScreen = pygame.image.load("resources/images/youwin.png")
abullet = pygame.image.load("resources/images/abullet.png")

space = pygame.transform.scale(space,(width,height))
bullet = pygame.transform.scale(bullet,(5,20))
abullet = pygame.transform.scale(bullet,(5,5))
badguy = pygame.transform.scale(badguy,(30,30))

gamestate= {'win':False,'gameover':False}

def youwin():

    winfont=pygame.font.Font(None,25)
    winmessage = winfont.render("To continue press x",1,(74,255,100))
    screen.blit(youwinScreen,(0,0))
    screen.blit(winmessage,(width/2-60,height/2))
    
    pygame.display.update()
    while gamestate['win']:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==K_x:
                    gamestate['win']=False
def gameover():
    
    losefont=pygame.font.Font(None,25)
    losemessage = losefont.render("To continue press x",1,(255,0,0))
    screen.blit(gameoverScreen,(0,0))
    screen.blit(losemessage,(width/2-60,height/2))
    
    pygame.display.update()
    while gamestate['gameover']:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==K_x:
                    gamestate['gameover']=False

class Platform():
    def __init__(self):
        self.block = pygame.image.load("resources/images/block.png")
        self.block = pygame.transform.scale(self.block,(10,10))
        self.blockpos=[]
        self.blockHit=[False for i in range(30)]
        for i in range(5):
            self.blockpos.append([106+(i*10),320])
        for i in range(5):
            self.blockpos.append([280+(i*10),320])
        for i in range(5):        
            self.blockpos.append([280+(i*10),330])
        for i in range(5):    
            self.blockpos.append([106+(i*10),330])
        for i in range(5):
            self.blockpos.append([454+(i*10),320])
        for i in range(5):
            self.blockpos.append([454+(i*10),330])
    def drawPlatform(self):
        for pos in self.blockpos:
            screen.blit(self.block,pos)
    

platform=Platform()
# 4 - keep looping through

running = 1
exitcode = 0

class Spaceship():
    def __init__(self):
        self.player = pygame.image.load("resources/images/spacecraft.png")
        self.playerpos=[width/2,height-80]

player=Spaceship()
player.player = pygame.transform.scale(player.player,(50,50))
while running:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    screen.blit(space,(0,0))

    message = font.render("Level %d" %level,1,(255,0,0))
    screen.blit(message,(0,height-20))
    scoremessage = font.render("score %d" %score,1,(255,0,0))
    screen.blit(scoremessage,(80,height-20))
    lifemessage = font.render("life %d" %life,1,(255,0,0))
    screen.blit(lifemessage,(180,height-20))
    
    # 6 - draw the screen element    
    screen.blit(player.player, player.playerpos)
    
    # 6.1 - move alien
    if move:
        for i,j in enumerate(alien_live):
            if j:
                badguypos[i][0]+=1 
    if not move:
        for i,j in enumerate(alien_live):
            if j:
                badguypos[i][0]-=1

    for i in badguypos:
        if i[0] > width-50:
            move = False
        if i[0] < 0:
            move = True
        
    # 6.1 - draw alien
    for i,alive in enumerate(alien_live):
        if alive:
            screen.blit(badguy,badguypos[i])

    ###############Platform
    
    # 6.2 - shoot bullet
    if not len(bulletpos)==0:
        for pos in bulletpos:
            pos[1] -= 5
            #6.2.1 - kill alien
            for i,hit in enumerate(badguypos):
                if (pos[0]>=hit[0] and pos[0]<=hit[0]+20) and (pos[1]>=hit[1] and pos[1]<=hit[1]+30):
                    bulletpos.remove(pos)
                    alien_live[i]=False
                    hit[0]=0
                    hit[1]=height
                    score += 1
            if pos[1]<0:
                bulletpos.remove(pos)
                
    if level==2 or level==3:
        if not len(abulletpos)==0:
            for pos in abulletpos:
                if level==2:
                    pos[1]+=3
                elif level==3:
                    pos[1]+=6
                
                if (pos[0]>=player.playerpos[0] and pos[0]<=player.playerpos[0]+45 and pos[1]>=player.playerpos[1]-5 and pos[1]<=player.playerpos[1]+45):
                    abulletpos.remove(pos)
                    life -= 1
                    pygame.time.delay(100)
                if pos[1]<=0:
                    abulletpos.remove(pos)
                if level==3:                    
                    for block in platform.blockpos:
                        if (pos[0]>=block[0] and pos[0]<=block[0]+10 and pos[1]>=block[1]):
                            
                            abulletpos.remove(pos)
                            platform.blockpos.remove(block)
                            
                        
    # 6.3 - draw bullet
    if not len(bulletpos)==0:
        for pos in bulletpos:
           screen.blit(bullet,pos)
    # 6.4 - draw alien bullet
    if level==2 or level==3:
        if not len(abulletpos)==0:
            for pos in abulletpos:
                screen.blit(abullet,pos)
                
    if level==3:
        platform.drawPlatform()    
    
    # 7 - update the screen
    pygame.display.flip()
    
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_a:
                keys[0]=True
            elif event.key==K_d:
                keys[1]=True
            elif event.key == K_w:
                bulletpos.append([player.playerpos[0],player.playerpos[1]])
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_a:
                keys[0]=False
            elif event.key==pygame.K_d:
                keys[1]=False
        #timer
        if event.type == USEREVENT+1:
            randomN=random.choice(badguypos)        
            abulletpos.append([randomN[0],randomN[1]])
        if event.type == QUIT:
            break
        
    if keys[0]:
        player.playerpos[0]-=5
    elif keys[1]:
        player.playerpos[0]+=5

    if player.playerpos[0]>width-60:
        keys[1]=False
    elif player.playerpos[0]<2:
        keys[0]=False
    #You win!
    if score==15 :
        gamestate['win']=True
        youwin()
        for i in range(alienN):
            alien_live[i]=True
        score=0
        level+=1
        life=3
        bulletpos=[]
        abulletpos=[]
        for i in range(15):
            badguypos[i][0] = 10 + 100 * (i - (floor(i/5) * 5))
            badguypos[i][1] = 10 + 40 * floor(i/5)
        
    #Game Over!
    if life == 0:
        gamestate['gameover']=True
        gameover()
        for i in range(alienN):
            alien_live[i]=True
        score=0
        
        level=1
        bulletpos=[]
        abulletpos=[]
        for i in range(15):
            badguypos[i][0] = 10 + 100 * (i - (floor(i/5) * 5))
            badguypos[i][1] = 10 + 40 * floor(i/5)

    if level==3:
        pass
            
pygame.display.flip()

        
 
