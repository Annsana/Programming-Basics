#defining a function for the cost of ground shipping
def ground_shipping(weight):
 
  if weight<=2:
    price_per_pound = 1.50
    flat_charge = 20.0
    print("price per pound = $1.50 and flat charge = $20.0")
  elif weight>2 and weight<=6:
     price_per_pound = 3.00
     flat_charge=20.0
     print("price per pound = $3.00 and flat charge = $20.0")
  elif weight>6 and weight<=10:
     price_per_pound = 4.00
     flat_charge = 20.0
     print("price per pound = $4.00 and flat charge = $20.0")
  else:
     price_per_pound = 4.75
     flat_charge = 20.0
     print("price per pound = $4.75 and flat charge = $20.0")
  cost_groundshipping=(weight * price_per_pound)+ (flat_charge)
  return cost_groundshipping
print("The cost of shipping through ground is $"+str(ground_shipping(8.4)))
#creating a variable for cost of ground shipping
premium_ground_shipping=125


#defining a function for the cost of drone shipping
def drone_shipping(weight):
  if weight<=2:
    price_per_pound = 4.50
    flat_charge = 0.0
    print("price per pound = $4.50 and flat charge = $0.0")
  elif weight>2 and weight<=6:
     price_per_pound = 9.00
     flat_charge=0.0
     print("price per pound = $9.00 and flat charge = $0.0")
  elif weight>6 and weight<=10:
     price_per_pound = 12.00
     flat_charge = 0.0
     print("price per pound = $12.00 and flat charge = $0.0")
  else:
     price_per_pound = 14.25
     flat_charge = 0.0
     print("price per pound = $14.25 and flat charge = $0.0")
  cost_droneshipping=(weight * price_per_pound)+ (flat_charge)
  return cost_droneshipping
print("The cost of shipping using drone is $"+str(drone_shipping(1.5)))

#defining a function to check which is the cheapest transportation facility
def cheapest_shipping(weight):
  ground=ground_shipping(weight)
  premium=premium_ground_shipping
  drone=drone_shipping(weight)
  if ground<premium and ground<drone:
    cost=ground
    print("You should ship using ground shipping,it will cost"+str(cost))
  elif premium<ground and premium<drone:
    cost=premium
    print("You should ship using premium shipping,it will cost"+str(cost))
  else:
    cost=drone
    print("You should ship using drone shipping,it will cost"+str(cost))
    
print(cheapest_shipping(4.8))
print(cheapest_shipping(41.5))
