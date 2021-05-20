from time import sleep

def take_input_1():
    print (" ")
    city = str(input("which city do you wish to travel to? \n Options are: delhi, kolkata, bombay, bengaluru : ").lower())
    print (" ")
    days = int(input("How many days are you travelling for? eg 1 - 100 : "))
    print (" ")
    spending_money = int(input("How much spending money do you plan on carrying?, eg 100 - 10000 : "))
    print ("Calculating...")
    sleep(3) 
    if len(city) > 0 and city.isalpha():
    	print (" ")
    else:
    	print ("Error ")
    	take_input_1()    	
    	if days > 0: 
    		print (" ")
    	else: 
    		print ("Error")
    		take_input_1() 
    		if spending_money > 0:
    			print (" ")
    		else:
    			print ("Error")
    			take_input_1()

    return city, days, spending_money, trip_cost(city,days,spending_money)


# segragating code for neatness. Trying to cover invalid inputs and loop to take_input_1()







# trying to collect user data



def hotel_cost(nights):
	return 10000 * nights

#the above does night calulation, convert to days minus 1 in final function

def plan_ride(city):
	if city == "delhi":
		return 9000
	elif city == "kolkata":
		return 4000
	elif city == "bombay":
		return 7000
	elif city == "bengaluru":
		return 5000

#this does the flight tariff calculation on approx

def car_rental(days):
	rent = 40 * days
	if days >= 7:
		rent -= 50
	elif days >= 3:
		rent -= 25
	return rent


# this does the calculation for car rental

def trip_cost(city, days, spending_money):
	x = hotel_cost(days-1) + plan_ride(city) + car_rental(days)
	print ("The cost of your trip including rental, flights and spending money is : " + str(x))



while True: 
	take_input_1()






