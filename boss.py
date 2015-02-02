from bullet import*
from random import*
import pygame
import constants
class Boss(pygame.sprite.Sprite):
	image = None
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		if Boss.image is None:
			Boss.image = pygame.image.load("assets/boss.png")
		self.image = Boss.image
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.topleft = (self.x,self.y)	
		self.width = constants.BOSS_WIDTH
		self.height = constants.BOSS_HEIGHT
