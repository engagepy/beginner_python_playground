# dice guess game
from random import randint
from time import sleep

def user_guess():
	guess = int(input("Please enter your guess: "))
	return guess

def suspense():
	sleep(1) 
	print (".") 
	sleep(1) 
	print ("..") 
	sleep(1) 
	print("... \n")


def dice_roll(sides):
	first_roll = randint (1,sides)
	second_roll = randint (1,sides)
	max_value = sides * 2
	print ("   Dice Game On! \n")
	print ("Max possible value is = %d \n" % max_value) 
	sleep(1)
	guess = user_guess()
	print (" ")
	if guess > max_value:
		print ("hey guess within limts? \n \n")
		sleep(1)
		print ("Try again now \n")
	else:
		print ("Rolling... \n")
		sleep(1)
		print ("First roll is = %d \n" % first_roll)
		sleep(1) 
		print ("Rolling second... \n")
		sleep(1)
		print ("Second roll is = %d \n" % second_roll) 
		total_roll_value = first_roll + second_roll
		sleep(1)
		print ("Total value of both roles is = %d \n" % total_roll_value)
		sleep(1) 
		print ("Results \n" ) 
		suspense()
		if guess == total_roll_value:
			print ("You guessed right, 6th sense alive! \n")
			print ("Try again now \n")
		else:
			print ("You guessed wrong, don't go gambling today \n")
			print ("Try again now \n")

while True:
  dice_roll(6)





