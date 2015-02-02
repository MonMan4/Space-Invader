import pygame
import constants
from bullet import *
class Tank(pygame.sprite.Sprite):
	image = None
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		if Tank.image is None:
			Tank.image = pygame.image.load("assets/spaceship.png")
		self.image = Tank.image
		self.rect = self.image.get_rect()
		self.x = 320
		self.y=875 
		self.numBullets = constants.START_BULLETS
		self.rect.topleft = (self.x,self.y)
		self.speed = constants.TANK_SPEED
		self.width = constants.TANK_WIDTH
		self.height = constants.TANK_HEIGHT
	def moveLeft(self):
		if self.x-self.speed >= 0:
			self.x=self.x-self.speed
			self.rect.topleft = (self.x, self.y)
	def moveRight(self):
		if self.x+ self.width+self.speed <= constants.SCREENWIDTH:
			self.x= self.x+self.speed
			self.rect.topleft = (self.x, self.y)
	def shoot (self): 
		if self.numBullets > 0 :
			self.numBullets = self.numBullets - 1 
			return Bullet(self.x + self.width/2,self.y, constants.TANK_BULLET)
	def recharge (self,recharge_number):
		if self.numBullets + recharge_number <= constants.CAP_BULLETS:
			self.numBullets = self.numBullets + recharge_number
		else: self.numBullets = constants.CAP_BULLETS

	def bullet_count(self):
		return self.numBullets

