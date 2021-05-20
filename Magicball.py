import random
name = input("Enter your name:  ")
print("\n")
question = input("Enter your Yes or No question:  ")
answer = " "
random_number = random.randint(1,9)
#print(random_number)
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "It is decidedly so."
elif random_number == 5:
  answer = "Reply hazy, try again."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "Outlook not so good."
elif random_number == 8:
  answer = "Very doubtful."
else:
  answer = "Error"

print(name + " asks: " + question +" ?")
print("\n")
print("Magic ball answers: " + answer)







