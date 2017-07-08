#파이썬 과제피하기 백업

#파이썬 과제피하기(양지원)

# 1 - Import library
import pygame
from pygame.locals import *
import random
import time

 
# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keys = [False, False, False, False,False,False,False,False,False]
playerpos=[320,450]
playerbox = [playerpos[0]+30,playerpos[1]+30]
badguypos1=[300,0]
solpos=[0,0]

forBlist=[]
ifBlist=[]
whileBlist=[]
classBlist=[]
sollist=[]
goright=1
goleft=0
t0=pygame.time.get_ticks()
store = 1
count = 0
font = pygame.font.Font(None,24)
healthvalue=194


# 3 - Load images
player = pygame.image.load("resources/images/jiwon.png")
player2 = pygame.image.load("resources/images/seongik.png")
player3 = pygame.image.load("resources/images/youngjoon.png")
badguyimg1 = pygame.image.load("resources/images/donghyun.png")
classroom = pygame.image.load("resources/images/classroom.jpg")
forB= pygame.image.load("resources/images/for.png")
ifB = pygame.image.load("resources/images/if.png")
whileB=pygame.image.load("resources/images/while.png")
classB=pygame.image.load("resources/images/class.png")
healthbar = pygame.image.load("resources/images/healthbar.png")
sol = pygame.image.load("resources/images/sol.png")
health = pygame.image.load("resources/images/health.png")
gameover = pygame.image.load("resources/images/Gameover.png")
# 3.1 - Load sound
pygame.mixer.music.load('resources/sound/background.mp3')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)



# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(classroom,(0,0))
    screen.blit(player, playerpos)
    screen.blit(badguyimg1, badguypos1)
    for forBpos in forBlist:
        screen.blit(forB,forBpos)
    for ifBpos in ifBlist:
        screen.blit(ifB,ifBpos)
    for whileBpos in whileBlist:
        screen.blit(whileB,whileBpos)
    for classBpos in classBlist:
        screen.blit(classB,classBpos)
    for solpos in sollist:
        screen.blit(sol,solpos)

    
    #Game over
    if healthvalue <=0:
        screen.fill(0)
        screen.blit(gameover,(0,140))
        playerpos = [-50,-50]
        

    # 6.1 - Draw health bar
    screen.blit(healthbar, (5,5))
    for health1 in range(healthvalue):
        screen.blit(health, (health1+8,8))

    # 6.2 - how healthvalue decreases
    playerrect= pygame.Rect(player.get_rect())
    playerrect.left=playerpos[0]
    playerrect.top=playerpos[1]
    for forBpos in forBlist:
        forBrect = pygame.Rect(forB.get_rect())
        forBrect.left=forBpos[0]
        forBrect.top=forBpos[1]
        if forBrect.colliderect(playerrect):
            healthvalue-=25
            forBlist.remove(forBpos)
    for ifBpos in ifBlist:
        ifBrect = pygame.Rect(ifB.get_rect())
        ifBrect.left=ifBpos[0]
        ifBrect.top=ifBpos[1]
        if ifBrect.colliderect(playerrect):
            healthvalue-=15
            ifBlist.remove(ifBpos)
    for whileBpos in whileBlist:
        whileBrect = pygame.Rect(whileB.get_rect())
        whileBrect.left=whileBpos[0]
        whileBrect.top=whileBpos[1]
        if whileBrect.colliderect(playerrect):
            healthvalue-=40
            whileBlist.remove(whileBpos)
    for classBpos in classBlist:
        classBrect = pygame.Rect(classB.get_rect())
        classBrect.left=classBpos[0]
        classBrect.top=classBpos[1]
        if classBrect.colliderect(playerrect):
            healthvalue-=50
            classBlist.remove(classBpos)

    #6.3 - how healthvalue increases
    
    for solpos in sollist:
        solrect = pygame.Rect(sol.get_rect())
        solrect.left=solpos[0]
        solrect.top=solpos[1]
        if solrect.colliderect(playerrect):
            healthvalue+=40
            count+=1
            sollist.remove(solpos)

    if healthvalue>= 194:
        healthvalue=194        

    # 6.4 - Change player
    if healthvalue <= 97:
        screen.blit(player2,playerpos)

    if count==5:
        screen.blit(player3,playerpos)
        
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
            if event.key==K_UP:
                keys[0]=True
            elif event.key==K_LEFT:
                keys[1]=True
            elif event.key==K_DOWN:
                keys[2]=True
            elif event.key==K_RIGHT:
                keys[3]=True

        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                keys[0]=False
            elif event.key==pygame.K_LEFT:
                keys[1]=False
            elif event.key==pygame.K_DOWN:
                keys[2]=False
            elif event.key==pygame.K_RIGHT:
                keys[3]=False

    # 9 - Move player
    if keys[0]:
        playerpos[1]-=3
        if playerpos[1] <= 80:
            playerpos[1] += 3
    elif keys[2]:
        playerpos[1]+=3
        if playerpos[1] >= 430:
            playerpos[1] -= 3
    if keys[1]:
        playerpos[0]-=3
        if playerpos[0]<=1:
            playerpos[0]+=3
    elif keys[3]:
        playerpos[0]+=3
        if playerpos[0] >=610:
            playerpos[0] -= 3

    # Move badguy
    if goright==1:
        badguypos1[0]+= 1.5
        if badguypos1[0]>580:
            goright=0
            goleft=1
    if goleft==1:
        badguypos1[0]-=1.5
        if badguypos1[0]<20:
            goright=1
            goleft=0

    #import randomnum
        what = random.randrange(4,9)
        rem = what%5
        if what==0:
            keys[4]=True
        elif what==1:
            keys[5]=True
        elif what==2:
            keys[6]=True
        elif what==3:
            keys[7]=True
        elif what==4:
            keys[8]=True

    #get time
    t1=pygame.time.get_ticks()
    t2=pygame.time.get_ticks()
    rmtime=120-(t2-t0)/1000
    text=font.render("Remain : "+str(rmtime),True,(0,255,0))
    screen.blit(text,[310,240])
    seconds=1-(t1-t0)/1000
    if seconds<=0:
        t0=t1
        store=1
    
    # Shooting Bullet and Sol
    if keys[4] and store==1:
        forBlist.append([badguypos1[0]+15,badguypos1[1]+30])
        keys[4]=False
        store = 0
    elif keys[5] and store==1:
        ifBlist.append([badguypos1[0]+15,badguypos1[1]+30])
        keys[5]=False
        store=0
    elif keys[6] and store==1:
        whileBlist.append([badguypos1[0]+15,badguypos1[1]+30])
        keys[6]=False
        store=0   
    elif keys[7] and store==1:
        classBlist.append([badguypos1[0]+15,badguypos1[1]+30])
        keys[7]=False
        store=0
    elif keys[8] and store==1:
        sollist.append([badguypos1[0]+15,badguypos1[1]+30])
        keys[8]=False
        store=0
    

    for forBpos in forBlist:
        forBpos[1] += 1.2
        if forBpos[1] >480:
            forBlist.remove(forBpos)
    for ifBpos in ifBlist:
        ifBpos[1] += 1.5
        if  ifBpos[1] >480:
            ifBlist.remove(ifBpos)
    for whileBpos in whileBlist:
        whileBpos[1] += 0.8
        if whileBpos[1] >480:
            whileBlist.remove(whileBpos)
    for classBpos in classBlist:
        classBpos[1] += 0.75
        if classBpos[1] >480:
            classBlist.remove(classBpos)
    for solpos in sollist:
        solpos[1] += 1
        if solpos[1] >480:
            sollist.remove(solpos)
