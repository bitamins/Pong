"""
author: Michael Bridges
date: october 3, 2016

info: play with the up and down arrow keys, you are the paddle on the right
    the ball speeds up after every round
    the first player to score 3 wins
"""
import sys
import pygame

# modules
from settings import Settings
from paddle import Paddle
from game_statistics import GameStats
from ball import Ball
from scoreboard import Scoreboard
from play_button import Button
import game_functions as gf


# main function
def run_game():
    # start a game, and create a. window.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Pong")
    # create the play button.
    play_button = Button(settings, screen, "Play")
    # create stats.
    stats = GameStats(settings)
    # create scoreboard.
    sb = Scoreboard(settings, screen, stats)
    # create pong paddles and ball.
    paddle1 = Paddle(settings, screen, 2) #paddle 1 on right
    paddle2 = Paddle(settings, screen, 1) #paddle 2 on left
    ball = Ball(settings, screen, stats, sb)  # start the main game loop.
    while True:
        # watch for keyboard and mouse events
        gf.check_events(settings, stats, screen, paddle1, paddle2, ball, sb, play_button)
        if stats.game_active:
            paddle1.update()
            #paddle2.update() #against another player
            gf.ai_move_paddle(settings, paddle2, ball) #against the pc
            ball.update()
        gf.update_screen(settings, stats, screen, paddle1, paddle2, ball, sb, play_button)

run_game()
