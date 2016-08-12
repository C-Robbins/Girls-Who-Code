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
PURPLE = (66,0,99)
BLUE = (0,0,255)
SLATE = (98,108,138)
AQUAMARINE = (0,230,161)
GREEN = (0,255,0)
LIME = (99,230,67)
RED = (255,0,0)
SUNSET = (252,85,58)
DUSKYROSE = (230,181,238)
CREAM = (231,240,156)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (127, 127, 127)



pygame.init()

# Set the width and height of the screen [width, height]
# SCREEN_WIDTH = 700
# SCREEN_HEIGHT = 500

clock = pygame.time.Clock()
screen_size = (700, 500)
screen1 = pygame.display.set_mode(screen_size)


pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False
#------Main Programme Loop------
while not done:
#----Main Event Loop----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen1.fill(GREEN)
    pygame.draw.circle(screen1, SLATE, (350,150), 30, 0)

# WRITE YOUR CODE HERE







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



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
