import pygame
import constants 
class Star (pygame.sprite.Sprite):
	def __init__ (self,xpos,star_type):
		pygame.sprite.Sprite.__init__(self)
		self.x = xpos
		self.y = 0
		self.star_type = star_type
		self.speed = constants.STAR_SPEED
		self.width = constants.STAR_WIDTH
		self.height = constants.STAR_HEIGHT
	def move (self):
		self.y = self.y + self.speed