def start() :
    print ("\n\nWelcome to the converter toolkit made by Z.\n")
    op = input ("Please input what operation you wish to perform.\n \n 1 for Fahrenheit to Celsius,\n 2 for meters to centimetres \n 3 for megabytes to gigabytes\n q to QUIT \n\n")


    if op == "1":
        f1 = input ("\nPlease enter fahrenheit unit: \n")
        f1 = int(f1)

        a1 = (f1 - 32) / 1.8
        a1 = str(a1)
        print("\n")

        print (a1+" celsius") 


    elif op == "2":
        m1 = input ("\nPlease input meters unit: \n")
        m1 = int(m1)
        m2 = (m1 * 100)

        m2 = str(m2)
        print("\n")
        print (m2+" m")


    elif op == "3":
        mb1 = input ("\nPlease input megabytes unit: \n")
        mb1 = int(mb1)
        mb2 = (mb1 / 1024)
        mb3 = (mb2 / 1024)
        mb3 = str(mb3)
        print("\n")
        print (mb3+" GB")


    elif op.lower() in {'q', 'quit', 'e', 'exit'}:
        print("\n\nGoodbye!")
        exit()

    else:
        print ("\nSorry, that was an invalid command!\n")

    


while True:
    start()