# Purpose : 1) To add two float numbers. 2) Delay the output by 2 seconds

import time
a=float(input("Enter a Number: "))
b=float(input("Enter a Number: "))

# Checking time before and after execution of sum.

print ("After Input : %s" %time.ctime())
time.sleep(2)
print("This is the sum total of numbers enters!", a+b )
print ("After Execution : %s" %time.ctime())


