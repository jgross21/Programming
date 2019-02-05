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
BLACK = (0, 0, 0)  # (Red, green, blue)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (120,120,120)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
pygame.init()

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

# Make my fonts
# Sys Font ('font_name', font_size, bold, italics)
my_font = pygame.font.SysFont('Calabri', 50, True, False)

score = 0

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

    # Rectangle (surface, color, [top_left_x, top_left_y, width, height], optional width])
    pygame.draw.rect(screen, RED, [100,50,200,100])
    pygame.draw.rect(screen, CYAN, [100, 50, 200, 100], 3)

    # elipse(surface, color, [top_left_x, top_left_y, width, height], optional width]
    pygame.draw.ellipse(screen, BLACK, [100, 50, 200, 100])

    # Line
    # line(surface, color, [x1, y1], [x2, y2], width)
    pygame.draw.line(screen, GREEN, [0, 0], [200, 100], 2)

    # Repeating objects
    for x in range(10, screen_width, 20):
        pygame.draw.line(screen, BLUE, [x, 0], [x, screen_height], 1)
    for y in range (10, screen_height, 20):
        pygame.draw.line(screen, BLUE, [0, y], [screen_width, y], 1)

    # Polygon
    # polygon(surface, color, [[x1, y1], [x2, y2], [x3, y3...], optional_width)
    pygame.draw.polygon(screen, RED, [[100, 200], [300, 200], [200, 400]])

    # Text
    # Make a font (usually outside the loop)
    # Render the text (usually inside the loop)
    # render(text, anti_alias, color)
    my_text = my_font.render('Score:', True, BLACK)
    # Blit the text onto the screen.
    # blit(text_object, [Top_left_x, Top_left_y])
    screen.blit(my_text, [400, 350])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

