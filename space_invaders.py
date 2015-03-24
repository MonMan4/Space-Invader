import pygame
import constants
from bullet import *
from tank import *
from Alien import *
from star import *
from boss import*
from highScore import*
from random import randint


##LargestNumber = 0
##file = open('HighScores.txt', 'r')
##for line in file:
##    if line > LargestNumber:
##            LargestNumber = line
##            
##print LargestNumber

pygame.init()
t = Tank()
score = 0
bullets = []
waves_killed = 0
recharge_slivers = []
aliens = []
alien_rows = []
stars = []
screen = pygame.display.set_mode([constants.SCREENWIDTH,constants.SCREENHEIGHT])
recharge_counter = 0
ammo_img = pygame.image.load("assets/tank_bullet.png")
bosses = []
mode = "playing"
YouLose = pygame.image.load("assets/boss.jpg")
YouLose = pygame.transform.scale(YouLose, (constants.SCREENWIDTH, constants.SCREENHEIGHT))
def ShowScore():
        myfont = pygame.font.SysFont("Arial", 50)
        label = myfont.render("Your score is: " +str(score), 1, pygame.color.THECOLORS['red'])
        screen.blit(label, (0, 50))
def hitAlien(b):
	global waves_killed, score
	for row in alien_rows:
		for x in range(len(row)-1, -1, -1):
			a = row[x]
			if b.x<=a.width+a.x and b.x >= a.x and b.y>= a.y and b.y<= a.y + a.height:
				if b.bulletType == constants.TANK_BULLET:
					row.remove(a)
					score = score + 1
					print "Your score is:", score
					if len (row) == 0:
						alien_rows.remove(row)
						waves_killed = waves_killed+1
					return True

def hitTank(b):
	if b.x<=t.width+t.x and b.x >= t.x and b.y>= t.y and b.y<= t.y + t.height:
		if b.bulletType == constants.ALIEN_BULLET:
			return True
def spawnALiens():
	row = []
	for x in range (0,5):
		a= Alien (x*250,50)
		row.append(a)
	alien_rows.append(row)


def spawnStars():
	for x in range (0,constants.SCREENWIDTH):
		if randint(0,200) == 4:
			star_type = randint(1,3)
			s= Star (x,star_type)
			stars.append(s)


def updateStars():
	for s in stars :
		if s.y > constants.SCREENHEIGHT :
			stars.remove(s)
		else:
			s.move()

def updateBullets():
        global mode
        for b in bullets:
                if b.is_offscreen():
                        bullets.remove(b)
                elif hitAlien(b):
                        bullets.remove(b)
                elif hitTank(b) :
                        mode = "lose"
 #                       f = open("HighScores.txt","a") #opens file with name of "test.txt"
 #                       f.write(str(score) + "\n")
 #                       f.close()
                        Highscore.write_score(score)
                else:
                        b.move()

def updateAlieans():
        for row in alien_rows:
                for a in row:
                        bullet = a.update()
                        if bullet != None:
                                bullets.append(bullet)

def drawBullets():
	for b in bullets:
		screen.blit(b.image,b.rect)

def drawStars():
	for s in stars:
		if s.star_type == 1:
			color = [255,255,255]
		if s.star_type == 2:
			color = [255,0,0]
		if s.star_type == 3:
			color = [255,255,0]
		pygame.draw.rect(screen, color, [s.x,s.y, s.width,s.height], 0)
def updateCounter():
	global recharge_counter
	if recharge_counter  == 0:
		recharge_slivers.append((pygame.Rect(50,945,2,10),[255,255,0]))
	else:
		new_rect_x = recharge_slivers[len(recharge_slivers)-1][0].x + 2
		new_color = [255,recharge_slivers[len(recharge_slivers)-1][1][1]-2.5 ,0]	
		new_rect = (pygame.Rect(new_rect_x, 945, 2, 10), new_color)
		recharge_slivers.append(new_rect)
	recharge_counter=recharge_counter + 1
	if recharge_counter == 100:
		t.recharge(1) 
		recharge_counter = 0
		del recharge_slivers[:]

spawnALiens()

while True:
     if mode == "playing":
        spawnStars()
        if len(alien_rows) == 0 and waves_killed < 2:
                spawnALiens()
        elif waves_killed == 2:
                bosses.append(Boss(0,0))
                waves_killed = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
                t.moveLeft()
        if keys[pygame.K_RIGHT]:
                t.moveRight()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                b = t.shoot()
                                if b != None: bullets.append(b)
        updateCounter()
        updateAlieans()
        updateBullets()
        updateStars()
        screen.fill([0,0,0])
        drawStars() 
        screen.blit(t.image,t.rect)
        drawBullets()
        for row in alien_rows:
                for a in row:
                        screen.blit(a.image,a.rect)
        for tup in recharge_slivers:
                pygame.draw.rect(screen,tup[1], tup[0])
        for x in range (0,t.bullet_count()):
                image_rect = pygame.Rect(1110 + 8*x,935,8,22)
                screen.blit(ammo_img,image_rect)
        for b in bosses:
                screen.blit(b.image,b.rect)
        ShowScore()
        
        pygame.display.update()
        pygame.time.delay(20)

     if mode == "lose":
              screen.blit(YouLose,(0,0))
              Highscore.get_top_scores(5)
              num = Highscore.get_top_scores(10)
              Highscore.show_high_scores(pygame, screen, num, 0, -40)
              pygame.display.update()
              pygame.time.delay(20)
              for event in pygame.event.get():
                      if event.type == pygame.QUIT:
                              pygame.quit()


        
        
