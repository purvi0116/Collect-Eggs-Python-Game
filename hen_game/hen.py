import pygame


class Hen():
	"""a class to represent a single hen."""
	def __init__(self,cg_settings,screen):
		"""initialize the hen and set its position."""
		self.screen =screen
		self.cg_settings = cg_settings
		self.screen_rect = screen.get_rect()
		#Load the alien image and set its rect attribute.
		self.image = pygame.image.load("images/hen.png")
		self.rect = self.image.get_rect()

		#Start each new hen near top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.screen_rect.top+20
		
		#store the hen's exact position

	def blitme(self):
		"""draw the hen at its position"""
		
		
		self.screen.blit(self.image, self.rect)	