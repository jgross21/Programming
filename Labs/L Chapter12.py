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
pygame.init()

class Rectangle:
    def __init__(self):
        self.height = random.randrange(21, 71)
        self.width = random.randrange(21, 71)
        self.change_x = random.randrange(-3, 3)
        self.change_y = random.randrange(-3, 3)
        if self.change_x == 0:
            self.change_x = random.randrange(-2, 2)
        if self.change_y == 0:
            self.change_y = random.randrange(-2, 2)
        self.x = random.randrange(0, screen_width - self.width)
        self.y = random.randrange(0, screen_height - self.height)
        self.color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])
        pygame.draw.rect(screen, BLACK, [self.x, self.y, self.width, self.height], 2)

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

class Elipse(Rectangle):
    def draw(self):
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.width, self.height])
        pygame.draw.ellipse(screen, BLACK, [self.x, self.y, self.width, self.height], 2)

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

my_list = []

for i in range (100):
    my_object = Rectangle()
    my_list.append(my_object)
    my_elipse = Elipse()
    my_list.append(my_elipse)

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
    screen.fill(WHITE)

    # --- Drawing code should go here
    my_object.draw()
    my_object.move()
    for i in range (len(my_list)):
        my_list[i].draw()
        my_list[i].move()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()