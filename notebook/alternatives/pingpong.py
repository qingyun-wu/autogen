# filename: pingpong.py
import pygame
import sys

# General setup
pygame.init()

# Setting up main window
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Game Variables
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
player = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 70, 10, 140)
opponent = pygame.Rect(10, HEIGHT // 2 - 70, 10, 140)
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)
ball_speed = 7
player_speed = 0
opponent_speed = 7

def ball_animation():
    global ball_speed, opponent_speed, player_speed
    ball.x += ball_speed
    ball.y += opponent_speed

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        opponent_speed *= -1
    if ball.left <= 0:
        ball_restart()
    if ball.right >= WIDTH:
        ball_restart()

    if ball.colliderect(player) and ball_speed > 0:
        ball_speed *= -1
    if ball.colliderect(opponent) and ball_speed < 0:
        ball_speed *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= HEIGHT:
        opponent.bottom = HEIGHT

def ball_restart():
    global ball_speed, opponent_speed
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed *= -1
    opponent_speed += 0.5 if opponent_speed > 0 else -0.5

# Drawing objects to the screen
def draw_objects():
    win.fill(bg_color)
    pygame.draw.rect(win, light_grey, player)
    pygame.draw.rect(win, light_grey, opponent)
    pygame.draw.ellipse(win, light_grey, ball)
    pygame.draw.aaline(win, light_grey, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

# Running the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 6
            if event.key == pygame.K_DOWN:
                player_speed += 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 6
            if event.key == pygame.K_DOWN:
                player_speed -= 6

    ball_animation()
    player_animation()
    opponent_ai()

    draw_objects()

    pygame.display.flip()