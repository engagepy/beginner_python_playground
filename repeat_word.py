# fun night code in learning stage
# figuring range and repetition 
from time import sleep
word=str(input("Enter a word to see it printed repeatedly: "))
times=int(input("How many times do you wish to repeat it?: "))
def print_times_100(word):
	a=1
	for i in range(times):
		print(str(a), word)
		a=a+1

	
print_times_100(word)
print ("Auto Close in 3 seconds")
sleep(2)
