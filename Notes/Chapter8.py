"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame

# Define some colors
BLACK = (0, 0, 0) # (Red, green, blue)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (120,120,120)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
NAVY = (36, 72, 140)

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

# Variables
box_x = 100
box_y = 100
box_speed_x = 3

car_x = 0
car_y = 300

health = 700

gb = 100
gb_speed = 1

ball_x = 0
ball_y = 450
ball_y_speed = -5
ball_y_accell = 0.05
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    box_x += box_speed_x

    if box_x > screen_width - 50:
        box_x = screen_width - 50
        box_speed_x *= -1
    if box_x < 0:
        box_x = 0
        box_speed_x *= -1

    #Car Wrapping
    car_x += 3

    if car_x > screen_width:
        car_x = -100


    # Health bar
    health -= 1
    if health < 0:
        health = 0

    # Color changing
    gb += gb_speed
    if gb >= 255 or gb <= 0:
        gb_speed *= -1

    # Accelerating ball
    ball_y_speed += ball_y_accell
    ball_y += ball_y_speed


    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here
    # Bouncing Box
    pygame.draw.rect(screen, RED, [box_x, box_y, 50, 50])
    # Car Wrapping
    pygame.draw.rect(screen, (255, gb, gb), [car_x, car_y, 100, 50])
    pygame.draw.ellipse(screen, BLACK, [car_x, car_y+40, 25, 25])
    pygame.draw.ellipse(screen, BLACK, [car_x+75, car_y+40, 25, 25])
    # Health bar
    pygame.draw.rect(screen, BLACK, [20, 20, 700, 20])
    pygame.draw.rect(screen, RED, [20, 20, health, 20])
    # Ball
    pygame.draw.ellipse(screen, MAGENTA, [ball_x, ball_y, 50 ,50])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()