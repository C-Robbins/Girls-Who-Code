print ("This is our madlib!! Have fun!")

difficulty = input("Press 1 or type 'easy' to play on easy. Press 2 or type 'medium' to play on medium. Press 3 or type 'hard' to play on hard.")

if difficulty == ("1") or difficulty == ("easy") :
	print ("You chose easy")
	Adjective1 = input ("Pick an adjective")
	Name1 = input ("Pick a person's name")
	Name2 = input ("Pick another person's name")
	Noun1 = input ("Pick any noun")
	Verb1 = input ("Pick a verb")
	Noun2 = input ("Pick another noun")
	print ("One " + Adjective1 + " day, " + Name1 + " and " + Name2 + " went to the beach! They decided to take " + Noun1 + " and " + Noun2 + " with them because " + Name1 + " wanted to " + Verb1 + " the " + Noun2 + ".")
	print ("FIN!")
elif difficulty == ("2") or difficulty == ("medium"):
	print ("You chose medium")
	Adjective1 = input ("Pick an adjective")
	Name1 = input ("Pick a person's name")
	Name2 = input ("Pick another person's name")
	Noun1 = input ("Pick any noun")
	Noun2 = input ("Pick another noun")
	Name3 = input ("Pick another name")
	Verb1 = input ("Pick a verb")
	Exclamation = input ("Pick an exclamation")
	print ("One " + Adjective1 + " day, " + Name1 + " and " + Name2 + " went to the beach! They decided to take " + Noun1 + " and " + Noun2 + " with them because " + Name1 + " wanted to " + Verb1 + " the " + Noun2 + ". As they reached the water," + Name3 + " shouted '" + Exclamation + ", you guys!'")
	print ("FIN!")
elif difficulty == ("3") or difficulty == ("hard"):
	print ("You chose hard")
	Adjective1 = input ("Pick an adjective")
	Name1 = input ("Pick a person's name")
	Name2 = input ("Pick another person's name")
	Noun1 = input ("Pick any noun")
	Noun2 = input ("Pick another noun")
	Name3 = input ("Pick another name")
	Verb1 = input ("Pick a verb")
	Exclamation = input ("Pick an exclamation")
	Verb2 = input ("Pick another verb +ing")
	Adjective2 = input ("Pick another adjective +ed")
	Emotion = input ("Pick an emotion")
	Verb3 = input ("Pick another verb +ed")
	print ("One " + Adjective1 + " day, " + Name1 + " and " + Name2 + " went to the beach! They decided to take " + Noun1 + " and " + Noun2 + " with them because " + Name1 + " wanted to " + Verb1 + " the " + Noun2 + ". As they reached the water, " + Name3 + " shouted '" + Exclamation + ", you guys!' " + Name1 + " and " + Name2 + " started " + Verb2 + " because they were " + Adjective2 + " to see " + Name3 + ". " + Name3 + " felt " + Emotion + " after " + Name1 + " and " + Name2 + " " + Verb3 + ". The " + Noun2 + " came to life and attacked them all!") 
	print ("FIN!")
else:
	print ("Please pick a difficulty.")