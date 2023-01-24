#Purpose : To calculate BMI
# Step 1: Take input , Step 2: To check if height is valid , Step 3:
def take_input():
    try:

        print (" ")
        name = input("Your name: ")
        print (" ")
        height = float(input("Your Height in meters, eg 1.5 = ")) 
        print (" ")
        weight = float(input("Your Weight in Kilograms, eg 70 = "))
        return name, height, weight
    except ValueError:
        print('INCORRECT ENTRY')
        

def height_unit_check(height):
    # 2.72 m is the recorded height for the tallest human ever.
    if height >= 2.72:
        print ("")
        print ("My ego ain't that tall, are you sure you are. Try again!")
    elif height == 0 :
        print ("")
        print ("Cant be that small. Grow up a little!")
    else:
        BMI_CAL(name,height,weight)


def BMI_CAL(name,height,weight):
    float_x = weight/height**2
    print (" ")
    print ("Hi" + " " + str(name))
    print (" ")
    print ("Your BMI is: " + str(float_x))
    print ( " ")
    
    if float_x == 25.00:
        print ("You are on the fine line leaning towards the Dark Side, Start working out!")
    elif float_x > 25.00 :
        print ("You have joined the Dark Side.If you care about your smile and want to keep it. Start working out today!")
    elif float_x <= 18.5 :
        print ("You are underweight my friend!")
    else: 
        print ("You are fit and fine smile away!")

while True: 
	name, height, weight = take_input()
	height_unit_check(height)


#try:
#    height_unit_check
#except unit_input_error:
#    print ("My ego ain't that tall, are you sure you are. Try again!")
