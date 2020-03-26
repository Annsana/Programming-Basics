#Python program to swap two numbers

a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
print("a before swapping = ",a)
print("b before swapping = ",b)

#swapping two numbers using temporary variable

c=a
a=b
b=c
print("a after swapping is :",a)
print("b after swapping is :",b)
