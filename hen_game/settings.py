import pygame

class Settings(object):
	""" A class to store all Settings for Game"""
	def __init__(self):
		"""Initialize game's settings"""
		#Screen settings
		self.screen_height = 700
		self.screen_width = 1200
		self.bg_color = (105, 0, 0)
		self.background = pygame.image.load("images/background2.jpg")

		#basket settings
		self.basket_speed_factor = 8

		#egg settings
		self.egg_speed_factor = 3
		self.golden_score = 20
		self.white_score = 10
		#poop settings
		self.poop_speed_factor = 3
		self.poop_score = -10

		#Settings related to levelling up
		self.base_level_score = 50
		self.drop_speed_increase = 0.5
		self.num_hens = 3

		#Settings related to game finish
		#self.game_finish =