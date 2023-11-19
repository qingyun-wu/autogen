# filename: game.py

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
SPEED = 2

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the player and the goal
player = pygame.Rect(WIDTH / 2, HEIGHT / 2, 50, 50)
goal = pygame.Rect(random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50), 50, 50)

# Set up the score
score = 0

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= SPEED
    if keys[pygame.K_RIGHT]:
        player.x += SPEED
    if keys[pygame.K_UP]:
        player.y -= SPEED
    if keys[pygame.K_DOWN]:
        player.y += SPEED

    # Check for collision with the goal
    if player.colliderect(goal):
        score += 1
        goal.x = random.randint(0, WIDTH - 50)
        goal.y = random.randint(0, HEIGHT - 50)

    # Fill the screen with a blue color
    screen.fill((0, 0, 255))

    # Draw the player and the goal to the screen
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (0, 255, 0), goal)

    # Display the score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), 1, (10, 10, 10))
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
