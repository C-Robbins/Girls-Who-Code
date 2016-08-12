#Pygame 1
import pygame 

#define some colours, maaaaaan
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

pygame.init() 
clock = pygame.time.Clock()#screen update time
screen_size = (700, 500)
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("Cat's Game")

done = False
#------Main Programme Loop------
while not done:
#----Main Event Loop----
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	#Do the stuff here
	screen.fill(PURPLE) #CLEAR
	pygame.draw.line(screen,LIME,(100,350),(300,350))
	pygame.display.flip()
	clock.tick(60)#60 frames/sec

pygame.quit()#QUIT YOU LOSER
exit()










