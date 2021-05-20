

def partner_share(no_partners,share_percent,amount):

	share = amount * share_percent / 100

	for i in range(no_partners):
		print('\n Partner {} share is: {}'.format(i+1,share))

	balance = amount - (share * no_partners)
	
	if balance > 0:
		print('\n Balance amount to be covered is: {}'.format(balance))
		remaining_partners = int(input(' Remaining equal partners: '))
		share_rem_part = float(input(' Share % per partner: '))
		share_left = amount * share_rem_part / 100
		
		for i in range(remaining_partners):
			print('\n Partner {} share is: {}'.format(i+1,share_left))

		balance_last = balance - (share_left * remaining_partners)
		print('\n Balance left now: {} '.format(balance_last))
	

while True:
	print('\n Welcome to Partner_Share_Calculator'.upper())
	no_partners = int(input('\n Enter No. of equal partners: '))
	share_percent = float(input(' Enter share % per partner: '))
	amount = float(input(' Enter amount to be split: '))
	partner_share(no_partners,share_percent,amount)

