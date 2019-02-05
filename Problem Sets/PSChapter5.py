# Chapter 05 Problem Set (16 points total)

# Using the base template below, make changes to accomplish each of the following:
# 1pt unless otherwise marked.

# 1.  Make the window inset display "Chapter 5 Problem Set" using set_caption function (see the chapter or template for example).
# 2.  Make a variable which represents the color YELLOW.
# 3.  Make a variable which represents the color SKY_BLUE.
# 4.  Make the background appear sky blue by changing the fill function.
# 5.  Use the ellipse function to make a yellow circle in the top left corner which is 100px wide and 100px high. This will be the sun.(2pt)
# 6.  Make a green rectangle which covers the bottom half of the screen starting at 0px x and 200px y.(2pt)
# 7.  Draw a 3px black horizontal line which separates your sky from your "grass".
# 8.  Make a red rectangle shape which is fully on the green field.  Make the rectangle 60px high and 80px wide. (2pt)
# 9.  Make a black triangle which sits on top of the box and makes it look like a little house. (2pt)
# 10.  Make a black rectangle which will represent a door on your house.  Give it a border of 2px.  Give the door an appropriate placement. (2pt)
# 11.  Create text with your name.  Make it display in the sky. (2pt)

# It's a pretty rudimentary picture, but if you can do this, you have all the skills to make more complex ones.


"""
 Pygame base template for opening a window
 Do the above items and change the code below appropriately.
"""

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SKY_BLUE = (20, 132, 229)

pygame.init()

# Set the width and height of the screen [width, height]
screen_width = 600
screen_height = 400
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

my_font = pygame.font.SysFont('Calabri', 50, True, False)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here
    screen.fill(SKY_BLUE)

    # --- Drawing code should go below here!!
    pygame.draw.ellipse(screen, YELLOW, [0, 0, 100, 100])
    pygame.draw.rect(screen, GREEN, [0, screen_height / 2, screen_width, screen_height / 2])
    pygame.draw.line(screen, BLACK, [0, screen_height / 2], [screen_width, screen_height / 2], 3)
    pygame.draw.rect(screen, RED, [260, 270, 80, 60])
    pygame.draw.polygon(screen, BLACK, [[260, 270], [340, 270], [300, 210]])
    pygame.draw.rect(screen, BLACK, [290, 290, 20, 40], 2)
    my_text = my_font.render('Jonah Gross', True, WHITE)
    screen.blit(my_text, [175, 100])


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()