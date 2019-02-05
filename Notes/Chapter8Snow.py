"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0) # (Red, green, blue)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (120,120,120)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
BROWN = (114, 70, 28)

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

snow_list = []
for i in range (500):
    x = random.randrange(screen_width)
    y = random.randrange(screen_height)
    speed = random.random() * 4 + 1
    size = speed + 2
    snowflake = [x, y, speed, size] # snowflake x and y pos
    snow_list.append(snowflake)
tree_x = 200
tree_y = 100
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    for snowflake in snow_list:
        snowflake[1] += snowflake[2]
        if snowflake[1] > screen_height:
            snowflake[1] = -5
            snowflake[0] = random.randrange(screen_width)
        pygame.draw.ellipse(screen, WHITE, [snowflake[0], snowflake[1], snowflake[3], snowflake[3]])
    pygame.draw.rect(screen, WHITE, [0, screen_height - 50, screen_width, screen_height])

    pygame.draw.rect(screen, BROWN, [60 + tree_x, 400 - 230 + tree_y, 30, 45])
    pygame.draw.polygon(screen, GREEN, [[150 + tree_x, 400 - 230 + tree_y], [75 + tree_x, 250 - 230 + tree_y], [0 + tree_x, 400 - 230 + tree_y]])
    pygame.draw.polygon(screen, GREEN, [[140 + tree_x, 350 - 230 + tree_y], [75 + tree_x, 230 - 230 + tree_y], [10 + tree_x, 350 - 230 + tree_y]])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()