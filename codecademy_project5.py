hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#First, let’s sum up all the prices of haircuts.
total_price=0
for i in prices:
  total_price += i
  
average_price=total_price/len(prices)
print("Average Haircut Price: "+str(average_price))

#That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.
new_prices=[price-5 for price in prices]
print(new_prices)


#Carly really wants to make sure that Carly’s Clippers is a profitable endeavor. She first wants to know how much revenue was brought in last week.
total_revenue=0
for j in range(len(hairstyles)):
  total_revenue+=prices[j] * last_week[j]
print("Total Revenue : "+ str(total_revenue))

#Find the average daily revenue
average_daily_revenue = total_revenue/7

#Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.
cuts_under_30=[hairstyles[i] for i in range(len(hairstyles)) if new_prices[i]<30]
print(cuts_under_30)
