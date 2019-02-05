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
pygame.init()

# Set the width and height of the screen [width, height]
screen_width = 710
screen_height = 442
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Image Rescources
background = pygame.image.load('Background.jpeg')
sprite_1 = pygame.image.load('Sprite1.png')
sprite_2 = pygame.image.load('Sprite2.png')

# Sound Resources
background_music = pygame.mixer.Sound('background music.ogg')
background_music.set_volume(.2)
background_music.play()

laser_beam = pygame.mixer.Sound('Laser Beam.wav')

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
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_speedx = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_speedy = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:
            laser_beam.play()
    # --- Game logic should go here
    x, y = pygame.mouse.get_pos()
    if x < 0:
        x = 0
    if x > screen_width - 121:
        x = screen_width - 121
    if y < 0:
        y = 0
    if y > screen_height - 217:
        y = screen_height - 217

    player_x += player_speedx
    if player_x < 0:
        player_x = 0
    if player_x > screen_width - 222:
        player_x = screen_width - 222

    player_y += player_speedy
    if player_y < 0:
        player_y = 0
    if player_y > screen_height - 174:
        player_y = screen_height - 174
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
    screen.blit(background, [0, 0])

    # --- Drawing code should go here
    screen.blit(sprite_1, [x, y])
    screen.blit(sprite_2, [player_x, player_y])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()