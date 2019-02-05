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

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

player = Block()
all_sprites_group = pygame.sprite.Group()
all_sprites_group.add(player)

good_block_group = pygame.sprite.Group()

for i in range(10000):
    good_block = Block()
    good_block.image.fill(GREEN)
    good_block.rect.x = random.randrange(screen_width - good_block.rect.width)
    good_block.rect.y = random.randrange(screen_width - good_block.rect.height)
    all_sprites_group.add(good_block)
    good_block_group.add(good_block)

score = 0
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    x, y = pygame.mouse.get_pos()
    player.rect.centerx = x
    player.rect.centery = y

# (what's looking to colide, group it's going to colide with, do you want to kill it)
    hit_list = pygame.sprite.spritecollide(player, good_block_group, True)
    for block in hit_list:
        score += 1
        '''
        print(score)
        new_size = player.rect.width + 2
        player.image = pygame.Surface([new_size, new_size])
        player.image.get_rect()
        player.image.fill(BLUE)
        '''
    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here
    all_sprites_group.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()