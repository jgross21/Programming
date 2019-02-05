
# 1.) Write a Python program that will print the following:
#
# 10
# 11 12
# 13 14 15
# 16 17 18 19
# 20 21 22 23 24
# 25 26 27 28 29 30
# 31 32 33 34 35 36 37
# 38 39 40 41 42 43 44 45
# 46 47 48 49 50 51 52 53 54
# Tips for Part 1
# Generate the output for part one using two for loops, one nested.
# To start, go back to chapter 6 and remember how to create a triangle of asterisks. Recreate that.
# Then create a new variable. Don't use i, j, row, or column, or whatever you already used.
# Set it to your starting value. Print that.
# This problem requires a bit of an “a-ha” to get. Make sure to ask around if you have problems.
# My students often find it to be one of the harder problems in this course.

print('1.)')
q = 10
for row in range (9):
    for column in range (row+1):
        print(q, end=' ')
        q += 1
    print()

# 2.) Create a big box out of n rows of little o's for any desired size n.
# Use an input statement to allow the user to enter the value for n and then print the properly sized box.
#
# E.g. n = 3
# oooooo
# o    o
# oooooo
#
# E.g. n = 8
# oooooooooooooooo
# o              o
# o              o
# o              o
# o              o
# o              o
# o              o
# oooooooooooooooo
# Tip: Break this problem into parts. First, draw the first line with the proper number of o's:
#
# oooooo
# Then, draw the last line too:
#
# oooooo
# oooooo
# Then, print an o between them:
#
# oooooo
# o
# oooooo
# Then repeat it:
#
# oooooo
# o
# o
# o
# o
# oooooo
# Then add another one:
#
# oooooo
# oo
# oo
# oo
# oo
# oooooo
# Then add spaces:
#
# oooooo
# o    o
# o    o
# o    o
# o    o
# oooooo
print('2.)')
n = abs(int(input('How many rows of o\'s do you want')))
for column in range (2 * n):
    print('o', end='')
print()
for row in range (n-2):
    print('o', end='')
    for row in range (2 * n-2):
        print(' ', end='')
    print('o', end='')
    print()
for column in range (2 * n):
    print('o', end='')
# Print the following for any positive integer n.
# Use an input statement to allow the user to enter the value for n and then print the properly sized box.

'''
E.g. n = 3
 
1 3 5 5 3 1
3 5     5 3
5         5
5         5
3 5     5 3
1 3 5 5 3 1
 
E.g. n = 5

1 3 5 7 9 9 7 5 3 1
3 5 7 9     9 7 5 3
5 7 9         9 7 5
7 9             9 7
9                 9
9                 9
7 9             9 7
5 7 9         9 7 5
3 5 7 9     9 7 5 3
1 3 5 7 9 9 7 5 3 1
Don't worry about handling the spacing for multi-digit numbers. 
Chapter 20 covers this if you want to look ahead, but it isn't needed.
'''
print('\n3.)')
n = abs(int(input('How big do you want your box?')))
for row in range (n):
    for column in range (n):
        print(2 * row + 2 * column + 1, end=' ')
    print()
# ??????????

# 4.)
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
screen_width = 700
screen_height = 500
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

    # If you want a background image, replace this clear with blitting the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here
    for x in range (0, 700, 20):
        for y in range (0, 500, 20):
            pygame.draw.rect(screen, MAGENTA, [x, y, 10, 10])


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()