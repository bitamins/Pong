"""
author: Michael Bridges
date: october 3, 2016
"""
import pygame
from pygame.sprite import Sprite 

class Paddle(Sprite):
	
	def __init__(self, settings, screen, player_number):
		"""initialize the player and the set starting position"""
		super().__init__()
		self.screen = screen
		self.settings = settings

		#load the player image.
		self.screen_rect = screen.get_rect()

		#paddle rect
		self.rect = pygame.Rect(0, 0, settings.paddle_width, settings.paddle_height)

		#start player at amount one side of the screen
		self.rect.centery = self.screen_rect.centery
		if player_number == 1:
			self.rect.left = self.screen_rect.left + 10  # 10 pixels from the left edge of the screen
		elif player_number == 2:
			self.rect.right = self.screen_rect.right - 10  # 10 pixels from the right edge of the screen

		#store the decimal value of the players center
		self.center = float(self.rect.centery)
		self.top = float(self.rect.top)
		self.bottom = float(self.rect.bottom)

		#attributes
		self.color = settings.white

		#movement flags, initially not moving
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""update the players position based on the movement flag."""
		if self.moving_up:
			self.center -= self.settings.paddle_speed_factor
		elif self.moving_down:
			self.center += self.settings.paddle_speed_factor
		
		#update the rect object from self.center
		self.rect.centery = self.center

	def draw_paddle(self):
		"""draw the paddle at the current location"""
		pygame.draw.rect(self.screen, self.color, self.rect)

	def center_paddle(self):
		"""center the paddle on the screen"""
		self.center = self.screen_rect.centery

		