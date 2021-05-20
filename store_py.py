from math import floor, ceil

# Store items :-
store_items = {
    'Potato':30,
    'Egg':3, 
    'Apple':300, 
    'Chicken':220,
    'Soap':10,
    'Onion':90,
    'Oil':150,'Juice':100
    }

# user bought :-
user_bought = {}

# printing store items
print('\nWelcome to Z Store. Please go ahead to buy something.\nOur store has :->\n')
for product, price in store_items.items():
    if ('Oil'in product) or ('Juice'in product):
        print(f'{product} : R {price}/liter.')
    elif ('Egg' in product) or ('Soap' in product):
        print(f'{product} : R {price}/piece.')
    else:
        print(f'{product} : R {price}/Kg.')
print('\n')


#function to take correct inputs only
while True:
    products = input('What do you want : ').title() 
    if products not in store_items:
        products = input('What do you want : ').title() 
    elif ('Oil' in products) or ('Juice'in products):
        quantities = int(input('How much do you want in liter : '))

    elif ('Egg' in products) or ('Soap' in products):
        quantities = float(input('How much do you want in piece : '))
    else:
        quantities = float(input('How much do you want in Kg. : '))

    user_bought[products] = quantities

#User continuation check
    user_said = input('Want more ? (Y/N) : ').lower()

    if ('y' in user_said) and ('n' in user_said) and (user_said != True):
        user_said = input('Invalid keyword. Type again : ')

    elif 'y' in user_said:
        continue
    else:
        break
    
        

# printing products with the total value
total = 0
print('\n')
for product, quantity in user_bought.items():
    total += store_items[product] * quantity
    x=int(total)

# adding round off feature to ease payment (Indian:)    
    if total-x >=.5:
        total = ceil(total)
    else:
        total = floor(total)
    if ('Oil' in product) or ('Juice'in product):
        print(f'{product} :R {store_items[product]}/ liter X {quantity} units=  R {store_items[product] * quantity}')
    elif ('Egg' in product) or ('Soap' in product):
        print(f'{product} :R {store_items[product]}/ piece X {quantity} units=  R {store_items[product] * quantity}')
    else:
        print(f'{product} :R {store_items[product]}/ kg X {quantity} units=  R {store_items[product] * quantity}')

print(f'\nYour total price INR {total}')

# pay the money :-
while True:
    money_input = float(input('\nPay the amount :R '))
    if money_input == total:
        print('Thank you for payment\nVisit again :)')
        break
    else:
        print('Please pay the correct amount.')
        continue
