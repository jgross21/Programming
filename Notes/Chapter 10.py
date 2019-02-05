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
BLUE = (0, 0, 255)
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

def stick_man(x, y, shirt_color):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, 83 - 83 + y, 10, 10], 0)

    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 100 - 83 + y], [10 + x, 110 - 83 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 100 - 83 + y], [0 + x, 110 - 83 + y], 2)

    # Body
    pygame.draw.line(screen, shirt_color, [5 + x, 100 - 83 + y], [5 + x, 90 - 83 + y], 2)

    # Arms
    pygame.draw.line(screen, shirt_color, [5 + x, 90 - 83 + y], [9 + x, 100 - 83 + y], 2)
    pygame.draw.line(screen, shirt_color, [5 + x, 90 - 83 + y], [1 + x, 100 - 83 + y], 2)

shirt_color = RED

pygame.mouse.set_visible(False)

player_x = 0
player_y = 0
player_speedx = 0
player_speedy = 0
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            shirt_color = GREEN
        elif event.type == pygame.MOUSEBUTTONUP:
            shirt_color = RED
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_speedx = 3
            if event.key == pygame.K_LEFT:
                player_speedx = -3
            if event.key == pygame.K_UP:
                player_speedy = -3
            if event.key == pygame.K_DOWN:
                player_speedy = 3
        elif event.type == pygame.KEYUP:
            print('You lifted your finger off the key.')
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_speedx = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_speedy = 0

    # --- Game logic should go here
    player_x += player_speedx
    if player_x < 0:
        player_x = 0
    if player_x > screen_width:
        player_x = screen_width

    player_y += player_speedy
    if player_y < 0:
        player_y = 0
    if player_y > screen_height - 10:
        player_y = screen_height - 10

    mouse_x, mouse_y = (pygame.mouse.get_pos())

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here
    stick_man(mouse_x, mouse_y, shirt_color)
    stick_man(player_x, player_y, BLUE)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()