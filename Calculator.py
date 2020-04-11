#Program to create a four function calculator 
result = 0 
# To get the input from user
val1 = float(input("Enter value 1: ")) 
val2 = float(input("Enter value 2: ")) 
op = input("Enter any one of the operator (+,-,*,/): ") 

#For addition
if op == "+":    
    result = val1 + val2 

#For subtraction
elif op == "-":    
    if val1 > val2:        
        result = val1 - val2    
    else:        
        result = val2 - val1

# For multiplication
elif op == "*":       
    result = val1 * val2 

#For division
elif op == "/":    
    if val2 == 0:        
        print("Error! Division by zero is not allowed. Program terminated")    
    else:        result = val1/val2
else:    
    print("Wrong input,program terminated") 
print("The result is ",result)
