import pygame
from pygame.sprite import Sprite

class Poop(Sprite):
	""" A class to represent eggs."""
	def __init__(self,screen, cg_settings):
		super(Poop,self).__init__()
		self.screen = screen

		# Create an egg at (0,0) and then correct its position
		self.cg_settings = cg_settings
		self.screen_rect = screen.get_rect()
		#Load the alien image and set its rect attribute.
		self.image = pygame.image.load("images/poop.jpg")
		self.rect = self.image.get_rect()

		#store the decimal value of egg's y-coordiante
		self.y = self.screen_rect.top+20

		#Start each new hen near top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.y
		
		#store speed 
		self.speed_factor=cg_settings.poop_speed_factor


	def blitme(self):
		"""draw the hen at its position"""
		
		
		self.screen.blit(self.image, self.rect)	
	
	def update(self):
		# update the deciaml position of the bullet's y-coor
		self.y += float(self.speed_factor)
		#update the rect position
		self.rect.y = self.y		