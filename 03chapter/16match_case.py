# This is aviable on the version of the Python 3.11.3

# This is also know as the match case statement in the python. This is the new feature of the python 3.10.0. 

x= int(input("Enter the number: "))

match x:
    case 1:
        print("The number is 1")
    case 2:
        print("The number is 2")
    case 3:
        print("The number is 3")
    case 4:
        print("The number is 4")
    case 5:
        print("The number is 5")
    case 6:
        print("The number is 6")
    case 7:
        print("The number is 7")
    case 8:
        print("The number is 8")
    case 9:
        print("The number is 9")
    case 10:
        print("The number is 10")
    case _:# This is the default case
        print("The number is not in the range of 1 to 10")

