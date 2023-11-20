import pygame
import sys

# Setting some basic color for the game
WHITE = (255, 255, 255)
ORANGE = (255, 140, 0)

# Defining the Ball class
class Ball:
    def __init__(self):
        self.x, self.y = 0, 0
        self.speed_x, self.speed_y = 3, 3
        self.radius = 15

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.speed_y *= -1
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.speed_x *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, ORANGE, (self.x, self.y), self.radius)

# Initializing Pygame and setting the window size
pygame.init()
WIDTH, HEIGHT = 600, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Game")

# Creating the Ball object
ball = Ball()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill(WHITE)
    ball.move()
    ball.draw(SCREEN)

    pygame.display.flip()
    pygame.time.delay(30)