#To keep track of the kinds of pizzas you sell, create a list
toppings=["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
#To keep track of how much each kind of pizza slice costs, create a list
prices=[2, 6, 1, 3, 2, 7, 2]
#To find the length of toppings
num_pizzas=len(toppings)
print("We sell "+str(num_pizzas)+ " different kinds of pizza!")
pizzas=list(zip(prices,toppings))
print(pizzas)
sorted_pizzas=pizzas.sort()
print(pizzas)
cheapest_pizza=pizzas[0]
print(cheapest_pizza)

#A man in a business suit walks in and shouts “I will have your MOST EXPENSIVE pizza!”Give him the last item in pizzas
priciest_pizza=pizzas[-1]
print(priciest_pizza)

#Three mice walk into the store. They don’t have much money (they’re mice), but they do each want different pizzas.
three_cheapest=pizzas[:3]
print(three_cheapest)

#Your boss wants you to do some research on $2 slices.
num_two_dollar_slices=prices.count(2)
print(num_two_dollar_slices)
