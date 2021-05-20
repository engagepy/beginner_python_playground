#reverse_tax
#to reverse calculate pre tax price

from time import sleep

print('-------------------------------------------------------------------------------------------------------')
print('\n ReverZ Tax Calculator v1.0 \n')
print('Loading....... \n')
print('Ready! \n')

remember = []

def reverse_tax(tp,tax_percent):
	
	short_remember = []
	pre_tax_price  = tp / ((tax_percent /100) + 1 )
	tax_amount = tp - pre_tax_price
	print('\n >	Pre Tax Amount: {y}, \n >	Tax%: {x} \n >	Actual Tax: {z}'.format(x = float(tax_percent), y = float(pre_tax_price), z = float(tax_amount)))
	short_remember.append(tp)
	short_remember.append(tax_percent)
	short_remember.append(pre_tax_price)
	short_remember.append(tax_amount)
	remember.append(short_remember)
	x = 1
	print('\n Calculated So far: \n')
	print('+Tax Price')
	print('+Tax %')
	print('+Pre Tax Price')
	print('+Tax Amount')
	print('---------------')
	for i in remember:
		for z in i:
			print(x,"	",z)
		print('---------------')
		x += 1


	#print('\n Tax Amount is: {z}'.format(z = tax_amount ))

while True:
	tp = float(input(' \n Enter Tax inclusive Amout: '))
	tax_percent = float(input(' \n Enter tax percentage: '))
	reverse_tax(tp, tax_percent)



