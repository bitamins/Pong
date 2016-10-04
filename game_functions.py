"""
author: Michael Bridges
date: october 3, 2016
"""
import sys
import pygame
from time import sleep


def check_keydown_events(event, paddle1, paddle2, ball, stats):
    # key presses
    # paddle 1
    if event.key == pygame.K_UP:
        paddle1.moving_up = True
    elif event.key == pygame.K_DOWN:
        paddle1.moving_down = True

    # paddle 2
    elif event.key == pygame.K_w:
        paddle2.moving_up = True
    elif event.key == pygame.K_s:
        paddle2.moving_down = True

    # quit
    elif event.key == pygame.K_q:
        game_over(stats, paddle1, paddle2, ball)

def check_keyup_events(event, paddle1, paddle2):
    # key releases
    # paddle 1
    if event.key == pygame.K_UP:
        paddle1.moving_up = False
    elif event.key == pygame.K_DOWN:
        paddle1.moving_down = False

        # paddle 2
    elif event.key == pygame.K_w:
        paddle2.moving_up = False
    elif event.key == pygame.K_s:
        paddle2.moving_down = False

def check_play_button(settings, stats, sb, play_button, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #reset the game settings.
        settings.initialize_dynamic_settings()
        #hide the mouse cursor
        pygame.mouse.set_visible(False)
        #reset game stats
        stats.reset_stats()
        stats.game_active = True
        #reset the scoreboard
        sb.paddle1_score()
        sb.paddle2_score()

def check_events(settings, stats, screen, paddle1, paddle2, ball, sb, play_button):
    """respond to keyboard and mouse presses"""
    for event in pygame.event.get():
        # quit the program
        if event.type == pygame.QUIT:
            sys.exit()

        # key presses
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, paddle1, paddle2, ball, stats)

        # key releases
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddle1, paddle2)

        # mouse events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, stats, sb, play_button, mouse_x, mouse_y)


def update_screen(settings, stats, screen, paddle1, paddle2, ball, sb, play_button):
    # updates the images on the screen and flips to the new screen
    # check for collisions
    ball_paddle_collision(settings, ball, paddle1, paddle2)
    ball_edge_collision(settings, stats, ball, paddle1, paddle2, sb)

    # redraw the screen
    screen.fill(settings.background_color)

    # draw the score information.
    sb.show_score()
    # redraw the ball & paddles
    ball.draw_ball()
    paddle1.draw_paddle()
    paddle2.draw_paddle()

    # draw play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # show most recently drawn screen
    pygame.display.flip()


def ball_paddle_collision(settings, ball, paddle1, paddle2):
    """this function manages ball and paddle collisions"""
    collision1 = pygame.sprite.collide_rect(ball, paddle1)
    collision2 = pygame.sprite.collide_rect(ball, paddle2)
    if collision1:
        # reverse the balls direction
        offset = paddle1.center - float(ball.rect.centery) #increase the bounce angle by the offset
        #bounces the ball and prevents multiple bounces off the same paddle
        if ball.direction <= 180:
            ball.bounce(offset)
            ball.hit_paddle = True
        else:
            ball.hit_paddle = False

    elif collision2:
        # reverse the balls direction
        offset = paddle2.center - float(ball.rect.centery) #increase the bounce angle by the offset
        #bounces the ball and prevents multiple bounces off the same paddle
        if ball.direction >= 180:
            ball.bounce(offset)
            ball.hit_paddle = True
        else:
            ball.hit_paddle = False

def ball_edge_collision(settings, stats, ball, paddle1, paddle2, sb):
     # check for screen edges
        # left
        if ball.x <= (settings.ball_size/2):
            ball.direction = (360 - ball.direction) % 360
            stats.score2 += 1 #update the score
            sb.paddle2_score() #prepare the score image
            ball.reset()
            paddle1.center_paddle()
            paddle2.center_paddle()
            settings.ball_speed_factor *= 1.1 #increase the ball's speed every round
            sleep(0.5) #give the player half a second for the reset
            if stats.score2 == settings.max_score:
                print('player 2 wins')
                stats.game_active = False
                pygame.mouse.set_visible(True) #show the mouse again
        # right
        if ball.x >= settings.screen_width - (settings.ball_size/2):
            ball.direction = (360 - ball.direction) % 360
            stats.score1 += 1 #update the score
            sb.paddle1_score() #prepare the score image
            ball.reset()
            paddle1.center_paddle()
            paddle2.center_paddle()
            settings.ball_speed_factor *= 1.1 #increase the ball's speed every round
            sleep(0.5) #give the player half a second for the reset
            if stats.score1 == settings.max_score:
                print('player 1 wins')
                stats.game_active = False
                pygame.mouse.set_visible(True) #show the mouse again
        #bottom
        if ball.y <= (settings.ball_size/2):
            ball.direction = (180 - ball.direction) % 360
        #top
        if ball.y >= settings.screen_height - (settings.ball_size/2):
            ball.direction = (180 - ball.direction) % 360

def ai_move_paddle(settings, paddle2, ball):
    #adjust the paddle according to the balls y value
    if ball.y >= paddle2.center: 
        paddle2.center += settings.ai_paddle_speed_factor
    elif ball.y <= paddle2.center:
        paddle2.center -= settings.ai_paddle_speed_factor
    paddle2.rect.centery = paddle2.center

def game_over(stats, paddle1, paddle2, ball):
    stats.reset_stats()
    paddle1.center_paddle()
    paddle2.center_paddle()
    ball.reset()
    stats.game_active = False
    pygame.mouse.set_visible(True) #show the mouse again

