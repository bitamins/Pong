"""
author: Michael Bridges
date: october 3, 2016
"""
class Settings():
	"""this class stores settings for pong."""

	def __init__(self):
		"""initialize game settings."""
		#colors
		self.blue = (0,0,255)
		self.white = (255,255,255)
		self.red = (255,0,0)
		self.green = (0,255,0)
		self.black = (0,0,0)
		self.yellow = (255,255,0)
		self.cyan = (0,255,255)
		self.magenta = (255,0,255)

		#screen settings
		self.screen_width = 800
		self.screen_height = 600
		self.background_color = self.black

		#direction 90 is to the right, 180 is to the left
		self.ball_direction_degrees = 90
		self.ball_size = 10

		#how quickly the game speeds up
		self.speedup_scale = 1.1

		#max score, set to 3 points
		self.max_score = 3

		#paddle settings
		self.paddle_height = 100
		self.paddle_width = 10

		#settings that change as the game go on
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""initialize settings that change each level."""
		self.paddle_speed_factor = 1.3
		self.ai_paddle_speed_factor = 1.2
		self.ball_speed_factor = 1.75
