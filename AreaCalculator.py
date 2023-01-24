# Purpose :Create a shape area calculator. 
# Step 1: Input , Step 2: Calculate , Step 3: Output

import time
print ("Shape Area Calculator starting up....")
# Delay of 1 second added .
time.sleep(1)
name = input("Enter C for Circle or T for Triangle: ")
if name == "c" or "C":
  radius = float(input("Enter the radius :"))
  area = 3.14159*(radius**2)
  print ("Area of the circle is " + str(area) + " .")
elif name == "t" or "T":
  base = float(input("Enter the base of the triangle :"))
  height = float(input("Enter the height of the triangle :"))
  area = 0.5*(base*height)
  print (" Area of the Triangle is " + str(area) + " ")
else:
  print ("Enter a valid shape. Try again.")
print ("Program Terminated.")



