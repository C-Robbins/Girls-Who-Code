import random
from random import randint

pokemon_list = ["ghastly","zubat","pidgey","magikarp","jynx","pikachu","dialga"]

play = True

class Pokemon():
	def __init__ (self, pokemon_type, name, cp, hp, attack_strength):
		self.pokemon_type = pokemon_type
		self.name = name
		self.cp = cp
		self.hp = hp
		self.attack_strength = attack_strength
	def get_status(self):
		self.get_status
		print(str(self.pokemon_type)+ ", " +str(self.name)+ ", Your CP: " +str(self.cp)+ ", Your HP: " +str(self.hp))
		return(self.pokemon_type, self.name, self.cp, self.hp)
	def rename(self):
		self.name = input("Give your Pokemon a nickname: ")
	def increase_cp(self, amount):
		self.cp = self.cp + amount
	def decrease_cp(self, amount):
		self.cp = self.cp - amount
	def is_attacked(self, damage):
		self.hp = self.hp - damage
	def attack(self, another, attack_strength):
			print ("A wild " +another+ " appeared!")
			if self.cp <= 20:
				attack_strength = attack_strength*1
			elif self.cp > 20 and self.cp <= 40:
				attack_strength = attack_strength*2
			elif self.cp > 40 and self.cp <= 60:
				attack_strength = attack_strength*3
			elif self.cp > 60 and self.cp <= 80:
				attack_strength = attack_strength*4
			elif self.cp > 80 and self.cp <= 100:
				attack_strength = attack_strength*5
			hit = randint(0,1)
			if hit == 0:
				print("Your attack was successful")
				self.increase_cp(5)
			elif hit == 1:
				print("Your attack missed! Your enemy counter attacked")
				self.decrease_cp(5)
				self.is_attacked(15)
			print("Your hp = " + str(self.hp))
			# self.get_status()
			# if self.cp <= 0 or self.hp <= 0:
			# 	print ("You can't battle anymore. Game over")
			# 	play = False
			# else:
			# 	play = True
class ghastly(Pokemon):
	def __init__(self, my_attack):
		self.my_attack = "nightshade"
	def special_attack(self, my_attack_strength):
		self.my_attack_strength = attack_strength+5
	def string_to_attack (self, other_pokemon):
		

class zubat(Pokemon):	
	def __init__(self, my_attack, my_attack_strength):
		self.my_attack = "confusion"
	def special_attack(self, my_attack_strength):
		self.my_attack_strength = attack_strength+5

class pidgey(Pokemon):
		
	def special_attack(self, fly):
		self.fly = attack_strength+10

class magikarp(Pokemon):

	def special_attack(self, splash):
		self.splash = attack_strength+1

class jynx(Pokemon):
		
	def special_attack(self, psychic):
		psychic = attack_strength+10

class pikachu(Pokemon):
		
	def special_attack(self, thunderbolt):
		thunderbolt = attack_strength+10

class dialga(Pokemon):
		
	def special_attack(self, dragon_breath):
		dragon_breath = attack_strength+15

other_pokemon = Pokemon(pokemon_list[randint(0,6)], "0", 10, 100, 10) 
my_pokemon = Pokemon(pokemon_list[randint(0,6)], "0", 10, 100, 10)
my_pokemon.get_status()
my_pokemon.rename()

# while play == True:
my_pokemon.get_status()
my_pokemon.attack(other_pokemon, 10) 
user_input = input("Play on? ")
	# if user_input == ("yes"):
	# 	play = True
	# elif user_input == ("no"):
	# 	play = False	
# print ("Thanks for playing!")


