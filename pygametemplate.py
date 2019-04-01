
# Pygame template - skeleton for new Pygame
import pygame
import random


WIDTH = 360
HEIGHT = 480
FPS = 30

# defined colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize Pygame & create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kitters")
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # keep loop running at right speed
    clock.tick(FPS)
    # Process input / events
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update


    # Draw / Render
    screen.fill(BLACK)
    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
