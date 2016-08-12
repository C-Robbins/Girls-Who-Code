#Free Code Robbins
#USE ctrl+f TO NAVIGATE HEADERS
#HEADERS TYPED IN CAPS 
#INDEX: LOOP START / GAME 1 / COLOUR GUESS PLAY LOOP / PLAY LOOP1 END / GAME 2 / ROLL A DIE PLAY LOOP / PLAY LOOP2 END / 
#GAME 3 / LOOP END A1 / LOOP END A2 / LOOP END A3 /

keep_playing = (True)
from random import randint
import webbrowser

print ("Hi! Welcome to my free code project. Here are a few games you can play: ")

while keep_playing == (True): #LOOP START
	print ("1. Colour Guess")
	print ("2. Roll a Die")
	print ("3. Bored Button")
	user_input = input("Press a number to select, and have fun! ")
	if user_input == ("1"): #GAME 1. Colour Guess
		print ("Welcome to Colour Guess")
		win = (False)
		while win == (False): #COLOUR GUESS PLAY LOOP
			user_guess = input("Try to guess my favourite colour. If you get it right, you win! : ")	
			if user_guess == ("purple"):
				print ("Congrats! You got it.")
				win = (True) #PLAY1 LOOP END
			else:
				print ("Sorry, not quite. Try again!")
		user_input2 = input("Would you like to play more games? ")
		if user_input2 == ("no"):
			keep_playing = (False) #LOOP END A1
		else:
			print ("Okay! Pick a new game: ")
	elif user_input == ("2"): #GAME 2 Roll a die
		print ("Welcome to Roll a Die")
		print ("Try to match the set number.")
		same = (False)
		while same == (False): #ROLL A DIE PLAY LOOP
			random = input("Press 1 to set a random number: ")
			if random == ("1"):
				num_set = str(randint (1,6))
				print ("Number set: " + num_set)
				user_roll = input("Press 2 to roll the die: ")
				if user_roll == ("2"):
					roll = str(randint (1,6))
					if roll == num_set:
						print ("Your roll: " +roll)
						print ("You rolled the same!")
						same = (True) #PLAY2 LOOP END
					else:
						print ("Your roll: " +roll)
						print ("Not quite.")
						user_input4 = input("Would you like to keep playing? ")
						if user_input4 == ("no"):
							same = (True) #PLAY2 LOOP END
						else:	
							same = (False)
							print ("Okay, let's go!")
			else:
				print ("Please set a number.")
		user_input2 = input("Would you like to play more games? ")
		if user_input2 == ("no"):
			keep_playing = (False) #LOOP END A2
		else:
			print ("Okay! Pick a new game: ")
	elif user_input == ("3"): #GAME 3. Bored Button		
		print ("Bored Button will take you to a website to occupy your boredom.")
		user_input3 = input("Go online? ")
		if user_input3 == ("yes"):
			webbrowser.open_new_tab("http://www.boredbutton.com/")
		else:
			user_input2 = input("Would you like to play more games? ")
			if user_input2 == ("no"):
				keep_playing = (False) #LOOP END A3
			else:
				print ("Okay! Pick a new game: ")
	else:
		print ("Please select a game to play.")

print ("Game End. Hope you had fun!")

