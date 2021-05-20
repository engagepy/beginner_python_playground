print("\n\n\n Welcome to Z Shipping \n\n")
print("We do shipping via 3 modes: \n +Ground \n +Drone \n +Premium Ground")
print(" \n 'AUTOMATED SELECTION ON WEIGHT = CHEAPEST SHIPPING FOR YOU.' \n\n")



def ground_shipping(weight):
  if weight <= 2:
    cost = weight * 1.50 + 20
    return cost
  elif weight > 2 and weight <= 6:
    cost = weight * 3 + 20
    return cost
  elif weight > 6 and weight <= 10:
    cost = weight * 4 + 20
    return cost
  else:
    cost = weight * 4.75 + 20
    return cost

premium_ground = 125

def drone_shipping(weight):
  if weight <= 2:
    cost = weight * 4.50
    return cost
  elif weight > 2 and weight <= 6:
    cost = weight * 9
    return cost
  elif weight > 6 and weight <= 10:
    cost = weight * 12
    return cost
  else:
    cost = weight * 14.25
    return cost

def cheapest_shipping(weight):
  if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_ground:
    print ("\nUse ground shipping.")
    ground_shipping(weight)
    print ("\nIt will cost INR: ", ground_shipping(weight), "\n\n")

  elif drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < premium_ground:
    print ("\nUse drone shipping. \n")
    drone_shipping(weight)
    print ("\nIt will cost INR: ", drone_shipping(weight), "\n\n" )
  else:
    print ("\nUse premium ground shipping")
    print ("\nIt will cost INR: ", premium_ground, "\n\n")

weight = float(input("Enter the weight of your package in kg: "))
cheapest_shipping(weight)
