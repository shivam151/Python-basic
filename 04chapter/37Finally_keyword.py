l=[1,21,2,24]
i= int(input("Enter a number: "))
try:
    print(l[i])
except Exception as e:
    print (e)

finally:
    print("This is the finally block")#This block of code is always executed no matter what4