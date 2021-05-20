# Store items :-
store_items = {
    'Potato':2,
    'Egg':0.2, 
    'Apple':1, 
    'Chicken': 5,
    'Soap':1,
    'Onion':1.5,
    'Oil':1.2
    }

# user bought :-
user_bought = {}

# printing store items
print('\nWelcome to Z Store. Please go ahead to buy something.\nOur store has :->\n')
for product, price in store_items.items():
    if 'Oil' in product:
        print(f'{product} : ${price}/liter.')

    elif ('Egg' in product) or ('Soap' in product):
        print(f'{product} : ${price}/piece.')
    else:
        print(f'{product} : ${price}/Kg.')
print('\n')

# asking user for the list
while True:
    products = input('What do you want : ').title()
    if 'Oil' in products:
        quantities = float(input('How much do you want in liter : '))

    elif ('Egg' in products) or ('Soap' in products):
        quantities = float(input('How much do you want in piece : '))
    else:
        quantities = float(input('How much do you want in Kg. : '))

    user_bought[products] = quantities
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
        total =  total
    else:
        total = total-(total-x)
    if 'Oil' in product:
        print(f'{product} :${store_items[product]}/liter X {quantity}liter =  ${store_items[product] * quantity}')

    if ('Egg' in product) or ('Soap' in product):
        print(f'{product} :${store_items[product]}/piece X {quantity}piece =  ${store_items[product] * quantity}')
    else:
        print(f'{product} :${store_items[product]}/Kg. X {quantity}Kg. =  ${store_items[product] * quantity}')

print(f'\nYour total price ${total}')

# pay the money :-
while True:
    money_input = float(input('\nPay the amount :$'))
    if money_input == total:
        print('Thank you for payment\nVisit again :)')
        break
    else:
        print('Sorry please pay the correct amount.')
        continue