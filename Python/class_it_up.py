#CLASS IT UP CODE

end = False

# students = ["Cal", "Sara", "Riley", "Sam"]

# name = ["0. Cal", "1. Sara", "2. Riley", "3. Sam"]
# hair_colour = ["brown", "blonde", "black", "red"]
# eye_colour = ["blue", "brown", "green", "hazel"]
# age = ["15", "16", "17", "18"]

class Student():
	def __init__(self, name, hair_colour, eye_colour, age):
		self.name = name
		self.hair_colour = hair_colour
		self.eye_colour = eye_colour
		self.age = age
	def conversation(self, greet, ask, describe, good_bye1, good_bye2):
		greet
		ask
		if ask == ("yes"):
			describe
			good_bye1
		else:
			good_bye2
		user_input2 = input("Would you like to meet someone else? ")
		if user_input2 == ("no"):
			end = True
		else:
			end = False

print ("Cal, Sara, Riley, Sam")
while end == False:

	user_input = input("Who would you like to meet? ")
	greet = print ("Hi! My name is" +name)
	ask = input("Can I tell you a bit about myself? ")
	describe = print ("I am " +(age)+ " years old. I have " +(hair_colour)+ " hair and " +(eye_colour)+ " eyes.")
	good_bye1 = print ("I have to go now. See you later!")
	good_bye2 = print ("Oh, ok. See you later then.")
	
	if user_input == ("Cal"):
		student = Student("Cal", "brown", "blue", "18")
		student.conversation(greet, ask, describe, good_bye1, good_bye2)
	elif user_input == ("Sara"):
		student = Student("Sara", "red", "brown", "16")
		student.conversation(greet, ask, describe, good_bye1, good_bye2)
	elif user_input == ("Riley"):
		student = Student("Riley", "blonde", "brown", "17")
		student.conversation(greet, ask, describe, good_bye1, good_bye2)
	else:
		student = Student("Sam", "black", "green", "15")
		student.conversation(greet, ask, describe, good_bye1, good_bye2)



