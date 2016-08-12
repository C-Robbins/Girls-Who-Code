import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")


class Snowflake():
	'''
	==========================================TASK ONE=========================================
	This class will be used to create the Snowflake objects.
	It takes as a parameter: 
		* size - an integer that tells us how big we want the snowflake to be
		* position - a tupe that tells us the coordinates of the snowflake (x,y) 
		* wind - a boolean that lets us know if there is any wind or not. 
				wind is automatically set to False.
	'''
	def __init__(self, size, position, wind=False):
		# define the __init__ function here! 
		self.size=size
		self.position=position
		self.wind=wind
	
	def fall(self, speed):
		"""
		==========================================TASK TWO=========================================
		This class updates the y position of the Snowflake by the speed at which it is falling to 
		simulate a falling snowflake. If wind == True, the x direction of the snowflake changes
		by a random amount in the same direction, simulating wind blowing the snowflakes horizontally. 
		
		fall takes as a parameter:
			* speed - an integer that represnts the speed at which the snowflake is falling 
					in the y-direction.  
					A positive integer will have the snowflake falling down the screen. 
					A negative integer will have the snowflake falling up the screen. 
		"""
		if self.wind==True:
			speed[0]=random.randint(-10,-5)
		else:
			self.position[0]+=speed[0]
		self.position[1]+=speed[1]
		
	def draw(self):
		"""
		==========================================TASK THREE=========================================
		Draws this Snowflake on the screen using the pygame.draw.circle method and this 
		Snowflake's attributes.
		"""
		pygame.draw.circle(screen, (255,255,255), self.position, self.size)
		

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Speed
speed = 1

# this list will hold our snowflakes
snow_list = []

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
	screen.fill(BLACK)

	# --- Drawing code should go here
	# Begin Snow
	
	'''
	==========================================TASK FOUR=========================================
	Create an instance of your Snowflake object with a random x position and y position = 0 
	(because snowflakes fall from the sky!). Add this new Snowflake to the list snow_list.
	'''
	snow=Snowflake(3,[random.randint(0,700),0], True)
	snow_list.append(snow)

	'''
	==========================================TASK FIVE=========================================
	For every flake in snow_list, draw the flake and then call fall() to have it update its 
	position to simulate a fall. 
	'''
	for sf in snow_list:
		sf.draw()
		sf.fall([0,10])
	# End Snow

	# --- Update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(5)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
