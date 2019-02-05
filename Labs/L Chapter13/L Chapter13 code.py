import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen_width = 700
screen_height = 400

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLACK)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.x <= -1:
            self.rect.x = 0
            bump.play()

        if self.rect.y <=-1:
            self.rect.y = 0
            bump.play()

        if self.rect.x >= screen_width - 14:
            self.rect.x = screen_width - 15
            bump.play()

        if self.rect.y >= screen_height - 14:
            self.rect.y = screen_height - 15
            bump.play()


class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """

    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """

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


# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen = pygame.display.set_mode([screen_width, screen_height])

my_font = pygame.font.SysFont('Helvetica', 30, True, False)

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
good_block_list = pygame.sprite.Group()
bad_block_list = pygame.sprite.Group()

# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    # This represents a block
    good_block = Block(GREEN, 20, 15)
    good_block.image = pygame.image.load('parker.png')

    # Set a random location for the block
    good_block.rect.x = random.randrange(screen_width - 20)
    good_block.rect.y = random.randrange(screen_height - 20)

    # Add the block to the list of objects
    good_block_list.add(good_block)
    all_sprites_list.add(good_block)

for i in range(50):
    # This represents a block
    bad_block = Block(RED, 20, 15)
    bad_block.image = pygame.image.load('latin.png')

    # Set a random location for the block
    bad_block.rect.x = random.randrange(screen_width - 20)
    bad_block.rect.y = random.randrange(screen_height - 20)

    # Add the block to the list of objects
    bad_block_list.add(bad_block)
    all_sprites_list.add(bad_block)

# Create a RED player block
player = Player(0, 0)
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0
cheer = pygame.mixer.Sound('Cheer.wav')
boo = pygame.mixer.Sound('boo.wav')
bump = pygame.mixer.Sound('edge.wav')

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)



    all_sprites_list.update()
    # Clear the screen
    screen.fill(WHITE)


    # See if the player block has collided with anything.
    good_blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
    bad_blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)

    my_text = my_font.render('Score:' + str(score), True, BLACK)
    screen.blit(my_text, [0, 370])

    # Check the list of collisions.
    for block in good_blocks_hit_list:
        cheer.play()
        score += 1
        print(score)

    for block in bad_blocks_hit_list:
        boo.play()
        score -= 1
        print(score)

    # Draw all the spites
    all_sprites_list.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()