#creating the class
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus


class Menu:
#the constructor method using __init__ (self)
  def __init__(self, name, items, start_time, end_time):
#must initialise the parameters in a class via self.**
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
#another application of dunder method, string representation 
  def __repr__(self):
#assigning the representative_string required format and values
    self.representative_string = self.name + " menu is available from {}:00 to {}:00 hours.".format(self.start_time, self.end_time)
    return self.representative_string

#added new_method, takes items totals bill
  def calculate_bill(self, purchased_items):
    self.purchased_items = purchased_items
    self.total  = 0
    for i in purchased_items:
      item = self.items.get(i)
      self.total += item
    return self.total


#Using the menu class to create the menus
brunch = Menu('Brunch', {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 11, 16)

early_bird = Menu('Early-bird', {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
} , 15, 18)

dinner = Menu('Dinner', {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 17, 23)

kids = Menu('Kids', {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11, 21)

#testing string representation.

print (brunch.__repr__ ,"\n", early_bird.__repr__,"\n", dinner.__repr__,"\n", kids.__repr__,"\n")

#testing calculate_bill method of Menu()
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['mushroom ravioli (vegan)', 'salumeria plate']))
    
    
