#31 = 25, 10, 1
def min_coins(cents):
	coins = [25, 10, 1]
	count = 0
	
	#if cents are greater than one, only then proceed!
	#Special case of cents under 35, being more suitable with 10
	if cents < 35:
		for i in (10, 1):
			count += cents / i 
			cents = cents % i
		return int(count)
	# regular case for cents >= 35
	elif cents >= 35:
		for i in coins:
			count += cents / i 
			cents = cents % i
		return int(count)
	# if zero cents provided

cents = int(input("Enter Cents?? "))
print(min_coins(cents))

	




