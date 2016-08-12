
# Pygame base template for opening a window

# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/

#  Explanation video: http://youtu.be/vRB_983kUMc
# 

import pygame
import random 
from random import randint

PURPLE = (66,0,99)
BLUE = (0,0,255)
SLATE = (98,108,138)
AQUAMARINE = (0,230,161)
DARKBLUE = (8,53,150)
GREEN = (0,255,0)
DARKGREEN = (8,150,34)
LIME = (99,230,67)
RED = (255,0,0)
SUNSET = (252,85,58)
DUSKYROSE = (230,181,238)
CREAM = (231,240,156)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (127, 127, 127)

pygame.init()

clock = pygame.time.Clock()
screen_size = (700, 500)
screen = pygame.display.set_mode(screen_size)

colours = [PURPLE,BLUE,SLATE,AQUAMARINE,DARKBLUE,GREEN,LIME,RED,SUNSET,DUSKYROSE,CREAM,WHITE,BLACK,GREY]

pygame.display.set_caption("Less Evil But Still A Butt")


x = 350
y = 250
done = False



while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(DARKGREEN)
    if x > 0:
        x = (x*1)
        y = (y*-1)
        pygame.draw.circle(screen, colours[randint(0,13)], (x,y), 30, 0)
        pygame.display.flip()
    elif x < 700:
        x+=(randint(5,15))
        y+=(randint(5,10))
        pygame.draw.circle(screen, colours[randint(0,13)], (x,y), 30, 0)
        pygame.display.flip()    
    elif y > 0:
        x+=(randint(5,15))
        y+=(randint(5,10))
        pygame.draw.circle(screen, colours[randint(0,13)], (x,y), 30, 0)
        pygame.display.flip()
    elif y < 500:
        x+=(randint(5,15))
        y+=(randint(5,10))
        pygame.draw.circle(screen, colours[randint(0,13)], (x,y), 30, 0)
        pygame.display.flip()

    clock.tick(10)
    # pygame.ball.move((randint(1-700,),randint(1-500)))

    # --- Game logic should go here

# --- Screen-clearing code goes here

# Here, we clear the screen to white. Don't put other drawing commands
# above this, or they will be erased with this command.

# If you want a background image, replace this clear with blit'ing the
# background image.
# screen.fill(WHITE)

# --- Drawing code should go here
    


pygame.quit()
exit()
