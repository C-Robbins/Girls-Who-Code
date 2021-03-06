# """
#  Pygame base template for opening a window

#  Sample Python/Pygame Programs
#  Simpson College Computer Science
#  http://programarcadegames.com/
#  http://simpson.edu/computer-science/

#  Explanation video: http://youtu.be/vRB_983kUMc
# """

import pygame
import random
from random import randint


# Define some colors
PURPLE = (66,0,99)
BLUE = (0,0,255)
SLATE = (98,108,138)
AQUAMARINE = (0,230,161)
DARKBLUE = (8,53,150)
GREEN = (0,255,0)
DARKGREEN = (8,150,34)
LIME = (99,230,67)
RED = (255,0,0)
RASPBERRY = (232,30,77)
SUNSET = (252,85,58)
DUSKYROSE = (230,181,238)
CREAM = (231,240,156)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (127, 127, 127)



pygame.init()




# Set the width and height of the screen [width, height]

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Source of My Misery")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


possible_ball_colors = [GREEN, RED, BLUE, PURPLE, SLATE, DARKBLUE, DARKGREEN, LIME, SUNSET, DUSKYROSE, CREAM, RASPBERRY]


# BOUNCING BALL CLASS CODE  

class BouncingBall(): 

    # CONSTRUCTOR METHOD 
    def __init__(self, x_location, y_location, x_speed, y_speed, ball_size):  
    # Attributes of the bouncing ball 
        self.x_location = x_location
        self.y_location = y_location  
        self.x_speed = x_speed
        self.y_speed = y_speed 
        self.ball_size = ball_size 

    # BALL METHODS 
    # Flash and Bounce: The actions the ball can perform 
    def flashBounce(self, screen, colors, screen_width, screen_height):

        ball_color = random.choice(possible_ball_colors) # This is outside because of variable scoping.

        if self.x_location >= screen_width - self.ball_size or self.x_location < self.ball_size:
            self.x_speed = self.x_speed * -1

        if self.y_location >= screen_height - self.ball_size or self.y_location < self.ball_size:
            self.y_speed = self.y_speed * -1

        self.x_location += self.x_speed 
        self.y_location += self.y_speed 

        pygame.draw.circle(screen, ball_color, [self.x_location, self.y_location], self.ball_size)


# -------- Main Program Loop -----------
ball = BouncingBall(randint(300,450), randint(300,450), randint(5,10), randint(5,10), 30)  
ball2 = BouncingBall(randint(300,450), randint(300,450), randint(5,10), randint(5,10), 30)
ball3 = BouncingBall(randint(300,450), randint(300,450), randint(5,10), randint(5,10), 30)
ball4 = BouncingBall(randint(300,450), randint(300,450), randint(5,10), randint(5,10), 30)
ball5 = BouncingBall(randint(300,450), randint(300,450), randint(5,10), randint(5,10), 30)
ball6 = BouncingBall(randint(300,450), randint(300,450), randint(5,10), randint(5,10), 30) 
ball7 = BouncingBall(randint(300,450), randint(300,450), randint(5,10), randint(5,10), 30)  
ball8 = BouncingBall(randint(300,450), randint(300,450), randint(5,10), randint(5,10), 30)   
ball9 = BouncingBall(randint(300,450), randint(300,450), randint(5,10), randint(5,10), 30)  
ball10 = BouncingBall(randint(300,450), randint(300,450), randint(5,10), randint(5,10), 30)  
ball11 = BouncingBall(randint(300,450), randint(300,450), randint(5,10), randint(5,10), 30)  
ball12 = BouncingBall(randint(300,450), randint(300,450), randint(5,10), randint(5,10), 30)  
ball13 = BouncingBall(randint(300,450), randint(300,450), randint(5,10), randint(5,10), 30)  
ball14 = BouncingBall(randint(300,450), randint(300,450), randint(5,10), randint(5,10), 30)  
ball15 = BouncingBall(randint(300,450), randint(300,450), randint(5,10), randint(5,10), 30)  
ball16 = BouncingBall(randint(300,450), randint(300,450), randint(5,10), randint(5,10), 30)  
ball17 = BouncingBall(randint(300,450), randint(300,450), randint(5,10), randint(5,10), 30)  
ball18 = BouncingBall(randint(300,450), randint(300,450), randint(5,10), randint(5,10), 30)  
ball19 = BouncingBall(randint(300,450), randint(300,450), randint(5,10), randint(5,10), 30)  
ball20 = BouncingBall(randint(300,450), randint(300,450), randint(5,10), randint(5,10), 30)  

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
    screen.fill(AQUAMARINE) 
    
    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.

    ball.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball2.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball3.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball4.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball5.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball6.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball7.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball8.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball9.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball10.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball11.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball12.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball13.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball14.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball15.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball16.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball17.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball18.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball19.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball20.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)

    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE


