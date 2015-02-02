import pygame
import constants
from bullet import *
from random import *
class Alien(pygame.sprite.Sprite):
	image = None 
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		if Alien.image is None:
			Alien.image = pygame.image.load("assets/alienspaceship.png")
		self.image = Alien.image
		self.rect = self.image.get_rect()
		self.x = x
		self.y= y

		self.steps_down = 0

		self.rect.topleft = (self.x,self.y)	
		self.speed = constants.ALIEN_SPEED
		self.moving_down = False 
		self.width = constants.ALIEN_WIDTH
		self.height = constants.ALIEN_HEIGHT
		self.direction = 1
	def moveHorizontal(self):
		self.x = self.x +  (self.direction*self.speed)
		self.rect.topleft = (self.x, self.y)
	
	def moveVertical(self):
		self.steps_down = self.steps_down + self.speed
		self.y = self.y + self.speed
		self.rect.topleft = (self.x, self.y)


	def shoot (self):
		if self.direction == -1:
			return Bullet(self.x, self.y, constants.ALIEN_BULLET)
		return Bullet(self.x+self.width/2, self.y+self.height/2, constants.ALIEN_BULLET)
	def update(self):
		if self.direction == 1:
			if self.x+ self.width+self.speed > constants.SCREENWIDTH:
				self.direction = -1
				self.moving_down = True
		elif self.x-self.speed < 0:
			self.direction = 1
			self.moving_down = True
		

		if not self.moving_down:
			self.moveHorizontal()
		else:
			self.moveVertical()

		if self.steps_down == 65:
			self.steps_down = 0
			self.moving_down = False	
		
		if randint (1,25) == 10:
			return self.shoot()


