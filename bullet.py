import pygame
import constants

class Bullet (pygame.sprite.Sprite):
	def __init__(self,xPos,yPos, bulletType):
		pygame.sprite.Sprite.__init__(self)
		self.x = xPos
		self.y = yPos
		self.bulletType = bulletType
		self.speed = constants.BULLET_SPEED
		self.width = constants.BULLET_WIDTH
		self.height = constants.BULLET_HEIGHT
		if self.bulletType == constants.TANK_BULLET:
			self.image = pygame.image.load("assets/tank_bullet.png")
		else:
			self.image = pygame.image.load("assets/alien_bullet.png")
		self.rect = self.image.get_rect()
		self.rect.topleft = (self.x,self.y)	



	def move (self):
		if self.bulletType == constants.TANK_BULLET:
			self.y = self.y - self.speed
		else:
			self.y = self.y + self.speed
		self.rect.topleft = (self.x,self.y)
	def is_offscreen(self):
		if self.y + self.height <= 0 or self.y > constants.SCREENHEIGHT:
			return True
		return False

 
