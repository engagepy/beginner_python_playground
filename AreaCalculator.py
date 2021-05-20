# create a shape area calculator. Input step 1, calculate step 2, output step 3
print ("Shape Calculator starting up....")
name = input("Enter C for circle or T for Traingle: ")
if name == "c":
  radius = float(input("Enter the radius :"))
  area = 3.14159*(radius**2)
  print ("Area is equal to " + str(area) + " .")
elif name == "t":
  base = float(input("Enter the base of the triangle :"))
  height = float(input("Enter the height of the triangle :"))
  area = 0.5*(base*height)
  print (" The area of the Triangle is " + str(area) + " ")
else:
  print ("Enter a valid shape. Try again.")
print ("Program Terminating")



