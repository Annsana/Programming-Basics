#declaring variables globally
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

#defining a function to convert fahrenheit to celcuis
def f_to_c(f_temp):
  c_temp = ((f_temp) - 32) * 5/9
  return c_temp
#calling the function
f100_in_celsius=f_to_c(100)

#defining a function to convert celcuis to fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return(f_temp)
#calling the function c_to_f
c0_in_fahrenheit=c_to_f(0)

#defining a function to find the force
def get_force(mass,acceleration):
  return(mass*acceleration)
train_force=get_force(train_mass,train_acceleration)
print("The GE train supplies "+ str(train_force))

#defining a function to find energy
def get_energy(mass,c):
  return(mass*c)
bomb_energy=get_energy(bomb_mass,3*10**8)
print("A 1kg bomb supplies "+ str(bomb_energy)+  " Joules.")

#defining a function to find work
def get_work(mass,acceleration,distance):
  work=train_force*distance
  return(work)
train_work=get_work(train_mass,train_acceleration,train_distance)
print("The GE train does "+ str(train_work)+ " Joules of work over " +str(train_distance)+ " meters.")

  


  
