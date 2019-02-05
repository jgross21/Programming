"""
The objective of this game is to fill a give percentage of the screen by holding down the mouse key. When they mouse
key is down, the player is active and grows. With the mouse key is lifted, the rectangle is inactive and doesnt move.
If the active boxes collide with an enemy box, the player will die and then game will end. If the enemy box hits an
inactive box, that enemy will bounce off of it and the game will continue. The player will level up when they have
filled the given percentage of the screen. This will lead them to another level in which they have to fill more of the
screen with faster and more abundant enemy boxes in the way.

Ava Ori
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (100, 100, 255)
HOT_PINK = (255, 0, 255)
CYAN = (0, 255, 255)
Yellow = (255, 255, 0)
LIGHT_BLUE = (204, 252, 255)
LIGHT_PURPLE = (200, 196, 250)
MINT = (176, 255, 219)
BABY_PINK = (255, 224, 234)

pygame.init()  # Starts Pygame

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

enemy_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
active_block_group = pygame.sprite.Group()
stopped_block_group = pygame.sprite.Group()

pygame.display.set_caption("Filler Game")

# variables

level = 1
rect_area = 0
percentage = round(((rect_area / 350000) * 100))


# ENEMY

class Block(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """

    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

        # Instance variables that control the edges of where we bounce
        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0

        # Instance variables for our current speed and direction
        self.change_x = 0
        self.change_y = 0

    def update(self):
        """ Called each frame. """
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
            self.change_x *= -1

        if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1


# PLAYER

class Player(Block):
    """ The player class derives from Block, but overrides the 'update'
    functionality with new a movement function that will move the block
    with the mouse. """

    def update(self):
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()

        # Fetch the x and y out of the list,
        # just like we'd fetch letters out of a string.
        # Set the player object to the mouse location
        self.rect.x = pos[0]
        self.rect.y = pos[1]



class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0

        self.change_x = 0
        self.change_y = 0
    def update(self):

        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
            self.change_x *= -1

        if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1


block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

# CREATING ENEMY

for i in range(level * 10):
    # This represents a block
    enemy = Enemy(BLACK, 10, 10)

    # Set a random location for the block
    enemy.rect.x = random.randrange(screen_width)
    enemy.rect.y = random.randrange(screen_height)

    enemy.change_x = random.randrange(-3, 4)
    enemy.change_y = random.randrange(-3, 4)
    enemy.left_boundary = 0
    enemy.top_boundary = 0
    enemy.right_boundary = screen_width
    enemy.bottom_boundary = screen_height

    # Add the block to the list of objects
    block_list.add(enemy)
    all_sprites_list.add(enemy)
    enemy_group.add(enemy)


