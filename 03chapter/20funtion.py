#There are two type of function in the python
#1. Built in function
#2. User defined function

def add(a,b):
    c=a+b
    return c

def sub(a,b):
    pass #It will run the program without thye error in the program.


a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
ans=add(a,b)
print("The value of the ans is ",ans)