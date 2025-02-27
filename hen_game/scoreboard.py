import pygame.font
from pygame.sprite import Group


class Scoreboard():
	"""A class to report scoring information."""

	def __init__(self, cg_settings, screen, stats):
		"""initialize scorekeeping attributes"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.cg_settings = cg_settings
		self.stats = stats

		# font settings for scoring information.
		self.text_color = (0,117,138)
		self.font = pygame.font.SysFont(None, 100)

		#preapare the initailize score images.
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		
	def prep_score(self):
		"""Turn the score into a rendered image."""
		rounded_score = int(round(self.stats.score, -1))
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str,True,self.text_color,self.cg_settings.bg_color)


		#display  the score at the top right of the screen.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right-20
		self.score_rect.top = 20


	def show_score(self):
		"""Draw score to the screen."""
		self.screen.blit(self.score_image,self.score_rect)	
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		#Draw  ships
		

	def prep_high_score(self):
		"""Turn the high score into a rendered image."""
		high_score = int(round(self.stats.high_score,-1))
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True,self.text_color, self.cg_settings.bg_color)

		# Center the high score at the top of the screen.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top


	def prep_level(self):
		"""Turn the level into a rendered image."""
		self.level_image = self.font.render(str(self.stats.level),True,
							self.text_color, self.cg_settings.bg_color)
		# Position the level below the score.
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10						

	