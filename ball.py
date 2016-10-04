"""
author: Michael Bridges
date: october 3, 2016
"""
import pygame
import math
import random
from pygame.sprite import Sprite


class Ball(Sprite):
    """this class manages the ball"""

    # create a ball in the middle of the screen
    def __init__(self, settings, screen, stats, sb):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.stats = stats
        self.sb = sb

        # create the ball rect at the center of the screen
        self.rect = pygame.Rect((settings.screen_width / 2), (settings.screen_height / 2), settings.ball_size,
                                settings.ball_size)
        self.rect.centerx = (settings.screen_width / 2)
        self.rect.centery = (settings.screen_height / 2)

        # store the ball's position as a decimal value.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.color = settings.white
        self.speed_factor = settings.ball_speed_factor

        # direction of the ball in degrees
        self.direction = self.settings.ball_direction_degrees #90 means to the right

        #True if a ball had just hit the paddle
        self.hit_paddle = False

        #size of the ball
        self.width = settings.ball_size
        self.height = settings.ball_size

    def bounce(self, offset):
        self.direction = (360-self.direction)%360
        self.direction -= offset

    def reset(self):
        self.x = (self.settings.screen_width / 2)
        self.y = (self.settings.screen_height / 2)
        self.speed_factor = self.settings.ball_speed_factor

        #direction of ball in degrees
        self.direction = self.settings.ball_direction_degrees

        #flip a coin for the balls initial direction
        if random.randrange(2)==0:
            self.direction += 180

    def update(self):
        """move the ball around the screen."""
        # find the direction in radians
        direction_radians = math.radians(self.direction)

        #prevents ball from bouncing top to bottom across the screen by adjusting the direction towards the opposite player (based off unit circle)
        if self.direction > 330 or (self.direction > 150 and self.direction < 180):
            self.direction -= 1
        if (self.direction < 210 and self.direction > 180) or self.direction < 30:
            self.direction += 1
       
        # Change the position (x and y) according to the speed and direction
        self.x += self.speed_factor * math.sin(direction_radians)
        self.y -= self.speed_factor * math.cos(direction_radians)

        # Move the image to where our x and y are
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_ball(self):
        """draw the ball to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

