class GameStats():
	"""Track statistics for Alien Invasion."""

	def __init__(self, cg_settings):
		"""Initialize statistics"""
		self.cg_settings = cg_settings
		self.reset_stats()
		# start Alien Invasion in an inactive state
		self.game_active = False
		#High score should never be reset.
		self.high_score = 0
		#To show game start
		self.game_start_msg = False


	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.score = 0	
		self.level = 1