"""
author: Michael Bridges
date: october 3, 2016
"""
class GameStats():
	"""Track stats for pong."""

	def __init__(self, settings):
		"""initialize stats."""
		self.settings = settings
		self.reset_stats()

		#start game in an inactive state
		self.game_active = False
	
	def reset_stats(self):
		"""initialize stats that can change during the game."""
		#initial scores
		self.score1 = 0
		self.score2 = 0