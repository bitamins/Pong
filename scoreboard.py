"""
author: Michael Bridges
date: october 3, 2016
"""
import pygame.font
from pygame.sprite import Group

class Scoreboard():
    """a class to report score information"""
    def __init__(self, settings, screen, stats):
        """initialize the score attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        #Font for the score
        self.text_color = self.settings.white
        self.font = pygame.font.SysFont(None, 64)

        #create the initial score image
        self.paddle1_score()
        self.paddle2_score()

    def paddle1_score(self):
        #get the score and create the image
        score1_str = "{:,}".format(self.stats.score1)
        self.score1_image = self.font.render(score1_str, True, self.text_color, self.settings.background_color)

        #show image at middle left of screen
        self.score1_rect = self.score1_image.get_rect()
        self.score1_rect.right = (self.screen_rect.right/2) - 10
        self.score1_rect.top = 20

    def paddle2_score(self):
        #get the score and create the image
        score2_str = "{:,}".format(self.stats.score2)
        self.score2_image = self.font.render(score2_str, True, self.text_color, self.settings.background_color)

        #show image at middle right of screen
        self.score2_rect = self.score2_image.get_rect()
        self.score2_rect.left = (self.screen_rect.right/2) + 10
        self.score2_rect.top = 20

    def show_score(self):
        """draw the score to the screen"""
        self.screen.blit(self.score1_image, self.score1_rect)
        self.screen.blit(self.score2_image, self.score2_rect)

    