class ActiveBlock(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.color = color
        self.image.fill(color)
        self.active = True
        self.size = 10
        self.rect = self.image.get_rect()

    def update(self):
        if self.active:
            x = self.rect.centerx
            y = self.rect.centery
            if self.active:
                self.size += 1
            self.image = pygame.Surface([self.size, self.size])
            self.image.fill(self.color)
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


def cut_screen():
    done = False
    frame = 300
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONUP:
                done = True
        screen.fill(LIGHT_PURPLE)
        my_text = my_font.render("FILLER GAME", True, BLACK)
        my_text2 = my_font.render("Try to fill " + str(level * 10) + "% of the screen ", True, BLACK)
        my_text3 = my_font.render("while avoiding the black boxes!", True, BLACK)
        my_text4 = my_font.render("Press and hold to grow.", True, BLACK)
        my_text5 = my_font.render("Click anywhere to play...", True, BLACK)
        screen.blit(my_text, [250, 100])
        screen.blit(my_text2, [170, 130])
        screen.blit(my_text3, [150, 160])
        screen.blit(my_text4, [190, 190])
        screen.blit(my_text5, [170, 270])

        pygame.display.flip()
        clock.tick(60)


cut_screen()


def cut_screen2():
    done = False
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        screen.fill(LIGHT_PURPLE)
        my_text = my_font.render("YOU WIN", True, BLACK)
        my_text2 = my_font.render("Try to fill " + str(level * 10) + "% of the screen ", True, BLACK)
        my_text3 = my_font.render("while avoiding the black boxes!", True, BLACK)
        my_text4 = my_font.render("Press and hold to grow.", True, BLACK)
        my_text5 = my_font.render("Click anywhere to start next level...", True, BLACK)
        screen.blit(my_text, [250, 100])
        screen.blit(my_text2, [170, 130])
        screen.blit(my_text3, [150, 160])
        screen.blit(my_text4, [190, 190])
        screen.blit(my_text5, [170, 270])

        pygame.display.flip()
        clock.tick(60)

def cut_screen3():
    done = False
    my_font = pygame.font.SysFont("Calibri", 30, True, False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
           #if event.type == pygame.MOUSEBUTTONUP:
                 #done = True
        screen.fill(LIGHT_PURPLE)
        my_text = my_font.render("YOU LOST.", True, BLACK)
        screen.blit(my_text, [250, 100])

        pygame.display.flip()
        clock.tick(60)

size_y = 10
size_x = 10
size_x_speed = 3
size_y_speed = 3
_level = level


# -------- Main Program Loop -----------

while not done:
    x, y = (pygame.mouse.get_pos())

    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("DOWN")
            _level = level

            block = ActiveBlock(BABY_PINK, 10, 10)
            block.active = True
            block.rect.centerx, block.rect.centery = event.pos
            all_sprites_list.add(block)
            active_block_group.add(block)

        if event.type == pygame.MOUSEBUTTONUP:
            for block in active_block_group:
                block.active = False
                if block.active == False:
                    stopped_block_group.add(block)

            print("UP")
            if _level == level:
                rect_area += round(block.size ** 2)


    # --- Screen-clearing code goes here
    percentage = round(((rect_area / 350000) * 100))



    if percentage >= (level * 10):
        rect_area = 0
        size = 0
        level += 1
        all_sprites_list.empty()
        enemy_group.empty()
        active_block_group.empty()
        stopped_block_group.empty()
        block_list.empty()

        for i in range(level * 10):
            enemy = Block(BLACK, 10, 10)
            enemy.rect.x = random.randrange(screen_width)
            enemy.rect.y = random.randrange(screen_height)
            enemy.change_x = random.randrange(-3, 4)
            enemy.change_y = random.randrange(-3, 4)
            enemy.left_boundary = 0
            enemy.top_boundary = 0
            enemy.right_boundary = screen_width
            enemy.bottom_boundary = screen_height
            block_list.add(enemy)
            all_sprites_list.add(enemy)
        cut_screen2()

    all_sprites_list.update()

    for enemy in block_list:
        hit_list = pygame.sprite.spritecollide(enemy, active_block_group, False)
        for block in hit_list:
            if block.active == True:
                block.kill()
                cut_screen3()
                done = True
            else:
                enemy.change_x *= -1
                enemy.change_y *= -1

    for block in active_block_group:
        if block.rect.x <= 0 or block.rect.right >= 700:
            block.active = False
            stopped_block_group.add(block)

    for block in active_block_group:
        if block.rect.y <= 0 or block.rect.bottom >= 500:
            block.active = False
            stopped_block_group.add(block)

    for block in active_block_group:
        hit_list_two = pygame.sprite.spritecollide(block, stopped_block_group, False)
        for hit in hit_list_two:
            block.active = False
            stopped_block_group.add(block)


   #for block in stopped_block_group:
        #hit_list = pygame.sprite.spritecollide(block, stopped_block_group, False)
       # for block in hit_list:
           # if block.active == True:
               # block.active == False'''


    screen.fill(WHITE)
    all_sprites_list.draw(screen)

    # --- Drawing code should go here
    my_font = pygame.font.SysFont("Calibri", 20, True, False)
    my_text = my_font.render("Percentage Filled : " + str(round(((rect_area / 350000) * 100))) + "%", True, BLACK)

    screen.blit(my_text, [440, 10])
    # enemy_group.draw(screen)



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # enemy_group.move()
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()