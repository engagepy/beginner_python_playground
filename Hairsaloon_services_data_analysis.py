ex#types of product/ services with no repeat items or duplciates
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

#princes for product, len(product) has to equal len(price)
prices = [30, 25, 40, 20, 20, 35, 50, 35]

#data set of products sold, weekly, can be any unit of time
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#main for data analysis
total_price = 0
for i in prices:
  total_price += i 
  #print(i)

#total/ avg inventory cost
print('Total Price:', total_price)
average = total_price/len(prices)
print('Average Haircut Price:', int(average))

#create new prices
new_prices = [x - 5 for x in prices]
print(new_prices)

#Old data set analysis for revenue in given timeline
total_revenue = 0
for i in range(len(hairstyles)):
  x = (prices[i] * last_week[i])
  print('Average Price per cut:', x)
  total_revenue += x
print('Total Revenue Last week:', total_revenue)
average_daily_revenue = total_revenue/7
print('Avg Daily Revenue:', average_daily_revenue)


#marketing/highlighting price filter based products for customer
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print('Cuts under 30: ', cuts_under_30)



