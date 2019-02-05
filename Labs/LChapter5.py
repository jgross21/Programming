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
LAVENDER = (211, 184, 255)
ORANGE = (239, 169, 71)
DARK_YELLOW = (255, 230, 0)
NAVY = (35, 94, 188)
pygame.init()

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 700
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

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
    pygame.draw.ellipse(screen, YELLOW, [(screen_width / 2)-250, (screen_height / 2)-200, 500, 500])
    pygame.draw.ellipse(screen, BLACK, [(screen_width / 2)-250, (screen_height / 2) - 200, 500, 500], 3)

    pygame.draw.ellipse(screen, YELLOW, [(screen_width / 2)-150, 25, 300, 300])
    pygame.draw.ellipse(screen, BLACK, [(screen_width / 2)-150, 25, 300, 300], 3)

    pygame.draw.polygon(screen, YELLOW, [[(screen_width / 2) + 150, (screen_height / 2) -100], [(screen_width / 2)+ 130, (screen_height / 2) +31], [670, 410]])
    pygame.draw.polygon(screen, BLACK, [[(screen_width / 2) + 150, (screen_height / 2) -100], [(screen_width / 2)+ 130, (screen_height / 2) +31], [670, 410]], 3)

    pygame.draw.polygon(screen, YELLOW, [[(screen_width / 2) - 150, (screen_height / 2) -100], [(screen_width / 2)- 130, (screen_height / 2) +31], [30, 410]])
    pygame.draw.polygon(screen, BLACK, [[(screen_width / 2) - 150, (screen_height / 2) -100], [(screen_width / 2)- 130, (screen_height / 2) +31], [30, 410]], 3)

    pygame.draw.polygon(screen, ORANGE, [[320, 175], [380, 175], [350, 290]])
    pygame.draw.polygon(screen, BLACK, [[320, 175], [380, 175], [350, 290]], 3)

    pygame.draw.ellipse(screen, LAVENDER, [260, 100, 50, 50])
    pygame.draw.ellipse(screen, BLACK, [260, 100, 50, 50], 3)

    pygame.draw.ellipse(screen, LAVENDER, [380, 100, 50, 50])
    pygame.draw.ellipse(screen, BLACK, [380, 100, 50, 50], 3)
    for y in range(350, 600, 15):
        pygame.draw.line(screen, DARK_YELLOW, [220, y], [480, y], 1)
    for x in range (220, 480, 15):
        pygame.draw.line(screen, DARK_YELLOW, [x, 350], [x, 600])
    pygame.draw.line(screen, BLACK, [230, 618], [230, 678], 5)
    pygame.draw.line(screen, BLACK, [230, 678], [200, 678], 5)
    pygame.draw.line(screen, BLACK, [230, 678], [230, 695], 5)
    pygame.draw.line(screen, BLACK, [230, 695], [215, 695], 5)
    pygame.draw.line(screen, BLACK, [230, 678], [260, 678], 5)

    pygame.draw.line(screen, BLACK, [470, 618], [470, 678], 5)
    pygame.draw.line(screen, BLACK, [470, 678], [500, 678], 5)
    pygame.draw.line(screen, BLACK, [470, 678], [470, 695], 5)
    pygame.draw.line(screen, BLACK, [470, 695], [485, 695], 5)
    pygame.draw.line(screen, BLACK, [470, 678], [440, 678], 5)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()